# Generated by Django 4.1.1 on 2023-06-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_notes_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='semester',
            field=models.CharField(default='VI', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notes',
            name='course',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='notes',
            name='program',
            field=models.CharField(max_length=100),
        ),
    ]