from project.player import Player
from project.guild import Guild

import unittest


class PlayerTest(unittest.TestCase):

    def test_assigning_player_in_the_same_guild(self):
        guild = Guild("GGXrd")
        player = Player("Pesho", 90, 90)
        guild.assign_player(player)
        message = guild.assign_player(player)
        expected = "Player Pesho is already in the guild."
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()
