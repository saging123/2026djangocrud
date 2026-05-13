from django.contrib import admin
from django.urls import path,include

#crudproject/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
     path('crud/', include('crudapp.urls')),
]
