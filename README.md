# drf_tutorials

Django Rest Framework tutorials

## Setting Up new enviroment

python -m venv venv

## Activate enviroment

.\venv\Scripts\Activate.ps1

pip list
python.exe -m pip install --upgrade pip
pip install -r requirements.txt

## Create django project

django-admin startpoject tutorials

cd tutorials

## Start App

python manage.py startapp snippets

## We'll need to add our new snippets app and the rest_framework app to INSTALLED_APPS. Let's edit the tutorial/settings.py file:

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'snippets',
]
```

## Create the migrations

```
python manage.py makemigrations snippets
python manage.py migrate snippets

```

## Test model and serializer

```
python manage.py shell
```

```
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

serializer = SnippetSerializer(snippet)
serializer.data
# {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
```
