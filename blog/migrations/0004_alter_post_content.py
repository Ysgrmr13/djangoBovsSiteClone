# Generated by Django 4.2.1 on 2023-05-25 13:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, help_text='не более 5000 символов', max_length=5000, null=True),
        ),
    ]