# Generated by Django 2.1.4 on 2018-12-16 06:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bazaar', '0002_auto_20181216_1233'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meal',
            new_name='Bazaar',
        ),
    ]