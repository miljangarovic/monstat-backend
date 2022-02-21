# Generated by Django 4.0.2 on 2022-02-21 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BracniStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Drzavljanstvno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EkonomskaAktivnost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Godina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('godina', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Grad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MaternjiJezik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalnost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pismenost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RacunarksaPismenost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stanovnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=255)),
                ('godina_rodjenja', models.DateTimeField()),
                ('bracni_status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stanovnici.bracnistatus')),
                ('drzavljanstvo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stanovnici.drzavljanstvno')),
                ('ekonomska_aktivnost_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stanovnici.ekonomskaaktivnost')),
                ('godina_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stanovnici.godina')),
                ('grad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stanovnici.grad')),
                ('jezik_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stanovnici.maternjijezik')),
                ('nacionalnost_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stanovnici.nacionalnost')),
            ],
        ),
        migrations.CreateModel(
            name='StepenObrazovanja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StraniJezik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vjeroispovijest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StanovnikStraniJezik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stanovnik_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stanovnik', to='stanovnici.stanovnik')),
                ('strani_jezik_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strani_jezik', to='stanovnici.stranijezik')),
            ],
        ),
        migrations.AddField(
            model_name='stanovnik',
            name='obrazovanje_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obrazovanje', to='stanovnici.stepenobrazovanja'),
        ),
        migrations.AddField(
            model_name='stanovnik',
            name='pismenost_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stanovnici.pismenost'),
        ),
        migrations.AddField(
            model_name='stanovnik',
            name='pol_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stanovnici.pol'),
        ),
        migrations.AddField(
            model_name='stanovnik',
            name='racunarska_pismenost_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stanovnici.racunarksapismenost'),
        ),
        migrations.AddField(
            model_name='stanovnik',
            name='vjeroispovijest_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stanovnici.vjeroispovijest'),
        ),
    ]
