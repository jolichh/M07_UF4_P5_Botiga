# Generated by Django 5.0.3 on 2024-04-17 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cataleg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cataleg.producte')),
            ],
        ),
    ]
