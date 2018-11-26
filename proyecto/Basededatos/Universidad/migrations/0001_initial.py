# Generated by Django 2.1.3 on 2018-11-05 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Docentes',
            fields=[
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_doc', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Docentes_en_semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_semestre', models.IntegerField(verbose_name=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, to='Universidad.estudiante'))),
            ],
        ),
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('cod_estudio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_est', models.CharField(max_length=128)),
                ('Apellido_est', models.CharField(max_length=128)),
                ('quesemestre', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='materias',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=128)),
                ('creditos', models.IntegerField()),
                ('activa', models.BooleanField(default=True)),
                ('semestre', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='semestre',
            fields=[
                ('periodo', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]