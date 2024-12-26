from django.urls import path

from snippets import views

urlpatterns = [
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/',views.SnippetHighlight.as_view())    
]