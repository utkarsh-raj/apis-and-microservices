# Generated by Django 2.1.5 on 2019-01-30 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default=1, max_length=1000)),
                ('duration', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=1, max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exerciseTracker.ExerciseUser'),
        ),
    ]
