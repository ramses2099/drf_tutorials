from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LANGUAGES_CHOICES, STYLE_CHOICES, Snippet


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
   
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'language', 'style','owner']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields =['id', 'username','snippets'] 
