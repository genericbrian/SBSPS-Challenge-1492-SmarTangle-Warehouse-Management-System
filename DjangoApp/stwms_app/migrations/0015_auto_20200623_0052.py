# Generated by Django 3.0.3 on 2020-06-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stwms_app', '0014_auto_20200622_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rawmaterialrequest',
            name='id',
        ),
        migrations.AddField(
            model_name='rawmaterialrequest',
            name='request_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
