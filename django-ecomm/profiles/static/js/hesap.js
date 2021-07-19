const teslimBtns = document.querySelectorAll('.teslim-alindi');


const teslimAl = (e) => {
    const urunID = e.target.dataset.urunid;
    const saticiID = e.target.dataset.saticiid;
    const siparisID = e.target.dataset.siparisid;
    const adet = e.target.dataset.adet;

    const csrf = e.target.dataset.csrf;

    const body = {
        urunID:urunID,
        saticiID:saticiID,
        siparisID: siparisID,
        adet:adet
    } 

    fetch('/teslim-al/', {
        "method":"POST",
        "headers":{
            "Accept":"application/json",
            "Content-Type":"application/json",
            "X-CSRFToken": csrf
        },
        "body": JSON.stringify(body)
    })
        .then(res => res.json())
            .then(data => console.log(data)); 

}




teslimBtns.forEach((btn) => {
    btn.addEventListener('click', teslimAl);
})





