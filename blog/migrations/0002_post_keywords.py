# Generated by Django 2.0.2 on 2018-02-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.CharField(default='AI, Startup, Robotics, Technology, Nepali', max_length=120, null=True),
        ),
    ]