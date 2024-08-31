#Main menu after start, for selecting game modes
label start:
    menu:
        "Story Mode":
            jump story_mode  
        "Practice Mode":
            jump practice_mode_selection
        "Two Players":
            $ ai_level = None  # Set ai_level to None for two-player mode
            jump two_player_game

# Story mode script
label story_mode:
    define rick = Character("Rick", color="0000FF")

    play music "audio/crickets.wav" loop

    scene rickdrivin1
    "Click anywhere to progress with the scene."

    $ scenes = ["rickdrivin2", "rickdrivin3", "rickdrivin4"] + [f"gs{i}" for i in range(1, 35)]
    
    python:
        for scene_name in scenes:
            renpy.call_in_new_context("display_scene", scene_name)
            if scene_name == "gs33":
                renpy.call("after_gs33")  

    stop music

    return

# Flag to trach if the user is in story mode
default is_story_mode = False

# Display a dialogue based on the scene_name variable
label display_scene(scene_name):
    scene expression scene_name  # No transition

    # Dialogue associated with the scenes.
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

# First walker enemy in story mode
label after_gs33:
    play music "audio/twdintro.mp3" loop
    scene unanglaban
    $ is_story_mode = True  # Set to True for story mode
    "Play TicTacToe and win, if you lose, Game Over."
    jump storya_mode_selection

# Two-player game mode, no AI.
label two_player_game:
    play music "audio/twdintro.mp3" loop 
    scene twoplayermode
    $ is_story_mode = False  # Practice mode, set to False
    $ board = ["", "", "", "", "", "", "", "", ""]
    $ current_player = "X"
    $ winner = None
    
    call screen tictactoe_screen

# Single-player or practice game mode with AI.
label single_player_game:
    play music "audio/twdintro.mp3" loop 
    scene practicemode with None
    $ board = ["", "", "", "", "", "", "", "", ""]
    $ current_player = "X"
    $ winner = None
    call screen tictactoe_screen

# Define your background image with scaling
image practicemode = im.Scale("images/practicemode.png", config.screen_width, config.screen_height)

# Story game mode, TicTacToe game
label iztorya_player_game:
    play music "audio/twdintro.mp3" loop 
    $ board = ["", "", "", "", "", "", "", "", ""]
    $ current_player = "X"
    $ winner = None
    
    call screen tictactoe_screen

# Selection for different AI levels in story mode 
label storya_mode_selection:
    menu:
        "Single Player (Dumb AI)":
            $ ai_level = "dumb"
            jump iztorya_player_game
        "Single Player (Medium AI)":
            $ ai_level = "medium"
            jump iztorya_player_game
        "Single Player (Expert AI)":
            $ ai_level = "expert"
            jump iztorya_player_game

# Selection for different AI levels in practice mode
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
    add im.Scale("grid_box.png", 650, 650) at Position(xalign=0.987, yalign=0.9)
    
    hbox: # The Tic-Tac-Toe 3x3 grid box
        spacing 5
        xalign 0.828
        yalign 0.82
        null width 1000
        grid 3 3:
            spacing 30
            for i in range(9):
                button:
                    background "#cccccc00"
                    hover_background "#ccac886e"
                    xysize (160, 160)
                    if board[i] == "X":
                        add im.Scale("x_image.png", 300, 300) at truecenter
                    elif board[i] == "O":
                        add im.Scale("o_image.png", 300, 300) at truecenter
                    # Disable the button if the game is over (winner is not None)
                    action If(not board[i] and not winner, [Function(make_move, i), Jump("check_winner")])
                    style "ttt_button"

    vbox: # Tic-Tac-Toe winner and current player indicator
        xalign 0.870
        yalign 0.365
        null height 20
        if winner:
            text "Winner: [winner]" style "menu_text"
        else:
            text "Current Player: [current_player]" style "menu_text"

    if winner:
        vbox: # Tic-Tac-Toe post-game block
            spacing 20
            xalign 0.980
            yalign 0.28
            if winner == "Draw":
                textbutton "Restart Game" action Jump("storya_mode_selection" if is_story_mode else "practice_mode_selection") style "menu_text"
            elif winner == "X" and is_story_mode:
                textbutton "Restart Game" action Jump("storya_mode_selection") style "menu_text"
                textbutton "Continue" action Jump("continue_story") style "menu_text"
            elif is_story_mode:
                textbutton "Advance" action Jump("game_over") style "menu_text"
            else:
                textbutton "Restart Game" action Jump("start") style "menu_text"
    else:
        textbutton "Restart Game" action Jump("start") style "menu_text" xalign 0.980 yalign 0.28

