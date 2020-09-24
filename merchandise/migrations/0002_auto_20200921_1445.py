# Generated by Django 3.0.2 on 2020-09-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamingproduct',
            name='gprod_img',
            field=models.ImageField(default='', upload_to='gamingsetup'),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_img',
            field=models.ImageField(default='', upload_to='shop'),
        ),
        migrations.AddField(
            model_name='video',
            name='vid_img',
            field=models.ImageField(default='', upload_to='video'),
        ),
    ]
