# Generated by Django 5.0.6 on 2024-05-25 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_qualification_specialization"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="qualification",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="group_qualification",
                to="app.qualification",
            ),
        ),
    ]
