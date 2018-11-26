# Generated by Django 2.1.3 on 2018-11-05 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Universidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocentesEnSemestre',
            fields=[
                ('id_semestre', models.ForeignKey(db_column='id_semestre', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Universidad.Semestre')),
            ],
            options={
                'managed': False,
                'db_table': 'docentes_en_semestre',
            },
        ),
        migrations.CreateModel(
            name='Estudianteysemestre',
            fields=[
                ('id_semestre', models.ForeignKey(db_column='id_semestre', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Universidad.Semestre')),
            ],
            options={
                'managed': False,
                'db_table': 'estudianteysemestre',
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('cod_materia', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_materia', models.CharField(blank=True, max_length=45, null=True)),
                ('creditos', models.IntegerField(blank=True, null=True)),
                ('semestre_id', models.IntegerField(blank=True, null=True)),
                ('activo', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'materia',
            },
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('tipodenota', models.CharField(max_length=75, primary_key=True, serialize=False)),
                ('notas', models.IntegerField(blank=True, null=True)),
                ('cod_materia', models.IntegerField()),
                ('cod_estudio', models.IntegerField()),
                ('cedula_doc', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'notas',
            },
        ),
        migrations.DeleteModel(
            name='Docentes_en_semestre',
        ),
        migrations.DeleteModel(
            name='materias',
        ),
        migrations.AlterModelOptions(
            name='docentes',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='estudiante',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='semestre',
            options={'managed': False},
        ),
        migrations.CreateModel(
            name='Materiayestudiantes',
            fields=[
                ('cod_estudio', models.IntegerField()),
                ('id_semestre', models.ForeignKey(db_column='id_semestre', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Universidad.Estudianteysemestre')),
            ],
            options={
                'managed': False,
                'db_table': 'materiayestudiantes',
            },
        ),
    ]
