label start:
    menu:
        "Story Mode":
            jump story_mode  # Placeholder for story mode content
        "Practice Mode":
            jump practice_mode_selection
        "Two Players":
            $ ai_level = None  # Set ai_level to None for two-player mode
            jump two_player_game

label story_mode:
    define rick = Character("Rick", color="0000FF")

    # Initial scene with user prompt
    scene rickdrivin1
    "Click anywhere to progress with the scene."

    # Additional scenes from rickdrivin2 to gs28
    $ scenes = ["rickdrivin2", "rickdrivin3", "rickdrivin4"] + [f"gs{i}" for i in range(1, 35)]
    
    python:
        for scene_name in scenes:
            renpy.call_in_new_context("display_scene", scene_name)
            if scene_name == "gs33":
                renpy.call("after_gs33")  # Use renpy.call to jump to the new label

    # End the story mode
    return

default is_story_mode = False

label display_scene(scene_name):
    scene expression scene_name  # No transition specified, so it will switch instantly

    if scene_name == "gs9":
        "<Flies Buzzing>"
    elif scene_name == "gs12":
        "<rustles>"
    elif scene_name == "gs21":
        rick "Little girl? I am a police Officer."
    elif scene_name == "gs23":
        rick "Don't be afraid, Little girl?"

    window hide  
    with None  
    $ renpy.pause()  

    return

label after_gs33:
    scene unanglaban
    $ is_story_mode = True  # Set to True for story mode
    "Play TicTacToe and win, if you lose, Game Over."
    jump storya_mode_selection

label two_player_game:
    scene twoplayermode
    $ is_story_mode = False  # Practice mode, set to False
    $ board = ["", "", "", "", "", "", "", "", ""]
    $ current_player = "X"
    $ winner = None
    
    call screen tictactoe_screen

label single_player_game:
    scene practicemode
    $ board = ["", "", "", "", "", "", "", "", ""]
    $ current_player = "X"
    $ winner = None
    
    call screen tictactoe_screen

label storya_mode_selection:
    menu:
        "Single Player (Dumb AI)":
            $ ai_level = "dumb"
            jump single_player_game
        "Single Player (Medium AI)":
            $ ai_level = "medium"
            jump single_player_game
        "Single Player (Expert AI)":
            $ ai_level = "expert"
            jump single_player_game

label practice_mode_selection:
    menu:
        "Single Player (Dumb AI)":
            $ ai_level = "dumb"
            jump single_player_game
        "Single Player (Medium AI)":
            $ ai_level = "medium"
            jump single_player_game
        "Single Player (Expert AI)":
            $ ai_level = "expert"
            jump single_player_game

screen tictactoe_screen:
    hbox:
        spacing 5
        xalign 0.950  # Align to the right
        yalign 0.5  # Align to the middle
        null width 1000  # Add space on the left to push the grid to the right
        grid 3 3:
            spacing 5
            for i in range(9):
                button:
                    background "#ccccccfb"
                    if board[i] == "X":
                        add im.Scale("x_image.png", 180, 180) at truecenter  # Adjust the size here
                    elif board[i] == "O":
                        add im.Scale("o_image.png", 180, 180) at truecenter  # Adjust the size here
                    action If(not board[i] and not winner, [Function(make_move, i), Jump("check_winner")])
                    style "ttt_button"

    vbox:
        xalign 0.970  # Align to the right
        yalign 0.30  # Slightly above the bottom
        null height 10  # Add space above to push it down
        if winner:
            text "Winner: [winner]" style "menu_text" 
        else:
            text "Current Player: [current_player]" style "menu_text" 

    if winner:
        vbox:
            spacing 20
            xalign 0.960
            yalign 0.73
            if winner == "Draw":
                textbutton "Restart Game" action Jump("storya_mode_selection" if is_story_mode else "practice_mode_selection") style "menu_text"
            elif winner == "X" and is_story_mode:  # Assuming X is the player's symbol
                textbutton "Restart Game" action Jump("storya_mode_selection") style "menu_text"
                textbutton "Continue" action Jump("continue_story") style "menu_text"
            elif is_story_mode:  # If it's story mode and the player lost
                textbutton "Advance" action Jump("game_over") style "menu_text"
            else:
                # For Two Players mode, return to main menu instead of restarting with difficulties
                textbutton "Restart Game" action Jump("start") style "menu_text"
    else:
        textbutton "Restart Game" action Jump("start") style "menu_text" xalign 0.980 yalign 0.73

init python:
    def make_move(index):
        if board[index] == "":
            board[index] = current_player

label check_winner:
    $ lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    $ winner = None
    
    python:
        # Check for a winner
        for line in lines:
            if board[line[0]] == board[line[1]] == board[line[2]] != "":
                winner = board[line[0]]
                break

    # Check for a draw
    if not winner and all(board):
        $ winner = "Draw"

    if not winner:
        if ai_level:  # Check if ai_level is set (i.e., single-player mode)
            if current_player == "X":
                $ current_player = "O"
                # Use a timer to simulate AI thinking without blocking the game
                $ ui.timer(0.5, [Function(dumb_ai if ai_level == "dumb" else run_medium_bot if ai_level == "medium" else expert_ai), SetVariable("current_player", "X")])
            else:
                $ current_player = "O" if current_player == "X" else "X"
        else:
            $ current_player = "O" if current_player == "X" else "X"

    call screen tictactoe_screen
    return

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

# Define button styles
style ttt_button:
    xsize 100
    ysize 100
    background "#333"
    text_align 0.5
    hover_background "#555"

style ttt_button_text:
    size 48
    xalign 0.5
    yalign 0.5
    color "#000"

style title_text:
    size 52
    xalign 0.5

style menu_text:
    size 32
    xalign 0.5

label game_over:
    scene unanglaban
    pause

    # Continue or return to the main menu
    menu:
        "Return to Main Menu":
            jump start
        "Restart Game":
            jump storya_mode_selection

label continue_story:
    scene ulwin1
    "<BANG>"
    pause
    scene ulwin2
    pause
    scene ulwin3
    pause
    scene ulwin4
    pause
    scene ulwin5
    pause 
    scene ulwin6
    pause
    scene ulwin7
    pause
    scene titlescreen
    "To Be Continue..."
    pause

    return
