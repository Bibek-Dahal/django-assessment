# Generated by Django 5.0.4 on 2024-04-08 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0002_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='roles', to='user_account.role'),
        ),
    ]