# Generated by Django 3.2 on 2021-04-27 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
    ]
