# Generated by Django 2.2.3 on 2019-07-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trafficlog',
            name='label',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trafficlog',
            name='sublabel',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
