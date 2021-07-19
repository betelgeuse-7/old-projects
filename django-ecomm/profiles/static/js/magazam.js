const cargoBtn = document.querySelectorAll(".cargo-btn");
const data = document.querySelectorAll(".data");

/*const siparisID = data.dataset.siparisid;
const csrf = data.dataset.csrf;
const userID = data.dataset.userid;
 */

const Kargola = (e) => {
    const siparisID = e.target.nextElementSibling.dataset.siparisid;
    const csrf = e.target.nextElementSibling.dataset.csrf;
    const userID = e.target.nextElementSibling.dataset.userid;

    body = {
        siparisID:siparisID,
        userID:userID
    }

    fetch('/kargola/', {
        "method":"POST",
        "headers":{
            "Accept": "application/json",
            "Content-Type":"application/json",
            "X-CSRFToken":csrf
        },
        "body": JSON.stringify(body)
    })
        .then(res => res.json())
            .then(data => console.log(data))

}


cargoBtn.forEach(btn => {
    btn.addEventListener('click', Kargola);
})




