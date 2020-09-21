from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoIndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.TodoDetailView.as_view(), name='detail'),
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('create/<str:status>/', views.TodoCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='delete'),
]