# Generated by Django 3.1.7 on 2021-04-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_pizza', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topping',
            options={'ordering': ('name',), 'verbose_name': 'topping', 'verbose_name_plural': 'toppings'},
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(db_index=True, max_length=20),
        ),
    ]
