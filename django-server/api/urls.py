from django.urls import path
from .views import HelloWorldView

# http://www.localhost:8000/api/*
urlpatterns = [
    # http://www.localhost:8000/api/helloworld/
    path('helloworld/', HelloWorldView.as_view(), name='api-helloworld'),
]
