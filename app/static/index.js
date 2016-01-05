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
  //var marker0 = createMarker({
  //  position: new google.maps.LatLng(33.808678, -117.918921),
  //  map: map,
  //  icon: "http://1.bp.blogspot.com/_GZzKwf6g1o8/S6xwK6CSghI/AAAAAAAAA98/_iA3r4Ehclk/s1600/marker-green.png"
  //}, "<h1>CALI SIDE</h1><p>Los Angeles.</p>");
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
            console.log("Result as is" + results[0].geometry.location);
        }
        else{
            alert('address not found!');
        }

        //{{ calculate_distance(request.json) }}
        var split_location = ("" + results[0].geometry.location).split(",");
        location_data = {};
        location_data['lat'] = split_location[0].replace("(", "");
        location_data['long'] = split_location[1].replace(")", "");
        console.log("split_locationn " + split_location + location_data['lat']);
        var marker1=null;
        var a = $.ajax({
            type : "POST",
            url : "/data_to_find_distance",
            data: JSON.stringify(location_data),
            contentType: 'application/json;charset=UTF-8;',
            success: function(result) {
                console.log(result);

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

                var parsedResult = JSON.parse(result);
                for (var key in parsedResult) {
                    console.log("Key = ",key," val = ",parsedResult[key][0],parsedResult[key][1]);
                    var lat = parseFloat(parsedResult[key][0]);
                    var lon = parseFloat(parsedResult[key][1]);
                    var marker1 = createMarker({
                        position: new google.maps.LatLng(lat, lon),
                        map: map,
                        icon: "http://1.bp.blogspot.com/_GZzKwf6g1o8/S6xwK6CSghI/AAAAAAAAA98/_iA3r4Ehclk/s1600/marker-green.png"
                        }, "<h1>"+key+"</h1><p></p>");
                    console.log("Marker added for ", key);
                }
                map.setZoom(17);
            }
        });
        console.log(a);
    });
}