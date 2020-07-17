# Generated by Django 2.2.6 on 2020-07-17 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0002_auto_20200716_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasoSospechoso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_sospechoso', models.DateTimeField()),
                ('sexo_sospechoso', models.BooleanField()),
                ('nombre_sospechoso', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_sospechoso', models.CharField(blank=True, max_length=50, null=True)),
                ('cuadro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='covid.CuadroMedico')),
            ],
        ),
    ]
