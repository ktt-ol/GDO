# Generated by Django 2.1.3 on 2018-11-07 08:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('keys', '0006_auto_20181105_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='id',
            field=models.UUIDField(default=uuid.UUID('094d13b1-34e3-44f8-b044-71326249b3fd'), editable=False, primary_key=True, serialize=False),
        ),
    ]
