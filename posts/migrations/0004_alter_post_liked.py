# Generated by Django 4.1 on 2022-09-28 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_picture'),
        ('posts', '0003_alter_post_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='like', to='accounts.profile'),
        ),
    ]