# Generated by Django 3.2.7 on 2021-09-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210909_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='depa',
            field=models.TextField(default='CSE'),
        ),
    ]
