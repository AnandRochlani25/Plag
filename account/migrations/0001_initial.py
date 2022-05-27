# Generated by Django 4.0.4 on 2022-05-27 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordHtml',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_1', models.CharField(max_length=15)),
                ('student_2', models.CharField(max_length=15)),
                ('similarity_code', models.FloatField()),
                ('similarity_ids', models.FloatField()),
                ('similarity_classes', models.FloatField()),
                ('similarity_content', models.FloatField()),
                ('similarity_type', models.FloatField()),
                ('similarity_value', models.FloatField()),
                ('similatity_hrefs', models.FloatField()),
                ('similarity_srcs', models.FloatField()),
                ('similarity_others', models.FloatField()),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.report')),
            ],
        ),
    ]