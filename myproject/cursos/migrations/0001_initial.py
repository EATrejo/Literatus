# Generated by Django 5.1.2 on 2024-10-20 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('banner', models.ImageField(blank=True, default='fallback.png', upload_to='')),
                ('description', models.TextField()),
                ('duracion_curso', models.DurationField(null=True)),
                ('lugar_curso', models.TextField()),
                ('fecha_de_inicio', models.DateTimeField(null=True)),
                ('costo_del_curso', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
    ]
