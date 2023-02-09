"""DEVOPS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from home import views

urlpatterns = [
    path('', views.home,name='home'),
    path('home/', views.home,name='home'),
    path('pet', views.pet,name='pet'),
    path('men/', views.men,name='men'),
    path('women/', views.women,name='women'),
    path('kids/', views.kids,name='kids'),
    path('appliances/', views.appliances,name='appliances'),
    path('electronics/', views.electronics,name='electronics'),
    path('con/',views.con,name='contact us'),
    path('padmin/',views.padmin,name="product admin"),
    path('product/<str:pid>',views.product,name='Product'),

]



