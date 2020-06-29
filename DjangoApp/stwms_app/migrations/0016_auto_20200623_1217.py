# Generated by Django 3.0.3 on 2020-06-23 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stwms_app', '0015_auto_20200623_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterialbatches',
            name='calories',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rawmaterialbatches',
            name='fat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rawmaterialbatches',
            name='proteins',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rawmaterialbatches',
            name='quality_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rawmaterialbatches',
            name='sodium',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]