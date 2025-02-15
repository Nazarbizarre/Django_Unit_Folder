# Generated by Django 5.1.6 on 2025-02-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_author_book_isbn_book_price_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='bookstore.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='book',
            name='publishing_date',
            field=models.DateField(auto_now=True),
        ),
    ]
