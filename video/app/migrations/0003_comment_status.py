# Generated by Django 2.1.2 on 2022-03-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
