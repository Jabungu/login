# Generated by Django 2.2.4 on 2021-03-01 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('Address_Line_1', models.CharField(max_length=40)),
                ('Address_Line_2', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=30)),
                ('State', models.CharField(max_length=20)),
                ('Zip', models.IntegerField(max_length=40)),
                ('Country', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=45, null=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=45, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('connections', models.ManyToManyField(blank=True, to='login.User')),
            ],
        ),
    ]