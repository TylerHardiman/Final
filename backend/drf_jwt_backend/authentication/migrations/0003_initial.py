# Generated by Django 4.0.4 on 2022-04-20 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('experiences', models.CharField(default='', max_length=256)),
                ('interests', models.CharField(default='', max_length=256)),
                ('image', models.ImageField(upload_to='')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
