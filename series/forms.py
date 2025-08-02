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

        # This block helps to check if the new movie name already exists or not.
        # In class-based views, we have to use it to check.
        def clean_movie_name(self):
            name = self.cleaned_data["movie_name"]
            if Movie.objects.filter(movie_name__iexact=name).exists():
                raise form.ValidationError("Sorry but this movie already exists.")
            return name


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
