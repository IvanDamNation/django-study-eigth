from django.urls import path

from accounts.views import add_subscribe
from .views import PostList, PostDetail, PostSearch, PostAdd, PostUpdateView, PostDeleteView

from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', cache_page(60*5)(PostDetail.as_view()), name='PostDetail'),
    path('search/', PostSearch.as_view(), name='NewsSearch'),
    path('add/', PostAdd.as_view(), name='NewsAdd'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='NewsEdit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='NewsDelete'),
    path('subscribe/<int:pk>/', add_subscribe, name='subscribe'),
]
