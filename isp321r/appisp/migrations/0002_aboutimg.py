# Generated by Django 5.0.2 on 2024-02-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appisp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='aboutslider/')),
                ('img2', models.ImageField(upload_to='aboutslider/')),
                ('img3', models.ImageField(upload_to='aboutslider/')),
            ],
        ),
    ]