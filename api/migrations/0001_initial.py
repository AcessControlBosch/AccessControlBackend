# Generated by Django 4.0.6 on 2022-07-28 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('status', models.BooleanField()),
                ('ipaddress', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='typeAssociente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('EDV', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseMachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
                ('idAssociateFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userReleaseMachine', to='api.user')),
                ('idMachineFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machineReleaseMachine', to='api.machine')),
            ],
        ),
        migrations.CreateModel(
            name='QRcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('router_ip', models.CharField(max_length=300)),
                ('idMachineFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machineQRcode', to='api.machine')),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
                ('idAssociateFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userObservation', to='api.user')),
                ('idMachineFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machineObservation', to='api.machine')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenanceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
                ('idAssociateFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userMaintenanceOrder', to='api.user')),
                ('idMachineFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machineMaintenanceOrder', to='api.machine')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
                ('idAssociateFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='api.user')),
                ('idMachineFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machineMaintenance', to='api.machine')),
            ],
        ),
        migrations.CreateModel(
            name='GreenBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('idMachineFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='machineGreenBook', to='api.machine')),
                ('typeQuestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='api.question')),
            ],
        ),
        migrations.CreateModel(
            name='Associate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('idAssociateFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userADM', to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='Apprentice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=30)),
                ('idApprenticeFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userApprentice', to='api.user')),
            ],
        ),
    ]