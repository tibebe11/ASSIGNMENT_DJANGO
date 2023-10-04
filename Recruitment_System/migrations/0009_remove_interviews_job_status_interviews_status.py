# Generated by Django 4.2.3 on 2023-07-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment_System', '0008_remove_interviews_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviews',
            name='job_status',
        ),
        migrations.AddField(
            model_name='interviews',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('scheduled', 'Scheduled'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending', max_length=15, null=True),
        ),
    ]