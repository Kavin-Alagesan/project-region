# Generated by Django 4.1 on 2022-08-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_regionmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='region_image'),
        ),
    ]