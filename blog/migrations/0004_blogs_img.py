# Generated by Django 2.2.1 on 2019-05-21 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190520_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='img',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.UploadImage', verbose_name='封面'),
        ),
    ]
