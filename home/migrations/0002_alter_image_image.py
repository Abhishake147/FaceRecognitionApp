# Generated by Django 3.2.5 on 2021-07-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='C://Users//crazy//PycharmProjects//ImageformProject//media//img', verbose_name=models.CharField(max_length=100)),
        ),
    ]
