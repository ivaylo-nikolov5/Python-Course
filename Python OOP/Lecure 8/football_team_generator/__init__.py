from project.player import Player
from project.team import Team


t = Team("Best", 10)
p = Player("Pall", 3, 3, 3, 3)
t.add_player(p)
exp = t.remove_player("Pall")
print(exp)
