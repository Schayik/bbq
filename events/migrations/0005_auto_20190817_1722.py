# Generated by Django 2.2.4 on 2019-08-18 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190817_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='meat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quantity', to='events.Meat'),
        ),
    ]
