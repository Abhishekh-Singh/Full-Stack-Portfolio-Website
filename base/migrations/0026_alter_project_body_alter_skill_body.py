# Generated by Django 4.0.1 on 2022-02-02 19:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0025_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]