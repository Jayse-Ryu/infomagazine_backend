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
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=40)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('landing_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Landing.Landing')),
            ],
        ),
    ]
