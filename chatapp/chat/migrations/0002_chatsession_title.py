# Generated by Django 2.2.2 on 2019-06-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatsession',
            name='title',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
    ]
