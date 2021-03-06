import unittest
from team import Team

class TestTeam(unittest.TestCase):
    def setUp(self):
        self.team = Team(2)

    def test_add(self):
        self.team.add("Player") 
        self.assertIn("Player", self.team)
    
    def test_multiple_add(self):
        self.team.add("Player1", "Player2")
        self.assertTrue("Player1" in self.team and "Player2" in self.team, msg=str(self.team.get_players()))
    
    def test_duplicate_add(self):
        self.team.add("Player") 
        self.assertRaises(AssertionError, self.team.add, "Player")

    def test_team_max(self):
        self.team.add("1")
        self.team.add("2")
        self.assertRaises(AssertionError, self.team.add, "3")

    def test_remove(self):
        self.team.add("Player")
        self.team.remove("Player")
        self.assertNotIn("Player", self.team)
    
    def test_remove_nonexisting(self):
        self.assertRaises(ValueError, self.team.remove, "Player")

    def test_get_players(self):
        self.team.add("Player")
        something = self.team.get_players()
        self.assertEqual(something, self.team.players)

    def test_iterable(self):
        y = iter(self.team)
        players = iter(self.team.players)

        compared_players = (x1 == x2 for x1, x2 in zip(y, players))
        self.assertTrue(all(compared_players))

    def test_iterable_realcase(self):
        self.team.add("Player1")
        self.team.add("Player2")
        found = False
        for player in self.team:
            if player == "Player2":
                found = True
        self.assertTrue(found)

    def test_clear(self):
        self.team.add("Player1")
        self.team.add("Player2")
        self.team.clear()
        self.team == None

    def test_bool(self):
        self.team.add("Player1")
        self.team.add("Player2")
        self.assertTrue(self.team)

if __name__ == '__main__':
    unittest.main()