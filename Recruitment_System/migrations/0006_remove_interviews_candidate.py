# Generated by Django 4.2.3 on 2023-07-21 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment_System', '0005_alter_interviews_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviews',
            name='candidate',
        ),
    ]
