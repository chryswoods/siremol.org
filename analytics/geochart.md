
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript" src="https://www.google.com/jsapi"></script>

<script type="text/javascript">
google.charts.load("current", {"packages":["geochart"]});
google.charts.setOnLoadCallback(drawUsageMaps);

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

function drawUsageMaps() 
{
    loadJSON("http://siremol.org/phonehome/usagestats_country.json", function(response)
    {
        json = JSON.parse(response);

        var options = {
          colorAxis: {minValue: 0, maxValue: 100, colors: ['#ffff55', '#5555ff']},
          backgroundColor: '#aaaaff',
          datalessRegionColor: '#eeeeee',
          defaultColor: '#f5f5f5',
          width: '800'
        };

        var charts = [];

        for (var t in json)
        {
            var data = [ ["country", "usage"] ];

            for (var key in json[t])
            {
                if (json[t][key] > 0)
                {
                    data.push( [ key, json[t][key] ] );
                }
            }

            var chart = new google.visualization.GeoChart(document.getElementById("map_by_" + t));
            chart.draw(google.visualization.arrayToDataTable(data), options);
            charts.push(chart);
        }
    });
}

</script>

## Who is using Sire?

Below you can see how many times a Sire-based application has been used over different periods of time.

<div style="width=80%">
  <ul class="nav nav-tabs" role="tablist">
    <li role="presentation" class="active"><a href="#today" aria-controls="today" role="tab" data-toggle="tab">Today</a></li>
    <li role="presentation"><a href="#week" aria-controls="week" role="tab" data-toggle="tab">Last Week</a></li>
    <li role="presentation"><a href="#month" aria-controls="week" role="tab" data-toggle="tab">Last Month</a></li>
    <li role="presentation"><a href="#year" aria-controls="year" role="tab" data-toggle="tab">Last Year</a></li>
    <li role="presentation"><a href="#alltime" aria-controls="alltime" role="tab" data-toggle="tab">All Time</a></li>
  </ul>
  <!-- Tab panes -->
  <div class="tab-content">
    <div role="tabpanel" class="tab-pane active" id="today"><div id="map_by_day"></div><div id="bar_by_day"></div></div>
    <div role="tabpanel" class="tab-pane" id="week"><div id="map_by_week"></div></div>
    <div role="tabpanel" class="tab-pane" id="month"><div id="map_by_month"></div></div>
    <div role="tabpanel" class="tab-pane" id="year"><div id="map_by_year"></div></div>
    <div role="tabpanel" class="tab-pane" id="alltime"><div id="map_by_all"></div></div>
  </div>
</div>
