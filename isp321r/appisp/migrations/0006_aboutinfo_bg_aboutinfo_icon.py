# Generated by Django 5.0.2 on 2024-02-25 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appisp', '0005_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinfo',
            name='bg',
            field=models.ImageField(default=1, upload_to='bg/', verbose_name='Фон'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aboutinfo',
            name='icon',
            field=models.ImageField(default=0, upload_to='icon/', verbose_name='Иконка'),
            preserve_default=False,
        ),
    ]
