# Generated by Django 3.2.7 on 2021-10-14 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210930_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]