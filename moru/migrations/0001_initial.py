# Generated by Django 4.2.11 on 2024-04-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('location', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='htels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('price', models.IntegerField(default=100)),
                ('image_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=1000)),
                ('content', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('photo_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('price', models.IntegerField(default=100)),
                ('image', models.ImageField(default='product.jpg', upload_to='media/')),
            ],
        ),
    ]
