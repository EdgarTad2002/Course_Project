# Generated by Django 4.2.11 on 2024-08-29 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='rate',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='CourseMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
