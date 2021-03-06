# Generated by Django 3.0.3 on 2020-03-15 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="address",
            field=models.CharField(default="", max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="baths",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="bedrooms",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="beds",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="check_in",
            field=models.TimeField(default="00:00:00"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="check_out",
            field=models.TimeField(default="00:00:00"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="city",
            field=models.CharField(default="", max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="country",
            field=django_countries.fields.CountryField(default="", max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, default="2020-01-01 00:00:00"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="description",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="guests",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="host",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="instant_book",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="room",
            name="name",
            field=models.CharField(default="", max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="price",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="room",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
