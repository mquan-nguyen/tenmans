from team import Team
import random

class Lobby():
    def __init__(self, max):
        self.player_list = []
        self.max = max
        self.ON_EACH_TEAM = max / 2
        self.team_one = Team(self.ON_EACH_TEAM)
        self.team_two = Team(self.ON_EACH_TEAM)
            
    def get_team_one(self):
        return self.team_one

    def get_team_two(self):
        return self.team_two
    

    def add(self, player, *args): #args = multiple players
        total_players = (player,) + args #comma to indicate it is a tuple
        for person in total_players:
            assert not person in self.player_list, "Player '" + str(person) + "' already exists in the lobby."
            assert len(self.player_list) + 1 <= self.max, "Lobby at max capacity."
            self.player_list.append(person)


    def remove(self, player):
        self.player_list.remove(player)
        if player in self.team_one:
            self.team_one.remove(player)
        
        if player in self.team_two:
            self.team_two.remove(player)

    def shuffle(self):
        self.team_one.clear()
        self.team_two.clear()
        random.shuffle(self.player_list)

        for x in range(len(self.player_list)):
            if x < (self.max / 2):
                self.team_one.add(self.player_list[x])
            else:
                self.team_two.add(self.player_list[x])
    
    def clear(self):
        self.team_one.clear()
        self.team_two.clear()
        self.player_list.clear()

    def swap(self, player1, player2):
        assert not self.team_one and not self.team_two, "Teams haven't been created!"
        assert player1 in self.player_list, player1 + " is not in the lobby."
        assert player2 in self.player_list, player2 + " is not in the lobby."

        assert not ((player1 in self.team_one and player2 in self.team_one) and 
                    (player1 in self.team_two and player2 in self.team_two)), "Both players are on the same team!" 

        if player1 in self.team_one:
            self.team_one.remove(player1) 
            self.team_one.add(player2)
            self.team_two.remove(player2)
            self.team_two.add(player1)

        else:
            self.team_one.remove(player2)
            self.team_one.add(player1)
            self.team_two.remove(player1)
            self.team_two.add(player2)

