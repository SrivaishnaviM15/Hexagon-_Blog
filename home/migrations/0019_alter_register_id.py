# Generated by Django 4.2.3 on 2023-07-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]