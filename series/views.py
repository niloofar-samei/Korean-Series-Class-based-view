from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import F
from series.forms import ActorForm, ActressForm, MovieForm
from .models import Movie

from django.views.generic import ListView
from django.views import View


class IndexListView(ListView):
    model = Movie
    template_name = "series/index.html"
    context_object_name = "movies"


# def index(request):
#    movie_list = Movie.objects.all().order_by("-voteup")
#    return render(request, "series/index.html", {"movie_list": movie_list})


def movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    actor = movie.actor_set.all()
    actress = movie.actress_set.all()
    return render(
        request,
        "series/movie.html",
        {"movie": movie, "actor": actor, "actress": actress},
    )


class MovieCreateView(View):
    def get(self, request):
        return render(
            request,
            "series/new_movie_django_form.html",
            {
                "form_movie": MovieForm(),
                "form_actor": ActorForm(),
                "form_actress": ActressForm(),
            },
        )

    def post(self, request):
        movie_form = MovieForm(request.POST, request.FILES)
        actor_form = ActorForm(request.POST, request.FILES)
        actress_form = ActressForm(request.POST, request.FILES)

        if all([movie_form.is_valid(), actor_form.is_valid(), actress_form.is_valid()]):
            movie = movie_form.save()
            actress = actress_form.save()
            actress.movie = movie
            actress.save()
            actor = actor_form.save()
            actor.movie = movie
            actor.save()

            return redirect("IndexListView")

        return render(
            request,
            "series/new_movie_django_form.html",
            {
                "form_movie": MovieForm(),
                "form_actor": ActorForm(),
                "form_actress": ActressForm(),
            },
        )


# def new_django_form(request):
#    if request.method == "POST":
#        form_movie = MovieForm(request.POST, request.FILES)
#        form_actress = ActressForm(request.POST, request.FILES)
#        form_actor = ActorForm(request.POST, request.FILES)
#        if form_movie.is_valid() and form_actress.is_valid() and form_actor.is_valid():
#            movie = form_movie.save()
#
#            actress = form_actress.save(commit=False)
#            actress.movie = movie
#            actress.save()
#
#            actor = form_actor.save(commit=False)
#            actor.movie = movie
#            actor.save()
#
#            return redirect("index")
#        else:
#            form_movie = MovieForm()
#            form_actress = ActressForm()
#            form_actor = ActorForm()
#            return render(
#                request,
#                "series/new_django_form.html",
#                {
#                    "form_movie": form_movie,
#                    "form_actress": form_actress,
#                    "form_actor": form_actor,
#                },
#            )
#
#    else:
#        form_movie = MovieForm()
#        form_actress = ActressForm()
#        form_actor = ActorForm()
#    return render(
#        request,
#        "series/new_django_form.html",
#        {
#            "form_movie": form_movie,
#            "form_actress": form_actress,
#            "form_actor": form_actor,
#        },
#    )


def delete(request, movie_id):
    print(movie_id)
    selected_movie = Movie.objects.get(pk=movie_id)
    selected_movie.delete()
    return redirect("index")


def voteup(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.voteup = F("voteup") + 1
    movie.save()
    return redirect("index")
