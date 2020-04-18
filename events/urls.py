from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.event_form, name='event_insert'), # get and post req. for insert operation
    path('<int:id>/', views.event_form, name='event_update'), # get and post req. for update operation
    path('delete/<int:id>/', views.event_delete, name='event_delete'),
    path('list/', views.event_list, name='event_list') # get req. to retrieve and display all records
]