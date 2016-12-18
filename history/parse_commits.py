
import json
import datetime

google_commits = []
svn_commits = []

# Read all of the commit messages from the google code 
# repository
for i in range(1,29):
    FILE = open("commits-page-%d.json" % i, "r")
    j = json.load(FILE)
    FILE.close()

    c = j["commits"]

    google_commits += c

# Now read all of the commits from the original svn repository
lines = open("original_repository_comments.txt", "r").readlines()

commit_id = None
commit_date = None
commit_msg = []

def to_date(s):
    words = s.split()
    ymd = words[0].split("-")
    hms = words[1].split(":")

    bst = (words[2].find("+0100") != -1)

    d = None

    if bst:
        if int(hms[0]) == 23:
            d = datetime.datetime(int(ymd[0]), int(ymd[1]), int(ymd[2])+1,
                                  0, int(hms[1]), int(hms[2]))
        else:
            d = datetime.datetime(int(ymd[0]), int(ymd[1]), int(ymd[2]),
                                  int(hms[0])+1, int(hms[1]), int(hms[2]))
    else:
        d = datetime.datetime(int(ymd[0]), int(ymd[1]), int(ymd[2]),
                              int(hms[0]), int(hms[1]), int(hms[2]))

    return "%4d-%02d-%02dT%02d:%02d:%02d.000000Z" % (d.year,d.month,d.day,d.hour,d.minute,d.second)

for line in lines:
    if line.find("------------------------------------------------------------------------") != -1:
        if commit_id:
            c = {}
            c["author"] = "chryswoods@gmail.com"
            c["commit"] = str(commit_id)
            c["date"] = to_date(commit_date)
            c["message"] = "\n".join(commit_msg).lstrip().rstrip()
            svn_commits.append(c)

            commit_id = None
            commit_date = None
            commit_msg = []
    elif not commit_id:
        # try to find the ID and date of this commit
        words = line.split()

        try:
            if words[0].find("r") == 0:
                commit_id = int(words[0][1:])

                words = line.split("|")
                commit_date = words[2].lstrip().rstrip()
        except:
            pass
    else:
        commit_msg.append(line.rstrip())

if commit_id:
    c = {}
    c["author"] = "chryswoods@gmail.com"
    c["commit"] = str(commit_id)
    c["date"] = to_date(commit_date)
    c["message"] = "\n".join(commit_msg).lstrip().rstrip()
    svn_commits.append(c)

jcommits = {}

jcommits["svn"] = svn_commits
jcommits["googlecode"] = google_commits

FILE = open("commits.json", "w")

json.dump(jcommits, FILE)

FILE.close()

