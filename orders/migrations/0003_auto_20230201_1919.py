# Generated by Django 3.2.13 on 2023-02-01 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.AddField(
            model_name='order',
            name='telefon',
            field=models.CharField(max_length=14, null=True),
        ),
    ]
