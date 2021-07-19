const myAcc = document.getElementById('my-acc');
const accDropDown = document.querySelector('.acc-dropdown');


const showAccInfo = () => {
    accDropDown.classList.remove('hidden');
}

const hideAccInfo = () => {
    accDropDown.classList.add('hidden');
}

myAcc.addEventListener('mouseover', showAccInfo);
accDropDown.addEventListener('mouseover', showAccInfo);
accDropDown.addEventListener('mouseout', hideAccInfo);

