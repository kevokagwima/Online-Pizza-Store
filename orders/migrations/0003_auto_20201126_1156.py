# Generated by Django 3.1.3 on 2020-11-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_pasta_salads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasta',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='salads',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
