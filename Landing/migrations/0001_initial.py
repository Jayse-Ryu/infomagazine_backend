# Generated by Django 2.1.2 on 2018-11-07 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.IntegerField(default=1)),
                ('header_script', models.CharField(blank=True, max_length=3000, null=True)),
                ('body_script', models.CharField(blank=True, max_length=3000, null=True)),
                ('mobile_only', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('hits', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.Company')),
            ],
            options={
                'db_table': 'Landing',
            },
        ),
    ]