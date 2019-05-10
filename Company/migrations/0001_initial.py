# Generated by Django 2.1.5 on 2019-04-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sub_name', models.CharField(blank=True, max_length=100, null=True)),
                ('header', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('corp_num', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=16, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]