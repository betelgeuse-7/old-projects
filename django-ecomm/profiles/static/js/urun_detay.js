const addToCartBtn = document.getElementById('add-to-cart');
const buyBtn = document.getElementById('buy');

const data = document.getElementById('data');

const csrfToken = data.dataset.csrf;
const userID = data.dataset.user;
const saticiID = data.dataset.seller;

const btnsDiv = document.querySelector('.btns');

const addToCart = (e) => {
    const id = e.target.dataset.urunid;

    console.log(`/sepete-ekle/${id}/`);
    //console.log(csrfToken, user);

    const body = {
        user: userID,
    }

    fetch(`/sepete-ekle/${id}/`, {
        "method": "POST",
        "headers": {
            "Accept": "application/json",
            "Content-Type":"application/json",
            "X-CSRFToken": csrfToken
        },
        "body": JSON.stringify(body)
    }).then(res => res.json()).then(data => btnsDiv.innerHTML +=`
                                                <small>${data['msg']}</small>                                            
    `);
    

    console.log(JSON.stringify(body));
}

const adet = document.getElementById('adet');



if (addToCartBtn){
    addToCartBtn.addEventListener('click', addToCart);
}
