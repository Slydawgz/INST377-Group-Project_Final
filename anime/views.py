import requests
from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import AnimeSearchForm
from itertools import chain

# Fetch data from Supabase APIs
def fetch_anime_data():
    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmc3FvdWt4cHluYmJjeHVvenlyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTU3NjA3NTQsImV4cCI6MjAzMTMzNjc1NH0.aNpGGnO4w_90OL3iLR7H2OVWLLJeAIn5Izi1x4IN3H8',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmc3FvdWt4cHluYmJjeHVvenlyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTU3NjA3NTQsImV4cCI6MjAzMTMzNjc1NH0.aNpGGnO4w_90OL3iLR7H2OVWLLJeAIn5Izi1x4IN3H8'
    }
    
    # Fetch data from the first Supabase API for anime viewing
    anime_viewing_response = requests.get('https://bfsqoukxpynbbcxuozyr.supabase.co/rest/v1/anime', headers=headers)
    anime_viewing_data = anime_viewing_response.json() if anime_viewing_response.status_code == 200 else []

    # Fetch data from the second Supabase API for scoring
    scoring_response = requests.get('https://bfsqoukxpynbbcxuozyr.supabase.co/rest/v1/score', headers=headers)
    scoring_data = scoring_response.json() if scoring_response.status_code == 200 else []

    top_5 = requests.get('https://bfsqoukxpynbbcxuozyr.supabase.co/rest/v1/top_5', headers=headers)
    top_5_data = top_5.json() if top_5.status_code == 200 else []

    # Combine anime data with scoring data based on the common ID
    combined_data = []
    for anime in anime_viewing_data:
        anime_id = anime['id']
        anime_score = next((score['score'] for score in scoring_data if score['id'] == anime_id), None)
        combined_data.append({
            'id': anime_id,
            'title': anime['title'],
            'image_url': anime['image_url'],
            'score': anime_score
        })
    top_5_combined = []
    for anime in top_5_data:
        anime_id = anime['id']
        anime_score = next((score['score'] for score in scoring_data if score['id'] == anime_id), None)
        top_5_combined.append({
            'id': anime_id,
            'title': anime['title'],
            'image_url': anime['image_url'],
            'score': anime_score
        })

    return combined_data, top_5_combined

def anime_viewing_view(request):
    form = AnimeSearchForm(request.GET)

    anime_list, top_5_anime = fetch_anime_data()

    paginator = Paginator(anime_list, 25)  # Show 25 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Anime_viewing.html', {'page_obj': page_obj, 'top_5_anime': top_5_anime, 'form':form})

def anime_detail_view(request, anime_id):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}/full"
    response = requests.get(url)
    anime_data = response.json()

    context = {
        'anime_data': anime_data,
    }
    return render(request, 'Anime_details.html', context)

def help_view(request):
    return render(request, 'Help.html')

def Contact_us_view(request):
    return render(request, 'Contact_us.html')

def About_view(request):
    return render(request, 'About.html')

def search_anime_view(request):
    form = AnimeSearchForm(request.GET)
    combined_results = []
    next_page = None

    if form.is_valid():
        query = form.cleaned_data['query']
        page = request.GET.get('page', 1)
        url = f"https://api.jikan.moe/v4/anime?q={query}&page={page}"
        response = requests.get(url)
        data = response.json()
        search_results = data.get('data', [])
        pagination = data.get('pagination', {})
        has_next_page = pagination.get('has_next_page', False)
        
        if has_next_page:
            next_page = int(page) + 1

        # Fetch scoring data from Supabase API
        headers = {
            'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmc3FvdWt4cHluYmJjeHVvenlyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTU3NjA3NTQsImV4cCI6MjAzMTMzNjc1NH0.aNpGGnO4w_90OL3iLR7H2OVWLLJeAIn5Izi1x4IN3H8',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmc3FvdWt4cHluYmJjeHVvenlyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTU3NjA3NTQsImV4cCI6MjAzMTMzNjc1NH0.aNpGGnO4w_90OL3iLR7H2OVWLLJeAIn5Izi1x4IN3H8'
        }
        scoring_response = requests.get('https://bfsqoukxpynbbcxuozyr.supabase.co/rest/v1/score', headers=headers)
        scoring_data = scoring_response.json() if scoring_response.status_code == 200 else []

        # Match mal_id from search results to id from scoring data
        for anime in search_results:
            mal_id = anime.get('mal_id')
            score_entry = next((entry for entry in scoring_data if entry['id'] == mal_id), None)
            if score_entry is not None:
                anime['new_score'] = score_entry['score']
            combined_results.append(anime)

    context = {
        'form': form,
        'combined_results': combined_results,
        'next_page': next_page,
    }
    return render(request, 'search_form.html', context)


def anime_detail(request, anime_id):
    anime_url = f'https://api.jikan.moe/v4/anime/{anime_id}'
    anime_res = requests.get(anime_url)
    anime_data = anime_res.json()

    character_url = f'https://api.jikan.moe/v4/anime/{anime_id}/characters'
    character_res = requests.get(character_url)
    character_data = character_res.json()

    context = {
        'anime_data': anime_data,
        'character_data': character_data
    }

    return render(request, 'anime_details.html', context)
