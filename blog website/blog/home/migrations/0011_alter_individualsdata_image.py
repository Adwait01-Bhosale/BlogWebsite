# Generated by Django 3.2.5 on 2023-04-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_individualsdata_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualsdata',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='media/profile_pics/'),
        ),
    ]