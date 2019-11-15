# Generated by Django 2.2.7 on 2019-11-14 21:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GhostPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ghostTitle', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=280)),
                ('is_boast', models.BooleanField()),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
