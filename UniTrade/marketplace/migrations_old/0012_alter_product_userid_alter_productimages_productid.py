# Generated by Django 5.0.3 on 2024-04-06 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0011_remove_product_id_alter_product_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='userID',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='productID',
            field=models.TextField(),
        ),
    ]
