
var map;
/*
 * use google maps api built-in mechanism to attach dom events
 */
google.maps.event.addDomListener(window, "load", function () {

  /*
   * create map
   */
    map = new google.maps.Map(document.getElementById("map_div"), {
        center: new google.maps.LatLng(37.773972 , -122.431297),
        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    /*
    * create infowindow (which will be used by markers)
    */
    var infoWindow = new google.maps.InfoWindow();

  /*
   * marker creater function (acts as a closure for html parameter)
   */
  function createMarker(options, html) {
    var marker = new google.maps.Marker(options);
    if (html) {
        google.maps.event.addListener(marker, "click", function () {
            infoWindow.setContent(html);
            infoWindow.open(options.map, this);
        });
    }
    return marker;
  }

  /*
   * add markers to map
   */
  var marker0 = createMarker({
    position: new google.maps.LatLng(33.808678, -117.918921),
    map: map,
    icon: "http://1.bp.blogspot.com/_GZzKwf6g1o8/S6xwK6CSghI/AAAAAAAAA98/_iA3r4Ehclk/s1600/marker-green.png"
  }, "<h1>Marker 0</h1><p>This is the home marker.</p>");

  var marker1 = createMarker({
    position: new google.maps.LatLng(33.818038, -117.928492),
    map: map
  }, "<h1>Marker 1</h1><p>This is marker 1</p>");

  var marker2 = createMarker({
    position: new google.maps.LatLng(33.803333, -117.915278),
    map: map
  }, "<h1>Marker 2</h1><p>This is marker 2</p>");
});

// Locate me method
function findPlace() {
    var location = document.getElementById("location_name").value;
    var geoCoder = new google.maps.Geocoder();

    geoCoder.geocode({
        'address':location
    }, function(results, status){

        if(status==google.maps.GeocoderStatus.OK){

            map.setCenter(results[0].geometry.location);
            marker=new google.maps.Marker({
                map:map,
                position:results[0].geometry.location
            });
        }
        else{
            alert('address not found!');
        }

        {{ calculate_distance(request.json) }}

        // $.ajax({
        //     type : "POST",
        //     url : "{{ url_for('data_to_find_distance') }}",
        //     data: JSON.stringify(results[0].geometry.location, null, '\t'),
        //     contentType: 'application/json;charset=UTF-8',
        //     success: function(result) {
        //         console.log(result);
        //     }
        // });
    });
}
