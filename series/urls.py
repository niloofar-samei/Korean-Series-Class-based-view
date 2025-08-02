from django.urls import path
from . import views

urlpatterns = [
    path("", IndexListView.as_view(), name="IndexListView"),
    #    path("movie/<int:movie_id>/", views.movie, name="movie"),
    #    path("new/", views.new, name="new"),
    #    path("new_django_form", views.new_django_form, name="new_django_form"),
    #    path("delete/<int:movie_id>", views.delete, name="delete"),
    #    path("voteup/<int:movie_id>", views.voteup, name="voteup"),
]
