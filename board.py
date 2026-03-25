class KnightBoard:
    def __init__(self, size=8):
        self.size = size
        self.num_explored = 0
        self.solution = None
        self.explored = set()

    def notation_to_coords(self, square):
        """
        Convert chess notation like 'a1' to (row, col).

        We use:
            a1 -> (7, 0)
            h8 -> (0, 7)
        so row 0 is the top of the board.
        """
        square = square.strip().lower()

        if len(square) < 2 or len(square) > 3:
            raise ValueError("Square must look like a1, b3, h8, etc.")

        file_char = square[0]
        rank_str = square[1:]

        if not ("a" <= file_char <= "z"):
            raise ValueError("Invalid file letter.")

        if not rank_str.isdigit():
            raise ValueError("Invalid rank number.")

        col = ord(file_char) - ord("a")
        rank = int(rank_str)

        if col < 0 or col >= self.size:
            raise ValueError("File is out of bounds for this board.")

        if rank < 1 or rank > self.size:
            raise ValueError("Rank is out of bounds for this board.")

        row = self.size - rank
        return (row, col)

    def coords_to_notation(self, state):
        row, col = state
        file_char = chr(ord("a") + col)
        rank = self.size - row
        return f"{file_char}{rank}"

    def neighbors(self, state):
        row, col = state

        candidate_moves = [
            ("up 2, right 1", (row - 2, col + 1)),
            ("up 2, left 1", (row - 2, col - 1)),
            ("down 2, right 1", (row + 2, col + 1)),
            ("down 2, left 1", (row + 2, col - 1)),
            ("right 2, up 1", (row - 1, col + 2)),
            ("right 2, down 1", (row + 1, col + 2)),
            ("left 2, up 1", (row - 1, col - 2)),
            ("left 2, down 1", (row + 1, col - 2)),
        ]

        results = []
        for action, (r, c) in candidate_moves:
            if 0 <= r < self.size and 0 <= c < self.size:
                results.append((action, (r, c)))

        return results

    def heuristic(self, state, goal):
        """
        Admissible lower-bound heuristic for knight moves.

        It never overestimates the true number of moves, which is what we want
        for A* optimality.
        """
        row1, col1 = state
        row2, col2 = goal

        dx = abs(row1 - row2)
        dy = abs(col1 - col2)

        # lower bounds based on how far a knight can reduce distance each move
        h1 = (max(dx, dy) + 1) // 2
        h2 = (dx + dy + 2) // 3

        return max(h1, h2)

    def print_board_with_path(self):
        if self.solution is None:
            print("No solution stored.")
            return

        _, cells = self.solution
        path_positions = {state: i for i, state in enumerate(cells)}

        print("\nChessboard Path:")
        print("    " + "  ".join(chr(ord("a") + col) for col in range(self.size)))

        for row in range(self.size):
            rank_label = str(self.size - row).rjust(2)
            print(f"{rank_label} ", end=" ")

            for col in range(self.size):
                state = (row, col)

                if state in path_positions:
                    label = str(path_positions[state]).rjust(2)
                else:
                    label = ".."

                print(label, end=" ")
            print()

        print("\n0 = start")
        print(f"{len(cells) - 1} = goal")