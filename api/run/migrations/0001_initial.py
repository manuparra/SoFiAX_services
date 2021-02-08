# Generated by Django 3.1.6 on 2021-02-04 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('sanity_thresholds', models.JSONField()),
            ],
            options={
                'db_table': 'run',
                'managed': False,
            },
        ),
    ]