# Generated by Django 2.1.4 on 2018-12-26 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='receiver',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='main.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transfer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='main.User'),
        ),
    ]