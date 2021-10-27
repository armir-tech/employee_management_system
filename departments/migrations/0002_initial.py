# Generated by Django 3.2.7 on 2021-10-07 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='dept_manager',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dept_manager', to='employees.employee'),
        ),
        migrations.AddField(
            model_name='department',
            name='parent',
            field=models.ManyToManyField(blank=True, to='departments.Department'),
        ),
    ]
