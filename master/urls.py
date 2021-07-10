
from django.urls import path
 
from .views import Create, Delete, Detail, Index, Update

urlpatterns = [
     
    path('',Index.as_view(),name='index'),
   
    path('task/<int:pk>/',Detail.as_view(),name='detail'),
    path('task-create/',Create.as_view(),name='create'),
    path('task-update/<int:pk>/',Update.as_view(),name='update'),
    path('task-delete/<int:pk>/',Delete.as_view(),name='delete'),
]
