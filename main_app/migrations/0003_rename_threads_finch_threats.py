# Generated by Django 5.0.1 on 2024-01-10 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_description_finch_threads_remove_finch_age_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finch',
            old_name='threads',
            new_name='threats',
        ),
    ]
