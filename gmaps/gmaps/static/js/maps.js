$(function() {
	var markers = [];
	var map;
	var coordinates = [];

	var config = {
		"current": null,
		"id": null,
		"length": 0,
		"marker": [],
		"color" : '#E3E3E3',	
	}

	config.setId = function(id) {
		config["id"] = id;
	}

	config.setLength = function(length) {
		console.log(length);
		config["length"] = length;
	}

	config.setCurrent = function(current) {
		config["current"] = current;
	}

	config.setMarker = function(marker) {
		config["marker"] = marker;
	}

	config.setColor = function(color) {
		config["color"] = color;
	}

	config.reset = function() {
		config["current"] = null;
		config["id"] = null;
		config["length"] = 0;
		config["marker"] = [];
		config["color"] = '#E3E3E3';	
	}

	function reset() {
		config.reset();
		markers = [];
		map = null;
		coordinates = [];
	}

	$(document).on("click", 'ul.paths li', function() {
		// call reset
		reset();
		console.log($(this));
		console.log($(this).attr('id'));
		id = $(this).attr('id');
		console.log(id);
		// call init
		init(id);
	});


	function init(id) {
		// set the id in config
		config.setId(id);
		$.ajax({
			type: 'POST',
			url: '/path/' + id + '/',
			data: JSON.stringify({"config" : config}),
			async: false ,
			contentType: 'json',
			success: function(response) {
				console.log("success");
				// set the config on response
				setConfigOnResponse(response);
				// set the map
				initMap();
			},
		});	
	}

	function setConfigOnResponse(response) {
		config.setMarker(response["marker"]);
		config.setCurrent(response["current"]);
		config.setLength(response["length"]);
		config.setColor(response["color"]);

		if (response["coordinates"]) {
			var tempCoordinates = response["coordinates"]
				$.each(tempCoordinates, function(index, ele) {
					var obj = new google.maps.LatLng(ele[0], ele[1]);
					coordinates.push(obj);
				}); 
		}
	}

	function updateMarker() {
		console.log("inside update marker");
		console.log(map);
		var marker = new google.maps.Marker({
			position: new google.maps.LatLng(config['marker'][0], config['marker'][1]),
		    map: map,
		});
		clearMarkers();
		markers.push(marker);
	}

	function setAllMap(map) {
		for (var i=0; i <markers.length; i++) {
			markers[i].setMap(map);
		}
	}

	function clearMarkers() {
		setAllMap(null);
	}

	function initMap(){
		console.log("inside init map");
		console.log(config);	
		var mapOptions = {
			zoom: 8,
			center: new google.maps.LatLng(config['marker'][0], config['marker'][1]),
			mapTypeId: google.maps.MapTypeId.ROADMAP
		};
		map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
		updateMarker();
		tracePath();
	}

	function tracePath() {
		var tempArray = []
			for (var i=0; i < config["length"]; i++) {
				tempArray.push(i);
			}
		console.log(tempArray);
		$.each(tempArray, function(index, value) {
			setTimeout(function() {
				callToServer();
			}, 5000 * (index+1));
		});
	}

	function callToServer() {
		$.ajax({
			type: 'POST',
		url: '/path/' + id + '/',
		data: JSON.stringify({"config" : config}),
		async: false ,
		contentType: 'json',
		success: function(response) {
			console.log("success");
			// set the config on response
			setConfigOnResponse(response);
			// set the map
			updateMap();
		},
		});	

	}

	function setPath(){
		console.log("inside setPath");
		var routePath = new google.maps.Polyline({
			path: coordinates,
		    geodesic: true,
		    strokeColor: config["color"],
		    strokeOpacity: 1.0,
		    strokeWeight: 3,
		})
		routePath.setMap(map);
	}

	function updateMap() {
		setPath();
		updateMarker();
	}
	/*
	   function setupMap(){
	   console.log("inside setupMap");
	   var mapOptions = {
	   zoom: 8,
	   center: new google.maps.LatLng(28.635248, 77.224434),
	   mapTypeId: google.maps.MapTypeId.TERRAIN
	   };
	   map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
	   }
	   */
	//google.maps.event.addDomListener(window, 'load', setupMap);
});		
