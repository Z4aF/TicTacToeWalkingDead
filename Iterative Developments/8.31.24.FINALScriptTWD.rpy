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
    define uc = Character("Unknown Caller", color="FFFFFF")
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

# Flag to track if the user is in story mode
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

# Story game mode, TicTacToe game
label ztorya_player_game:
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
            jump ztorya_player_game
        "Single Player (Medium AI)":
            $ ai_level = "medium"
            jump ztorya_player_game
        "Single Player (Expert AI)":
            $ ai_level = "expert"
            jump ztorya_player_game

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

# Label for the game over sequence
label game_over:
    play movie "images/video/gameovers.webm"
    scene gameover1
    pause
    
    menu:
        "Return to Main Menu":
            return
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
    pause 2.0
    scene as1
    "Rick's family, his main objective is to find them."
    pause
    scene as2
    "Without gas, his police car is rendered useless in the middle of nowhere."
    pause
    scene as3
    "So he grabs his family picture and his police guns"
    "Not entirely sure if he is ever going back to his police car"
    pause
    scene as4
    "He continue to find his family"
    "on foot"
    pause
    scene as5
    "Rick calls out anyone who might hear him before going near the house"
    rick "Hello? Police officer out here."
    "Announcing himself loudly"
    pause
    scene as6
    rick "Can I borrow some gas?"
    "Rick shouts"
    "He carefully approaches the door"
    pause
    scene as7
    "Rick didn't find anyone"
    pause
    scene as8
    "alive"
    pause
    scene as9 
    "Terrified and sick of what Rick just saw."
    "He calms himself before checking out the car in front of the house"
    pause
    scene as10
    "Checks if there are keys in it"
    "Nothing"
    pause
    scene as11
    "<rustles>"
    "<snickers>"
    pause
    scene as12
    "<neigh>"
    "A horse"
    pause
    scene as13
    "Rick needs a ride, he approaches the horse calmly."
    rick "Easy now, easy."
    pause
    scene as14
    rick "I am not gonna hurt you, nothing like that."
    rick "More like a proposal."
    pause
    scene as13
    rick "Atlanta is just down the road ways, it's safe there."
    rick "Food, shelter, people."
    pause
    scene as14
    rick "other horses too I bet."
    rick "How's that sound?"
    pause
    scene as15
    "Atlanta"
    "Rick now travels with his new friend, both of them looking for his family."
    pause
    scene as16
    "Atlanta welcomes Rick with"
    pause
    scene as17
    "empty streets"
    pause
    scene as18
    "aftermath of the battle between the living and the dead"
    pause
    scene as19
    "the aftermath of chaos,"
    "<flying helicopter sounds>"
    pause
    scene as20
    "and hope"
    "Rick finds the source of the sound"
    pause
    scene as21
    "Looking at a distance, he saw something moving in the skies"
    pause
    scene as22
    "A helicopter!"
    pause
    scene as23
    rick "YAH!"
    "Rick rushes to follow the helicopter"
    "with his trusty steed and"
    pause
    scene as24
    "the dead"
    pause
    scene as25
    "countless rotting dead"
    pause
    scene as26
    "Rick manuevers his horse away from the dead"
    "But there's too many"
    pause
    scene as27
    "His trusty steed panics as the dead swarms them, resulting in"
    pause
    scene as28
    "Rick falling off his horse"
    pause
    scene as29
    "and his trusty steed being devoured and ripped apart alive"
    "crying for Rick's help and comfort"
    pause
    scene as30
    "Rick quickly looks for a way out"
    "There is none, except"
    pause
    scene as31
    "Rick crawls under the tank away from"
    pause
    scene as32 
    "the dead"
    pause
    scene as33 
    "Rick crawls to the other side of the tank"
    "Hoping for a way out"
    pause
    scene as34
    "But the dead awaits him on the other side"
    pause
    scene fs1
    "Rick looks back, pull out his Colt Python, and aims"
    jump second_match

default second_game_match = False

# Continue the story after the second story mode walker match
label second_match:
    play music "audio/twdintro.mp3" loop
    scene secondlaban
    $ second_game_match = True  # Set to True for story mode
    "Play TicTacToe and win, if you lose, Game Over."
    "It is recommended to play against DUMB AI"
    jump second_story_selection

