###############IMPORT####################################
import records
db = records.Database("postgres://localhost/sports_analysis")

###################Stat Search (Existing Team)#############################
team_name_input = input("Whats the team name? ")
rows = db.query("SELECT * FROM epl_data.py WHERE team_name = :data ;", data=team_name_input)
for row in rows:
   print(row)
#########################CREATE NEW TEAM#######################
new_team_name = input("Whats the new team name? ")
new_team_wins = input("How many wins? ")
new_team_losses = input("How many losses? ")
new_team_points = input("How many points? ")

db.query("INSERT INTO epl_data VALUES (:team_name, :wins, :losses, :points);",
team_name=new_team_name,
wins=new_team_wins,
losses=new_team_losses,
points=new_team_points
)
