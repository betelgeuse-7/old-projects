# Generated by Django 3.1.4 on 2021-01-08 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_auto_20210108_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='magaza',
            name='e_mail',
        ),
        migrations.RemoveField(
            model_name='magaza',
            name='sifre',
        ),
        migrations.AddField(
            model_name='magaza',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.customuser'),
        ),
    ]
