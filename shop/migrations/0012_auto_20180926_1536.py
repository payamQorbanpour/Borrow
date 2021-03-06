# Generated by Django 2.0.7 on 2018-09-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20180926_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_per_day',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_per_month',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_per_week',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_per_year',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10),
        ),
    ]
