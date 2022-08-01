# Generated by Django 4.0.6 on 2022-07-20 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_alter_profiles_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=1, upload_to='profiles'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profiles',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
