"""
URL configuration for botiga_grupJ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework import routers

from cataleg import views as cataleg_views
from pagaments import views as pagaments_views
from carreto import views as carreto_views
from comandes import views as comandes_views



router = routers.DefaultRouter()
router.register(r'users', cataleg_views.UserViewSet)
router.register(r'groups', cataleg_views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('pagament/', pagaments_views.pagaments, name="pagament"),
    path('pagament/<int:pk>/', pagaments_views.update_delete_pagament, name="update_pagament"),
    path('cataleg/', cataleg_views.cataleg, name='cataleg'),
    path('cataleg/<int:pk>/', cataleg_views.update_delete_cataleg, name="update_producte"),
    path('carreto/', carreto_views.Cart , name="carreto"),
    path('carreto/<int:carrito_id>/', carreto_views.CartModify , name="carreto"),
    path('comanda/', comandes_views.comanda_list , name="comanda"),


]