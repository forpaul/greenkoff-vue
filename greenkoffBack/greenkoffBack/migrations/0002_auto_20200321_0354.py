# Generated by Django 2.2 on 2020-03-21 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenkoffBack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
