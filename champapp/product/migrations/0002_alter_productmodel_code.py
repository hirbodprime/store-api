# Generated by Django 4.1.7 on 2023-02-26 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='code',
            field=models.CharField(max_length=12),
        ),
    ]
