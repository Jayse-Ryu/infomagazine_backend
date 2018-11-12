# Generated by Django 2.1.2 on 2018-11-07 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('landing_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Landing.Landing')),
            ],
            options={
                'db_table': 'Files',
            },
        ),
    ]
