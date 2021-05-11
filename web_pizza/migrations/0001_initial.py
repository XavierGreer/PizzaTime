# Generated by Django 3.2 on 2021-04-29 06:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name', 'slug'),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.CharField(default='69140', editable=False, max_length=100, primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_index=True, max_length=50)),
                ('lastname', models.CharField(db_index=True, max_length=50)),
                ('phone', models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{3}-\\d{4}$')])),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=1024, verbose_name='Address line 1')),
                ('zipcode', models.CharField(editable=False, max_length=12, verbose_name='ZIP / Postal code')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(choices=[('Pizza', 'Pizza'), ('Soda', 'Soda'), ('Side', 'Side')], max_length=25)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('priceSm', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('priceMd', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('priceLg', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sizePizza', models.IntegerField(choices=[(12, 'Small'), (14, 'Medium'), (16, 'Large')], default=12)),
                ('priceSodaSm', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('priceSodaLg', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('sizeSoda', models.IntegerField(choices=[(1, '12 Oz'), (2, '2 Liter')], default=1)),
                ('priceSide', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='web_pizza.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
            ],
            options={
                'verbose_name': 'topping',
                'verbose_name_plural': 'toppings',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ToppingAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(choices=[(1, 'Regular'), (2, 'Double')], default=1)),
                ('pizza', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_pizza.product')),
                ('topping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_pizza.topping')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='topping',
            field=models.ManyToManyField(through='web_pizza.ToppingAmount', to='web_pizza.Topping'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.CharField(default='D2604', editable=False, max_length=100, primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=2, editable=False, max_digits=4)),
                ('discount', models.DecimalField(decimal_places=0, max_digits=2)),
                ('status', models.IntegerField(choices=[(0, 'Order Received'), (1, 'Baking'), (2, 'On The Way'), (3, 'Delivered')], default=0)),
                ('customer', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='web_pizza.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
            ],
            options={
                'verbose_name': 'pizza',
                'verbose_name_plural': 'pizzas',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('web_pizza.product',),
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
            ],
            options={
                'verbose_name': 'side',
                'verbose_name_plural': 'sides',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('web_pizza.product',),
        ),
        migrations.CreateModel(
            name='Soda',
            fields=[
            ],
            options={
                'verbose_name': 'soda',
                'verbose_name_plural': 'sodas',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('web_pizza.product',),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
