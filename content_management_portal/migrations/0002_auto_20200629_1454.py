# Generated by Django 2.2.1 on 2020-06-29 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_management_portal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='user',
            new_name='user_id',
        ),
    ]
