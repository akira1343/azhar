# Generated by Django 5.0.6 on 2024-05-25 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_alter_specialization_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="studentgroup",
            options={
                "verbose_name": "Группа студента",
                "verbose_name_plural": "Группа студента",
            },
        ),
        migrations.AlterModelTable(
            name="studentgroup",
            table="student_group",
        ),
    ]
