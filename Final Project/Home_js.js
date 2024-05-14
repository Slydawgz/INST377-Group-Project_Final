function loadAnimeData() {
    fetch(`https://api.jikan.moe/v4/anime?q=Naruto`) //for testing purposes
        .then((res) => res.json())
        .then(data => {
            console.log(data); 
        })
        .catch(error => console.log(error));
}


// Function to fetch and display top 5 airing anime
function displayTop5AiringAnime() {
    fetch(`https://api.jikan.moe/v4/anime?airing=true`)
        .then((res) => res.json())
        .then(data => {
            console.log(data)
            const animeImagesContainer = document.querySelector('.animeImages');
            animeImagesContainer.innerHTML = '';

            for (let i = 0; i < 5; i++) {
                const anime = data[i];

                const image = document.createElement('img');
                image.src = anime.images.jpg.image_url;
                //image.alt = anime.titles[0].title;
                animeImagesContainer.appendChild(image);

                const title = document.createElement('p');
                title.textContent = anime.titles[0].title;
                animeImagesContainer.appendChild(title);
            }
        })
        .catch(error => console.log(error));
}

// Function to fetch and display all airing anime
function showAllAiringAnime() {
    fetch(`https://api.jikan.moe/v4/anime?airing=true`)
        .then((res) => res.json())
        .then(data => {
            const animeImagesContainer = document.querySelector('.animeImages');
            animeImagesContainer.innerHTML = '';

            data.forEach(anime => {
                const image = document.createElement('img');
                image.src = anime.images.jpg.image_url;
                image.alt = anime.titles[0].title;
                animeImagesContainer.appendChild(image);

                const title = document.createElement('p');
                title.textContent = anime.titles[0].title;
                animeImagesContainer.appendChild(title);
            });
        })
        .catch(error => console.log(error));
}

window.onload = displayTop5AiringAnime;

