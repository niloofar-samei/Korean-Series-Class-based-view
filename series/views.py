from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import F
from django.urls import reverse_lazy
from series.forms import ActorForm, ActressForm, MovieForm
from .models import Movie

from django.views.generic import DeleteView, DetailView, ListView, DetailView
from django.views import View


class IndexListView(ListView):
    model = Movie
    template_name = "series/index.html"
    context_object_name = "movies"
    ordering = ["-voteup"]


class MovieDetailView(DetailView):
    model = Movie
    template_name = "series/movie.html"
    context_object_name = "movie"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.object
        context["actress"] = movie.actress_set.all()
        context["actor"] = movie.actor_set.all()
        return context


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


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy("IndexListView")

    # This block helps to delete without ask for confirmation.
    def get(self, rquest, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)


# def voteup(request, movie_id):
#    movie = get_object_or_404(Movie, pk=movie_id)
#    movie.voteup = F("voteup") + 1
#    movie.save()
#    return redirect("index")
