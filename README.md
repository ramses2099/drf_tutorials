# drf_tutorials

Django Rest Framework tutorials

# Setting Up new enviroment

python -m venv venv

# Activate enviroment

.\venv\Scripts\Activate.ps1

pip list
python.exe -m pip install --upgrade pip
pip install -r requirements.txt

# Create django project

django-admin startpoject tutorials

cd tutorials

# Start App

python manage.py startapp snippets

# We'll need to add our new snippets app and the rest_framework app to INSTALLED_APPS. Let's edit the tutorial/settings.py file:

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'snippets',
]
```
