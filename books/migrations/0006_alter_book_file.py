# Generated by Django 5.0 on 2023-12-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(upload_to='books'),
        ),
    ]
