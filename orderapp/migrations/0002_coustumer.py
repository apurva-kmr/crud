# Generated by Django 3.1.5 on 2021-03-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coustumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transaction_ID', models.IntegerField()),
                ('Customer_ID', models.IntegerField()),
                ('Transdate', models.DateField()),
                ('Cfname', models.CharField(max_length=64)),
                ('Clname', models.CharField(max_length=64)),
                ('Country', models.CharField(max_length=64)),
                ('Ccity', models.CharField(max_length=64)),
                ('Product', models.CharField(max_length=64)),
                ('Qty', models.IntegerField()),
                ('Amount', models.IntegerField()),
            ],
        ),
    ]
