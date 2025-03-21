# Generated by Django 5.1.7 on 2025-03-21 16:35

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("hr", "0010_alter_employee_about"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="employee",
            index=django.contrib.postgres.indexes.BrinIndex(
                fields=["created"], name="hr_employee_created_ix", pages_per_range=2
            ),
        ),
    ]
