# Generated by Django 2.1.7 on 2019-03-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.TextField()),
                ('shortened', models.CharField(max_length=30)),
            ],
        ),
    ]
