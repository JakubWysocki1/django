from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Letter, Comment

class LetterListView(ListView):
    model = Letter
    template_name = 'letter_list.html'

class LetterDetailView(DetailView):
    model = Letter
    template_name = 'letter_detail.html'


class LetterUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Letter
    fields = ('title', 'body',)
    template_name = 'letter_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class LetterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Letter
    template_name = 'letter_delete.html'
    success_url = reverse_lazy('letter_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class LetterCreateView(LoginRequiredMixin,CreateView):
    model = Letter
    fields = ('title', 'body')
    template_name = 'letter_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreateCommentView(CreateView):
    model = Comment
    fields = ('letter','comment','author')
    template_name = 'comment_new.html'
    success_url = reverse_lazy('letter_list')
  
    

