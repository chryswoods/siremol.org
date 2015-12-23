#!/usr/bin/perl -W

use Cwd;

# Find the name of the tgz file to unpack
$webtgz = $ARGV[0];

# Find out whether or not to deploy to production
$production = $ARGV[1];

# Use a lock file to ensure that only a single invocation of this
# program is running at a time

$lockfile = ".deploy.lock";

if ( -e $lockfile )
{
    print "Cannot deploy as deployment already in progress...\n";
    exit(0);
}

# Use a key to protect against a race condition
$key = sprintf("%s", rand());

open LOCKFILE,">>$lockfile" or die "Cannot create the lock file! $!";
print LOCKFILE "$key\n";
close(LOCKFILE);

# check that this is the invocation that wrote the key
open LOCKFILE,"<$lockfile" or die "Cannot read the lock file! $!";

$test_key = <LOCKFILE>;
chomp $test_key;

if ($key != $test_key)
{
    print "RACE CONDITION!\n";
    exit(0);
}

# Ok, only a single script can be here at a time
open LOGFILE,">>deploylog.txt" or die "Cannot open logfile! $!";

sub quitScript
{
    unlink $lockfile;
    $nowtime = localtime;
    print "[$nowtime] Deployment complete!\n";
    close(LOGFILE);
    exit(0);
}

*STDOUT = LOGFILE;
*STDERR = LOGFILE;

$nowtime = localtime;
print "\n[$nowtime] Starting a deployment\n";

if ( ! $webtgz )
{
    print " \\-- Cannot deploy as you must specify a filename!\n";
    &quitScript();
}

if ( ! (-e $webtgz) )
{
    print " \\-- Cannot deploy a non-existing website tgz file ($webtgz)\n";
    &quitScript();
}

print " \\-- Trying to deploy $webtgz\n";

if ($production)
{
    $deploy_location = "..";
    print " \\-- Production deployment!\n";
}
else
{
    $deploy_location = "../devel";
    print " \\-- Development deployment!\n";
}

# look for all files that end in .tgz
if (!opendir (DIR, "."))
{
	print " \\-- Cannot open the directory for reading! $!\n";
    &quitScript();
}

$newest_file = 0;
$newest_time = 0;

print " \\-- Scanning directory for tgz files...\n";

while (my $file = readdir(DIR)) 
{
    if ($file =~ m/.tgz$/)
    {
        $mtime = (stat $file)[9];
        print "   \\ -- Considering file $file to unpack [$mtime]...\n";

        if ($mtime > $newest_time)
        {
            $newest_time = $mtime;
            $newest_file = $file;
        }
    }
}

if ($newest_time == 0)
{
    print "   /-- Strange - no website data to deploy...\n";
    &quitScript();
}

if ($newest_file ne $webtgz)
{
    print "  /-- Strange - the newest website data is not the one specified!\n";
    print "  /-- $newest_file vs. $webtgz\n";
    print "  /-- Removing $webtgz\n";
    unlink $webtgz;
    &quitScript();
}

print "   /-- Using $newest_file\n";

$oldcwd = getcwd();

print " \\-- OLDCWD = $oldcwd\n";

if ( ! chdir $deploy_location )
{
    print " \-- CANNOT CHANGE TO DEPLOYMENT LOCATION '$deploy_location': $!\n";
    &quitScript();
}

$newcwd = getcwd;

print " \\-- NEWCWD = $newcwd\n";

print " \\-- Unpacking $oldcwd/$newest_file...\n";

@lines = `tar -zxvf $oldcwd/$newest_file 2>&1`;

foreach $line (@lines)
{
    print "    \\-- $line";
}

chdir $oldcwd;

print "  \\-- Unpacking complete - removing $newest_file\n";
unlink $newest_file;

&quitScript();
