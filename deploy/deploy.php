<?php

// Get the information posted by the user - this will be a key
// that will ensure that the deploy script is only called by
// travis (who also has the key)
$userkey = $_POST["userkey"];

print("PENDING: STARTED DEPLOYMENT...\n");

if (empty($userkey))
{
    die ("ERROR: NO USER KEY");
}

// read the deploy key from the local filesystem
require_once("/home/siremolo/php/siremolo_deploy.php");

if ($userkey != $deploy_key)
{
    die ("ERROR: SUPPLIED USER KEY IS NOT VALID: $userkey");
}

// Now get the name of the file that has been uploaded
$filename = $_POST["filename"];

if (empty($filename))
{
    die ("ERROR: NO SPECIFIED USERNAME!");
}

// Now get whether or not to deploy as production or development
$production = $_POST["production"];

if (empty($production))
{
    $production = 0;
}

if ($production == 1)
{
    exec("perl deploy.pl $filename 1 > /dev/null &");
}
else
{
    exec("perl deploy.pl $filename 0 > /dev/null &");
}

print("SUCCESS: DEPLOYING WEBSITE FROM $filename");

?>
