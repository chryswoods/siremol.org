<?php

/**
 * @param string $domain Pass $_SERVER['SERVER_NAME'] here
 * @param bool $debug
 *
 * @debug bool $debug
 * @return string
 */
function getDomain($domain, $debug = false)
{
	$original = $domain = strtolower($domain);
	if (filter_var($domain, FILTER_VALIDATE_IP)) { return $domain; }
	$debug ? print('<strong style="color:green">&raquo;</strong> Parsing: '.$original) : false;
	$arr = array_slice(array_filter(explode('.', $domain, 4), function($value){
		return $value !== 'www';
	}), 0); //rebuild array indexes
	if (count($arr) > 2)
	{
		$count = count($arr);
		$_sub = explode('.', $count === 4 ? $arr[3] : $arr[2]);
		$debug ? print(" (parts count: {$count})") : false;
		if (count($_sub) === 2) // two level TLD
		{
			$removed = array_shift($arr);
			if ($count === 4) // got a subdomain acting as a domain
			{
				$removed = array_shift($arr);
			}
			$debug ? print("<br>\n" . '[*] Two level TLD: <strong>' . join('.', $_sub) . '</strong> ') : false;
		}
		elseif (count($_sub) === 1) // one level TLD
		{
			$removed = array_shift($arr); //remove the subdomain
			if (strlen($_sub[0]) === 2 && $count === 3) // TLD domain must be 2 letters
			{
				array_unshift($arr, $removed);
			}
			else
			{
				// non country TLD according to IANA
				$tlds = array(
					'aero',
					'arpa',
					'asia',
					'biz',
					'cat',
					'com',
					'coop',
					'edu',
					'gov',
					'info',
					'jobs',
					'mil',
					'mobi',
					'museum',
					'name',
					'net',
					'org',
					'post',
					'pro',
					'tel',
					'travel',
					'xxx',
				);
				if (count($arr) > 2 && in_array($_sub[0], $tlds) !== false) //special TLD don't have a country
				{
					array_shift($arr);
				}
			}
			$debug ? print("<br>\n" .'[*] One level TLD: <strong>'.join('.', $_sub).'</strong> ') : false;
		}
		else // more than 3 levels, something is wrong
		{
			for ($i = count($_sub); $i > 1; $i--)
			{
				$removed = array_shift($arr);
			}
			$debug ? print("<br>\n" . '[*] Three level TLD: <strong>' . join('.', $_sub) . '</strong> ') : false;
		}
	}
	elseif (count($arr) === 2)
	{
		$arr0 = array_shift($arr);
		if (strpos(join('.', $arr), '.') === false
			&& in_array($arr[0], array('localhost','test','invalid')) === false) // not a reserved domain
		{
			$debug ? print("<br>\n" .'Seems invalid domain: <strong>'.join('.', $arr).'</strong> re-adding: <strong>'.$arr0.'</strong> ') : false;
			// seems invalid domain, restore it
			array_unshift($arr, $arr0);
		}
	}
	$debug ? print("<br>\n".'<strong style="color:gray">&laquo;</strong> Done parsing: <span style="color:red">' . $original . '</span> as <span style="color:blue">'. join('.', $arr) ."</span><br>\n") : false;
	return join('.', $arr);
}

function toNum($s, $default)
{
    if (is_numeric($s)){ return floatval($s); }
    else { return $default; }
}

function toInt($s, $default)
{
    if (is_numeric($s)){ return intval($s); }
    else { return $default; }
}

function trimString($s, $length)
{
    $s = trim($s);

    if (strlen($s) < $length){ return $s; }
    else
    {
        return substr($s, 0, $length);
    }
}

function getMagic($s, $length)
{
    return trimString( strtolower( str_replace(" ", "_", trim($s)) ), $length );
}

// make sure we only process post requests
if ( $_SERVER["REQUEST_METHOD"] != "POST" )
{
    die ("POST ONLY");
}

// Get the information posted by the user
$data = $_POST["data"];

if (empty($data))
{
    die ("NO POSTED DATA");
}

