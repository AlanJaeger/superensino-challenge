# Generated by Django 3.2 on 2022-06-29 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220628_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercises', models.ManyToManyField(blank=True, related_name='exercise_list', to='core.Exercise')),
            ],
        ),
    ]