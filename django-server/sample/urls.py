from django.urls import path
from .views import index

# http://www.localhost:8000/
urlpatterns = [
    path('', index, name='sample-index'),  # http://www.localhost:8000/ -> index
]
