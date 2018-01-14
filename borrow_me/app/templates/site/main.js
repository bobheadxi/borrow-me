function selectItem() {
	
   $('#sent-msg').append("<div class='alert alert-success' role='alert'> Email Sent. Please wait for our response email.</div>");
 
}

function showGeoLocation() {
	var x = document.getElementById("longitude");
	var y = document.getElementById("latitude");
	getLocation();
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    y.innerHTML = position.coords.latitude;
    x.innerHTML = position.coords.longitude; 
}
