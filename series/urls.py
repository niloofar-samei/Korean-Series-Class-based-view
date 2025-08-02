from django.urls import path
from . import views
from series.views import (
    IndexListView,
    MovieCreateView,
)

urlpatterns = [
    path("", IndexListView.as_view(), name="IndexListView"),
    #    path("movie/<int:movie_id>/", views.movie, name="movie"),
    #    path("new/", views.new, name="new"),
    path("movie/new/", MovieCreateView.as_view(), name="MovieCreateView"),
    #    path("delete/<int:movie_id>", views.delete, name="delete"),
    #    path("voteup/<int:movie_id>", views.voteup, name="voteup"),
]
