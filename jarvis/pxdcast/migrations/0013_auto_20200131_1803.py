# Generated by Django 3.0.1 on 2020-01-31 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pxdcast', '0012_auto_20200131_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='podcast',
            old_name='apple_podcasts_id',
            new_name='itunes_id',
        ),
        migrations.AlterField(
            model_name='episode',
            name='podcast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='pxdcast.Podcast'),
        ),
    ]
