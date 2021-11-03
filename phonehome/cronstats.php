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

function getAppAllUsage($conn)
{
    $result = $conn->query("select Executable, count(*) as c from RunLog group by Executable");
    $usage = array();

    if ($result->num_rows > 0) 
    {
        while($row = $result->fetch_assoc())
        {
            $usage[$row["Executable"]] = (int)$row["c"];
        }
    } 
    
    return $usage;
}

function getAppUsage($conn, $start_time)
{
    $strdate = $start_time->format("Y-m-d");
    $result = $conn->query("select Executable, count(*) as c from RunLog where RunTime>'$strdate' group by Executable");
    $usage = array();

    if ($result->num_rows > 0) 
    {
        while($row = $result->fetch_assoc())
        {
            $usage[$row["Executable"]] = (int)$row["c"];
        }
    } 
    
    return $usage;
}

if ($get_apps)
{
    echo "<p>Getting app usage stats...</p>";
    
    $run_usage = array();
    $run_usage["day"] = getAppUsage($conn, $today);
    $run_usage["week"] = getAppUsage($conn, $last_week);
    $run_usage["month"] = getAppUsage($conn, $last_month);
    $run_usage["year"] = getAppUsage($conn, $last_year);
    $run_usage["all"] = getAppAllUsage($conn);

    file_put_contents("usagestats_app.json", json_encode($run_usage));
}

function getCountryUsage($conn, $start_time)
{
    $strdate = $start_time->format("Y-m-d");
    $result = $conn->query("select ClientIP.Country, count(*) as c from RunLog inner join ClientIP on RunLog.C_ID=ClientIP.C_ID where RunTime>'$strdate' group by ClientIP.Country");
    $usage = array();

    if ($result->num_rows > 0) 
    {
        while($row = $result->fetch_assoc())
        {
            $usage[$row["Country"]] = (int)$row["c"];
        }
    } 
    
    return $usage;
}

function getCountryAllUsage($conn)
{
    $result = $conn->query("select ClientIP.Country, count(*) as c from RunLog inner join ClientIP on RunLog.C_ID=ClientIP.C_ID group by ClientIP.Country");
    $usage = array();

    if ($result->num_rows > 0) 
    {
        while($row = $result->fetch_assoc())
        {
            $usage[$row["Country"]] = (int)$row["c"];
        }
    } 
    
    return $usage;
}

if ($get_country)
{
    echo "<p>Getting country usage stats...</p>";

    $country_usage = array();
    $country_usage["day"] = getCountryUsage($conn, $today);
    $country_usage["week"] = getCountryUsage($conn, $last_week);
    $country_usage["month"] = getCountryUsage($conn, $last_month);
    $country_usage["year"] = getCountryUsage($conn, $last_year);
    $country_usage["all"] = getCountryAllUsage($conn);

    file_put_contents("usagestats_country.json", json_encode($country_usage));
}

function getVersionUsage($conn, $start_time)
{
    $strdate = $start_time->format("Y-m-d");
    $result = $conn->query("select Version.Version, count(*) as c from RunLog inner join Version on RunLog.V_ID=Version.V_ID where RunTime>'$strdate' group by Version.Version");
    $usage = array();

    if ($result->num_rows > 0) 
    {
        while($row = $result->fetch_assoc())
        {
            $usage[$row["Version"]] = (int)$row["c"];
        }
    } 
    
    return $usage;
}

function getVersionAllUsage($conn)
{
    $result = $conn->query("select Version.Version, count(*) as c from RunLog inner join Version on RunLog.V_ID=Version.V_ID group by Version.Version");
    $usage = array();

    if ($result->num_rows > 0) 
    {
        while($row = $result->fetch_assoc())
        {
            $usage[$row["Version"]] = (int)$row["c"];
        }
    } 
    
    return $usage;
}

if ($get_version)
{
    echo "<p>Getting version usage stats...</p>";

    $version_usage = array();
    $version_usage["day"] = getVersionUsage($conn, $today);
    $version_usage["week"] = getVersionUsage($conn, $last_week);
    $version_usage["month"] = getVersionUsage($conn, $last_month);
    $version_usage["year"] = getVersionUsage($conn, $last_year);
    $version_usage["all"] = getVersionAllUsage($conn);

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
