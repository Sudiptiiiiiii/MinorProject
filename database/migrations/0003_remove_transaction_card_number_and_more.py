# Generated by Django 5.0.2 on 2024-02-29 10:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_cards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='Card_Number',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='Number_of_Items',
        ),
        migrations.AddField(
            model_name='transaction',
            name='card',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='database.cards'),
            preserve_default=False,
        ),
    ]
