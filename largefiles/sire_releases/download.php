<?php // HTTP Headers for ZIP File Downloads
// http://perishablepress.com/press/2010/11/17/http-headers-file-downloads/
// Modified by C Woods to add error checking, stop download any file from server
// and also to add in recording downloads to a mysql database

$filename = $_GET["name"];
$filename = basename($filename);

if(!file_exists($filename)) 
{
  die("File not found : $filename");
}

// now let's now get IP address of the downloader so that we can record
// who is downloading what

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

if ($C_ID == 0)
{
    // this IP is not in the database. Look up the IP
    // information and then add
    $host = gethostbyaddr($data["ipaddr"]);
    $loc = file_get_contents("http://freegeoip.net/json/".$data["ipaddr"]);
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

// now try to find the filename information
$F_SID = trimString($filename, 255);

$F_ID = getSQLID($conn, "select F_ID from Files where F_SID=? LIMIT 1", $F_SID);

if ($F_ID == 0)
{
    // this filename is not in the database
    $sql = $conn->prepare("INSERT INTO Files (F_SID) VALUES (?) ON DUPLICATE KEY UPDATE F_SID=F_SID");
    if ( ! $sql ){ dieSQL(); }

    $sql->bind_param("s", $F_SID);
    $sql->execute();
    $sql->close();

    // now find the ID of the filename
    $F_ID = $conn->insert_id;

    if ($F_ID == 0)
    {
        $F_ID = getSQLID($conn, "select F_ID from Files where F_SID=? LIMIT 1", $F_SID);
    }
}

// now record all of this into the database, together with the time of download
$sql = $conn->prepare("INSERT INTO DownloadLog (DLTime, C_ID, F_ID) VALUES (now(), ?, ?)");
if ( ! $sql ){ dieSQL(); }

$sql->bind_param("ii", $C_ID, $F_ID);
$sql->execute();
$sql->close();

// http headers for zip downloads
header("Pragma: public");
header("Expires: 0");
header("Cache-Control: must-revalidate, post-check=0, pre-check=0");
header("Cache-Control: public");
header("Content-Description: File Transfer");
header("Content-type: application/octet-stream");
header("Content-Disposition: attachment; filename=\"".$filename."\"");
header("Content-Transfer-Encoding: binary");
header("Content-Length: ".filesize($filepath.$filename));
ob_end_flush();
@readfile($filename);
?>
