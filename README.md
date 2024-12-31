<!--
Copyright (C) Pipin Fitriadi - All Rights Reserved

Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Pipin Fitriadi <pipinfitriadi@gmail.com>, 31 December 2024
-->

# How to Run This Webapp

- Run this sequences command on your Unix-like Terminal, only for setup at the first time:

    ```sh
    python3 -m venv venv/
    . venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    python -c 'from django.core.management.utils import get_random_secret_key; print(f"SECRET_KEY='"'"'{get_random_secret_key()}'"'"'")' > .env
    ```

- Run this command on your Unix-like Terminal, everytime Webapp need to run locally:

    ```sh
    python manage.py runserver
    ```

> [!IMPORTANT]
> Local webapp can be access at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
