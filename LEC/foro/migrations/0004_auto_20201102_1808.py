# Generated by Django 3.1.1 on 2020-11-02 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foro', '0003_auto_20201102_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoria',
            name='Posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foro.post', verbose_name='Posts'),
        ),
    ]
