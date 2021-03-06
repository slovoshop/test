# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-07 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_monthjournal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='student_name',
        ),
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': 'Exam', 'verbose_name_plural': 'Exams'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Group', 'verbose_name_plural': 'Groups'},
        ),
        migrations.AlterModelOptions(
            name='monthjournal',
            options={'verbose_name': 'Month journal', 'verbose_name_plural': 'Month journals'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='Date/Time'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='exam_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='students.Group', verbose_name='Group'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='teacher',
            field=models.CharField(max_length=256, verbose_name='Teacher'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Student', verbose_name='Leader'),
        ),
        migrations.AlterField(
            model_name='group',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Extra Notes'),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='monthjournal',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student', unique_for_month=b'date', verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=256, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=256, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, default=b'', max_length=256, verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Extra Notes'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group', verbose_name='Group'),
        ),
        migrations.AlterField(
            model_name='student',
            name='ticket',
            field=models.CharField(max_length=256, verbose_name='Ticket'),
        ),
        migrations.DeleteModel(
            name='Journal',
        ),
    ]
