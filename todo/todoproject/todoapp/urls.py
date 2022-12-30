from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [

    path('',views.demo,name='demo'),
    #path('details',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:up_id>/',views.update,name='update'),
    path('listview/',views.listviewhome.as_view(),name='listview'),
path('detailview/<int:pk>/',views. Detailviewhome.as_view(),name='detailview'),
path('updateview/<int:pk>/',views. updateview.as_view(),name='updateview'),
path('deleteview/<int:pk>/',views. deleteview.as_view(),name='deleteview'),


]