label second_story_selection:
    menu:
        "Single Player (Dumb AI)":
            $ ai_level = "dumb"
            jump second_story_game
        "Single Player (Medium AI)":
            $ ai_level = "medium"
            jump second_story_game
        "Single Player (Expert AI)":
            $ ai_level = "expert"
            jump second_story_game

# Story game mode for the second Tic-Tac-Toe match
label second_story_game:
    play music "audio/twdintro.mp3" loop 
    $ board = ["", "", "", "", "", "", "", "", ""]
    $ current_player = "X"
    $ winner = None
    
    call screen tictactoe_screen

# Continue the story after winning against the second story mode walker
label after_second_continue:
    play music "audio/pythonbang.mp3" noloop
    scene fs2
    "<BANG>"
    pause
    scene secondwin
    "One down"
    "Unto the next one"
    pause
    jump third_match

default third_game_match = False

# Continue the story after the third story mode walker match
label third_match:
    play music "audio/twdintro.mp3" loop
    scene thirdlaban
    $ third_game_match = True  # Set to True for story mode
    "Prepare yourself for more"
    "Initiating Tic-Tac-Toe match"
    jump third_story_selection

label third_story_selection:
    menu:
        "Single Player (Dumb AI)":
            $ ai_level = "dumb"
            jump third_story_game
        "Single Player (Medium AI)":
            $ ai_level = "medium"
            jump third_story_game
        "Single Player (Expert AI)":
            $ ai_level = "expert"
            jump third_story_game

# Story game mode for the third Tic-Tac-Toe match
label third_story_game:
    play music "audio/twdintro.mp3" loop 
    $ board = ["", "", "", "", "", "", "", "", ""]
    $ current_player = "X"
    $ winner = None
    
    call screen tictactoe_screen

# Continue the story after winning against the third story mode walker
label after_third_continue:
    play music "audio/pythonbang.mp3" noloop
    scene thirdwin
    "<BANG>"
    pause
    scene thirdwin2
    "<Walker Dies>"
    pause
    scene fourthlaban
    "Rick looks back at the other side of the tank"
    jump fourth_match

default fourth_game_match = False

# Continue the story after the fourth story mode walker match
label fourth_match:
    play music "audio/twdintro.mp3" loop
    scene fourthlaban2
    $ fourth_game_match = True  # Set to True for story mode
    "Win the Tic-Tac-Toe game for your life"
    jump fourth_story_selection

label fourth_story_selection:
    menu:
        "Single Player (Dumb AI)":
            $ ai_level = "dumb"
            jump fourth_story_game
        "Single Player (Medium AI)":
            $ ai_level = "medium"
            jump fourth_story_game
        "Single Player (Expert AI)":
            $ ai_level = "expert"
            jump fourth_story_game

# Story game mode for the fourth Tic-Tac-Toe match
label fourth_story_game:
    play music "audio/twdintro.mp3" loop 
    $ board = ["", "", "", "", "", "", "", "", ""]
    $ current_player = "X"
    $ winner = None
    
    call screen tictactoe_screen

# Continue the story after winning against the fourth story mode walker
label after_fourth_continue:
    play music "audio/pythonbang.mp3" noloop
    scene fourthwin
    "<BANG>"
    pause
    scene fourthwin2
    "<Walker Dies>"
    pause
    scene fifthlaban
    "Rick moves on to the next walker beside the walker he just shot in the head"
    jump fifth_match

default fifth_game_match = False

# Continue the story after the fifth story mode walker match
label fifth_match:
    play music "audio/twdintro.mp3" loop
    scene fifthlaban
    $ fifth_game_match = True  # Set to True for story mode
    "Initiating Tic-Tac-Toe match"
    jump fifth_story_selection

label fifth_story_selection:
    menu:
        "Single Player (Dumb AI)":
            $ ai_level = "dumb"
            jump fifth_story_game
        "Single Player (Medium AI)":
            $ ai_level = "medium"
            jump fifth_story_game
        "Single Player (Expert AI)":
            $ ai_level = "expert"
            jump fifth_story_game

# Story game mode for the fifth Tic-Tac-Toe match
label fifth_story_game:
    play music "audio/twdintro.mp3" loop 
    $ board = ["", "", "", "", "", "", "", "", ""]
    $ current_player = "X"
    $ winner = None
    
    call screen tictactoe_screen

