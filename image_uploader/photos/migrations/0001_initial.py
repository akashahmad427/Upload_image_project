# Generated by Django 4.1.7 on 2023-07-08 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='My_image')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
