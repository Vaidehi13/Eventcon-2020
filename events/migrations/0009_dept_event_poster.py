# Generated by Django 3.1 on 2020-11-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_departmental_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='dept',
            name='event_poster',
            field=models.TextField(default='Equinox.jpg', max_length=20),
            preserve_default=False,
        ),
    ]
