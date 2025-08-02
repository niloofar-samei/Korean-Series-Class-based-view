from django.urls import path
from . import views
from series.views import (
    IndexListView,
    MovieCreateView,
    MovieDeleteView,
    MovieDetailView,
)

urlpatterns = [
    path("", IndexListView.as_view(), name="IndexListView"),
    path("movie/new/", MovieCreateView.as_view(), name="MovieCreateView"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="MovieDetailView"),
    path("movie/<int:pk>/delete/", MovieDeleteView.as_view(), name="MovieDeleteView"),
]
