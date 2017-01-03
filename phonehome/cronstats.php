<?php

// get variables for useful dates
$today = new DateTime( date("Y-m-d") );
$today->sub( date_interval_create_from_date_string('1 day') );
$last_week = new DateTime( date("Y-m-d") );
$last_week->sub( date_interval_create_from_date_string('7 days') );
$last_month = new DateTime( date("Y-m-d") );
$last_month->sub( date_interval_create_from_date_string('1 month') );
$last_year = new DateTime( date("Y-m-d") );
$last_year->sub( date_interval_create_from_date_string('1 year') );

// make sure we only process get requests
if ( $_SERVER["REQUEST_METHOD"] == "POST" )
{
    die ("GET ONLY");
}

// see which data we will update...
$get_apps = $_GET["apps"];
$get_os = $_GET["OS"];
$get_country = $_GET["country"];
$get_version = $_GET["version"];

// connect to the database
require_once("/home/siremolo/php/siremolo_usage.php");

// Create connection
$conn = new mysqli($servername, $username, $password, "siremolo_usagestats");

// Check connection
if ($conn->connect_error) 
{
    die("Connection failed: " . $conn->connect_error);
}

function dieSQL()
{
    die("SQL failed: (" . $conn->errno . ") " . $conn->error);
}

function getAppUsage($conn, $app, $start_time)
{
    $s = $conn->prepare("select count(*) from RunLog where Executable=? and RunTime>?");
    if (!$s){ dieSQL(); }
    $strdate = $start_time->format("Y-m-d");
    $s->bind_param("ss",$app,$strdate);
    $s->execute();
    $result = 0;
    $s->bind_result($result);
    $s->fetch();
    $s->close();
    return $result;
}

function getAppAllUsage($conn, $app)
{
    $s = $conn->prepare("select count(*) from RunLog where Executable=?");
    if (!$s){ dieSQL(); }
    $s->bind_param("s",$app);
    $s->execute();
    $result = 0;
    $s->bind_result($result);
    $s->fetch();
    $s->close();
    return $result;
}

if ($get_apps)
{
    echo "<p>Getting app usage stats...</p>";

    // get the list of all unique Sire apps
    $apps = array();
    $result = $conn->query("select distinct Executable from RunLog");

    if ($result->num_rows > 0) 
    {
        while($row = $result->fetch_assoc())
        {
            $apps[] = $row["Executable"];
        }
    } 

    // now find out how many times each app has been used today, in the last week,
    // in the last month, in the last year and over all time
    $n_apps = count($apps);

    $usage_day = array();
    $usage_week = array();
    $usage_month = array();
    $usage_year = array();
    $usage_all = array();

    for ($i = 0; $i < $n_apps; $i++) 
    {
        $app = $apps[$i];
        $usage_day[$app] = getAppUsage($conn, $app, $today);
        $usage_week[$app] = getAppUsage($conn, $app, $last_week);
        $usage_month[$app] = getAppUsage($conn, $app, $last_month);
        $usage_year[$app] = getAppUsage($conn, $app, $last_year);
        $usage_all[$app] = getAppAllUsage($conn, $app);
    }

    $run_usage = array();
    $run_usage["day"] = $usage_day;
    $run_usage["week"] = $usage_week;
    $run_usage["month"] = $usage_month;
    $run_usage["year"] = $usage_year;
    $run_usage["all"] = $usage_all;

    file_put_contents("usagestats_app.json", json_encode($run_usage));
}

function getCountryUsage($conn, $country, $start_time)
{
    $s = $conn->prepare("select count(*) from RunLog inner join ClientIP on RunLog.C_ID=ClientIP.C_ID where ClientIP.Country=? and RunLog.RunTime>?");
    if (!$s){ dieSQL(); }
    $strdate = $start_time->format("Y-m-d");
    $s->bind_param("ss",$country,$strdate);
    $s->execute();
    $result = 0;
    $s->bind_result($result);
    $s->fetch();
    $s->close();
    return $result;
}

function getAllCountryUsage($conn, $country)
{
    $s = $conn->prepare("select count(*) from RunLog inner join ClientIP on RunLog.C_ID=ClientIP.C_ID where ClientIP.Country=?");
    if (!$s){ dieSQL(); }
    $s->bind_param("s",$country);
    $s->execute();
    $result = 0;
    $s->bind_result($result);
    $s->fetch();
    $s->close();
    return $result;
}

if ($get_country)
{
    echo "<p>Getting country usage stats...</p>";

    // get the list of unique ClientIDs that use Sire
    $countries = array();
    $result = $conn->query("select distinct Country from ClientIP");

    if ($result->num_rows > 0) 
    {
        while($row = $result->fetch_assoc())
        {
            $countries[] = $row["Country"];
        }
    } 

    $n_countries = count($countries);

    $country_day = array();
    $country_week = array();
    $country_month = array();
    $country_year = array();
    $country_all = array();

    for ($i = 0; $i < $n_countries; $i++)
    {
        $country = $countries[$i];

        $country_day[$country] = getCountryUsage($conn, $country, $today);
        $country_week[$country] = getCountryUsage($conn, $country, $last_week);
        $country_month[$country] = getCountryUsage($conn, $country, $last_month);
        $country_year[$country] = getCountryUsage($conn, $country, $last_year);
        $country_all[$country] = getAllCountryUsage($conn, $country);
    }

    $country_usage = array();
    $country_usage["day"] = $country_day;
    $country_usage["week"] = $country_week;
    $country_usage["month"] = $country_month;
    $country_usage["year"] = $country_year;
    $country_usage["all"] = $country_all;

    file_put_contents("usagestats_country.json", json_encode($country_usage));
}

