function loadAnimeData() {
    fetch(`https://api.jikan.moe/v4/anime?q=Naruto`) //for testing purposes
        .then((res) => res.json())
        .then(data => {
            console.log(data); 
        })
        .catch(error => console.log(error));
}


// Function to fetch and display top 5 airing anime
//NOTE: This now retreives the top 5 (if you uncomment window.onload, but it's duplicated multiple times. Need to fix.
function displayTop5AiringAnime() {
    fetch(`https://api.jikan.moe/v4/anime?airing=true`)
    .then((res) => res.json())
    .then(data => {

        myArr = []
        allAnimeImages.innerHTML = '';
        Object.values(data.data).forEach(anime => {
            

            imageTitle = anime.title;
            imageUrl = anime.images.jpg.image_url;
            animeRank = anime.rank;
            
            const img = new Image();
            img.src = imageUrl;
            allAnimeImages.append(img);
            allAnimeImages.append(imageTitle);

            const arrItem = {
                title: imageTitle,
                link: imageUrl,
                rank: animeRank
            }
            myArr.push(arrItem);
    
        myArr.sort((a,b) => a.rank - b.rank);
        topFive = myArr.slice(0,5);

        fiveAnimeImages.innerHTML = '';
        Object.values(topFive).forEach(anime => {
            console.log(anime);
                imageTitle = anime.title;
                imageUrl = anime.link;
                
                const img = new Image();
                img.src = imageUrl;
                allAnimeImages.append(img);
                allAnimeImages.append(imageTitle);
                
                //console.log(img)
        })  
        });
    })
    .catch(error => console.log(error));
}


// Function to fetch and display all airing anime
//NOTE: This now works, just need to do CSS and/or put this on the image slider 
function showAllAiringAnime() {
    fetch(`https://api.jikan.moe/v4/anime?airing=true`)
        .then((res) => res.json())
        .then(data => {

            showAllText.innerHTML = 'All Airing Anime';

            allAnimeImages.innerHTML = '';
            Object.values(data.data).forEach(anime => {
                

                console.log(anime);
                imageTitle = anime.title;
                imageUrl = anime.images.jpg.image_url;
                
                const img = new Image();
                img.src = imageUrl;
                allAnimeImages.append(img);
                allAnimeImages.append(imageTitle);
                
                
                console.log(img)
                
            });
        })
        .catch(error => console.log(error));
}

//window.onload = displayTop5AiringAnime, loadAnimeData;

