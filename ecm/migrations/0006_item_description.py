# Generated by Django 3.2.4 on 2021-07-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecm', '0005_stream_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, max_length=6000, null=True),
        ),
    ]