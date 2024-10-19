import unittest
from RPS import player

class TestRPS(unittest.TestCase):
    def test_player(self):
        self.assertIn(player("", []), ["R", "P", "S"])  # 첫 게임에서 무작위 선택
        self.assertEqual(player("R", ["R"]), "P")  # 상대가 바위를 냈을 때 보 선택
        self.assertEqual(player("P", ["P"]), "S")  # 상대가 보를 냈을 때 가위 선택
        self.assertEqual(player("S", ["S"]), "R")  # 상대가 가위를 냈을 때 바위 선택

if __name__ == "__main__":
    unittest.main()
