# Generated by Django 5.0.3 on 2024-05-07 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('DEPTNO', models.IntegerField(primary_key=True, serialize=False)),
                ('DNAME', models.CharField(max_length=20, unique=True)),
                ('LOC', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GRADE', models.IntegerField()),
                ('LOSAL', models.DecimalField(decimal_places=2, max_digits=10)),
                ('HISAL', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('Emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('ENAME', models.CharField(max_length=100)),
                ('JOB', models.CharField(max_length=50)),
                ('HIREDATE', models.DateField()),
                ('SAL', models.IntegerField()),
                ('COMM', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('DEPTNO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
                ('MGR', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.emp')),
            ],
        ),
    ]
