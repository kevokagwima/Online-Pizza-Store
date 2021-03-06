# Generated by Django 3.1.3 on 2020-12-09 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20201201_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('date_ordered', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='order_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_eight', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='dinner_platters', to='orders.dinner_platters')),
                ('product_five', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pasta', to='orders.pasta')),
                ('product_four', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='orders.subs')),
                ('product_one', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='regular_pizza', to='orders.regular_pizza')),
                ('product_seven', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='salads', to='orders.salads')),
                ('product_six', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pasta', to='orders.salads')),
                ('product_three', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='topping', to='orders.toppings')),
                ('product_two', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='silican_pizza', to='orders.silican_pizza')),
            ],
        ),
        migrations.DeleteModel(
            name='orders',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order_items'),
        ),
    ]
