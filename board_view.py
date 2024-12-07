import tkinter as tk
from constants import *  # Ensure constants like BG_COLOR, CELL_SIZE, etc., are defined elsewhere

class BoardView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bg=BG_COLOR)
        self.controller = controller
        self.status_label = None  # Initialize status_label to avoid AttributeError
        self.algorithm_var = tk.StringVar()  # Variable to track selected algorithm
        self.difficulty_var = tk.StringVar()  # Variable to track selected difficulty
        self.algorithm = "Other"  # Set a default value for the algorithm
        self.difficulty = "minimax"  # Set a default value for the difficulty
        self.setup_ui()

    def setup_ui(self):
        # Create a container frame for the algorithm selection
        self.algorithm_frame = tk.Frame(self, bg=BG_COLOR)
        self.algorithm_frame.pack(pady=20)

        tk.Label(
            self.algorithm_frame,
            text="Select AI Algorithm",
            font=('Arial', 16),
            bg=BG_COLOR
        ).pack(pady=10)

        # Dropdown menu for algorithm selection
        algorithms = ["hard"]
        self.algorithm_var.set(algorithms[0])  # Default selection
        
        tk.OptionMenu(
            self.algorithm_frame,
            self.algorithm_var,
            *algorithms,
            command=self.update_algorithm  # Update algorithm dynamically
        ).pack(pady=10)

        # Create another container frame for difficulty selection
        self.difficulty_frame = tk.Frame(self, bg=BG_COLOR)
        self.difficulty_frame.pack(pady=20)

        tk.Label(
            self.difficulty_frame,
            text="Select Difficulty Level",
            font=('Arial', 16),
            bg=BG_COLOR
        ).pack(pady=10)

        # Dropdown menu for difficulty selection
        difficulty_levels = ["minimax_pruning", "minimax", "expect"]
        self.difficulty_var.set(difficulty_levels[1])  # Default selection
        
        tk.OptionMenu(
            self.difficulty_frame,
            self.difficulty_var,
            *difficulty_levels,
            command=self.update_difficulty  # Update difficulty dynamically
        ).pack(pady=10)

        # Button to confirm algorithm and difficulty and start game
        tk.Button(
            self.algorithm_frame,
            text="Start Game",
            font=('Arial', 12),
            command=self.start_game
        ).pack(pady=10)

    def start_game(self):
        """Start the game with the selected AI algorithm and difficulty."""
        selected_algorithm = self.algorithm_var.get()
        selected_difficulty = self.difficulty_var.get()
        
        # Set the selected algorithm and difficulty in the controller
        self.controller.set_algorithm(selected_algorithm)
        self.controller.set_difficulty(selected_difficulty)
        
        # Hide the selection menus and display the game board
        self.algorithm_frame.pack_forget()
        self.difficulty_frame.pack_forget()
        self.create_board()

    def update_algorithm(self, selected_algorithm):
        """Update the AI algorithm dynamically during the game."""
        self.controller.set_algorithm(selected_algorithm)
        if self.status_label:
            self.status_label.config(text=f"AI Algorithm changed to: {selected_algorithm}")

    def update_difficulty(self, selected_difficulty):
        """Update the difficulty level dynamically during the game."""
        self.controller.set_difficulty(selected_difficulty)
        if self.status_label:
            self.status_label.config(text=f"Difficulty level changed to: {selected_difficulty}")

      
    def create_board(self):
        """Create the game board UI."""
        self.board_frame = tk.Frame(
            self,
            bg=BOARD_COLOR,
            padx=PADDING,
            pady=PADDING
        )
        self.board_frame.pack()

        # Scoreboard frame
        self.score_frame = tk.Frame(self, bg=BG_COLOR)
        self.score_frame.pack(pady=10)

        # Human score label
        self.human_score_label = tk.Label(
            self.score_frame,
            text=f"Human: {self.controller.board.score['X']}",
            font=('Arial', 12),
            bg=BG_COLOR
        )
        self.human_score_label.grid(row=0, column=0, padx=10)

        # AI score label
        self.ai_score_label = tk.Label(
            self.score_frame,
            text=f"AI: {self.controller.board.score['O']}",
            font=('Arial', 12),
            bg=BG_COLOR
        )
        self.ai_score_label.grid(row=0, column=1, padx=10)

        # Add dropdown to change algorithms during the game
        self.algorithm_selector_frame = tk.Frame(self, bg=BG_COLOR)
        self.algorithm_selector_frame.pack(pady=10)
        
        tk.Label(
            self.algorithm_selector_frame,
            text="Change AI Algorithm:",
            font=('Arial', 12),
            bg=BG_COLOR
        ).grid(row=0, column=0, padx=5)
        
        algorithms = ["Other"]
        self.algorithm_var.set(self.controller.get_algorithm())  # Set current algorithm
        tk.OptionMenu(
            self.algorithm_selector_frame,
            self.algorithm_var,
            *algorithms,
            command=self.update_algorithm  # Update algorithm dynamically
        ).grid(row=0, column=1, padx=5)
        # Create the board
        self.cells = []
        for row in range(ROWS):
            row_cells = []
            for col in range(COLS):
                cell = tk.Canvas(
                    self.board_frame,
                    width=CELL_SIZE,
                    height=CELL_SIZE,
                    bg=BOARD_COLOR,
                    highlightthickness=0
                )
                cell.grid(row=row, column=col, padx=2, pady=2)
                cell.bind('<Button-1>', lambda e, col=col: self.controller.handle_click(col))
                
                # Create empty circle
                cell.create_oval(
                    CELL_SIZE//2 - PIECE_RADIUS,
                    CELL_SIZE//2 - PIECE_RADIUS,
                    CELL_SIZE//2 + PIECE_RADIUS,
                    CELL_SIZE//2 + PIECE_RADIUS,
                    fill=EMPTY_COLOR
                )
                row_cells.append(cell)
            self.cells.append(row_cells)
        
        # Create reset button
        reset_button = tk.Button(
            self,
            text="New Game",
            command=self.controller.reset_game,
            font=('Arial', 12)
        )
        reset_button.pack(pady=10)
    def update_status(self, player):
        """Update the status label with the current player's turn."""
        if self.status_label:  # Ensure status_label exists
            if player == 'X':
                self.status_label.config(text=f"Player {player}'s turn")
            else:
                self.status_label.config(text=f"AI's turn")
    def update_cell(self, row, col, player):
        """Update a cell with the player's marker."""
        cell = self.cells[row][col]
        cell.delete("all")
        cell.create_oval(
            CELL_SIZE//2 - PIECE_RADIUS,
            CELL_SIZE//2 - PIECE_RADIUS,
            CELL_SIZE//2 + PIECE_RADIUS,
            CELL_SIZE//2 + PIECE_RADIUS,
            fill=PLAYER_COLORS[player]
        )
        self.update_scores()

    def update_scores(self):
        """Update the score labels dynamically."""
        self.human_score_label.config(text=f"Human: {self.controller.board.score['X']}")
        self.ai_score_label.config(text=f"AI: {self.controller.board.score['O']}")

    def update_board(self, board):
        """Update the entire board based on the current state."""
        for row in range(ROWS):
            for col in range(COLS):
                cell = self.cells[row][col]
                cell.delete("all")  # Remove previous content (if any)
                player = board[row][col]
                if player != ' ':  # Only update non-empty cells
                    cell.create_oval(
                        CELL_SIZE//2 - PIECE_RADIUS,
                        CELL_SIZE//2 - PIECE_RADIUS,
                        CELL_SIZE//2 + PIECE_RADIUS,
                        CELL_SIZE//2 + PIECE_RADIUS,
                        fill=PLAYER_COLORS[player]
                    )
                else:
                    cell.create_oval(
                        CELL_SIZE//2 - PIECE_RADIUS,
                        CELL_SIZE//2 - PIECE_RADIUS,
                        CELL_SIZE//2 + PIECE_RADIUS,
                        CELL_SIZE//2 + PIECE_RADIUS,
                        fill=EMPTY_COLOR
                    )

    def reset_board(self):
        """Reset the board to its initial state."""
        for row in range(ROWS):
            for col in range(COLS):
                cell = self.cells[row][col]
                cell.delete("all")
                cell.create_oval(
                    CELL_SIZE//2 - PIECE_RADIUS,
                    CELL_SIZE//2 - PIECE_RADIUS,
                    CELL_SIZE//2 + PIECE_RADIUS,
                    CELL_SIZE//2 + PIECE_RADIUS,
                    fill=EMPTY_COLOR
                )
