# Generated by Django 3.1.1 on 2020-10-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0010_auto_20201011_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
