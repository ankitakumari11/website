# Generated by Django 4.1.7 on 2023-03-05 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='vdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('activity', models.CharField(max_length=30)),
                ('dept', models.CharField(max_length=20)),
                ('academic_year', models.CharField(max_length=10)),
                ('module', models.CharField(max_length=20)),
                ('div', models.CharField(max_length=10)),
                ('current_add', models.CharField(max_length=200)),
                ('prn', models.BigIntegerField()),
                ('roll', models.BigIntegerField()),
                ('contact_num', models.FloatField()),
                ('verified', models.IntegerField(default=0)),
                ('submitted', models.IntegerField(default=0)),
                ('Objective_of_the_Activity', models.CharField(default='', max_length=1000)),
                ('Description_of_the_Activity', models.CharField(default='', max_length=1000)),
                ('Benefits_to_Society', models.CharField(default='', max_length=1000)),
                ('Benefits_to_Self', models.CharField(default='', max_length=1000)),
                ('Learning_Experiences_challenges', models.CharField(default='', max_length=1000)),
                ('How_did_it_help_you_to_shape_your_Empathy', models.CharField(default='', max_length=1000)),
                ('url', models.URLField(default='', max_length=1000)),
                ('Cordinator', models.CharField(default='', max_length=40)),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='issec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=30)),
                ('gender', models.CharField(default='', max_length=10)),
                ('dept', models.CharField(default='', max_length=20)),
                ('academic_year', models.CharField(default='', max_length=10)),
                ('domain', models.CharField(default='', max_length=20)),
                ('module', models.CharField(default='', max_length=20)),
                ('div', models.CharField(default='', max_length=10)),
                ('current_add', models.CharField(default='', max_length=100)),
                ('prn', models.BigIntegerField(default=0)),
                ('roll', models.BigIntegerField(default=0)),
                ('contact_num', models.FloatField(default=0)),
                ('Cordinator', models.CharField(default='', max_length=40)),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='iscoord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(default='', max_length=40)),
                ('email', models.EmailField(default='', max_length=30)),
                ('gender', models.CharField(default='', max_length=10)),
                ('dept', models.CharField(default='', max_length=40)),
                ('academic_year', models.CharField(default='', max_length=10)),
                ('module', models.CharField(default='', max_length=20)),
                ('div', models.CharField(default='', max_length=10)),
                ('current_add', models.CharField(default='', max_length=100)),
                ('prn', models.BigIntegerField(default=0)),
                ('roll', models.BigIntegerField(default=0)),
                ('contact_num', models.FloatField(default=0)),
                ('verified', models.IntegerField(default=0)),
                ('submitted', models.IntegerField(default=0)),
                ('Objective_of_the_Activity', models.CharField(default='', max_length=1000)),
                ('Description_of_the_Activity', models.CharField(default='', max_length=1000)),
                ('Benefits_to_Society', models.CharField(default='', max_length=1000)),
                ('Benefits_to_Self', models.CharField(default='', max_length=1000)),
                ('Learning_Experiences_challenges', models.CharField(default='', max_length=1000)),
                ('How_did_it_help_you_to_shape_your_Empathy', models.CharField(default='', max_length=1000)),
                ('url', models.URLField(default='', max_length=1000)),
                ('Secretary', models.CharField(default='', max_length=40)),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
