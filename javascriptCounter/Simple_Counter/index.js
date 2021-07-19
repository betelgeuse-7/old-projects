const count = document.getElementById('count');
const decrease = document.getElementById('decrease');
const increase = document.getElementById('increase');
const reset = document.getElementById('reset');


decrease.addEventListener('click', decreaseCount);
reset.addEventListener('click', resetCounter);
increase.addEventListener('click', increaseCounter);


function decreaseCount(){
    count.style.color = 'red';
    count.textContent -= 1;
}

function resetCounter(){
    count.style.color = 'black';
    count.textContent = 0;
}

function increaseCounter(){
    count.style.color = 'green';
    count.textContent++;
}