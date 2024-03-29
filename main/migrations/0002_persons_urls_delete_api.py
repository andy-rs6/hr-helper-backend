# Generated by Django 4.0 on 2022-11-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('master_id', models.TextField(blank=True, null=True)),
                ('ctc', models.IntegerField(blank=True, null=True)),
                ('cts', models.IntegerField(blank=True, null=True)),
                ('ttc', models.FloatField(blank=True, null=True)),
                ('tts', models.FloatField(blank=True, null=True)),
                ('device', models.TextField(blank=True, null=True)),
                ('locale', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'persons',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('url', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('unique_clicks', models.IntegerField(blank=True, null=True)),
                ('total_clicks', models.IntegerField(blank=True, null=True)),
                ('top', models.IntegerField(blank=True, null=True)),
                ('pbc', models.IntegerField(blank=True, null=True)),
                ('pbs', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'urls',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Api',
        ),
    ]
