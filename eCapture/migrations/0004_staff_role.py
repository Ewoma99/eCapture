# Generated by Django 2.2.7 on 2020-07-25 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eCapture', '0003_auto_20200725_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='eCapture.Role'),
        ),
    ]
