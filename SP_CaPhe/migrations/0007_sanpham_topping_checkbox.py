# Generated by Django 5.0.1 on 2024-05-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SP_CaPhe', '0006_sanpham_suger_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanpham',
            name='Topping_checkbox',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]
