# Generated by Django 4.1 on 2022-08-19 19:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_regionmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionmodel',
            name='region_code',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]