function getVersionUsage($conn, $version, $start_time)
{
    $s = $conn->prepare("select count(*) from RunLog inner join Version on RunLog.V_ID=Version.V_ID where Version.Version=? and RunLog.RunTime>?");
    if (!$s){ dieSQL(); }
    $strdate = $start_time->format("Y-m-d");
    $s->bind_param("ss",$version,$strdate);
    $s->execute();
    $result = 0;
    $s->bind_result($result);
    $s->fetch();
    $s->close();
    return $result;
}

function getAllVersionUsage($conn, $version)
{
    $s = $conn->prepare("select count(*) from RunLog inner join Version on RunLog.V_ID=Version.V_ID where Version.Version=?");
    if (!$s){ dieSQL(); }
    $s->bind_param("s",$version);
    $s->execute();
    $result = 0;
    $s->bind_result($result);
    $s->fetch();
    $s->close();
    return $result;
}

if ($get_version)
{
    echo "<p>Getting version usage stats...</p>";

    // get a list of unique Sire versions in use
    $versions = array();
    $result = $conn->query("select distinct Version from Version");

    if ($result->num_rows > 0) 
    {
        while($row = $result->fetch_assoc())
        {
            $versions[] = $row["Version"];
        }
    } 

    $n_versions = count($versions);

    $version_day = array();
    $version_week = array();
    $version_month = array();
    $version_year = array();
    $version_all = array();

    for ($i = 0; $i < $n_versions; $i++)
    {
        $version = $versions[$i];

        $version_day[$version] = getVersionUsage($conn, $version, $today);
        $version_week[$version] = getVersionUsage($conn, $version, $last_week);
        $version_month[$version] = getVersionUsage($conn, $version, $last_month);
        $version_year[$version] = getVersionUsage($conn, $version, $last_year);
        $version_all[$version] = getAllVersionUsage($conn, $version);
    }

    $version_usage = array();
    $version_usage["day"] = $version_day;
    $version_usage["week"] = $version_week;
    $version_usage["month"] = $version_month;
    $version_usage["year"] = $version_year;
    $version_usage["all"] = $version_all;

    file_put_contents("usagestats_version.json", json_encode($version_usage));
}

function getOSPlatform($conn, $os)
{
    $s = $conn->prepare("select Platform from System where System.OS=?");
    if (!$s){ dieSQL(); }
    $s->bind_param("s",$os);
    $s->execute();
    $result = 0;
    $s->bind_result($result);
    $s->fetch();
    $s->close();
    return $result;
}

function getOSUsage($conn, $os, $start_time)
{
    $s = $conn->prepare("select count(*) from RunLog inner join System on RunLog.S_ID=System.S_ID where System.OS=? and RunLog.RunTime>?");
    if (!$s){ dieSQL(); }
    $strdate = $start_time->format("Y-m-d");
    $s->bind_param("ss",$os,$strdate);
    $s->execute();
    $result = 0;
    $s->bind_result($result);
    $s->fetch();
    $s->close();
    return $result;
}

function getAllOSUsage($conn, $os)
{
    $s = $conn->prepare("select count(*) from RunLog inner join System on RunLog.S_ID=System.S_ID where System.OS=?");
    if (!$s){ dieSQL(); }
    $s->bind_param("s",$os);
    $s->execute();
    $result = 0;
    $s->bind_result($result);
    $s->fetch();
    $s->close();
    return $result;
}

if ($get_os)
{
    echo "<p>Getting OS usage stats...</p>";

    // get a list of unique Sire operating systems in use
    $oss = array();
    $result = $conn->query("select distinct OS from System");

    if ($result->num_rows > 0)
    {
        while($row = $result->fetch_assoc())
        {
            $oss[] = $row["OS"];
        }
    } 

    $n_oss = count($oss);

    $os_day = array();
    $os_week = array();
    $os_month = array();
    $os_year = array();
    $os_all = array();

    for ($i = 0; $i < $n_oss; $i++)
    {
        $os = $oss[$i];

        $platform = getOSPlatform($conn, $os);

        if ($platform == "Darwin"){ $platform = "Apple OS X"; }

        $os_string = "$os($platform)";

        $os_day[$os_string] = getOSUsage($conn, $os, $today);
        $os_week[$os_string] = getOSUsage($conn, $os, $last_week);
        $os_month[$os_string] = getOSUsage($conn, $os, $last_month);
        $os_year[$os_string] = getOSUsage($conn, $os, $last_year);
        $os_all[$os_string] = getAllOSUsage($conn, $os);
    }

    $os_usage = array();
    $os_usage["day"] = $os_day;
    $os_usage["week"] = $os_week;
    $os_usage["month"] = $os_month;
    $os_usage["year"] = $os_year;
    $os_usage["all"] = $os_all;

    file_put_contents("usagestats_os.json", json_encode($os_usage));
}

$conn->close();

echo "<p>OK</p>";

?>
