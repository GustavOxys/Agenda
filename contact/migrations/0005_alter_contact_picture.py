# Generated by Django 4.2.2 on 2023-06-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_contact_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='picture',
            field=models.ImageField(blank=True, upload_to='picture/%Y/%m/'),
        ),
    ]
