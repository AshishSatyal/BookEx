# Generated by Django 4.1.3 on 2023-03-02 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookexapp', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletteruserslist',
            name='uname',
        ),
    ]