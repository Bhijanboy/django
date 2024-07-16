from django.urls import path
from .views import*

urlpatterns=[
    path('create_person/',create_person,name='createperson'),
    path('edit_person/<int:id>/',edit_person,name='editperson'),
    path('delete_person/<int:id>/',delete_person,name='deleteperson')


]