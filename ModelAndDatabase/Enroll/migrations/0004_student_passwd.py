# Generated by Django 2.2.24 on 2022-06-07 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enroll', '0003_remove_student_passwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='passwd',
            field=models.CharField(default='not available', max_length=100),
        ),
    ]