# Generated by Django 2.0.2 on 2018-06-19 16:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2018, 6, 19, 16, 19, 57, 770099, tzinfo=utc))),
            ],
        ),
    ]
