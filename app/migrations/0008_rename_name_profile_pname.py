# Generated by Django 4.1.5 on 2023-03-15 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_post_bimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='pname',
        ),
    ]
