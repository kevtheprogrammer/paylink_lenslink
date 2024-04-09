# Generated by Django 4.1.7 on 2024-04-09 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(default='category.png', upload_to='category/cover/')),
                ('title', models.CharField(max_length=700)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=700)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumb', models.ImageField(default='products.png', upload_to='products/thum/')),
                ('name', models.CharField(max_length=900)),
                ('description', models.TextField(verbose_name='product description')),
                ('price', models.DecimalField(decimal_places=2, default=1.0, max_digits=1000, max_length=7)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=1000, max_length=7)),
                ('is_pub', models.BooleanField(default=False, verbose_name='is published')),
                ('img1', models.ImageField(blank=True, upload_to='products/thum/', verbose_name='first image')),
                ('img2', models.ImageField(blank=True, upload_to='products/thum/', verbose_name='second image')),
                ('img3', models.ImageField(blank=True, upload_to='products/thum/', verbose_name='third image')),
                ('slug', models.SlugField(default=None)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='product.category')),
                ('favourite', models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='tags', to='product.tag')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('Not Yet Shipped', 'Not Yet Shipped'), ('Shipped', 'Shipped'), ('Cancelled', 'Cancelled'), ('Refunded', 'Refunded')], default='Not Yet Shipped', max_length=120)),
                ('shipping_fee', models.DecimalField(decimal_places=2, default=8.0, max_digits=1000)),
                ('email', models.EmailField(blank=True, help_text='enter your active email', max_length=111)),
                ('address', models.CharField(blank=True, help_text='house no. or P.O.Box', max_length=400)),
                ('city', models.CharField(blank=True, max_length=111)),
                ('state', models.CharField(blank=True, help_text='province, country.', max_length=111)),
                ('zip_code', models.CharField(blank=True, max_length=111)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
                ('orderitems', models.ManyToManyField(related_name='orderitems', to='product.cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='product.product'),
        ),
    ]
