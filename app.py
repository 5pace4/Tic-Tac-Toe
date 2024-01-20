import streamlit as st
import numpy as np

# Initialize game variables
if "board" not in st.session_state:
    st.session_state.board = np.array([''] * 9)
    st.session_state.player = 0
    st.session_state.game_started = False
    st.session_state.game_over = False

def show_board():
    st.subheader(f"Player {st.session_state.player + 1}'s turn")

    # Create a 3x3 grid layout with adjusted column widths
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            cell_label = st.session_state.board[index] if st.session_state.board[index] else ''
            if i == 0:
                button = col1.button(cell_label, key=index, on_click=on_button_click, args=(i, j))
            elif i == 1:
                button = col2.button(cell_label, key=index, on_click=on_button_click, args=(i, j))
            else:
                button = col3.button(cell_label, key=index, on_click=on_button_click, args=(i, j))

            if button:
                on_button_click(i, j)

    # Add Restart and Exit buttons in the same row
    col4.button("Restart", on_click=reset_game)
    col4.button("Exit", on_click=st.stop)

def draw():
    return '' not in st.session_state.board

def valid(row, col):
    return st.session_state.board[row * 3 + col] == ''

def check_win(player):
    chk = 'X' if player == 0 else 'O'

    # Check row
    if np.all(st.session_state.board[[0, 1, 2]] == chk) or np.all(st.session_state.board[[3, 4, 5]] == chk) or np.all(st.session_state.board[[6, 7, 8]] == chk):
        return True
    # Check column
    if np.all(st.session_state.board[[0, 3, 6]] == chk) or np.all(st.session_state.board[[1, 4, 7]] == chk) or np.all(st.session_state.board[[2, 5, 8]] == chk):
        return True
    # Check diagonal
    if np.all(st.session_state.board[[0, 4, 8]] == chk) or np.all(st.session_state.board[[2, 4, 6]] == chk):
        return True
    return False

def on_button_click(row, col):
    if st.session_state.game_started and not st.session_state.game_over and valid(row, col):
        index = row * 3 + col
        st.session_state.board[index] = 'X' if st.session_state.player == 0 else 'O'
        if check_win(st.session_state.player):
            st.success(f"Player {st.session_state.player + 1} Wins!")
            st.session_state.game_over = True
        elif draw():
            st.warning("Match Draw!")
            st.session_state.game_over = True
        else:
            st.session_state.player ^= 1

def reset_game():
    st.session_state.board = np.array([''] * 9)
    st.session_state.player = 0
    st.session_state.game_over = False

# Streamlit app
def main():
    st.title("Tic Tac Toe")

    if not st.session_state.game_started:
        play_start = st.button("Play Game")
        if play_start:
            st.session_state.game_started = True
            show_board()
    else:
        show_board()

if __name__ == "__main__":
    main()


