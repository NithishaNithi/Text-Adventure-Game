# text_adventure_game_streamlit.py

import streamlit as st

# Sidebar Difficulty Setup
def set_difficulty():
    st.sidebar.title("🎮 Game Settings")
    difficulty = st.sidebar.radio("Choose your difficulty:", ["Easy", "Medium", "Hard"])
    st.session_state.difficulty = difficulty.lower()

# Game Screens
def intro():
    st.title("🌲 Text Adventure Game")
    st.markdown("Welcome, brave soul! Choose your path through danger and mystery.")
    if st.button("🚀 Begin Adventure"):
        st.session_state.stage = "first_choice"

def first_choice():
    st.header("🌄 Crossroads")
    st.write("You stand at the edge of a dark forest. Paths lead **north** and **east**.")
    choice = st.radio("Which way do you want to go?", ["North", "East"])
    if st.button("Go"):
        st.session_state.stage = "dark_forest" if choice == "North" else "river_crossing"

def dark_forest():
    st.header("🌲 Dark Forest Encounter")
    st.write("The trees thicken. A wolf emerges, growling in the darkness!")
    choice = st.radio("What do you do?", ["Run", "Fight"])
    if st.button("Choose Action"):
        if choice == "Run":
            st.info("You escape safely back to the starting point.")
            st.session_state.stage = "first_choice"
        elif choice == "Fight":
            if st.session_state.difficulty == "easy":
                st.success("You scare the wolf away and find treasure! You win!")
            elif st.session_state.difficulty == "medium":
                st.warning("You're injured but alive. You limp back.")
                st.session_state.stage = "first_choice"
                return
            else:
                st.error("The wolf overpowers you. You lose.")
            st.session_state.stage = "play_again"

def river_crossing():
    st.header("🏞️ River Crossing")
    st.write("A wide river blocks your path. A boat lies nearby—but no oars!")
    choice = st.radio("What do you do?", ["Swim", "Search for oars"])
    if st.button("Try it"):
        if choice == "Swim":
            if st.session_state.difficulty == "easy":
                st.success("You swim across and find treasure. You win!")
            elif st.session_state.difficulty == "medium":
                st.warning("You barely make it across and collapse.")
                st.session_state.stage = "first_choice"
                return
            else:
                st.error("The current sweeps you away. You drown.")
            st.session_state.stage = "play_again"
        elif choice == "Search for oars":
            if st.session_state.difficulty == "hard":
                st.error("You find nothing. You're stuck here.")
            else:
                st.success("You find oars and cross safely. You win!")
            st.session_state.stage = "play_again"

def play_again():
    st.header("🔁 Play Again?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Yes, play again!"):
            st.session_state.stage = "intro"
    with col2:
        if st.button("❌ No, exit."):
            st.session_state.stage = "exit"

def exit_screen():
    st.title("👋 Thanks for playing!")
    st.write("Reload the page to start a new adventure.")

# Main App
if __name__ == "__main__":
    if "stage" not in st.session_state:
        st.session_state.stage = "intro"
        st.session_state.difficulty = "easy"

    set_difficulty()

    if st.session_state.stage == "intro":
        intro()
    elif st.session_state.stage == "first_choice":
        first_choice()
    elif st.session_state.stage == "dark_forest":
        dark_forest()
    elif st.session_state.stage == "river_crossing":
        river_crossing()
    elif st.session_state.stage == "play_again":
        play_again()
    elif st.session_state.stage == "exit":
        exit_screen()