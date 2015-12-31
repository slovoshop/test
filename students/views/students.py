# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.students import Student
from ..models.groups import Group

from datetime import datetime

from django.contrib import messages 

# Views for Students
def students_list(request):
		students = Student.objects.all()

		# try to order students list
		order_by = request.GET.get('order_by', '')
		if order_by == '':
			students = students.order_by('last_name') 				
		elif order_by == 'ticket':
			students = students.extra(select={'ticket': 'CAST(ticket AS UNSIGNED)'}).extra(order_by = ['ticket'])					
		elif order_by in ('id', 'last_name', 'first_name'):
			students = students.order_by(order_by)
		if request.GET.get('reverse', '') == '1':
			students = students.reverse()			
		
		per_page = 3		

		paginator = Paginator(students, per_page)
		page = request.GET.get('page')
		try:
			students = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			students = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver
			# last page of results.
			students = paginator.page(paginator.num_pages)

		# Добавка к forloop.counter при сортировке по полю №
		id_sort = per_page * (students.number - 1)
	
		# формирование списка номеров для поля № при реверсной сортировке
		id_reverse = []				
		if request.GET.get('reverse', '') == '1':		
			for i in range(paginator._count - id_sort, paginator._count - id_sort - per_page, -1):
					id_reverse.append(i)	
		
		test = 'none'		

		return render(request, 'students/students_list.html',
		{'students': students, 'id_sort': id_sort, 'id_reverse': id_reverse, 'test': test})




def students_add(request):

	# was form posted?
	if request.method == "POST":		

		# was form add button clicked?
		if request.POST.get('add_button') is not None:

			# TODO: validate input from user

			# errors collection
			errors = {}
			
			# validate student data will go here
			data = {'middle_name': request.POST.get('middle_name'),
			'notes': request.POST.get('notes')}

			# validate user input
			first_name = request.POST.get('first_name', '').strip()
			if not first_name:
				errors['first_name'] = u"Ім'я є обов'язковим"
			else:
				data['first_name'] = first_name
			
			last_name = request.POST.get('last_name', '').strip()
			if not last_name:
				errors['last_name'] = u"Прізвище є обов'язковим"
			else:
				data['last_name'] = last_name

			birthday = request.POST.get('birthday', '').strip()
			if not birthday:
				errors['birthday'] = u"Дата народження є обов'язковою"
			else:
				try:
					datetime.strptime(birthday, '%Y-%m-%d')
				except Exception as e:
					errors['birthday'] = 	u"Введіть коректний формат дати (напр. 1984-12-30)" + \
																" exception: " + e.message
				else:
					data['birthday'] = birthday

			ticket = request.POST.get('ticket', '').strip()
			if not ticket:
				errors['ticket'] = u"Номер білета є обов'язковим"
			else:
				data['ticket'] = ticket

			student_group = request.POST.get('student_group', '').strip()
			if not student_group:
				errors['student_group'] = u"Оберіть групу для студента"
			else:
				groups = Group.objects.filter(pk=student_group)
				if len(groups) != 1:
					errors['student_group'] = u"Оберіть коректну групу"
				else:
					data['student_group'] = groups[0]

			photo = request.FILES.get('photo')
			if photo:
				if not photo.content_type.split("/")[-1] in ('jpeg', 'png', 'bmp'):
					errors['photo'] = u"Оберіть файл типу .jpg, .jpeg, .png, .bmp"
				elif photo._size > 2000000:
					errors['photo'] = u"Максимальний розмір файлу - 2 МБ"
				else:
					data['photo'] = photo

			# save student
			if not errors:
				student = Student(**data)
				student.save()
				# redirect to students list
				messages.tags = []
				messages.add_message(request, messages.INFO, u'Студента %s %s успішно додано!' % (first_name, last_name))
				return HttpResponseRedirect(reverse('home'))

			else:
				# render form with errors and previous user input
				return render(request, 'students/students_add.html',
				{'groups': Group.objects.all().order_by('title'),
				'errors': errors})

		elif request.POST.get('cancel_button') is not None:
			# redirect to home page on cancel button
			messages.tags = []
			messages.add_message(request, messages.INFO, 'Додавання студента скасовано!')
			return HttpResponseRedirect(reverse('home'))

	else:
		# initial form render
		return render(request, 'students/students_add.html', 
		{'groups': Group.objects.all().order_by('title')})




def students_edit(request, sid):
  return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
  return HttpResponse('<h1>Delete Student %s</h1>' % sid)

