from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),   # admin panel
    path('', include('core.urls')),    # connect your app
]