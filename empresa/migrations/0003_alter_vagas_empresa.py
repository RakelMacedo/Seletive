# Generated by Django 4.1.3 on 2022-11-10 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0002_alter_vagas_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vagas",
            name="empresa",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="empresa.empresa",
            ),
        ),
    ]