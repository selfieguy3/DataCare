# Generated by Django 5.0.6 on 2024-06-13 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_staff_salary_activityexpense_childexpense_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='age',
        ),
        migrations.AlterField(
            model_name='child',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='child',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='child',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
