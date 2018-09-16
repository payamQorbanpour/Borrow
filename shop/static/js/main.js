//***** Masonry  *****//

$(function(){
  $('.grid').masonry({
    // options
    itemSelector : '.grid-item',
  });
});



//***** ammap *****//
AmCharts.makeChart( "mapdiv", {
  "dragMap": false,
  "type": "map",
  "dataProvider": {
    "map": "iranHigh",
    "areas": [
        { "id": "IR-32", "color": "#0080ff" , "url":"http://www.tehran.ir" },
        { "id": "IR-15", "color": "#0080ff" },
        { "id": "IR-13", "color": "#0080ff" },
        { "id": "IR-31", "color": "#0080ff" },
        { "id": "IR-30", "color": "#0080ff" },
        { "id": "IR-29", "color": "#0080ff" },
        { "id": "IR-16", "color": "#0080ff" },
        { "id": "IR-19", "color": "#0080ff" },
        { "id": "IR-17", "color": "#0080ff" },
        { "id": "IR-01", "color": "#0080ff" },
        { "id": "IR-02", "color": "#0080ff" },
        { "id": "IR-28", "color": "#0080ff" },
        { "id": "IR-11", "color": "#0080ff" },
        { "id": "IR-24", "color": "#0080ff" },
        { "id": "IR-26", "color": "#0080ff" },
        { "id": "IR-22", "color": "#0080ff" },
        { "id": "IR-03", "color": "#0080ff" },
        { "id": "IR-23", "color": "#0080ff" },
        { "id": "IR-05", "color": "#0080ff" },
        { "id": "IR-20", "color": "#0080ff" },
        { "id": "IR-10", "color": "#0080ff" },
        { "id": "IR-08", "color": "#0080ff" },
        { "id": "IR-25", "color": "#0080ff" },
        { "id": "IR-07", "color": "#0080ff" },
        { "id": "IR-12", "color": "#0080ff" },
        { "id": "IR-21", "color": "#0080ff" },
        { "id": "IR-27", "color": "#0080ff" },
        { "id": "IR-14", "color": "#0080ff" },
        { "id": "IR-04", "color": "#0080ff" },
        { "id": "IR-06", "color": "#0080ff" },
        { "id": "IR-18", "color": "#0080ff" },
      ]
  },
  "areasSettings": {
    "autoZoom": true,
    "selectedColor": "#00ffff"
  },
  "zoomControl": {
    "zoomControlEnabled": false,
    "homeButtonEnabled": false,
  },
  } );
