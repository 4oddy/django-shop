# Generated by Django 3.2.13 on 2023-02-05 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_basket_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='season_list',
            field=models.CharField(max_length=30, null=True, verbose_name='Сезон'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thorn',
            field=models.CharField(max_length=6, null=True, verbose_name='Шипы есть нет'),
        ),
    ]
