# Generated by Django 5.1.3 on 2024-12-15 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tertulias', '0006_alter_tertulia_tertulia_lugares'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tertulia',
            name='tertulia_lugares',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
