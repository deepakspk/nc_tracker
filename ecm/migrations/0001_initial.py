# Generated by Django 3.2.4 on 2021-07-08 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600, null=True)),
                ('description', models.TextField(blank=True, max_length=6000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.BigIntegerField(null=True)),
                ('email', models.EmailField(max_length=70, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=290, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream', models.CharField(max_length=60, null=True)),
                ('description', models.TextField(blank=True, max_length=6000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(max_length=60, null=True)),
                ('description', models.TextField(blank=True, max_length=6000, null=True)),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step_stream', to='ecm.stream')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=600, null=True)),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_step', to='ecm.step')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('note', models.TextField(max_length=600, null=True)),
                ('comment_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emp_comment', to='accounts.admin')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_can', to='ecm.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='stream',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='can_stream', to='ecm.stream'),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=600, null=True)),
                ('document', models.FileField(upload_to='documents/')),
                ('doc_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_type', to='ecm.doctype')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_can', to='ecm.item')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('note', models.TextField(blank=True, max_length=600, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_can', to='ecm.item')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='act_status', to='ecm.status')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='act_step', to='ecm.step')),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='act_stream', to='ecm.stream')),
            ],
        ),
    ]
