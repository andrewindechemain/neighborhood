# Generated by Django 3.2.9 on 2021-11-03 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='health_tell',
            new_name='emergency_helpline',
        ),
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='police_number',
            new_name='police_contacts',
        ),
    ]
