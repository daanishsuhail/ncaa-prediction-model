import avg_diff
import sys
import os

# this is the master file where all functions are going to be run.
# do as little work as possible on this file, we'll can call them by classes later.
# all function calling should happen here

# function finds the average point difference. See avg_diff.py for more

# differences - A dictionary set with the key as the teamcode and the value as the average point differential
differences = {}
print(os.path.abspath('data/team_data/'))
for filename in os.listdir(os.path.abspath('data/team_data/')):
    if filename.endswith(".csv"):
        diff = avg_diff.difference_average(filename)
        print(diff)
        differences[filename.split('.')[0]] = diff
    else:
        continue

print(differences)