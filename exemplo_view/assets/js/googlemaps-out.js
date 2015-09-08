// funções para exibição do mapa

var jsonPaises = [
	{"pais": "Inglaterra", 	"estudantes": 5},
	{"pais": "Suecia", 		"estudantes": 2},
	{"pais": "Austria", 	"estudantes": 1},
	{"pais": "Finlandia", 	"estudantes": 1},
	{"pais": "Russia", 		"estudantes": 3},
	{"pais": "Argentina", 	"estudantes": 1},
	{"pais": "Mexico", 		"estudantes": 5},
	{"pais": "Australia", 	"estudantes": 6},
];

function initMap(){
	var geocoder = new google.maps.Geocoder();
	var map = new google.maps.Map(document.getElementById('map-out'), {
		center: {lat: 20.632784, lng: 23.527223},
		zoom: 2
	});
	geocodeAddress(geocoder, map);
}

function geocodeAddress(geocoder, resultsMap) {
	var lineSymbol = {
	    path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW
	};
	var icon_student = 'assets/img/student_filled.png';
	for (var i = jsonPaises.length - 1; i >= 0; i--) {
		var pais = jsonPaises[i]["pais"];
		geocoder.geocode({'address': pais}, function(results, status) {
		    if (status === google.maps.GeocoderStatus.OK) {
		    	latLngPais = results[0].geometry.location;
				var line = new google.maps.Polyline({
					path: [{lat: -29.6880527, lng: -53.8165283}, latLngPais],
					icons: [{
						icon: lineSymbol,
						offset: '95%'
					}],
					strokeColor: '#356AA0',
					strokeOpacity: 0.95,
					strokeWeight: 1,
					map: resultsMap
				});
				var markerClient = new google.maps.Marker({
					position: latLngPais,
					map: resultsMap,
					icon: icon_student
					
				});
				
					
				
		    } else {
		      alert('Geocode was not successful for the following reason: ' + status);
		    }
		});
	}
	
}

