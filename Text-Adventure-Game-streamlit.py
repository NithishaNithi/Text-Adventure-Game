import streamlit as st

def intro():
    st.title("🌲 Text Adventure Game")
    st.write("Welcome, brave soul! Choose your path through danger and mystery.")

    difficulty = st.radio("Choose your difficulty:", ["Easy", "Medium", "Hard"])
    if st.button("Start Adventure"):
        st.session_state.difficulty = difficulty.lower()
        st.session_state.stage = "first_choice"

def first_choice():
    st.write("You stand at the edge of a dark forest. Paths lead **north** and **east**.")
    choice = st.radio("Which way do you want to go?", ["North", "East"])
    if st.button("Go"):
        if choice == "North":
            st.session_state.stage = "dark_forest"
        else:
            st.session_state.stage = "river_crossing"

def dark_forest():
    st.write("🌲 The trees thicken. A wolf emerges, growling in the darkness!")
    choice = st.radio("What do you do?", ["Run", "Fight"])
    if st.button("Choose Action"):
        if choice == "Run":
            st.write("You escape safely back to the starting point.")
            st.session_state.stage = "first_choice"
        elif choice == "Fight":
            if st.session_state.difficulty == "easy":
                st.success("You scare the wolf away and find treasure! You win!")
                st.session_state.stage = "play_again"
            elif st.session_state.difficulty == "medium":
                st.warning("You're injured but alive. You limp back.")
                st.session_state.stage = "first_choice"
            else:
                st.error("The wolf overpowers you. You lose.")
                st.session_state.stage = "play_again"

def river_crossing():
    st.write("🏞️ A river blocks your path. A boat lies nearby—but no oars!")
    choice = st.radio("What do you do?", ["Swim", "Search for oars"])
    if st.button("Try it"):
        if choice == "Swim":
            if st.session_state.difficulty == "easy":
                st.success("You swim across and find treasure. You win!")
                st.session_state.stage = "play_again"
            elif st.session_state.difficulty == "medium":
                st.warning("You barely make it across and collapse.")
                st.session_state.stage = "first_choice"
            else:
                st.error("The current sweeps you away. You drown.")
                st.session_state.stage = "play_again"
        elif choice == "Search for oars":
            if st.session_state.difficulty == "hard":
                st.error("You find nothing. You're stuck here.")
                st.session_state.stage = "play_again"
            else:
                st.success("You find oars and cross safely. You win!")
                st.session_state.stage = "play_again"

def play_again():
    st.subheader("Do you want to play again?")
    if st.button("Play Again"):
        st.session_state.stage = "intro"
    if st.button("Exit"):
        st.write("Thanks for playing! 👋")
        st.session_state.stage = "exit"

if __name__ == "__main__":
    if "stage" not in st.session_state:
        st.session_state.stage = "intro"
        st.session_state.difficulty = "easy"

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
        st.write("Goodbye! Reload the page to start over.")
