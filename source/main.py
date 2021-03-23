import avg_diff
import SRS
import sys
import os
import csv
import platform
import re
from sportsipy.ncaab import conferences
from sportsipy.ncaab import teams

Teams = teams.Teams(2021)
Conferences = conferences.Conferences(2021)
# this is the master file where all functions are going to be run.
# do as little work as possible on this file, we'll can call them by classes later.
# all function calling should happen here

# function finds the average point difference. See avg_diff.py for more

# differences - A dictionary set with the key as the teamcode and the value as the average point differential

######################################

# This only works for CSVs structured like a dictionary. Essentially, they can only have two headers:
# One that functions like a key, and one that functions like the value w/ the key provided
def csvToDict(csvPath, keyHeader, valHeader):
    c = open(csvPath, mode='r')
    reader = csv.DictReader(c)
    l = list(reader)
    d = dict()
    for d1 in l:
        d[d1[keyHeader]] = d1[valHeader]
    return d

def dumpDictCSV(filepath, dict, fieldnames):
    with open(filepath, 'w') as dump:
        writer = csv.DictWriter(dump, fieldnames=fieldnames)
        writer.writeheader()
        for k, v in dict.items():
            writer.writerow({fieldnames[0]: k, fieldnames[1]: v})

def dumpSetCSV(filepath, set, fieldname):
    with open(filepath, 'w') as dump:
        writer = csv.DictWriter(dump, fieldnames=fieldname)
        writer.writeheader()
        for i in set:
            writer.writerow({fieldname[0]: i})

def mergeListsAsDict(keys, vals):
    d = dict()
    if len(keys) == len(vals):
        for k in keys:
            d[k] = vals[keys.index(k)]
    return d

# This function returns an entire column as a list.
def parseCSV(csvPath, colNum, rowStart):
    l = list()
    file = open(csvPath, mode='r')
    reader = csv.reader(file)
    parsed = list(reader)
    rows = len(list(open(csvPath)))
    for r in range(rowStart, rows):
        l.append(parsed[r][colNum])
    return l

######################################

# REMOVE COMMENTS BELOW FOR CSV DUMP OF AVERAGE TEAM DIFFERENTIALS

# with open('data/team_avg_diffs.csv', 'w') as dump:
#     fieldnames = ["Teams", "Avg Point Diff"]
#     writer = csv.DictWriter(dump, fieldnames=fieldnames)
#     writer.writeheader()
#     for filename in os.listdir(os.path.abspath('data/team_data/')):
#         if filename.endswith(".csv"):
#             diff = avg_diff.difference_average(filename)
#             print(diff)
#             writer.writerow({"Teams": filename.split('.')[0], "Avg Point Diff": diff})
#         else:
#             continue

#####################################

# REMOVE COMMENTS BELOW FOR CSV DUMP OF ALL TEAMS PLAYED

# all_teams = set()

# for filename in os.listdir('data/team_data/'):
#     if filename.endswith(".csv"):
#         with open(os.path.abspath('data/team_data/'+filename), 'r') as file:
#             reader = csv.reader(file)
#             listreader = list(reader)
#             totalrows = len(list(open(os.path.abspath('data/team_data/'+filename))))
#             column = 5
#             for row in range(1, totalrows):
#                 opp = str(listreader[row][column])
#                 final = opp
#                 final = re.sub(r"\s\(\d*\)", "", opp)
#                 all_teams.add(final)
#     else:
#         continue

# dumpSetCSV('data/allTeams.csv', all_teams, ["ALL OPPONENTS"])

# def SRSmain(avg_team_diffs, conf_spread, conf_summary):
#     # atd = the dictionary of every team's average point differential.
#     atd = csvToDict(avg_team_diffs, "Teams", "Avg Point Diff")
#     # confSpread = the dictionary used tor referring teams to their respective conferences
#     confSpread = csvToDict(conf_spread, "Team", "Conference")
#     # confProp = the dictionary with every team stored with their respective conference proportion
#     # this weighs each conference based on how many teams the conference chose for the NCAA tournament.
#     confProp = mergeListsAsDict(parseCSV(conf_summary, 1, 1), parseCSV(conf_summary, 9, 1))
#     # SRSs = the calculated dictionary of all the SRSs. the final number is the number of iterations the recursive function will calculate.
#     SRSs = SRS.calcSRS(atd, confSpread, confProp, 50000)
#     # finally, the SRSs are dumped to "data/SRSs.csv" for further analysis.
#     dumpDictCSV('data/SRSs.csv', SRSs, ["Teams", "SRS"])

# SRSmain('data/team_avg_diffs.csv', 'data/conf_data/ncaa-conf-spread.csv', 'data/conf_data/conf_summary.csv')

conference_weight = {}
scores = {}
for c, d in Conferences.conferences.items():
    print(c+":")
    confWeight = 0
    teams = 0
    for teamabb in d["teams"]:
        print("        "+teamabb+'\n            = '+str(Teams.__getitem__(teamabb).simple_rating_system)+'')
        teams += 1
        try: confWeight += Teams.__getitem__(teamabb).simple_rating_system
        except TypeError: continue
    confWeight /= teams
    print("weight:"+str(confWeight)+'\n')
    conference_weight[c] = confWeight
        

for team in Teams:
    print(team.conference)
    confWeight = conference_weight[team.conference]
    try: scores[team.name] = (team.simple_rating_system + team.strength_of_schedule)*(confWeight)/2
    except TypeError: scores[team.name] = 0

dumpDictCSV('data/Scores.csv', scores, ["Teams", "SRS"])