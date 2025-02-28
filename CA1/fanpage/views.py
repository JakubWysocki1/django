from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'


class AlbumsPageView(TemplateView):
    template_name = 'albums.html'


class MoviesPageView(TemplateView):
    template_name = 'movies.html'