# Generated by Django 3.0.2 on 2020-09-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0002_auto_20200921_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_color',
            field=models.CharField(default='White', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_desc',
            field=models.CharField(default='', max_length=500),
        ),
    ]
