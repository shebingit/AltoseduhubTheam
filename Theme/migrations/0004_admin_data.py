# Generated by Django 4.1 on 2023-07-11 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Theme', '0003_templates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_image', models.ImageField(blank=True, null=True, upload_to='categorie')),
                ('u_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('u_desig', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('u_password', models.CharField(blank=True, default=0, max_length=255, null=True)),
                ('u_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]