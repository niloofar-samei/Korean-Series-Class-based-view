from django import forms
from .models import Movie, Actress, Actor


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        exclude = ("voteup",)

        labels = {
            "movie_name": "movie_name",
            "released_year": "released_year",
            "movie_image": "movie_image",
            "movie_about": "movie_about",
        }


class ActressForm(forms.ModelForm):
    class Meta:
        model = Actress
        fields = "__all__"
        exclude = ("movie",)


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = "__all__"
        exclude = ("movie",)
