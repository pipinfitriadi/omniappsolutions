#!/usr/bin/env python

# Copyright (C) Pipin Fitriadi - All Rights Reserved

# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Pipin Fitriadi <pipinfitriadi@gmail.com>, 1 January 2025

import json

from django.db import transaction
from django.shortcuts import get_object_or_404, render

from .models import Movie


def index(request):
    return render(request, "index.html", {"data": Movie.objects.all()})


def detail(request, movie_id):
    return render(
        request,
        "detail.html",
        {"movie": get_object_or_404(Movie, pk=movie_id)}
    )


def json_to_db():
    with open("movies.json") as file:
        with transaction.atomic():
            for row in json.load(file):
                Movie(**{
                    {
                        "imgPath": "img_path",
                        "mpaaRating": "mpaa_rating",
                        "userRating": "user_rating"
                    }.get(key, key): value
                    for key, value in row.items()
                }).save()
