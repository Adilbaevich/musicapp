# Generated by Django 4.2.2 on 2023-07-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/%Y%m%d/'),
        ),
    ]
