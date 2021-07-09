# Generated by Django 3.2.4 on 2021-07-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('ecm', '0003_status_stream'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_group', models.CharField(max_length=100, unique=True)),
                ('user', models.ManyToManyField(to='accounts.Admin')),
            ],
        ),
    ]
