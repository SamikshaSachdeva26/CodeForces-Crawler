# Generated by Django 2.0.7 on 2020-05-29 23:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20200530_0517'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='chat',
            unique_together={('user1', 'user2')},
        ),
    ]
