# Generated by Django 2.2.2 on 2019-08-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('android_app', '0003_auto_20190828_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='version',
            field=models.IntegerField(max_length=10),
        ),
    ]
