# Generated by Django 3.0.10 on 2020-11-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0008_auto_20201101_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='items_onsale',
        ),
        migrations.AddField(
            model_name='client',
            name='items_onsale',
            field=models.ManyToManyField(blank=True, to='bidding.Sinfo'),
        ),
    ]