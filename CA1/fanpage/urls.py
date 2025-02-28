from django.urls import path
from .views import HomePageView, AlbumsPageView, MoviesPageView

urlpatterns = [ 
    path('Movies/', MoviesPageView.as_view(), name='movies'),
    path('Albums/', AlbumsPageView.as_view(), name='albums'),
    path('', HomePageView.as_view(), name='home'),
]