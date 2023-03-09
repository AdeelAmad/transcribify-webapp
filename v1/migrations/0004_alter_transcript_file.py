# Generated by Django 4.1.7 on 2023-03-08 01:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0003_alter_transcript_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcript',
            name='file',
            field=models.FileField(upload_to='transcripts/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(['mp3', 'wav', 'm4a'])]),
        ),
    ]
