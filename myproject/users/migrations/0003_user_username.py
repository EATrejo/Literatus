# Generated by Django 5.1.3 on 2024-11-28 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_groups_user_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=False, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
