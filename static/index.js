const home = document.getElementById('home-div');
const footer = document.getElementById('footer-content-div');
const us_a = document.getElementById('us-a');
const locations_a = document.getElementById('locations-a');
const fb_a = document.getElementById('fb-a');
const tw_a = document.getElementById('tw-a');
const ig_a = document.getElementById('ig-a');
const reserve_a = document.getElementById('reserve-a');

let vision = "hidden";

document.addEventListener("DOMContentLoaded", function() {
    getMenu(1);
});

function testNav() {
    if (vision === "hidden") {
        if (home) {
            home.style.visibility = "hidden";
        };
        if (footer) {
            footer.style.visibility = "hidden";
        };
        us_a.style.visibility = "visible";
        locations_a.style.visibility = "visible";
        fb_a.style.visibility = "visible";
        tw_a.style.visibility = "visible";
        ig_a.style.visibility = "visible";
        reserve_a.style.visibility = "visible";
        vision = "visible";
    } else {
        if (home) {
            home.style.visibility = "visible";
        };
        if (footer) {
            footer.style.visibility = "visible";
        };
        us_a.style.visibility = "hidden";
        locations_a.style.visibility = "hidden";
        fb_a.style.visibility = "hidden";
        tw_a.style.visibility = "hidden";
        ig_a.style.visibility = "hidden";
        reserve_a.style.visibility = "hidden";
        vision = "hidden";
    };
};

var slideIndex = 0;
carousel();

function carousel() {
    var i;
    var x = document.getElementsByClassName("slides");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    };
    slideIndex++;
    if (slideIndex > x.length) {
        slideIndex = 1;
    };
    x[slideIndex - 1].style.display = "block";
    setTimeout(carousel, 3000); // Change image every 3 seconds
};

let xhttp = new XMLHttpRequest();

function getMenu(period_id) {
    let hmcdiv = document.getElementById("home-menu-container-div");
    hmcdiv.innerHTML = "";

    let mfrag = new DocumentFragment();

    xhttp.open("GET", "/menu/" + period_id, true);
    xhttp.onreadystatechange = function() {

        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(this.responseText)

            for (res in response) {
                for (r in response[res]) {
                    let hmidiv = document.createElement('div');
                    hmidiv.setAttribute('class', 'home-menu-item-div');

                    let hmih3pdiv = document.createElement('div');
                    hmih3pdiv.setAttribute('class', 'home-menu-item-h3-p-div');

                    let hmih3 = document.createElement('h3');
                    hmih3.setAttribute('class', 'home-menu-item-h3');
                    hmih3.innerText = response[res][r].name;

                    let hmip = document.createElement('p');
                    hmip.setAttribute('class', 'home-menu-item-p');
                    hmip.innerText = response[res][r].description;

                    let hmispan = document.createElement('span');
                    hmispan.setAttribute('class', 'home-menu-item-span');
                    hmispan.innerText = response[res][r].price;

                    hmih3pdiv.appendChild(hmih3);
                    hmih3pdiv.appendChild(hmip);
                    hmidiv.appendChild(hmih3pdiv);
                    hmidiv.appendChild(hmispan);

                    mfrag.appendChild(hmidiv);
                };
            };
            hmcdiv.appendChild(mfrag);
        };
    };
    xhttp.send();
};