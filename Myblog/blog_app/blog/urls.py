from django.urls import path
from . import views
from .views import UserListView

urlpatterns = [
    path('', views.connect, name='connect'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('inscription/', views.singin, name='singin'),
    path('index/', views.bonjour, name='home'),
    path('modifier/<int:user_id>', views.modifier, name=''),
    path('supprimer/<int:user_id>', views.supprimer, name='supprimer'),
    path('poste_form/', views.creat_post, name='creat_post'),
    path('affichage/', views.see_postes, name='affichage'),
]