// Creating map object
var myMap = L.map("map", {
  center: [37.4316, -78.6569],
  zoom: 7
});

// Adding tile layer to the map
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

var link =  "../../Data/dmv_crime.csv"

// Grab the data with d3
d3.json(link, function(response) {
  console.log(response);
  // Create a new marker cluster group
  var markers = L.markerClusterGroup();

  // Loop through data
  for (var i = 0; i < response.length; i++) {

    // Set the data location property to a variable
    var long = response[i]["Longitude\r"];
    var lat = response[i].Latitude;
    console.log(long,lat);
    // Add a new marker to the cluster group and bind a pop-up
      markers.addLayer(L.marker([lat, long])
        .bindPopup(response[i].City));
    

  }

// Add our marker cluster layer to the map
  myMap.addLayer(markers);

});
