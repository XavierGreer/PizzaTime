# Generated by Django 3.2.2 on 2021-05-11 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerID',
            field=models.CharField(default='27E46', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderID',
            field=models.CharField(default='96ACD', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
    ]
