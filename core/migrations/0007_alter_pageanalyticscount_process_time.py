# Generated by Django 3.2.9 on 2022-03-13 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20220313_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageanalyticscount',
            name='process_time',
            field=models.FloatField(verbose_name='Process Time'),
        ),
    ]
