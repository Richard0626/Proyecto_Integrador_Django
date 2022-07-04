# Generated by Django 4.0.5 on 2022-06-27 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_cat', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fec_re', models.DateField(verbose_name='Fecha de Registro')),
            ],
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id_com', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descrip', models.CharField(max_length=250, verbose_name='Descripcion')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('stock', models.IntegerField()),
                ('img', models.ImageField(upload_to='eatfood/images')),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eatfood.categoria', verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('id_com', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eatfood.comida')),
            ],
        ),
    ]