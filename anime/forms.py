from django import forms

class AnimeSearchForm(forms.Form):
    query = forms.CharField(label='Search Anime', max_length=100)
