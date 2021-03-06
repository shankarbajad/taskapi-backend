# Generated by Django 3.1.2 on 2020-10-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name', max_length=120)),
                ('detail', models.TextField(help_text='details')),
                ('toDate', models.DateTimeField(verbose_name='To Date')),
                ('fromDate', models.DateTimeField(verbose_name='From Date')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
