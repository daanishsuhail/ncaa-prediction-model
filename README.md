# 2021-NCAA-prediction-model
---
Creates a basic model for ncaa predictions.

### Adding Data
Data can be added by
1. Deleting the contents of the data folder
2. Placing the contents of the extracted data folder into the project data folder
3. It should have the same directory structure as the current dataless repo with placeholder files.

Directory structure should resemble

ncaa-prediction-model
                 |
                 |
                 |_data
                        |
                        |_team_data
                        |
                        |_conf_data

### School Codes
School Codes found in the [school_codes.md](team_codes.md) file

### Team Average Point Differentials CSV
Apon running the main file with proper csv files of each team, a "team_avg_diffs.csv" file will appear in the main project directory. This will then be fed through "SRS.py" where each average point margin will balance eachother out in a matrix-type solution. (Credit to [sports-reference.com](https://www.pro-football-reference.com/blog/index4837.html?p=3) for the formula)

References:
* https://sports.sites.yale.edu/game-team-statistics-nba
* https://www.pro-football-reference.com/blog/index4837.html?p=3
* All data taken from www.sports-reference.com and www.espn.com
* https://sportsreference.readthedocs.io/en/stable/