function decodeJSON($string)
{
    if (strlen($string) > 12000)
    {
        die('Maximum string size exceeded!');
    }

    $output = json_decode($string, 3);

    switch (json_last_error()) 
    {
    case JSON_ERROR_NONE:
        break;
    case JSON_ERROR_DEPTH:
        die('Maximum stack depth exceeded');
        break;
    case JSON_ERROR_STATE_MISMATCH:
        die('Underflow or the modes mismatch');
        break;
    case JSON_ERROR_CTRL_CHAR:
        die('Unexpected control character found');
        break;
    case JSON_ERROR_SYNTAX:
        die('Syntax error, malformed JSON');
        break;
    case JSON_ERROR_UTF8:
        die('Malformed UTF-8 characters, possibly incorrectly encoded');
        break;
    default:
        die('Unknown error');
        break;
    }

    return $output;
}

$data = decodeJSON($data);

// check we have everything
function checkEmpty($name, $variable)
{
    if (empty($variable))
    {
        die("Variable " . $name . " has not been set!");
    }
}

checkEmpty("root", $data);

// standalone data
if (empty($data["clockspeed"])){ $data["clockspeed"] = "0"; }
if (empty($data["executable"])){ $data["executable"] = "unknown"; }
if (empty($data["numcores"])){ $data["numcores"] = "0"; }

// operating system data
if (empty($data["OS"])){ $data["OS"] = "unknown"; }
if (empty($data["platform"])){ $data["platform"] = "unknown"; }
if (empty($data["uname"])){ $data["uname"] = "unknown"; }

// processor data
if (empty($data["processor"])){ $data["processor"] = "unknown"; }
if (empty($data["vendor"])){ $data["vendor"] = "unknown"; }

// sire version data
if (empty($data["version"])) { $data["version"] = "unknown"; }
if (empty($data["repository"])){ $data["repository"] = "unknown"; }
if (empty($data["repository_version"])){ $data["respository_version"] = "unknown"; }

// now get the IP information of the connection
$data["ipaddr"] = $_SERVER['REMOTE_ADDR'];

// all of the data is here. Now it can be added to the database

// connect to the database
require_once("/home/siremolo/php/siremolo_record.php");

// Create connection
$conn = new mysqli($servername, $username, $password, "siremolo_usagestats");

// Check connection
if ($conn->connect_error) 
{
    die("Connection failed: " . $conn->connect_error);
}

// try to add the IP information
$sql = $conn->prepare("select C_ID from ClientIP where C_SID=? LIMIT 1");

function dieSQL()
{
    die("SQL failed: (" . $conn->errno . ") " . $conn->error);
}

function getSQLID($conn, $sql, $ID)
{
    $s = $conn->prepare($sql);
    if (!$s){ dieSQL(); }
    $s->bind_param("s",$ID);
    $s->execute();
    $result = 0;
    $s->bind_result($result);
    $s->fetch();
    $s->close();
    return $result;
}

// try to find the IP address in the database
$C_ID = getSQLID($conn, "select C_ID from ClientIP where C_SID=? LIMIT 1", $data["ipaddr"]);

function get_file_contents($url)
{
    $ch = curl_init();
    curl_setopt ($ch, CURLOPT_URL, $url);
    curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT, 5);
    curl_setopt ($ch, CURLOPT_RETURNTRANSFER, true);
    $contents = curl_exec($ch);
    if (curl_errno($ch))
    {
        echo curl_error($ch);
        echo "\n<br />";
        $contents = '';
    } 
    else
    {
        curl_close($ch);
    }

    return $contents;
}

if ($C_ID == 0)
{
    // this IP is not in the database. Look up the IP
    // information and then add
    $host = gethostbyaddr($data["ipaddr"]);
    $loc = get_file_contents("http://freegeoip.net/json/".$data["ipaddr"]);
    $country = "unknown";
    $region = "unknown";
    $city = "unknown";

    $loc = decodeJSON($loc);

    if (!empty($loc["country_name"])){ $country = $loc["country_name"];}
    if (!empty($loc["region_name"])){ $region = $loc["region_name"];}
    if (!empty($loc["city"])){ $city = $loc["city"];}

    // now make sure that all of the information is the right length
    $ipaddr = trimString($data["ipaddr"], 45);
    $country = trimString($country, 255);
    $region = trimString($region, 255);
    $city = trimString($city, 255);
    $domain = trimString(getDomain($host), 255);

    // now we have the information, add this to the database
    $sql = $conn->prepare("INSERT INTO ClientIP (C_SID, Country, Region, City, Domain) VALUES (?, ?, ?, ?, ?) ON DUPLICATE KEY UPDATE C_SID=C_SID");
    if ( ! $sql ){ dieSQL(); }

    $sql->bind_param("sssss", $ipaddr, $country, $region, $city, $domain);
    $sql->execute();
    $sql->close();

    // now find the ID of the added IP
    $C_ID = $conn->insert_id;

    if ($C_ID == 0)
    {
        $C_ID = getSQLID($conn, "select C_ID from ClientIP where C_SID=? LIMIT 1", $data["ipaddr"]);
    }
}

