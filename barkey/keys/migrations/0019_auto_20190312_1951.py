# Generated by Django 2.1.7 on 2019-03-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keys', '0018_auto_20190312_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='key_value',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
    ]
