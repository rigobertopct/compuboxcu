# Generated by Django 3.2.19 on 2023-09-08 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Modelos', '0008_alter_contadorgolpes_esquina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pugil',
            name='edad',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