// now try to find the processor information
$vendor = trimString($data["vendor"], 255);
$processor = trimString($data["processor"], 255);
$P_SID = getMagic( $vendor."_".$processor, 255 );

$P_ID = getSQLID($conn, "select P_ID from Processor where P_SID=? LIMIT 1", $P_SID);

if ($P_ID == 0)
{
    // this processor is not in the database
    $sql = $conn->prepare("INSERT INTO Processor (P_SID, Vendor, Processor) VALUES (?, ?, ?) ON DUPLICATE KEY UPDATE P_SID=P_SID");
    if ( ! $sql ){ dieSQL(); }

    $sql->bind_param("sss", $P_SID, $vendor, $processor);
    $sql->execute();
    $sql->close();

    // now find the ID of the processor
    $P_ID = $conn->insert_id;

    if ($P_ID == 0)
    {
        $P_ID = getSQLID($conn, "select P_ID from Processor where P_SID=? LIMIT 1", $P_SID);
    }
}

// now try to find the sire version information
$version = trimString($data["version"], 255);
$repository = trimString($data["repository"], 255);
$repoversion = trimString($data["repository_version"], 255);
$V_SID = getMagic( $version."_".$repository."_".$repoversion, 768 );

$V_ID = getSQLID($conn, "select V_ID from Version where V_SID=? LIMIT 1", $V_SID);

if ($V_ID == 0)
{
    // this sire version is not in the database
    $sql = $conn->prepare("INSERT INTO Version (V_SID, Version, Repository, Checkout) VALUES (?, ?, ?, ?) ON DUPLICATE KEY UPDATE V_SID=V_SID");
    if ( ! $sql ){ dieSQL(); }

    $sql->bind_param("ssss", $V_SID, $version, $repository, $repoversion);
    $sql->execute();
    $sql->close();

    $V_ID = $conn->insert_id;

    if ($V_ID == 0)
    {
        $V_ID = getSQLID($conn, "select V_ID from Version where V_SID=? LIMIT 1", $V_SID);
    }
}

// now try to find the operating system information
$os = trimString($data["OS"], 255);
$platform = trimString($data["platform"], 255);
$uname = trimString($data["uname"], 255);
$S_SID = getMagic( $os."_".$platform."_".$uname, 768 );

$S_ID = getSQLID($conn, "select S_ID from System where S_SID=? LIMIT 1", $S_SID);

if ($S_ID == 0)
{
    // this operating system is not in the database
    $sql = $conn->prepare("INSERT INTO System (S_SID, Platform, OS, Uname) VALUES (?, ?, ?, ?) ON DUPLICATE KEY UPDATE S_SID=S_SID");
    if ( ! $sql ){ dieSQL(); }

    $sql->bind_param("ssss", $S_SID, $platform, $os, $uname);
    $sql->execute();
    $sql->close();

    $S_ID = $conn->insert_id;

    if ($S_ID == 0)
    {
        $S_ID = getSQLID($conn, "select S_ID from System where S_SID=? LIMIT 1", $S_SID);
    }
} 

// we can now add all of this information to the runlog
if ( $C_ID == 0 or $P_ID == 0 or $V_ID == 0 or $S_ID == 0 )
{
    die("Something went wrong adding data: $C_ID, $P_ID, $V_ID, $S_ID");
}

$exe = trimString($data["executable"], 255);
$clockspeed = toNum($data["clockspeed"], 0);
$numcores = toInt($data["numcores"], 0);

$sql = $conn->prepare("INSERT INTO RunLog (RunTime, C_ID, Executable, P_ID, S_ID, V_ID, NumCores, ClockSpeed) VALUES (now(), ?, ?, ?, ?, ?, ?, ?)");
if ( ! $sql ){ dieSQL(); }

$sql->bind_param("isiiiid", $C_ID, $exe, $P_ID, $S_ID, $V_ID, $numcores, $clockspeed);
$sql->execute();
$sql->close();

?>
