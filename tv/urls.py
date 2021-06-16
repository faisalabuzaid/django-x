from django.urls import path
from .views import (
    TvListView,
    TvDetailView,
    TvCreateView,
    TvUpdateView,
    TvDeleteView
)

urlpatterns = [
    path('', TvListView.as_view(), name='tv_list'),
    path('<int:pk>/', TvDetailView.as_view(), name='tv_detail'),
    path('create/', TvCreateView.as_view(), name='tv_create'),
    path('<int:pk>/update/', TvUpdateView.as_view(), name='tv_update'),
    path('<int:pk>/delete/', TvDeleteView.as_view(), name='tv_delete')
]