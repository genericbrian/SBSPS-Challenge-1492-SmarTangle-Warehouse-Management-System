# Generated by Django 3.0.3 on 2020-06-15 18:32

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
            name='RawMaterials',
            fields=[
                ('rawMaterial_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('rawMaterial_name', models.CharField(max_length=25, unique=True)),
                ('price', models.IntegerField()),
                ('requestsFromUser', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StoreDetails',
            fields=[
                ('store_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('storeManager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('supplier_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=25)),
                ('supplier_rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitsAvailable', models.BigIntegerField()),
                ('rawMaterial_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='stwms_app.RawMaterials')),
            ],
        ),
        migrations.CreateModel(
            name='StoreInventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitsAvailable', models.BigIntegerField()),
                ('rawMaterial_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stwms_app.RawMaterials')),
                ('storeId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stwms_app.StoreDetails')),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterialBatches',
            fields=[
                ('uniqueBatch_id', models.IntegerField(primary_key=True, serialize=False)),
                ('units', models.IntegerField()),
                ('rawMaterial_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stwms_app.RawMaterials')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stwms_app.Suppliers')),
            ],
        ),
    ]