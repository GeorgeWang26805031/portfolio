# Generated by Django 2.0.5 on 2018-06-11 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Time', '0002_auto_20180611_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], max_length=1),
        ),
    ]
