# Generated by Django 4.0.2 on 2022-02-22 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stanovnici', '0005_alter_stanovnik_grad_id_delete_stanovnikstranijezik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stanovnik',
            name='grad_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stanovnici', to='stanovnici.grad'),
        ),
    ]
