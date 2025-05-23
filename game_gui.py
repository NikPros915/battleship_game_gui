import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime

# Constants
BOARD_SIZE = 6
SHIP_SIZES = [3, 2, 2, 1, 1, 1]

# Factory Pattern for Ship Creation
class ShipFactory:
    @staticmethod
    def create_ship(size, positions):
        return Ship(size, positions)

class Ship:
    def __init__(self, size, positions):
        self.size = size
        self.positions = positions  # list of (row, col)
        self.hits = set()

    def is_sunk(self):
        return len(self.hits) == self.size

    def register_hit(self, position):
        if position in self.positions:
            self.hits.add(position)
            return True
        return False

class Board:
    def __init__(self):
        self.ships = []
        self.hits = set()
        self.misses = set()

    def place_ship(self, ship):
        self.ships.append(ship)

    def is_valid_position(self, positions):
        for ship in self.ships:
            for pos in ship.positions:
                if pos in positions:
                    return False
        return True

    def receive_attack(self, position):
        for ship in self.ships:
            if position in ship.positions:
                ship.register_hit(position)
                self.hits.add(position)
                return True
        self.misses.add(position)
        return False

    def all_ships_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)

class Player:
    def __init__(self, is_ai=False):
        self.board = Board()
        self.is_ai = is_ai
        self.generate_ships()

    def generate_ships(self):
        for size in SHIP_SIZES:
            placed = False
            while not placed:
                orientation = random.choice(['H', 'V'])
                if orientation == 'H':
                    row = random.randint(0, BOARD_SIZE - 1)
                    col = random.randint(0, BOARD_SIZE - size)
                    positions = [(row, col + i) for i in range(size)]
                else:
                    row = random.randint(0, BOARD_SIZE - size)
                    col = random.randint(0, BOARD_SIZE - 1)
                    positions = [(row + i, col) for i in range(size)]

                if self.board.is_valid_position(positions):
                    ship = ShipFactory.create_ship(size, positions)
                    self.board.place_ship(ship)
                    placed = True

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Battleship Game")
        self.player = Player()
        self.ai = Player(is_ai=True)

        self.buttons = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

        self.create_widgets()
        self.log_file = open("game_log.txt", "w")
        self.log("Game started")

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log_file.write(f"[{timestamp}] {message}\n")
        self.log_file.flush()

    def create_widgets(self):
        label = tk.Label(self.root, text="Click to shoot at the enemy board")
        label.grid(row=0, column=0, columnspan=BOARD_SIZE)

        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                btn = tk.Button(self.root, width=4, height=2, bg='gray',
                                command=lambda r=i, c=j: self.player_shoot(r, c))
                btn.grid(row=i+1, column=j)
                self.buttons[i][j] = btn

    def player_shoot(self, row, col):
        pos = (row, col)
        if pos in self.ai.board.hits or pos in self.ai.board.misses:
            return

        hit = self.ai.board.receive_attack(pos)
        self.buttons[row][col].configure(bg='red' if hit else 'blue')
        self.log(f"Player shoots at {pos} - {'HIT' if hit else 'MISS'}")

        if self.ai.board.all_ships_sunk():
            self.log("Player wins")
            messagebox.showinfo("Game Over", "You Win!")
            self.log_file.close()
            self.root.quit()
        else:
            self.root.after(500, self.ai_turn)

    def ai_turn(self):
        while True:
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - 1)
            pos = (row, col)
            if pos not in self.player.board.hits and pos not in self.player.board.misses:
                break

        hit = self.player.board.receive_attack(pos)
        self.log(f"AI shoots at {pos} - {'HIT' if hit else 'MISS'}")

        if self.player.board.all_ships_sunk():
            self.log("AI wins")
            messagebox.showinfo("Game Over", "AI Wins!")
            self.log_file.close()
            self.root.quit()