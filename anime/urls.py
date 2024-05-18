from django.urls import path
from . import views

urlpatterns = [
    path('', views.anime_viewing_view, name='Home'),
    path('animedetails/<int:anime_id>/', views.anime_detail_view, name='anime_detail'),
    path('about/', views.About_view, name='About'),
    path('help/', views.help_view, name='Help'),
    path('ContactUs/', views.Contact_us_view, name='Contact_us'),
    path('SearchAnime', views.search_anime_view, name='search_anime'),
    path('anime/<int:anime_id>/', views.anime_detail, name='anime_detail'),
]