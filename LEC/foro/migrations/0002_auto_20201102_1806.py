# Generated by Django 3.1.1 on 2020-11-02 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='Subcategoria',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='foro.subcategoria', verbose_name='Subcategoria'),
        ),
    ]
