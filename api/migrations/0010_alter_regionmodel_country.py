# Generated by Django 4.1 on 2022-08-20 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_regionmodel_country_alter_regionmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionmodel',
            name='country',
            field=models.CharField(choices=[('Unknown', '0'), ('India', '1'), ('2', 'USA'), ('3', 'Japan'), ('4', 'China'), ('5', 'Cambodia'), ('6', 'Rwanda'), ('7', 'Thailand')], max_length=30),
        ),
    ]
