# Generated by Django 5.0.3 on 2024-04-10 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='marketplace.department')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('condition', models.CharField(choices=[('pre_owned', 'Pre-owned'), ('new_with_box', 'New with Box'), ('new_without_box', 'New without Box'), ('new_with_defects', 'New with Defects')], default='new_with_box', max_length=20)),
                ('description', models.TextField()),
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('userID', models.CharField(max_length=100, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.department')),
            ],
        ),
        migrations.CreateModel(
            name='Productimage',
            fields=[
                ('imageID', models.AutoField(primary_key=True, serialize=False)),
                ('imageURL', models.ImageField(default='https://png.pngtree.com/png-clipart/20190918/ourmid/pngtree-load-the-3273350-png-image_1733730.jpg', upload_to='product_images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.product')),
            ],
        ),
    ]
