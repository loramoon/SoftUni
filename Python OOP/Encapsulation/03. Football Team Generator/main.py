from project.player import Player
from project.team import Team


def test_team_init(self):
    t = Team("Best", 10)
    self.assertEqual(t._Team__name, "Best")
    self.assertEqual(t._Team__rating, 10)
    self.assertEqual(len(t._Team__players), 0)