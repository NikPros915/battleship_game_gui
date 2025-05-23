import unittest
from game_gui import Ship, Board, Player

class TestBattleshipGame(unittest.TestCase):

    def test_ship_hit_and_sunk(self):
        ship = Ship(2, [(0, 0), (0, 1)])
        self.assertFalse(ship.is_sunk())
        ship.register_hit((0, 0))
        self.assertFalse(ship.is_sunk())
        ship.register_hit((0, 1))
        self.assertTrue(ship.is_sunk())

    def test_board_receive_attack(self):
        board = Board()
        ship = Ship(1, [(2, 2)])
        board.place_ship(ship)
        self.assertTrue(board.receive_attack((2, 2)))
        self.assertFalse(board.receive_attack((0, 0)))

    def test_all_ships_sunk(self):
        board = Board()
        ship1 = Ship(1, [(0, 0)])
        ship2 = Ship(1, [(1, 1)])
        board.place_ship(ship1)
        board.place_ship(ship2)
        board.receive_attack((0, 0))
        board.receive_attack((1, 1))
        self.assertTrue(board.all_ships_sunk())

    def test_player_ship_generation(self):
        player = Player()
        total_cells = sum(len(ship.positions) for ship in player.board.ships)
        self.assertEqual(total_cells, sum([3, 2, 2, 1, 1, 1]))

if __name__ == '__main__':
    unittest.main()