# Continue the story after winning against the fifth story mode walker
label after_fifth_continue:
    play music "audio/pythonbang.mp3" noloop
    scene fourthwin
    "<BANG>"
    pause
    scene fifthwin2
    "<Walker Dies>"
    "With the double dead walkers Rick just killed,"
    "Rick Blocks the walkers coming from the back of the double dead walkers,"
    pause
    scene fifthwin3
    "Temporarily"
    "The walkers kept coming"
    "But slowly, because of the walkers Rick just killed"
    pause
    scene fifthwin4
    "Stuck and scared of being ripped alive"
    "He lays on his back and tries to kill himself"
    rick "Lori, Carl, I am sorry..."
    pause
    scene fifthwin5
    "After laying on his back, he saw an opening through inside the tank"
    pause
    scene fifthwin6
    "He goes in and quickly closes the opening"
    pause
    scene fifthwin7
    "He moves away from the closed opening"
    "Scared and relieved"
    pause
    scene fifthwin8
    "Rick loots the dead soldier beside him"
    "Took its grenade and pistol"
    "And checked the magazine"
    pause
    scene fifthwin9 
    "<Walker growls>"
    pause 2.0
    scene fifthwin10
    "Should have asked permission"
    rick ":O"
    jump sixth_match

default sixth_game_match = False

# Continue the story after the fifth story mode walker match
label sixth_match:
    scene sixlaban
    $ sixth_game_match = True  # Set to True for story mode
    "Initiating Tic-Tac-Toe match"
    jump sixth_story_selection

label sixth_story_selection:
    menu:
        "Single Player (Dumb AI)":
            $ ai_level = "dumb"
            jump sixth_story_game
        "Single Player (Medium AI)":
            $ ai_level = "medium"
            jump sixth_story_game
        "Single Player (Expert AI)":
            $ ai_level = "expert"
            jump sixth_story_game

# Story game mode for the fifth Tic-Tac-Toe match
label sixth_story_game:
    play music "audio/twdintro.mp3" loop 
    $ board = ["", "", "", "", "", "", "", "", ""]
    $ current_player = "X"
    $ winner = None
    
    call screen tictactoe_screen

# Continue the story after winning against the fifth story mode walker
label after_sixth_continue:
    play music "audio/pythonbang.mp3" noloop
    scene fourthwin
    "<BANG>"
    pause
    scene sixthwin
    "<Soldier Walker Dies>"
    pause
    scene sixthwin2
    "Shooting a gun in an enclosed area"
    "The shockwave dazed Rick"
    "Ears ringing, he collected himself"
    "Dragged himself to the top opening of the tank"
    pause
    scene sixthwin3
    "He looked around for his guns"
    "But he saw walkers climbing the tank"
    pause
    scene sixthwin4
    "Rick closed the opening"
    pause
    scene sixthwin5
    rick "<thud>"
    "Falling on his ass"
    "Rick looked around for anything to use"
    pause
    scene sixthwin6
    "He found nothing besides the weapons he looted from the solider"
    "He prepares the gun he just got and pondered for ideas"
    "and ways out of the situation he got himself in."
    "<buzz>"
    pause
    scene sixthwin7
    play music "audio/spacejunk.mp3" noloop
    "<Tank radio buzzes>"
    uc "Hey you?"
    pause
    scene sixthwin8
    uc "Dumbass."
    pause
    scene sixthwin7
    uc "Yeah, you in the tank?"
    pause
    scene sixthwin8
    uc "Cozy in there?"
    pause
    scene sixthwin9
    "<Horse cries>"
    "No horses harmed"
    "Walker kill count:"
    "May vavry"
    "Andrew Lincoln - Rick Grimes (dumbass)"
    "Song - spacejunk"
    "by Wang Chung"
    "Quiz 1 midterms SOLO"
    "Thanks to Ren'Py and Python"
    "Improvements:"
    "Practice Mode - when choosing the mark O, the AI should go first"
    "Create external labels out of the main code and to be used in main code by calling the external labels"
    "to shorten the code and"
    "Seperate gameplay and story code"
    "That's all!"
    "Thank you for playing!"
    "Created by - ZAF"
    "Enjoy the music"
    pause
    scene titlescreen
    "By AMC"
    "Based on Robert Kirkman's The walking dead comics"
    "End of Episode 1"
    "To be continue..."
    pause 5.0

    return

