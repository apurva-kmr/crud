# Generated by Django 3.1.5 on 2021-03-11 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Coustumer_id', models.IntegerField()),
                ('Email_id', models.CharField(max_length=64)),
                ('Pass', models.CharField(max_length=64)),
                ('Attempts', models.IntegerField()),
                ('Locked', models.IntegerField()),
            ],
        ),
    ]
