# Generated by Django 4.2.6 on 2023-11-11 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_remove_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(upload_to='products/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productimages', to='market.product'),
        ),
    ]
