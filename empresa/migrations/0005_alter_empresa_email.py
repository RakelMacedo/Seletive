# Generated by Django 4.1.3 on 2022-11-13 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0004_alter_vagas_titulo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresa",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
