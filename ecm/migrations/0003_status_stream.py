# Generated by Django 3.2.4 on 2021-07-09 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecm', '0002_rename_doc_type_document_document_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='stream',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='status_stream', to='ecm.stream'),
            preserve_default=False,
        ),
    ]
