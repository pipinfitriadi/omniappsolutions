#!/usr/bin/env python

# Copyright (C) Pipin Fitriadi - All Rights Reserved

# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Pipin Fitriadi <pipinfitriadi@gmail.com>, 1 January 2025

from django.apps import AppConfig


class MovieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie'
