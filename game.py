import streamlit as st
import random

if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

st.title("Guess the Number Game!")

guess = st.number_input("Enter your guess (between 1 and 100):", min_value=1, max_value=100)

if st.button("Submit Guess"):
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.write("Your guess is too low! Try again.")
    elif guess > st.session_state.number:
        st.write("Your guess is too high! Try again.")
    else:
        st.write(f"Congratulations! You've guessed the number {st.session_state.number} in {st.session_state.attempts} attempts.")
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0


if st.button("Restart Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.write("Game restarted! Guess a new number.")
