
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript" src="https://www.google.com/jsapi"></script>

<script type="text/javascript">
google.charts.load("current", {"packages":["geochart"]});
google.charts.setOnLoadCallback(drawRegionsMap);

function loadJSON(filename, callback)
{   
    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', filename, true);
    xobj.onreadystatechange = function () {
          if (xobj.readyState == 4 && xobj.status == "200") {
            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
            callback(xobj.responseText);
          }
    };
    xobj.send(null);  
}

function loadMapData() {
    var day_data = [ ["Country", "Usage" ] ];
    var week_data = [ ["Country", "Usage" ] ];
    var month_data = [ ["Country", "Usage" ] ];
    var year_data = [ ["Country", "Usage" ] ];
    var all_data = [ ["Country", "Usage" ] ];

    loadJSON("http://siremol.org/phonehome/usagestats_country.json", function(response)
    {
        data = JSON.parse(response);

        for (var key in data["day"])
        {
            day_data.push( [ key, data["day"][key] ] );
        }

        for (var key in data["week"])
        {
            week_data.push( [ key, data["week"][key] ] );
        }

        for (var key in data["month"])
        {
            month_data.push( [ key, data["month"][key] ] );
        }

        for (var key in data["year"])
        {
            year_data.push( [ key, data["year"][key] ] );
        }

        for (var key in data["all"])
        {
            all_data.push( [ key, data["all"][key] ] );
        }

        var options = {};

        var day_chart = new google.visualization.GeoChart(document.getElementById("map_by_day"));
        day_chart.draw(google.visualization.arrayToDataTable(day_data), options);

        var week_chart = new google.visualization.GeoChart(document.getElementById("map_by_week"));
        week_chart.draw(google.visualization.arrayToDataTable(week_data), options);

        var month_chart = new google.visualization.GeoChart(document.getElementById("map_by_month"));
        month_chart.draw(google.visualization.arrayToDataTable(month_data), options);

        var year_chart = new google.visualization.GeoChart(document.getElementById("map_by_year"));
        year_chart.draw(google.visualization.arrayToDataTable(year_data), options);

        var all_chart = new google.visualization.GeoChart(document.getElementById("map_by_all"));
        all_chart.draw(google.visualization.arrayToDataTable(all_data), options);
    });
}

function drawRegionsMap() {
    loadMapData();
}
</script>

<div id="map_by_day" style="width: 900px; height: 500px;"></div>
<div id="map_by_week" style="width: 900px; height: 500px;"></div>
<div id="map_by_month" style="width: 900px; height: 500px;"></div>
<div id="map_by_year" style="width: 900px; height: 500px;"></div>
<div id="map_by_all" style="width: 900px; height: 500px;"></div>

