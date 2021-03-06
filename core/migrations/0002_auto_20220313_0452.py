# Generated by Django 3.2.9 on 2022-03-13 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageAnalyticsCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('url', models.CharField(max_length=2000, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Page Visit Count',
                'verbose_name_plural': 'Page Visit Counts',
                'ordering': ('-created',),
                'get_latest_by': 'created',
            },
        ),
        migrations.DeleteModel(
            name='PageVisitCount',
        ),
    ]
