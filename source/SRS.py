import csv

# despite what the file name may suggest in statistics, in this project, SRS is an abbreviation for Simple Rating System.

# this is the function responsible for actually calculating every SRS


def calcSRS(atdDict):
    d = dict()
    for k, v in atdDict:
        
    return d


def SRS(avg_team_diffs):
    atd = open(avg_team_diffs, mode='r')
    reader = csv.DictReader(atd)
    l = list(reader)
    atdDict = dict()
    for d in l:
        avg_diffs[d["Teams"]] = d["Avg Point Diff"]
    