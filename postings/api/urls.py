from django.urls import path
from .view import BlogPostRudView, BlogPostAPIView

app_name = 'postings'

urlpatterns = [
    path('', BlogPostAPIView.as_view(), name='post-create'),
    path('<int:pk>/', BlogPostRudView.as_view(), name='post-rud')
]
