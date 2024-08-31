init python:
    import random  # Import the random module at the beginning

    def dumb_ai():
        import random
        while True:
            a = random.randint(0, 2)
            b = random.randint(0, 2)
            if board[a*3 + b] == "":
                board[a*3 + b] = "O"
                break

    def run_medium_bot():
        global current_player, board, i_last_move

        # Determine the opponent
        if current_player == "X":
            i_opponent = "O"
        else:
            i_opponent = "X"

        # Check for first move
        if board.count("") == 9:  # If it's the first move
            i_last_move = random.choice([i for i in range(9) if board[i] == ""])
        else:
            i_last_move = -1  # Initialize i_last_move to an invalid position
            check_win_and_dont_lose(i_opponent)  # Check don't lose
            check_win_and_dont_lose(current_player)  # Check win
            
            # If no valid move was set in check_win_and_dont_lose, choose a random one
            if i_last_move == -1 or board[i_last_move] != "":
                i_last_move = random.choice([i for i in range(9) if board[i] == ""])

        # Update game state
        board[i_last_move] = current_player

    def check_win_and_dont_lose(player):
        global board, i_last_move
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for line in lines:
            line_values = [board[i] for i in line]
            if line_values.count(player) == 2 and line_values.count("") == 1:
                i_last_move = line[line_values.index("")]
                return

    def expert_ai():
        best_score = -1000
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i*3 + j] == "":
                    board[i*3 + j] = "O"
                    score = minimax(board, 0, False)
                    board[i*3 + j] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        board[best_move[0]*3 + best_move[1]] = "O"

    def minimax(new_board, depth, is_maximizing):
        scores = {"X": -10, "O": 10, "Draw": 0}
        result = check_winner_state(new_board)
        if result:
            return scores[result]
        
        if is_maximizing:
            best_score = -1000
            for i in range(3):
                for j in range(3):
                    if new_board[i*3 + j] == "":
                        new_board[i*3 + j] = "O"
                        score = minimax(new_board, depth + 1, False)
                        new_board[i*3 + j] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = 1000
            for i in range(3):
                for j in range(3):
                    if new_board[i*3 + j] == "":
                        new_board[i*3 + j] = "X"
                        score = minimax(new_board, depth + 1, True)
                        new_board[i*3 + j] = ""
                        best_score = min(score, best_score)
            return best_score

    def check_winner_state(grid):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if grid[line[0]] == grid[line[1]] == grid[line[2]] != "":
                return grid[line[0]]
        if all(grid):
            return "Draw"
        return None