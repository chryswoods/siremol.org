
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
    loadJSON("http://siremol.org/phonehome/usagestats_app.json", function(response)
    {
        json = JSON.parse(response);

        var baroptions = {
          width: '800',
          height: '600',
          hAxis: {"logScale" : true}
        };

        var charts = [];

        for (var t in json)
        {
            var data = [ ["version", "usage"] ];

            for (var key in json[t])
            {
                data.push( [ key, json[t][key] ] );
                console.log(key + " " + json[t][key]);
            }

            tabledata = google.visualization.arrayToDataTable(data);

            var bar = new google.visualization.BarChart(document.getElementById("bar_by_" + t));
            bar.draw(tabledata, baroptions);
            charts.push(bar);
        }
    });
}

</script>

## Sire Usage Analytics

<div class="grid">
  <a href="./geochart.html">
    <div class="grid-item cw-box cw-bbutton-1-1">
      <h3>Who is using Sire?</h3>
    </div>
  </a>
  <a href="./appchart.html">
    <div class="grid-item cw-box cw-bbutton-2-2">
      <h3>Which apps are in use?</h3>
    </div>
  </a>
  <a href="./versionchart.html">
    <div class="grid-item cw-box cw-bbutton-3-3">
      <h3>Which versions are used?</h3>
    </div>
  </a>
  <a href="./oschart.html">
    <div class="grid-item cw-box cw-bbutton-4-4">
      <h3>What operating systems are used?</h3>
    </div>
  </a>
</div>

Sire has in-built analytics to let the developers know whether or not Sire is useful and is being used.

Every time Sire runs, a small amount of data is collected and then transmitted back to http://siremol.org.
This data is very useful for us, as it tells us what sort of computers Sire is being run on, which versions
of Sire are actively used, and which Sire applications are popular.

**It is very easy to stop Sire from sending this information.**

Just set the environment variable
  **SIRE_DONT_PHONEHOME** to any value, e.g. add `export SIRE_DONT_PHONEHOME=1` to your `.bashrc` file,
  or run Sire applications with `SIRE_DONT_PHONEHOME=1` before the call, e.g.
  `SIRE_DONT_PHONEHOME=1 $HOME/sire.app/bin/ligandswap ...`

The code that collects and sends the data can be [seen here](https://github.com/michellab/Sire/blob/devel/wrapper/__init__.py).
The function is called `_uploadUsageData()`, and you can see in this code that it involves collecting information
about the operating system, computer processor, version of Sire and the name of the executable that uses Sire. This
information is converted to JSON and sent to the PHP script [postusagestats.php](https://github.com/chryswoods/siremol.org/blob/master/phonehome/postusagestats.php). This is then decoded and placed into a set of SQL databases, together with a rough (country/region) lookup
of the IP address from which the http request originated. 

This data is then processed daily using the script [cronstats.php](https://github.com/chryswoods/siremol.org/blob/master/phonehome/cronstats.php).
This extracts summaries from the databases that are converted to JSON files that are hosted on this website, e.g.
Sire application data is [http://siremol.org/phonehome/usagestats_app.json](http://siremol.org/phonehome/usagestats_app.json).

The pages linked to via the buttons above use this data to draw nice graphs, using the Google chart library (note that **no information is sent to Google,
as all drawing occurs on your local machine**).

Note that this data is only available since the (private) release of Sire 2015.0, and only widely used in the 
public releases of Sire since 2016.1 (i.e. after April 2016).


