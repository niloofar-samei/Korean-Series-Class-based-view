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
    #    path("movie/<int:movie_id>/", views.movie, name="movie"),
    #    path("new/", views.new, name="new"),
    path("movie/new/", MovieCreateView.as_view(), name="MovieCreateView"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="MovieDetailView"),
    path("movie/<int:pk>/delete/", MovieDeleteView.as_view(), name="MovieDeleteView"),
    #    path("delete/<int:movie_id>", views.delete, name="delete"),
    #    path("voteup/<int:movie_id>", views.voteup, name="voteup"),
]
