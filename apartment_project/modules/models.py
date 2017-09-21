from django.db import models


class Cleaning(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    place = models.TextField(unique=True)  # This field type is a guess.
    responsible_user = models.ForeignKey('User', models.DO_NOTHING, db_column='responsible_user', unique=True)
    date_from = models.DateField()
    date_to = models.DateField()

    class Meta:
        managed = False
        db_table = 'cleaning'


class User(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.TextField(unique=True)  # This field type is a guess.
    password = models.TextField()  # This field type is a guess.
    avatar = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField()  # This field type is a guess.
    admin = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'user'
