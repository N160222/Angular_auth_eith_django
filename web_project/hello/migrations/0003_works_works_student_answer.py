# Generated by Django 4.0.5 on 2022-06-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_adding_works'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='works_student_answer',
            field=models.TextField(default=False),
        ),
    ]
