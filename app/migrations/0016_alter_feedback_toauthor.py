# Generated by Django 4.1.5 on 2023-03-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_feedback_toauthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='toauthor',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
