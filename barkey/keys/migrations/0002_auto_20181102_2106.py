# Generated by Django 2.1.1 on 2018-11-02 20:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('keys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='key',
            name='description',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='key',
            name='first_used',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='key',
            name='valid_for',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='id',
            field=models.UUIDField(default=uuid.UUID('94f5ea5e-a2aa-4de9-bdcc-f14940f26dd8'), editable=False, primary_key=True, serialize=False),
        ),
    ]
