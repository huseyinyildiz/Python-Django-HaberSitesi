# Generated by Django 3.2.3 on 2021-05-22 13:56

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_images_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
