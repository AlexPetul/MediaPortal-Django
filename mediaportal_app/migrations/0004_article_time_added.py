# Generated by Django 2.2.4 on 2019-10-12 09:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mediaportal_app', '0003_auto_20191012_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='time_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
