# Generated by Django 2.2 on 2019-06-04 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instafish', '0003_auto_20190604_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='achievement',
            new_name='achievements',
        ),
    ]