# Generated by Django 4.0.5 on 2022-06-30 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_portugues_p1_alter_portugues_p2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portugues',
            name='link_arquivo1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='portugues',
            name='link_arquivo2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='portugues',
            name='link_arquivo3',
            field=models.TextField(blank=True),
        ),
    ]
