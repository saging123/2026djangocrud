from django.urls import path
from . import views

urlpatterns = [
    path('',views.list,name="product_list"),
    path('add',views.add,name="product_add")
]
