from django.urls import path
from .views import *

urlpatterns = [
    path('author/<int:author_id>/', author_detail, name='author_detail'),
    path('all-quotes/', all_quotes, name='all_quotes'),
]