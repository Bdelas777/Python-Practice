class Ship:
    """Represents a ship with its properties and state."""
    
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []  # List of (row, col) tuples
        self.hits = set()    # Set of hit positions
    
    def place(self, start_row, start_col, orientation):
        """Place the ship at given position with specified orientation."""
        self.positions = []
        
        if orientation == 'horizontal':
            for i in range(self.size):
                self.positions.append((start_row, start_col + i))
        elif orientation == 'vertical':
            for i in range(self.size):
                self.positions.append((start_row + i, start_col))
        else:
            raise ValueError("Orientation must be 'horizontal' or 'vertical'")
    
    def is_hit(self, row, col):
        """Check if this position hits the ship."""
        return (row, col) in self.positions
    
    def hit(self, row, col):
        """Register a hit on this ship."""
        if self.is_hit(row, col):
            self.hits.add((row, col))
            return True
        return False
    
    def is_sunk(self):
        """Check if the ship is completely sunk."""
        return len(self.hits) == self.size
    
    def __str__(self):
        return f"{self.name} (size {self.size})"


class BattleshipBoard:
    """Represents a player's battleship board."""
    
    GRID_SIZE = 10
    
    # Ship types and quantities as specified
    FLEET = [
        ("Aircraft Carrier", 5, 1),
        ("Battleship", 4, 1),
        ("Submarine", 3, 1),
        ("Destroyer", 3, 2),
        ("Patrol Boat", 2, 2)
    ]
    
    def __init__(self):
        # Initialize empty grid (None = empty, 'M' = miss, 'H' = hit)
        self.grid = [[None for _ in range(self.GRID_SIZE)] for _ in range(self.GRID_SIZE)]
        self.ships = []
        self.ship_positions = {}  # Maps (row, col) to ship object
        
        # Create fleet
        for ship_name, size, quantity in self.FLEET:
            for i in range(quantity):
                # If multiple ships of same type, add number suffix
                name = ship_name if quantity == 1 else f"{ship_name} {i+1}"
                self.ships.append(Ship(name, size))
    
    def is_valid_position(self, row, col):
        """Check if position is within grid bounds."""
        return 0 <= row < self.GRID_SIZE and 0 <= col < self.GRID_SIZE
    
    def can_place_ship(self, ship, start_row, start_col, orientation):
        """Check if a ship can be placed at the given position."""
        positions = []
        
        # Calculate all positions the ship would occupy
        if orientation == 'horizontal':
            for i in range(ship.size):
                pos = (start_row, start_col + i)
                positions.append(pos)
        elif orientation == 'vertical':
            for i in range(ship.size):
                pos = (start_row + i, start_col)
                positions.append(pos)
        else:
            return False, "Invalid orientation"
        
        # Check if all positions are valid and empty
        for row, col in positions:
            if not self.is_valid_position(row, col):
                return False, "Ship extends outside grid"
            if (row, col) in self.ship_positions:
                return False, "Position already occupied by another ship"
        
        return True, "Valid placement"
    
    def place_ship(self, ship_index, start_row, start_col, orientation):
        """Place a ship on the board."""
        if ship_index < 0 or ship_index >= len(self.ships):
            return False, "Invalid ship index"
        
        ship = self.ships[ship_index]
        
        # Check if ship is already placed
        if ship.positions:
            return False, "Ship is already placed"
        
        # Validate placement
        can_place, message = self.can_place_ship(ship, start_row, start_col, orientation)
        if not can_place:
            return False, message
        
        # Place the ship
        ship.place(start_row, start_col, orientation)
        
        # Update ship positions mapping
        for pos in ship.positions:
            self.ship_positions[pos] = ship
        
        return True, f"{ship.name} placed successfully"
    
    def hit_square(self, row, col):
        """Process a hit on the given square."""
        if not self.is_valid_position(row, col):
            return False, "Invalid coordinates"
        
        # Check if square was already targeted
        if self.grid[row][col] is not None:
            return False, "Square already targeted"
        
        # Check if there's a ship at this position
        if (row, col) in self.ship_positions:
            ship = self.ship_positions[(row, col)]
            ship.hit(row, col)
            self.grid[row][col] = 'H'  # Hit
            
            if ship.is_sunk():
                return True, f"Hit! {ship.name} sunk!"
            else:
                return True, "Hit!"
        else:
            self.grid[row][col] = 'M'  # Miss
            return True, "Miss!"
    
    def has_lost(self):
        """Check if all ships have been sunk."""
        return all(ship.is_sunk() for ship in self.ships)
    
    def get_ship_by_name(self, name):
        """Get ship by name for easier testing."""
        for ship in self.ships:
            if ship.name == name:
                return ship
        return None
    
    def display_board(self, show_ships=True):
        """Display the board (for debugging/visualization)."""
        print("   A B C D E F G H I J")
        for row in range(self.GRID_SIZE):
            line = f"{row} "
            for col in range(self.GRID_SIZE):
                if self.grid[row][col] == 'H':
                    line += " X"  # Hit
                elif self.grid[row][col] == 'M':
                    line += " ·"  # Miss
                elif show_ships and (row, col) in self.ship_positions:
                    line += " S"  # Ship
                else:
                    line += " ~"  # Water
            print(line)
    
    def get_fleet_status(self):
        """Get status of all ships."""
        status = []
        for ship in self.ships:
            if ship.positions:  # Only show placed ships
                sunk = "SUNK" if ship.is_sunk() else f"HITS: {len(ship.hits)}/{ship.size}"
                status.append(f"{ship.name}: {sunk}")
        return status


