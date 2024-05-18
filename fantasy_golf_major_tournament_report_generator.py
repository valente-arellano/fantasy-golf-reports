from datetime import datetime
import requests
from models import Player, Team

API_URL = "https://live-golf-data.p.rapidapi.com/leaderboard"
MASTERS_TOURN_ID = "014"
PGA_CHAMP_TOURN_ID = "033"

tournId = PGA_CHAMP_TOURN_ID

querystring = {"orgId":"1","tournId":tournId,"year":"2024"}

headers = {
	"X-RapidAPI-Key": "15a9c6e441msh4cff9fab63dbf94p18c537jsnc1b724eedfd4",
	"X-RapidAPI-Host": "live-golf-data.p.rapidapi.com"
}

# get current leaderboard for given tournament
response = requests.get(API_URL, headers=headers, params=querystring)

data = response.json()

teams = [];

if tournId == MASTERS_TOURN_ID:
    teams = [
    Team("Andre", [
        Player("Scottie Scheffler"), 
        Player("Brooks Koepka"), 
        Player("Hideki Matsuyama"), 
        Player("Jordan Spieth"), 
        Player("Cameron Young"), 
        Player("Ludvig Åberg"), 
    ]), 
    Team("Albert", [
        Player("Jon Rahm"), 
        Player("Viktor Hovland"), 
        Player("Will Zalatoris"), 
        Player("Brian Harman"), 
        Player("Matt Fitzpatrick"), 
        Player("Sahith Theegala"), 
        ]), 
    Team("Frank", [
        Player("Xander Schauffele"), 
        Player("Cameron Smith"), 
        Player("Wyndham Clark"), 
        Player("Phil Mickelson"), 
        Player("Akshay Bhatia"), 
        Player("Justin Thomas"), 
        ]), 
    Team("Valente", [
        Player("Joaquin Niemann"), 
        Player("Rory McIlroy"), 
        Player("Dustin Johnson"), 
        Player("Patrick Cantlay"), 
        Player("Jason Day"), 
        Player("Tiger Woods"), 
        ])]
elif tournId == PGA_CHAMP_TOURN_ID:
    teams = [
    Team("Andre", [
        Player("Rory McIlroy"), 
        Player("Jon Rahm"), 
        Player("Justin Thomas"), 
        Player("Collin Morikawa"), 
        Player("Viktor Hovland"), 
        Player("Patrick Cantlay")]), 
    Team("Albert", [
        Player("Scottie Scheffler"), 
        Player("Cameron Smith"), 
        Player("Wyndham Clark"), 
        Player("Joaquin Niemann"),
        Player("Jason Day"), 
        Player("Sepp Straka")]), 
    Team("Frank", [
        Player("Cameron Young"), 
        Player("Brooks Koepka"), 
        Player("Bryson Dechambeau"), 
        Player("Jordan Spieth"), 
        Player("Tommy Fleetwood"), 
        Player("Tony Finau")]), 
    Team("Valente", [
        Player("Xander Schauffele"),
        Player("Ludvig Åberg"), 
        Player("Max Homa"), 
        Player("Hideki Matsuyama"), 
        Player("Will Zalatoris"), 
        Player("Sahith Theegala")])
]

for team in teams:
    for player in team.players:
        first_name = player.name.split(" ")[0]
        last_name = player.name.split(" ")[1]
        for row in data["leaderboardRows"]:
            if row["firstName"].lower() == first_name.lower() and row["lastName"].lower() == last_name.lower():
                player.position = row["position"]
                player.total = row["total"]
                player.status = row["status"]
                player.thru = row["thru"]
                player.currentRoundScore = row["currentRoundScore"]
                player.currentRound = row["currentRound"]["$numberInt"]
                player.teeTime = row["teeTime"]

field = [];         
for team in teams:
    for player in team.players:
        field.append(player)

print(f"Total players in field: {len(field)}")

def fieldByPositions(player):
    pos = player.position
    if pos != None and pos != '-':
        pos = int(pos.replace("T", ""))
    else:
        pos = 1000
    return pos 

field.sort(key=fieldByPositions)

for rank, player in enumerate(field):
    # print(rank, player)
    for team in teams:
        if player in team.players:
            pos = player.position
            if pos != None and pos != '-':
                pos = int(pos.replace("T", ""))
                player.points += (16.6667/(pos))
                team.points += player.points

teams.sort(key=lambda x: x.points, reverse=True)
for i, team in enumerate(teams):
    if i == 0:
        team.place = "1st"
    if i == 1:
        team.place = "2nd"
    if i == 2:
        team.place = "3rd"
    if i == 3:
        team.place = "4th"
    
    
print(f"\nFantasy {'Masters' if tournId == MASTERS_TOURN_ID else 'PGA Championship'} 2024 Standings as of {datetime.today().strftime('%Y-%m-%d %I:%M %p')}:")
for team in teams:
    print(team)