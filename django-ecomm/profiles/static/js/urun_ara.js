const prodSearch = document.getElementById('prod-search');
const prodSearchBtn = document.getElementById('prod-search-btn');

const csrf = prodSearch.dataset.csrf;


const sendQuery = () => {
    const query = prodSearch.value;

    console.log(query);

    if(query !== ''){
        fetch(`/urun-ara/${query}/`, {
            "method":"POST",
            "headers":{
                "Accept":"application/json",
                "Content-Type":"application/json",
                "X-CSRFToken": csrf
            },
        });
    }
}




prodSearchBtn.addEventListener('click', sendQuery);

