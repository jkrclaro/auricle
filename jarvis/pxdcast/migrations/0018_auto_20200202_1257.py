# Generated by Django 3.0.1 on 2020-02-02 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200202_1251'),
        ('pxdcast', '0017_auto_20200202_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcast',
            name='subscriptions',
        ),
        migrations.AddField(
            model_name='podcast',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscribers', through='pxdcast.Subscription', to='accounts.Pxdcast'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Pxdcast'),
        ),
    ]
