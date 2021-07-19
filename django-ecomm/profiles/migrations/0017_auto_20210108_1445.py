# Generated by Django 3.1.4 on 2021-01-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20210108_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('username', models.CharField(max_length=60, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='magaza',
            name='e_mail',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='magaza',
            name='sifre',
            field=models.CharField(default='sifre', max_length=100, verbose_name='Şifre'),
        ),
    ]
