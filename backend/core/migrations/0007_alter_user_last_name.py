# Generated by Django 3.2.3 on 2021-05-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
