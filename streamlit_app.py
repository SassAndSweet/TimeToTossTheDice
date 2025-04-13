import streamlit as st
import random
import time

# Set page config - must be the first Streamlit command
st.set_page_config(page_title="Time To Toss The Dice", page_icon="🎲")

# Custom CSS for font and styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&display=swap');
    
    .stApp, .stButton>button, .stMarkdown, p, div, h1, h2, h3, h4, h5, h6 {
        font-family: 'Quicksand', sans-serif !important;
    }
    
    .dice-container {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
    
    .dice-image {
        width: 250px;
        transition: transform 0.5s;
    }
    
    .rolling {
        animation: diceRoll 1.5s ease-in-out;
    }
    
    @keyframes diceRoll {
        0% { transform: rotate(0deg) scale(1); }
        25% { transform: rotate(90deg) scale(0.9); }
        50% { transform: rotate(180deg) scale(1.1); }
        75% { transform: rotate(270deg) scale(0.9); }
        100% { transform: rotate(360deg) scale(1); }
    }
</style>
""", unsafe_allow_html=True)

# App title
st.title("Time To Toss The Dice")
st.subheader("Click the button to roll the d20!")

# Initialize session state
if 'result' not in st.session_state:
    st.session_state.result = None
if 'rolling' not in st.session_state:
    st.session_state.rolling = False
if 'roll_history' not in st.session_state:
    st.session_state.roll_history = []
if 'animation_complete' not in st.session_state:
    st.session_state.animation_complete = True

# Center everything
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # The dice container with animation
    if st.session_state.rolling:
        st.markdown(f"""
        <div class="dice-container">
            <img src="https://raw.githubusercontent.com/SassAndSweet/TimeToTossTheDice/main/d20.png" class="dice-image rolling">
        </div>
        """, unsafe_allow_html=True)
        
        # Set a timeout for the animation
        time.sleep(1.5)
        st.session_state.rolling = False
        st.session_state.animation_complete = True
        st.experimental_rerun()
    else:
        # Regular dice image
        st.markdown(f"""
        <div class="dice-container">
            <img src="https://raw.githubusercontent.com/SassAndSweet/TimeToTossTheDice/main/d20.png" class="dice-image">
        </div>
        """, unsafe_allow_html=True)
    
    # Roll button
    if st.button("Roll the Dice!", use_container_width=True):
        if st.session_state.animation_complete:
            st.session_state.rolling = True
            st.session_state.animation_complete = False
            # Generate random number
            st.session_state.result = random.randint(1, 20)
            st.session_state.roll_history.append(st.session_state.result)
            st.experimental_rerun()

    # Show the result
    if st.session_state.result is not None and st.session_state.animation_complete:
        st.markdown(f"<h1 style='text-align: center; color: #00008B;'>You rolled: {st.session_state.result}</h1>", 
                    unsafe_allow_html=True)

# Show roll history
if len(st.session_state.roll_history) > 0:
    st.divider()
    with st.expander("View Roll History"):
        roll_df = {"Roll #": list(range(1, len(st.session_state.roll_history) + 1)),
                  "Result": st.session_state.roll_history}
        st.dataframe(roll_df, use_container_width=True)
        
        # Option to clear history
        if st.button("Clear History"):
            st.session_state.roll_history = []
            st.experimental_rerun()
