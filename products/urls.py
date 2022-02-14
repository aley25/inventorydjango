from django.urls import path
from django.urls.resolvers import URLPattern

from . import views
from users import views as userviews

urlpatterns = [
    path('brand/', views.brand),
    path('new/', views.product),
    path('', views.main),
]