# Generated by Django 3.0.5 on 2020-05-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iportal', '0011_auto_20200501_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='college',
            field=models.CharField(default='NIT Raipur', max_length=300),
        ),
    ]
