# Generated by Django 3.0.7 on 2020-07-09 09:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('building', models.CharField(max_length=50)),
                ('number_floors', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=1)])),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='floor',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(limit_value=1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='device',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='device.Location'),
        ),
    ]
