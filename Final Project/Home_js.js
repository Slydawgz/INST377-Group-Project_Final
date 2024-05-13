function loadAnime() {
    return fetch(`https://api.jikan.moe/v4/anime`)
    .then((res) => res.json())
    .then(data => {console.log(data)})
    .catch(error => console.log(error));
}

window.onload = loadAnime;