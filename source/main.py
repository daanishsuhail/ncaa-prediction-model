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

# REMOVE COMMENTS BELOW FOR CSV DUMP OF AVERAGE TEAM DIFFERENTIALS

# with open('team_avg_diffs.csv', 'w') as dump:
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

SRS.SRS('data/team_avg_diffs.csv', 'ABILENECHRISTIAN')