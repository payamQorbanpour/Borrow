# Generated by Django 2.0.7 on 2018-09-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20180926_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='uuid',
            field=models.CharField(default=482653433405020998, editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to='products/%Y/%m/%d/%f'),
        ),
    ]
