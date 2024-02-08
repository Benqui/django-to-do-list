from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.logout_usr,name='logout'),
    path('register/',views.register_usr,name='register'),
    path('add_task/',views.add_task,name='add_task'),
    path('task/<int:pk>',views.tasko,name='task'),
    path('del_task/<int:pk>',views.del_task,name='del_task'),
    path('edit_task/<int:pk>',views.edit_task,name='edit_task'),
]