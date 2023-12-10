# Generated by Django 4.1.1 on 2023-06-23 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_customuser_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('serialno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'contact_us',
            },
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]