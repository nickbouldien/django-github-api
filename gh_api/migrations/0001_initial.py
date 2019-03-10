# Generated by Django 2.1.7 on 2019-03-10 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar_url', models.CharField(max_length=50)),
                ('blog', models.CharField(max_length=50)),
                ('bio', models.TextField(max_length=200)),
                ('company', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=50)),
                ('followers', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('public_gists', models.IntegerField(default=0)),
                ('public_repos', models.IntegerField(default=0)),
                ('url', models.CharField(max_length=50)),
                ('account_created_at', models.DateTimeField()),
                ('account_updated_at', models.DateTimeField()),
            ],
        ),
    ]