screen tictactoe_screen:
    add im.Scale("grid_box.png", 650, 650) at Position(xalign=0.987, yalign=0.9)
    
    hbox:  # The Tic-Tac-Toe 3x3 grid box
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
                    action If(not board[i] and not winner, [Function(make_move, i), Jump("check_winner")])
                    style "ttt_button"

    vbox:  # Tic-Tac-Toe winner and current player indicator
        xalign 0.870
        yalign 0.365
        null height 20
        if winner:
            text "Winner: [winner]" style "menu_text"
        else:
            text "Current Player: [current_player]" style "menu_text"

    if winner:
        vbox:  # Tic-Tac-Toe post-game block
            spacing 20
            xalign 0.980
            yalign 0.28
            if winner == "Draw":
                textbutton "Restart Game" action Jump("storya_mode_selection" if is_story_mode else "practice_mode_selection") style "menu_text"
            elif winner == "X" and is_story_mode:
                if sixth_game_match:
                    textbutton "Restart Game" action Jump("storya_mode_selection") style "menu_text"
                    textbutton "Continue" action Jump("after_sixth_continue") style "menu_text"
                elif fifth_game_match:
                    textbutton "Restart Game" action Jump("storya_mode_selection") style "menu_text"
                    textbutton "Continue" action Jump("after_fifth_continue") style "menu_text"
                elif fourth_game_match:
                    textbutton "Restart Game" action Jump("storya_mode_selection") style "menu_text"
                    textbutton "Continue" action Jump("after_fourth_continue") style "menu_text"
                elif third_game_match:
                    textbutton "Restart Game" action Jump("storya_mode_selection") style "menu_text"
                    textbutton "Continue" action Jump("after_third_continue") style "menu_text"
                elif second_game_match:
                    textbutton "Restart Game" action Jump("storya_mode_selection") style "menu_text"
                    textbutton "Continue" action Jump("after_second_continue") style "menu_text"
                else:
                    textbutton "Restart Game" action Jump("storya_mode_selection") style "menu_text"
                    textbutton "Continue" action Jump("continue_story") style "menu_text"  # Updated this to continue to after_sixth_continue
            elif second_game_match or third_game_match or fourth_game_match or fifth_game_match:
                textbutton "Advance" action Jump("gameover") style "menu_text"
            elif is_story_mode:
                textbutton "Advance" action Jump("game_over") style "menu_text"
            else:
                textbutton "Restart Game" action Jump("start") style "menu_text"
    else:
        textbutton "Restart Game" action Jump("start") style "menu_text" xalign 0.980 yalign 0.28

# Label for the game over sequence
label gameover:
    play movie "images/video/gameover2.webm"
    scene gameover2
    pause
    
    menu:
        "Return to Main Menu":
            return
        "Restart Game":
            jump story_mode

define x_sound = "audio/gunclick.mp3"  # Replace with your actual file path
define o_sound = "audio/gunclick.mp3"  # Replace with your actual file path

# Function to handle player moves
init python:
    def make_move(index):
        if board[index] == "":
            board[index] = current_player
            if current_player == "X":
                renpy.play(x_sound)
            elif current_player == "O":
                renpy.play(o_sound)

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
        "ulwin2", "ulwin3", "ulwin4", "ulwin5", "ulwin6", "ulwin7", "titlescreen",
        "as1", "as2", "as3", "as4", "as5", "as6", "as7", "as8", "as9", "as10", "as11", 
        "as12", "as13", "as14", "as15", "as16", "as17", "as18", "as19", "as20", "as21", 
        "as22", "as23", "as24", "as25", "as26", "as27", "as28", "as29", "as30", "as31", "as32",
        "as33", "as34", "fs1", "fs2", "thirdlaban", "secondlaban", "secondwin", "thirdwin",
        "fourthwin", "fourthwin2", "thirdwin2", "fourthlaban", "fourthlaban2", "fifthlaban",
        "fifthwin2", "fifthwin3", "fifthwin4", "fifthwin5", "fifthwin7", "fifthwin6", "fifthwin8",
        "fifthwin9", "fifthwin10", "sixlaban", "sixthwin", "sixthwin2", "sixthwin3", "sixthwin4", 
        "sixthwin5", "sixthwin6", "sixthwin7", "sixthwin8", "sixthwin9", "gameover2"
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