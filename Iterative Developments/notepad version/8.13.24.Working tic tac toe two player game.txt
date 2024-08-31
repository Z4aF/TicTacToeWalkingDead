label start:
    # Initialize the board and other variables
    $ board = ["", "", "", "", "", "", "", "", ""]
    $ current_player = "X"
    $ winner = None

    call screen tictactoe_screen

screen tictactoe_screen:
    vbox:
        spacing 10
        text "Tic-Tac-Toe" style "title_text"
        grid 3 3:
            spacing 5
            for i in range(9):
                button:
                    background "#ccc"  # Adding a background color to ensure the button is visible
                    text "[board[i]]" style "ttt_button_text"  # Display the current player's mark
                    action If(not board[i] and not winner, [Function(make_move, i), Jump("check_winner")])
                    style "ttt_button"
        
        # Conditional text display for current player or winner
        if winner:
            text "Winner: [winner]" style "menu_text"
        else:
            text "Current Player: [current_player]" style "menu_text"
        
        textbutton "Restart Game" action Jump("start")

init python:
    def make_move(index):
        """Update the board with the current player's move."""
        if board[index] == "":
            board[index] = current_player

label check_winner:
    $ lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    $ winner = None
    
    python:
        for line in lines:
            if board[line[0]] == board[line[1]] == board[line[2]] != "":
                winner = board[line[0]]
                break

    # Check if the game is a draw
    if not winner and all(board):
        $ winner = "Draw"

    # Switch players if no winner
    if not winner:
        $ current_player = "O" if current_player == "X" else "X"

    call screen tictactoe_screen
    return

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
    color "#000"  # Ensure the text color is visible

style title_text:
    size 52
    xalign 0.5

style menu_text:
    size 32
    xalign 0.5
