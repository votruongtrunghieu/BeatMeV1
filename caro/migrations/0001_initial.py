# Generated by Django 3.0.4 on 2020-03-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='botInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.PositiveIntegerField()),
                ('lose', models.PositiveIntegerField()),
                ('draw', models.PositiveIntegerField()),
                ('elo', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
