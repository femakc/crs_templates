from django.urls import path
from . import views

app_name = 'message'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_message/', views.MessageView.as_view(), name='new_message'),
]
