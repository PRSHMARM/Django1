# Generated by Django 2.1.4 on 2018-12-23 06:42

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credits', models.IntegerField(null=True)),
                ('description', models.CharField(default='BALANCE', max_length=100)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('time', models.DateField(default=datetime.time, verbose_name='time')),
            ],
        ),
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit', models.IntegerField(null=True)),
                ('description', models.CharField(default='BALANCE', max_length=100)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='date')),
                ('time', models.DateField(default=datetime.time, verbose_name='time')),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(500)]),
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.AddField(
            model_name='debit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
        migrations.AddField(
            model_name='credit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.User'),
        ),
    ]