# Generated by Django 3.2.6 on 2022-05-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Child', '0024_rename_name_customer_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daycare',
            name='approved',
            field=models.BooleanField(default=True, verbose_name='Approved'),
        ),
    ]