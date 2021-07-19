const games = [
    {
        name: 'Cyberpunk 2077',
        release_date: '2020',
        genre: 'RPG',
        img: 'https://media.comicbook.com/2020/11/cyberpunk-2077-logo-2-1245840-1280x0.jpeg',
        developer: 'CD Projekt',
        metascore: '86',
        summary: 'Cyberpunk 2077 is an open-world, action-adventure story set in Night City, a megalopolis obsessed with power, glamour and body modification. Assume the role of V, a mercenary outlaw going after a one-of-a-kind implant that is the key to immortality. You can customize your character’s…'
    },
    {
        name: 'The Long Dark',
        release_date: '2014',
        genre: 'Survival',
        img: 'https://s3.gaming-cdn.com/images/products/521/orig/the-long-dark-cover.jpg',
        developer: 'Hinterland Studio',
        metascore: '77',
        summary: ' Imagine the lights go out, never to return. Bright aurora flare across the sky, and all humanity’s technological might is laid to waste, neutralized in a kind of quiet apocalypse. Everything that has shielded humanity from the disinterested power of Mother Nature is suddenly wrenched from…'
    },
    {
        name: 'Metro: Last Light',
        release_date: '2013',
        genre: 'Survival Horror',
        img: 'https://m.media-amazon.com/images/I/51Gtg6kXIZL._SY445_.jpg',
        developer: '4A Games',
        metascore: '82',
        summary: 'The year is 2034. Beneath the rubble of post-apocalyptic Moscow, in the tunnels of the Metro, the remnants of our species are besieged by deadly threats. Mutants stalk the catacombs beneath the desolate surface, and hunt amidst the poisoned skies above. But rather than stand united, the…'
    },
    {
        name: 'The Legend of Zelda: Breath of the Wild',
        release_date: '2017',
        genre: 'Adventure',
        img: 'https://images-na.ssl-images-amazon.com/images/I/91jvZUxquKL._AC_SY445_.jpg',
        developer: 'Nintendo',
        metascore: '97',
        summary: 'Forget everything you know about The Legend of Zelda games. Step into a world of discovery, exploration and adventure in The Legend of Zelda: Breath of the Wild, a boundary-breaking new game in the acclaimed series. Travel across fields, through forests and to mountain peaks as you discover…'
    },
    {
        name: 'Kingdom Come: Deliverance',
        release_date: '2018',
        genre: 'RPG',
        img: 'https://i1.wp.com/www.oyunindir.club/wp-content/uploads/2018/02/kingsdom.jpg?resize=400%2C570',
        developer: 'Warhorse Studios',
        metascore: '76',
        summary: 'Kingdom Come: Deliverance is an open world, action-adventure, role-playing game featuring blockbuster production values, a nonlinear story and revolutionary, first-person melee combat.'
    }
]

const container = document.getElementById('container');
const p_card = document.getElementById('card');
const p_name = document.getElementById('name');
const p_metascore = document.getElementById('metascore');
const p_releaseDate = document.getElementById('release-date');
const p_genre = document.getElementById('genre');
const imgTag = document.getElementById('img');
const p_developer = document.getElementById('developer');
const p_summary = document.getElementById('summary');

const arrow = document.querySelectorAll('.arrow');

const prev = document.getElementById('previous');
const next = document.getElementById('next');

const gameList = games.map((game)=>game);

let current = 1;

prev.addEventListener('click', decCurrent);
next.addEventListener('click', incCurrent);

function setItems(index){
    p_name.textContent = gameList[index].name;
    p_metascore.textContent = gameList[index].metascore;
    p_releaseDate.textContent = gameList[index].release_date;
    p_genre.textContent = gameList[index].genre;
    imgTag.src = gameList[index].img;
    p_developer.textContent = gameList[index].developer;
    p_summary.textContent = gameList[index].summary;
}

function decCurrent(){
    current--;
    if(current===0){
        prev.style.display = 'none';
    }
    if(current<gameList.length-1){
        next.style.display = 'block';
    }
    setItems(current);
}

function incCurrent(){
    current++;
    setItems(current);
    if(current>0){
        prev.style.display = 'block';
    }
    if(current===gameList.length-1){
        next.style.display = 'none';
    }
}


setItems(current)