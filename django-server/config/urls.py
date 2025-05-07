from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sample.urls')),  # http://www.localhost:8000/ -> sample app
    path('api/', include('api.urls')),  # http://www.localhost:8000/api/ -> api app
]
