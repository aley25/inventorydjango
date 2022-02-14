# Generated by Django 4.0 on 2021-12-22 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100)),
                ('mrp', models.FloatField()),
                ('discount', models.FloatField()),
                ('price', models.FloatField()),
                ('quantity', models.SmallIntegerField()),
                ('sold', models.SmallIntegerField()),
                ('available', models.SmallIntegerField()),
                ('defective', models.SmallIntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField()),
                ('status', models.SmallIntegerField()),
                ('subTotal', models.FloatField()),
                ('itemDiscount', models.FloatField()),
                ('tax', models.FloatField()),
                ('shipping', models.FloatField()),
                ('total', models.FloatField()),
                ('promo', models.CharField(max_length=50)),
                ('discount', models.FloatField()),
                ('grandTotal', models.FloatField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('type', models.SmallIntegerField()),
                ('mode', models.SmallIntegerField()),
                ('status', models.SmallIntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='sales.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
                ('quantity', models.SmallIntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='sales.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='sales.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='sales.order'),
        ),
        migrations.AddField(
            model_name='item',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.product'),
        ),
        migrations.AddField(
            model_name='item',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='users.user'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('middleName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('line1', models.CharField(max_length=50)),
                ('line2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='sales.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='users.user')),
            ],
        ),
    ]