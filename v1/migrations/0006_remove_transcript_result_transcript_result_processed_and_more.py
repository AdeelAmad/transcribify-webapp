# Generated by Django 4.1.7 on 2023-03-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0005_transcript_language_alter_transcript_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transcript',
            name='result',
        ),
        migrations.AddField(
            model_name='transcript',
            name='result_processed',
            field=models.TextField(blank=True, default='Processing... Check Back Soon'),
        ),
        migrations.AddField(
            model_name='transcript',
            name='result_raw',
            field=models.TextField(blank=True, default='Processing... Check Back Soon'),
        ),
    ]
