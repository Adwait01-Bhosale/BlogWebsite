# Generated by Django 3.2.5 on 2023-04-11 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_account_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user_image',
        ),
    ]