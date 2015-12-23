<?php

print("PENDING: STARTED DEPLOYMENT...\n");

// Get the information posted by the user - this will be a key
// that will ensure that the deploy script is only called by
// travis (who also has the key)
$userkey = $_POST["userkey"];

if (empty($userkey))
{
    print("ERROR: NO USER KEY");
    die ("ERROR: NO USER KEY");
}

print("PENDING: CONTINUING 1...\n");

// read the deploy key from the local filesystem
require_once("/home/siremolo/php/siremolo_deploy.php");

print("PENDING: CONTINUING 2...\n");

if ($userkey != $deploy_key)
{
    print("ERROR: SUPPLIED USER KEY IS NOT VALID: $userkey");
    #die ("ERROR: SUPPLIED USER KEY IS NOT VALID: $userkey");
}

print("PENDING: CONTINUING 3...\n");

// Now get the name of the file that has been uploaded
$filename = $_POST["filename"];

print("PENDING: CONTINUING 4...\n");

if (empty($filename))
{
    print("ERROR: NO SPECIFIED FILENAME!");
    die ("ERROR: NO SPECIFIED FILENAME!");
}

// Now get whether or not to deploy as production or development
$production = $_POST["production"];

print("PENDING: CONTINUING 5...\n");

if (empty($production))
{
    $production = 0;
}

print("PENDING: CONTINUING 6...\n");

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
