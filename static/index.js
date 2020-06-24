const us_a = document.getElementById('us-a');
const locations_a = document.getElementById('locations-a');
const fb_a = document.getElementById('fb-a');
const tw_a = document.getElementById('tw-a');
const ig_a = document.getElementById('ig-a');
const reserve_a = document.getElementById('reserve-a');


let vision = "hidden";

function testNav() {
    if (vision === "hidden") {
        us_a.style.visibility = "visible";
        locations_a.style.visibility = "visible";
        fb_a.style.visibility = "visible";
        tw_a.style.visibility = "visible";
        ig_a.style.visibility = "visible";
        reserve_a.style.visibility = "visible";
        vision = "visible";
    } else {
        us_a.style.visibility = "hidden";
        locations_a.style.visibility = "hidden";
        fb_a.style.visibility = "hidden";
        tw_a.style.visibility = "hidden";
        ig_a.style.visibility = "hidden";
        reserve_a.style.visibility = "hidden";
        vision = "hidden";
    };
};
