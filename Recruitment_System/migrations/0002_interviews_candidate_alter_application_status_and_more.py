# Generated by Django 4.2.3 on 2023-07-21 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment_System', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviews',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Recruitment_System.candidate'),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_review', 'in review'), ('rejected', 'rejected'), ('hired', 'hired')], default='pending', max_length=15),
        ),
        migrations.AlterField(
            model_name='interviews',
            name='job_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('rejected', 'Rejected'), ('hired', 'hired')], max_length=25),
        ),
    ]
