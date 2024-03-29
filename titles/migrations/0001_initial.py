# Generated by Django 3.0.5 on 2020-11-27 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('genres', '0002_auto_20201127_0243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('year', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='categories.Category')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='genres.Genre')),
            ],
        ),
    ]
