# Generated by Django 5.2.1 on 2025-07-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0003_drawoffset'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawoffset',
            name='scheduled_draw_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
