# Generated by Django 3.1.2 on 2020-10-14 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_editor_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['first_name']},
        ),
    ]
