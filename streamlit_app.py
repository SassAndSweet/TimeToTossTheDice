import streamlit as st
import random
import time

# Custom CSS for Maiandra GD font
st.markdown("""
<style>
    @import url('https://fonts.cdnfonts.com/css/maiandra-gd');
    
    * {
        font-family: 'Maiandra GD', sans-serif !important;
    }
    
    h1, h2, h3, h4, h5, h6, .stButton button, .stMarkdown p {
        font-family: 'Maiandra GD', sans-serif !important;
    }
</style>
""", unsafe_allow_html=True)

# Set page config
st.set_page_config(page_title="Time To Toss The Dice", page_icon="🎲")

# Rest of your code remains unchanged...

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

# Center everything
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Show the dice image (centered)
    st.image("d20.png", width=250, caption="D20 Die")
    
    # Roll button
    if st.button("Roll the Dice!", use_container_width=True):
        st.session_state.rolling = True
        # Show rolling animation
        with st.spinner("Rolling..."):
            # Simulate the dice rolling with a delay
            time.sleep(1.5)
            # Generate random number
            st.session_state.result = random.randint(1, 20)
            st.session_state.roll_history.append(st.session_state.result)
            st.session_state.rolling = False

    # Show the result
    if st.session_state.result is not None:
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
            st.rerun()
