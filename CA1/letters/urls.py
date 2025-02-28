from django.urls import path
from .views import(
    LetterListView,
    LetterUpdateView,
    LetterDetailView,
    LetterDeleteView,
    LetterCreateView,
    CreateCommentView
)


urlpatterns = [
    path('<int:pk>/edit/', LetterUpdateView.as_view(), name='letter_edit'),
    path('<int:pk>/', LetterDetailView.as_view(), name='letter_detail'),
    path('<int:pk>/edit/', LetterUpdateView.as_view(), name='letter_edit'),
    path('<int:pk>/delete/', LetterDeleteView.as_view(), name='letter_delete'),
    path('commentnew/', CreateCommentView.as_view(), name='comment_new'),
    path('new/', LetterCreateView.as_view(), name='letter_new'),
    path('', LetterListView.as_view(), name='letter_list'),
]