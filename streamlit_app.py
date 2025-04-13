import streamlit as st
import random

def main():
    st.title("D20 Roller")
    st.write("Click the button to spin a teal 20-sided die and get a random number from 1 to 20.")

    # Display your teal/gold D20 image
    # Replace "my_teal_d20.png" with the actual filename or path to your image
    st.image("my_teal_d20.png", width=200, caption="Ocean Teal D20")

    # If we haven’t rolled yet, set initial value in session state
    if "roll_result" not in st.session_state:
        st.session_state["roll_result"] = None

    # A button to spin (roll) the D20
    if st.button("Roll the D20!"):
        # Generate a random integer from 1 to 20
        st.session_state["roll_result"] = random.randint(1, 20)

    # If we have a roll result, display it
    if st.session_state["roll_result"] is not None:
        st.write(f"**You rolled a {st.session_state['roll_result']}!**")

if __name__ == "__main__":
    main()

streamlit run app.py
