
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript" src="https://www.google.com/jsapi"></script>

<script type="text/javascript">
google.charts.load("current", {"packages":["corechart", "geochart"]});
google.charts.setOnLoadCallback(drawUsageCharts);

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

function drawUsageCharts() 
{
    loadJSON("http://siremol.org/phonehome/usagestats_os.json", function(response)
    {
        json = JSON.parse(response);

        var baroptions = {
          height: '800',
          width: '1024',
          hAxis: {"scaleType" : "mirrorLog"},
          series: [{visibleInLegend: false}, {}, {}]
        };

        var charts = [];

        for (var t in json)
        {
            var data = [ ["version", "usage", { role: 'style' }] ];

            linux_keys = [ ];
            osx_keys = [ ];
            win_keys = [ ];
            other_keys = [ ];

            linux_count = 0;
            osx_count = 0;
            win_count = 0;
            other_count = 0;

            for (key in json[t])
            {
                if (key.search("Linux") != -1)
                {
                    linux_count += json[t][key];
                    linux_keys.push(key);
                }
                else if (key.search("Apple") != -1)
                {
                    osx_count += json[t][key];
                    osx_keys.push(key);
                }
                else if (key.search("Windows") != -1)
                {
                    win_count += json[t][key];
                    win_keys.push(key);
                }
                else
                {
                    other_count += json[t][key];
                    other_keys.push(key);
                }
            }

            linux_keys.sort();
            osx_keys.sort();
            win_keys.sort();
            other_keys.sort();

            if (osx_count > 0)
            {
                data.push( ["Apple OS X Total", osx_count, "black"] );

                for (var i in osx_keys)
                {
                    key = osx_keys[i];
                    if (json[t][key] > 0)
                    {
                        data.push( [ key, json[t][key], "green" ] );
                    }
                }
            }

            if (linux_count > 0)
            {
                data.push( ["Linux Total", linux_count, "black"] );

                for (var i in linux_keys)
                {
                    key = linux_keys[i];
                    if (json[t][key] > 0)
                    {
                        data.push( [ key, json[t][key], "gray" ] );
                    } 
                }
            }

            if (win_count > 0)
            {
                data.push( ["Windows Total", win_count, "black"] );

                for (var i in win_keys)
                {
                    key = win_keys[i];
                    if (json[t][key] > 0)
                    {
                        data.push( [ key, json[t][key], "blue" ] );
                    }
                }
            }

            if (other_count > 0)
            {
                data.push( ["Other Total", other_count, "black"] );

                for (var i in other_keys)
                {
                    key = other_keys[i];
                    if (json[t][key] > 0)
                    {
                        data.push( [ key, json[t][key], "red" ] );
                    }
                }
            }

            tabledata = google.visualization.arrayToDataTable(data);

            var bar = new google.visualization.BarChart(document.getElementById("bar_by_" + t));
            bar.draw(tabledata, baroptions);
            charts.push(bar);
        }
    });
}

</script>

## On which operating systems is Sire being run?

Below you can see how many times a Sire-based application has been run on different operating systems over different periods of time.

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
    <div role="tabpanel" class="tab-pane active" id="today"><div id="bar_by_day"></div></div>
    <div role="tabpanel" class="tab-pane" id="week"><div id="bar_by_week"></div></div>
    <div role="tabpanel" class="tab-pane" id="month"><div id="bar_by_month"></div></div>
    <div role="tabpanel" class="tab-pane" id="year"><div id="bar_by_year"></div></div>
    <div role="tabpanel" class="tab-pane" id="alltime"><div id="bar_by_all"></div></div>
  </div>
</div>

Note that "10.11", "10.12" etc. refer to different versions of Apple OS X.

Note that this data is only available since the (private) release of Sire 2015.0, and only widely used as part of the 
public release of Sire 2016.1, so it does not yet cover most Sire users.

***

[Return to analytics overview](README.md)
