# Generated by Django 2.1.4 on 2018-12-20 10:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(150), django.core.validators.MinValueValidator(0)])),
                ('email', models.CharField(default='enter username', max_length=256, null=True, unique=True, validators=[django.core.validators.EmailValidator])),
                ('password', models.CharField(default='enter password', max_length=6)),
                ('mob', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(10)])),
                ('address', models.CharField(max_length=100)),
                ('account_type', models.CharField(choices=[('C', 'CURRENT_ACCOUNT'), ('F', 'FIXED_DEPOSITE'), ('R', 'RECURRING_DEPOSITE')], max_length=1)),
                ('gender', models.CharField(choices=[('F', 'FEMALE'), ('M', 'MALE')], max_length=1)),
            ],
        ),
    ]