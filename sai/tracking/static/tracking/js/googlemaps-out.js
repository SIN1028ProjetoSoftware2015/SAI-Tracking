// funções para exibição do mapa

var jsonPaises = [
	{"pais": "Inglaterra", 	"graduacao": 5, "mestrado": 2, "doutorado": 9, "posdoc": 1 },
	{"pais": "Suecia", 		"graduacao": 2, "mestrado": 3, "doutorado": 0, "posdoc": 2 },
	{"pais": "Austria", 	"graduacao": 1, "mestrado": 5, "doutorado": 1, "posdoc": 4 },
	{"pais": "Finlandia", 	"graduacao": 1, "mestrado": 1, "doutorado": 2, "posdoc": 3 },
	{"pais": "Russia", 		"graduacao": 3, "mestrado": 0, "doutorado": 7, "posdoc": 5 },
	{"pais": "Argentina", 	"graduacao": 1, "mestrado": 3, "doutorado": 6, "posdoc": 3 },
	{"pais": "Mexico", 		"graduacao": 5, "mestrado": 8, "doutorado": 4, "posdoc": 2 },
// 	{"pais": "Australia", 	"graduacao": 6, "mestrado": 2, "doutorado": 2, "posdoc": 2 },
];

function initMap(){
	var geocoder = new google.maps.Geocoder();
	var map = new google.maps.Map(document.getElementById('map-in'), {
		center: {lat: 20.565129, lng: 14.191874},
		zoom: 2
	});
    for (var i = jsonPaises.length - 1; i >= 0; i--) {
        var arrPais = jsonPaises[i];
        geocodeAddress(geocoder, map, arrPais);
    }
}

function geocodeAddress(geocoder, resultsMap, pais) {
	var lineSymbol = {
	    path: google.maps.SymbolPath.FORWARD_CLOSED_ARROW
	};
	var icon_student = '/static/tracking/images/student_filled.png';
    geocoder.geocode({'address': pais['pais']}, function(results, status) {
        if (status === google.maps.GeocoderStatus.OK) {
            var line = new google.maps.Polyline({
                path: [{lat: -29.6880527, lng: -53.8165283}, results[0].geometry.location],
                icons: [{
                    icon: lineSymbol,
                    offset: '10%'
                }],
                strokeColor: '#356AA0',
                strokeOpacity: 0.95,
                strokeWeight: 1,
                map: resultsMap
            });
            var markerClient = new google.maps.Marker({
                position: results[0].geometry.location,
                map: resultsMap,
                icon: icon_student
            });
            var infowindow = new google.maps.InfoWindow();
            google.maps.event.addListener(markerClient, 'click', (function(markerClient, pais) {
                return function() {
                    var contentString = '<div>'+
                        '<div><h5>'+ pais['pais'] +'</h5></div>'+
                        '<div>Estudantes em graduação: '+ pais['graduacao'] +'</div>'+
                        '<div>Estudantes em mestrado: '+ pais['mestrado'] +'</div>'+
                        '<div>Pesquisadores em doutorado: '+ pais['doutorado'] +'</div>'+
                        '<div>Pesquisadores em pós doutorado: '+ pais['posdoc'] +'</div>'+
                        '</div>'
                    infowindow.setContent(contentString);
                    infowindow.open(resultsMap, markerClient);
                }
            })(markerClient, pais));

        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
}