class BattleshipGame:
    """Main game controller for Battleship."""
    
    def __init__(self):
        self.player1_board = BattleshipBoard()
        self.player2_board = BattleshipBoard()
        self.current_player = 1
        self.game_over = False
        self.winner = None
    
    def get_current_board(self):
        """Get the current player's board."""
        return self.player1_board if self.current_player == 1 else self.player2_board
    
    def get_opponent_board(self):
        """Get the opponent's board."""
        return self.player2_board if self.current_player == 1 else self.player1_board
    
    def place_ship(self, ship_index, start_row, start_col, orientation):
        """Place a ship for the current player."""
        if self.game_over:
            return False, "Game is over"
        
        board = self.get_current_board()
        return board.place_ship(ship_index, start_row, start_col, orientation)
    
    def make_shot(self, row, col):
        """Current player makes a shot at opponent's board."""
        if self.game_over:
            return False, "Game is over"
        
        opponent_board = self.get_opponent_board()
        success, message = opponent_board.hit_square(row, col)
        
        if success:
            # Check if opponent has lost
            if opponent_board.has_lost():
                self.game_over = True
                self.winner = self.current_player
                message += f" Player {self.current_player} wins!"
            
            # Switch turns
            self.current_player = 2 if self.current_player == 1 else 1
        
        return success, message
    
    def is_setup_complete(self, player=None):
        """Check if ship placement is complete for a player."""
        if player is None:
            player = self.current_player
        
        board = self.player1_board if player == 1 else self.player2_board
        return all(len(ship.positions) > 0 for ship in board.ships)


# Example usage and testing
if __name__ == "__main__":
    # Create a game
    game = BattleshipGame()
    
    # Example: Place ships for Player 1
    print("=== Placing ships for Player 1 ===")
    board1 = game.player1_board
    
    # Place Aircraft Carrier (index 0) horizontally at A0
    success, msg = board1.place_ship(0, 0, 0, 'horizontal')
    print(f"Aircraft Carrier: {success} - {msg}")
    
    # Place Battleship (index 1) vertically at C0
    success, msg = board1.place_ship(1, 0, 2, 'vertical')
    print(f"Battleship: {success} - {msg}")
    
    # Place Submarine (index 2) horizontally at F6
    success, msg = board1.place_ship(2, 6, 5, 'horizontal')
    print(f"Submarine: {success} - {msg}")
    
    # Place first Destroyer (index 3) vertically at I9
    success, msg = board1.place_ship(3, 7, 9, 'vertical')
    print(f"Destroyer 1: {success} - {msg}")
    
    # Place second Destroyer (index 4) horizontally at E3
    success, msg = board1.place_ship(4, 3, 4, 'horizontal')
    print(f"Destroyer 2: {success} - {msg}")
    
    # Place first Patrol Boat (index 5) vertically at G1
    success, msg = board1.place_ship(5, 1, 6, 'vertical')
    print(f"Patrol Boat 1: {success} - {msg}")
    
    # Place second Patrol Boat (index 6) horizontally at H7
    success, msg = board1.place_ship(6, 7, 7, 'horizontal')
    print(f"Patrol Boat 2: {success} - {msg}")
    
    print(f"\nPlayer 1 setup complete: {game.is_setup_complete(1)}")
    print("\nPlayer 1 Board:")
    board1.display_board(True)
    
    # Test some shots
    print("\n=== Testing shots ===")
    shots = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (6, 5)]
    
    for row, col in shots:
        success, msg = board1.hit_square(row, col)
        print(f"Shot at ({row}, {col}): {msg}")
    
    print(f"\nPlayer 1 has lost: {board1.has_lost()}")
    print("\nFleet Status:")
    for status in board1.get_fleet_status():
        print(f"  {status}")
    
    print("\nBoard after shots:")
    board1.display_board(True)