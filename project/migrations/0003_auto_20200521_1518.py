# Generated by Django 3.0.3 on 2020-05-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_award_edit_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='award',
            name='folder_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='awards',
            name='folder_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
