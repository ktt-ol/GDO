# Generated by Django 2.1.1 on 2018-11-02 21:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('keys', '0003_auto_20181102_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='first_used',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='id',
            field=models.UUIDField(default=uuid.UUID('12532a6f-c7dd-479e-8a26-662b6c73d091'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='key',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='keys.key'),
        ),
    ]
