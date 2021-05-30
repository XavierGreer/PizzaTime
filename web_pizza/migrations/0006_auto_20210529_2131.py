# Generated by Django 3.2 on 2021-05-30 03:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_pizza', '0005_auto_20210523_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerID',
            field=models.CharField(default='43FAD', editable=False, max_length=100, primary_key=True, serialize=False, verbose_name='Customer ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='firstname',
            field=models.CharField(db_index=True, max_length=50, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lastname',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=12, null=True, validators=[django.core.validators.RegexValidator('^\\d{3}(-)?\\d{3}(-)?\\d{4}$')], verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderID',
            field=models.CharField(default='02383', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'Order Received'), (1, 'Baking'), (2, 'On The Way'), (3, 'Delivered')], default=0, verbose_name='Order Status'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('Pizza', 'Pizza'), ('Soda', 'Soda'), ('Side', 'Side')], default=None, max_length=25),
        ),
    ]