# Generated by Django 3.2.8 on 2022-06-03 12:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220528_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='plagiarismreport',
            name='token',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
