# Generated by Django 3.2.19 on 2023-06-13 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_contact_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_us',
            name='subject',
        ),
    ]
