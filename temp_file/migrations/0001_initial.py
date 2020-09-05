# Generated by Django 3.0.5 on 2020-08-29 17:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DB_model',
            fields=[
                ('userName', models.CharField(max_length=100, null=True)),
                ('userID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('textLen', models.TextField()),
                ('retweetsCount', models.TextField()),
                ('favoriteCount', models.TextField()),
                ('source', models.TextField()),
                ('language', models.TextField()),
                ('favourited', models.TextField()),
                ('retweeted', models.TextField()),
                ('userLocation', models.TextField()),
                ('URL', models.URLField()),
                ('userfollowers_count', models.TextField()),
                ('userfriends_count', models.TextField()),
                ('userListed_count', models.TextField()),
                ('userFavorites_count', models.TextField()),
                ('userStatuses_count', models.TextField()),
                ('userVerified', models.TextField()),
                ('userProtected', models.TextField()),
                ('sentiment', models.IntegerField(default=-4)),
                ('predictedlabel', models.IntegerField(default=-4)),
                ('flag', models.IntegerField(default=-1)),
                ('userHomelink', models.URLField(default='https://twitter.com/')),
                ('user_profileImg', models.URLField(default='https://twitter.com/')),
                ('topics', models.CharField(default='covid', max_length=100, null=True)),
            ],
        ),
    ]
