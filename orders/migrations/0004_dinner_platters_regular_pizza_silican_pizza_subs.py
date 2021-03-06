# Generated by Django 3.1.3 on 2020-11-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20201126_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='dinner_platters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price_one', models.DecimalField(decimal_places=3, max_digits=5)),
                ('price_two', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='regular_pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price_one', models.DecimalField(decimal_places=3, max_digits=5)),
                ('price_two', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='silican_pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price_one', models.DecimalField(decimal_places=3, max_digits=5)),
                ('price_two', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price_one', models.DecimalField(decimal_places=3, max_digits=5)),
                ('price_two', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
    ]
