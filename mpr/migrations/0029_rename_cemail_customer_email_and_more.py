# Generated by Django 5.0.1 on 2024-04-15 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpr', '0028_remove_auctionroom_artistid_remove_auctionroom_uid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='cemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='customer_pimage',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='cname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='cphone',
            new_name='phone',
        ),
    ]
