# Generated by Django 4.1.7 on 2023-03-10 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_book', models.CharField(max_length=100)),
            ],
        ),
    ]