# Generated by Django 3.2.4 on 2021-07-06 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecm', '0007_auto_20210704_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='Stream',
            new_name='stream',
        ),
        migrations.AlterField(
            model_name='activity',
            name='note',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.CharField(choices=[('Rental Agreement', 'Rental Agreement'), ('Expense Receipt', 'Expense Receipt'), ('CV', 'CV'), ('Visa', 'Visa')], max_length=110),
        ),
    ]