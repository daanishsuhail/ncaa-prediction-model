import avg_diff
import sys

# this is the master file where all functions are going to be run.
# do as little work as possible on this file, we'll can call them by classes later.
# all function calling should happen here

# function finds the average point difference. See avg_diff.py for more

# USE raw_input() for Python 2.x and input() for Python 3.x

def sysInput(str):
    if sys.version_info[0] == 2:
        return raw_input(str(str))
    if sys.version_info[0] == 3:
        return input(str(str))
print("please type in the school code")
print(avg_diff.difference_average(sysInput(str)))
print("Average Tmm-Opp value^\n\n")
