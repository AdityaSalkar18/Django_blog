# Generated by Django 4.1.5 on 2023-03-08 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_myprofile_alter_post_author_alter_post_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Myprofile',
            new_name='Profile',
        ),
    ]
