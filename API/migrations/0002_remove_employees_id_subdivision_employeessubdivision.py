# Generated by Django 4.1.1 on 2022-11-16 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='id_subdivision',
        ),
        migrations.CreateModel(
            name='EmployeesSubdivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='API.employees')),
                ('id_subdivison', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='API.subdivisions')),
            ],
        ),
    ]