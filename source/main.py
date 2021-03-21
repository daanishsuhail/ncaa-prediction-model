import avg_diff
import SRS
import sys
import os
import csv

# this is the master file where all functions are going to be run.
# do as little work as possible on this file, we'll can call them by classes later.
# all function calling should happen here

# function finds the average point difference. See avg_diff.py for more

# differences - A dictionary set with the key as the teamcode and the value as the average point differential

# REMOVE COMMENTS UNDERNEATH TO DUMP THE AVG DIFF CSV

# Change

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

SRS.SRS('data/team_avg_diffs.csv', "ABILENECHRISTIAN")