# Function to handle player moves
init python:
    def make_move(index):
        if board[index] == "":
            board[index] = current_player

# Background images that requires adapting to the current resolution
init python:
    # List of image filenames (without the .png extension)
    image_names = [
        "rickdrivin1", "rickdrivin2", "rickdrivin3", "rickdrivin4",
        "gs1", "gs2", "gs3", "gs4", "gs5", "gs6", "gs7", "gs8",
        "gs9", "gs10", "gs11", "gs12", "gs13", "gs14", "gs15", "gs16",
        "gs17", "gs18", "gs19", "gs20", "gs21", "gs22", "gs23", "gs24",
        "gs25", "gs26", "gs27", "gs28", "gs29", "gs30", "gs31", "gs32",
        "gs33", "unanglaban", "twoplayermode", "gameover1", "ulwin1", 
        "ulwin2", "ulwin3", "ulwin4", "ulwin5", "ulwin6", "ulwin7", "titlescreen"
    ]

    # Background images will are forced to fit the screen no matter the resolution
    for name in image_names:
        renpy.image(name, im.Scale(f"images/{name}.png", config.screen_width, config.screen_height))

# Checking the winner after each move
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
    if not winner and all(cell != "" for cell in board):
        $ winner = "Draw"

    if winner:
        $ current_player = None  # Disable current player to prevent further moves
        call screen tictactoe_screen  # Update the screen with the winner
        return

    # Switch players if no winner
    if not winner:
        if ai_level and current_player == "X":  # Player just moved
            $ current_player = "O"
            $ ui.timer(0.5, [Function(dumb_ai if ai_level == "dumb" else run_medium_bot if ai_level == "medium" else expert_ai), Jump("check_winner")])
        else:
            $ current_player = "O" if current_player == "X" else "X"

    call screen tictactoe_screen
    return

# AI and game logic for different difficulty levels
init python:
    import random  # Import the random module at the beginning

    # Dumb AI randomly selects a move
    def dumb_ai():
        import random
        while True:
            a = random.randint(0, 2)
            b = random.randint(0, 2)
            if board[a*3 + b] == "":
                board[a*3 + b] = "O"
                break

    # Medium AI with basic strategy to block or win
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

    # Block or win based on available lines
    def check_win_and_dont_lose(player):
        global board, i_last_move

        # Lines to check (rows, columns, diagonals)
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for line in lines:
            line_values = [board[i] for i in line]
            if line_values.count(player) == 2 and line_values.count("") == 1:
                i_last_move = line[line_values.index("")]
                return

    # Expert AI implementation
    def expert_ai():
        best_score = -1000
        best_move = None

        # Evaluate all possible moves
        for i in range(3):
            for j in range(3):
                if board[i*3 + j] == "":
                    board[i*3 + j] = "O"
                    score = minimax(board, 0, False)
                    board[i*3 + j] = ""

                    # Track the best move
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        # Make the best move
        board[best_move[0]*3 + best_move[1]] = "O"

    # Minimax algorithm for determining the best move
    def minimax(new_board, depth, is_maximizing):
        scores = {"X": -10, "O": 10, "Draw": 0}
        result = check_winner_state(new_board)

        # Return the score if the game is over
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

    # Check the current state of the board for a winner       
    def check_winner_state(grid):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        
        # Check each line for a win
        for line in lines:
            if grid[line[0]] == grid[line[1]] == grid[line[2]] != "":
                return grid[line[0]]
        
        # Check for a draw
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

# Label for the game over sequence
label game_over:
    play movie "images/video/gameovers.webm"
    scene gameover1
    pause

    menu:
        "Return to Main Menu":
            jump start
        "Restart Game":
            jump after_gs33

# Continue the story after winning against the first story mode walker
label continue_story:
    play music "audio/pythonbang.wav" noloop
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
    "To Be Continued..."
    pause

    return
# end of code, more story to come if need be