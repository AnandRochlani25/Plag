# Generated by Django 3.2.8 on 2022-06-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_plagiarismreport_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plagiarismreport',
            name='token',
            field=models.CharField(max_length=100000),
        ),
    ]