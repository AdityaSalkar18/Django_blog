# Generated by Django 4.1.5 on 2023-03-30 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_post_slink_post_stype_alter_profile_pimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='aboutme',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='flink',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='ilink',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='llink',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]