# Generated by Django 5.1.6 on 2025-02-12 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('publishing_date', models.DateField()),
                ('type', models.CharField(choices=[('P', 'Paper'), ('E', 'Electronic')], default='P', max_length=1)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='bookstore.genre')),
            ],
            options={
                'ordering': ['title'],
                'indexes': [models.Index(fields=['title'], name='bookstore_b_title_92b564_idx')],
            },
        ),
    ]
