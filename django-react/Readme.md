# Installation

> pip install virtualenv
> source venv/bin/activate
> python -m pip install django djangorestframework
> django-admin startproject [PROJECT_NAME]
> django-admin startapp [APP_NAME]

# Integration

> Install app via [PROJECT_NAME].settings.py in `INSTALLED_APPS`
> To be able to access you app, you need to add it on [PROJECT_NAME].urls.py
> In your [APP_name], create a file urls.py for your urls and declare functions in the views.py

# Development

> Fat models -> more logic
> Thin views

# Migrations

> python manage.py makemigrations
> python manage.py migrate
> Create serializers.py in [APP_NAME] directory -> this will translate model.py to a JSON format

# Troubleshooting

Running django - https://stackoverflow.com/questions/35184458/no-module-named-django-but-it-is-installed
