# Installation
### Dependencies
* Python 3.8 or higher
* Django 3.2 or higher
* Git
# How to install
* Clone Repository by using: **git clone (newest link)**
# Running server
* Get to the folder with the terminal
* Then in the terminal type **py manage.py runserver**
# Tests to run
* To run tests get to the folder with the terminal
* Then in the terminal type **py manage.py test**
# API
### GET
* anime_viewing_response: This gets the data from the first Supabase API for anime viewing
* scoring_response: This gets data from the second Supabase API for scoring
* top_5: This gets data from the second Supabase API to get the top 5 animes based on scores
# Known Bugs
* Some anime titles with special characters may not be properly read.
* API rate limiting from the Jikan API may cause temporary data fetching issues.
# Future Road Map
* Fix encoding issues with special characters in anime titles.
* Add user authentication and profiles to save favorite anime lists.
* Enhance the search functionality with more filters.
* Add additional anime-related data sources.
