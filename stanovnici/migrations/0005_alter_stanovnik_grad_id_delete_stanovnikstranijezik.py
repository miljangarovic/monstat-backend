# Generated by Django 4.0.2 on 2022-02-21 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stanovnici', '0004_stanovnik_strani_jezici'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stanovnik',
            name='grad_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grad', to='stanovnici.grad'),
        ),
        migrations.DeleteModel(
            name='StanovnikStraniJezik',
        ),
    ]
