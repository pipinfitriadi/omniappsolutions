#!/usr/bin/env python

# Copyright (C) Pipin Fitriadi - All Rights Reserved

# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Pipin Fitriadi <pipinfitriadi@gmail.com>, 1 January 2025

from django.db import models


# Create your models here.
class Movie(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    img_path = models.TextField()
    duration = models.SmallIntegerField()
    genre = models.JSONField(default=list)
    language = models.TextField()
    mpaa_rating = models.JSONField(default=dict)
    user_rating = models.TextField()
