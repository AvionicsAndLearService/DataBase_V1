# Generated by Django 3.0.7 on 2021-06-09 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orden',
            fields=[
                ('ot', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('matricula', models.CharField(max_length=150)),
                ('cliente', models.CharField(blank=True, max_length=15, null=True)),
                ('hangar', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('serie', models.CharField(blank=True, max_length=40, null=True)),
                ('tt_planeador', models.CharField(blank=True, max_length=40, null=True)),
                ('ct_planeador', models.CharField(blank=True, max_length=40, null=True)),
                ('tt_motor1', models.CharField(blank=True, max_length=40, null=True)),
                ('ct_motor1', models.CharField(blank=True, max_length=40, null=True)),
                ('tt_motor2', models.CharField(blank=True, max_length=40, null=True)),
                ('ct_motor2', models.CharField(blank=True, max_length=40, null=True)),
                ('reporte', models.TextField(max_length=7000)),
                ('acciones_correctivas', models.TextField(max_length=7000)),
                ('estado', models.CharField(choices=[('C', 'Concluido'), ('P', 'Pendiente'), ('T', 'Trabajando')], default='P', max_length=1)),
                ('observaciones', models.TextField(max_length=7000)),
                ('tecnico', models.CharField(max_length=100)),
                ('horas', models.CharField(max_length=15)),
                ('fecha', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='contabilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.CharField(max_length=40)),
                ('pago', models.CharField(choices=[('C', 'Concluido'), ('P', 'Pendiente'), ('T', 'Trabajando')], default='P', max_length=1)),
                ('observaciones', models.TextField(max_length=7000)),
                ('fecha', models.TimeField(auto_now_add=True)),
                ('orden_trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.orden')),
            ],
        ),
    ]