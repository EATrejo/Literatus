# Generated by Django 5.1.3 on 2024-12-12 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_rename_name_contact_first_name_contact_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[(0, 'Me interesa coordinar tertulia literartia'), (1, 'Reclamo'), (1, 'Sugerencia'), (1, 'Felicitaciones')])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]