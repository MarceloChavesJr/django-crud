# Generated by Django 4.1.5 on 2023-01-11 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.FloatField()),
                ('fabricante', models.CharField(max_length=30)),
                ('quantidade', models.IntegerField()),
            ],
        ),
    ]
