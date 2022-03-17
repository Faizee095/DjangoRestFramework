# Generated by Django 4.0.3 on 2022-03-17 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangorestAPI', '0002_personaldetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField()),
                ('hobby_name', models.CharField(max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangorestAPI.student')),
            ],
        ),
        migrations.DeleteModel(
            name='PersonalDetails',
        ),
    ]
