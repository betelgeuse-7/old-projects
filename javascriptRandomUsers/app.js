const divContainer = document.getElementById('container');
const cardDiv = document.getElementById('card');
const picture = document.getElementById('picture');
const info = document.getElementById('info');

const nameIcon = document.getElementById('nameIcon');
const ageIcon = document.getElementById('ageIcon');
const genderIcon = document.getElementById('genderIcon');
const emailIcon = document.getElementById('emailIcon');
const usernameIcon = document.getElementById('usernameIcon');
const passwordIcon = document.getElementById('passwordIcon');
const numberIcon = document.getElementById('numberIcon');
const locationIcon = document.getElementById('locationIcon');

const randomButton = document.getElementById('random');

randomButton.addEventListener('click', getUserInfo);

function getUserInfo(){
    fetch('https://randomuser.me/api')
    .then((res) => res)
    .then((data) => data.json())
    .then((users) => {
        let list = users;
        userList = list.results.map((user) => user);
        l = userList[0];
        picture.src = l.picture.large;
        let genderVar = l.gender.charAt(0).toUpperCase() + l.gender.slice(1);
        info.innerHTML = `My name <div class = 'line'></div>${l.name.title} ${l.name.first} ${l.name.last}`

        nameIcon.addEventListener('mouseover', setName);
        ageIcon.addEventListener('mouseover', setAge);
        genderIcon.addEventListener('mouseover', setGender);
        emailIcon.addEventListener('mouseover', setEmail);
        usernameIcon.addEventListener('mouseover', setUsername);
        passwordIcon.addEventListener('mouseover', setPassword);
        numberIcon.addEventListener('mouseover', setNumber);
        locationIcon.addEventListener('mouseover', setLocation);


        function setName(){
            info.innerHTML = `My name <div class = 'line'></div>${l.name.title} ${l.name.first} ${l.name.last}`
        }

        function setAge(){
            info.innerHTML = `I am <div class = 'line'></div>${l.dob.age}`
        }

        function setGender(){
            info.innerHTML = `I am a <div class = 'line'></div>${genderVar}`
        }

        function setEmail(){
            info.innerHTML = `My E-mail <div class = 'line'></div>${l.email}`
        }

        function setUsername(){
            info.innerHTML = `My username <div class = 'line'></div>${l.login.username}`
        }

        function setPassword(){
            info.innerHTML = `My password <div class = 'line'></div>${l.login.password}`
        }

        function setNumber(){
            info.innerHTML = `My phone number <div class = 'line'></div>${l.cell}`
        }

        function setLocation(){
            info.innerHTML = `I live in <div class = 'line'></div>${l.location.city}/${l.location.state}/${l.location.country}`
        }
    });
}

getUserInfo()




