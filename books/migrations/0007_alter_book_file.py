# Generated by Django 5.0 on 2023-12-20 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(upload_to='books/files'),
        ),
    ]