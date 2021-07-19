# Generated by Django 3.1.4 on 2021-01-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210102_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='urun',
            name='urun_resmi',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/urun_resimleri'),
        ),
        migrations.AddField(
            model_name='urun',
            name='urun_resmi_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]