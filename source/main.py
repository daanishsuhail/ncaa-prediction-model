import avg_diff
import SRS
import sys
import os
import csv
import platform

# this is the master file where all functions are going to be run.
# do as little work as possible on this file, we'll can call them by classes later.
# all function calling should happen here

# function finds the average point difference. See avg_diff.py for more

# differences - A dictionary set with the key as the teamcode and the value as the average point differential

######################################

# REMOVE COMMENTS BELOW FOR CSV DUMP OF AVERAGE TEAM DIFFERENTIALS

# with open('data/team_avg_diffs.csv', 'w') as dump:
#     fieldnames = ["Teams", "Avg Point Diff"]
#     writer = csv.DictWriter(dump, fieldnames=fieldnames)
#     linux_stringa = ''
#     linux_stringb = ''
#     if platform.system() == 'Linux':
#         linux_stringa = '../'
#     writer.writeheader()
#     for filename in os.listdir(os.path.abspath(linux_stringa+'data/team_data/')):
#         if filename.endswith(".csv"):
#             diff = avg_diff.difference_average(filename)
#             print(diff)
#             writer.writerow({"Teams": filename.split('.')[0], "Avg Point Diff": diff})
#         else:
#             continue

def dumpCSV(filepath, dict, fieldnames):
    with open(filepath, 'w') as dump:
        writer = csv.DictWriter(dump, fieldnames=fieldnames)
        writer.writeheader()
        for k, v in dict.items():
            writer.writerow({fieldnames[0]: k, fieldnames[1]: v})

def SRSmain(avg_team_diffs, conf_spread, conf_summary):
    atd = SRS.csvToDict(avg_team_diffs, "Teams", "Avg Point Diff")
    confSpread = SRS.csvToDict(conf_spread, "Team", "Conference")
    confProp = SRS.mergeListsAsDict(SRS.parseCSV(conf_summary, 1, 1), SRS.parseCSV(conf_summary, 9, 1))
    SRSs = SRS.calcSRS(atd, confSpread, confProp, 2000)
    dumpCSV('data/SRSs.csv', SRSs, ["Teams", "SRS"])

SRSmain('data/team_avg_diffs.csv', 'data/conf_data/ncaa-conf-spread.csv', 'data/conf_data/conf_summary.csv')