# Generated by Django 3.1.2 on 2020-11-12 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='test user', max_length=255, verbose_name='Name'),
        ),
    ]
