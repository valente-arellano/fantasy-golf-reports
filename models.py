class Team:
  def __init__(self, name, players, place = "1st", points = 0.0):
    self.name = name
    self.players = players
    self.place = place
    self.points = points

  def __str__(self):
    def sortByPositions(player):
        pos = player.position
        if pos != None and pos != '-':
            pos = int(pos.replace("T", ""))
        else:
            pos = 1000
        return pos 
    sorted_players = sorted(self.players, key=sortByPositions)
    # team_str = f"{self.place}\t{self.name}\t{round(self.points, 2)}pts total\n"
    team_str = f"--------------------------------------------------------------------------------------------------------------------------------------\n"
    team_str += "|  %-12s %-24s %-12s %-12s %-12s %-12s %-12s %-12s %-12s  |" % (self.place, self.name, f"{round(self.points, 2)}", "", "", "", "", "", "")
    team_str += f"\n--------------------------------------------------------------------------------------------------------------------------------------\n"
    team_str += "|  %-12s %-24s %-12s %-12s %-12s %-12s %-12s %-12s %-12s  |\n" % ("Position", "Name", "Fantasy Pts", "Tee Time", "Curr. Round", "Round Score", "Thru", "Round Status", "Total Score")
    for player in sorted_players:
      team_str += f"{player}\n"
    team_str += f"--------------------------------------------------------------------------------------------------------------------------------------\n"
    return team_str

  

class Player:
  def __init__(self, name, total = "E", position = None, status = "", points = 0.0, currentRound = "", currentRoundScore = "", thru = "", teeTime = ""):
    self.name = name
    self.total = total
    self.position = position
    self.status = status
    self.points = points
    self.currentRound = currentRound
    self.currentRoundScore = currentRoundScore
    self.thru = thru
    self.teeTime = teeTime
  def __str__(self):
    player_str = "|  %-12s %-24s %-12s %-12s %-12s %-12s %-12s %-12s %-12s  |" % (self.position, self.name, round(self.points, 2), self.teeTime, self.currentRound, self.currentRoundScore, self.thru, self.status, self.total)
    return player_str
    # return f"{self.name}\t| Total: {self.total}\t| Position: {self.position} | Status: {self.status}"