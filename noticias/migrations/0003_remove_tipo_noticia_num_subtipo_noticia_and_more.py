# Generated by Django 4.1.2 on 2023-06-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_tipo_noticia_num_subtipo_noticia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo_noticia',
            name='num_subtipo_noticia',
        ),
        migrations.AddField(
            model_name='noticia',
            name='num_subtipo_noticia',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]