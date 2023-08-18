"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# urls.py

from django.urls import path
from app import views

urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("create/", views.create_contact, name="create_contact"),
    path("<int:pk>/", views.view_contact, name="view_contact"),
    path("<int:pk>/edit/", views.edit_contact, name="edit_contact"),
    path("<int:pk>/delete/", views.delete_contact, name="delete_contact"),
]
