# Generated by Django 2.0.3 on 2018-05-08 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('branch', models.CharField(choices=[('CSE', 'Computer Science & Engineering'), ('ECE', 'Electronics & Communication Engineering'), ('EEE', 'Electronics & Electrical Engineering'), ('BBA', 'Bachelor of Business Administration'), ('BCA', 'Bachelors in Computer Application'), ('Animation', 'Animation & Multimedia')], default='CSE', max_length=5)),
                ('semester', models.IntegerField(choices=[(1, 'first'), (2, 'second'), (3, 'third'), (4, 'fouth'), (5, 'fifth'), (6, 'sixth'), (7, 'seventh'), (8, 'eighth')], default=1)),
                ('subject', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('year', models.IntegerField(choices=[(2010, '2010'), (2011, '2011'), (2012, '2012'), (2013, '2013'), (2014, '2014'), (2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018')], default='')),
                ('time_period', models.CharField(choices=[('midsem', 'midsem'), ('endsem', 'endsem')], default='midsem', max_length=6)),
                ('file', models.FileField(blank=True, null=True, upload_to='files')),
                ('uploaded_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
    ]