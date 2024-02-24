from django.urls import path
from pages import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("details/", views.project_index, name="project_index"),
    path('new/', views.newProject, name='NewGroup'),
    path("list/", views.project_list, name="project_list"),
    path("books/", views.books, name='books'),
    path('newCulture/', views.newCulture, name='NewGroup'),
    path('culture_list/', views.culture_list, name='NewGroup'),
    
]