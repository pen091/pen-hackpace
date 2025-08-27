from django.urls import path
from . import views

app_name = 'hackspace_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<slug:slug>/', views.topic_detail, name='topic_detail'),
]
