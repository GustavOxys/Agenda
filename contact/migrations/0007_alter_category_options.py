# Generated by Django 4.2.2 on 2023-06-28 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_category_contact_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
