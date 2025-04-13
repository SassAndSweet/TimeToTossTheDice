import streamlit as st
import random
import time

# Set page config
st.set_page_config(page_title="Time To Toss The Dice", page_icon="🎲")

# Custom CSS for styling
st.markdown("""
<style>
    .dice-container {
        display: flex;
        justify-content: center;
        margin: 30px 0;
    }
    .d20 {
        width: 200px;
        height: 200px;
        cursor: pointer;
        transition: transform 0.5s;
    }
    .spinning {
        animation: spin 1s infinite linear;
    }
    @keyframes spin {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.1); }
        100% { transform: rotate(360deg) scale(1); }
    }
    .result {
        font-size: 3rem;
        text-align: center;
        font-weight: bold;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# App title
st.title("Time To Toss The Dice")
st.subheader("Click the d20 to roll!")

# Initialize session state
if 'rolling' not in st.session_state:
    st.session_state.rolling = False
if 'result' not in st.session_state:
    st.session_state.result = None
if 'roll_history' not in st.session_state:
    st.session_state.roll_history = []

# Function to roll the dice
def roll_dice():
    st.session_state.rolling = True
    st.session_state.result = None
    st.experimental_rerun()

# Create a container for the dice
dice_container = st.container()

with dice_container:
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # The clickable dice image
        d20_html = f"""
        <div class="dice-container">
            <img src="https://i.imgur.com/7I4sxZL.png" 
                 class="d20 {'spinning' if st.session_state.rolling else ''}" 
                 onclick="window.parent.postMessage({{type: 'dice-click'}}, '*')">
        </div>
        """
        st.markdown(d20_html, unsafe_allow_html=True)
        
        # Display the rolling result
        if st.session_state.rolling:
            # Simulate rolling for a moment
            time.sleep(1)
            st.session_state.result = random.randint(1, 20)
            st.session_state.rolling = False
            st.session_state.roll_history.append(st.session_state.result)
            st.experimental_rerun()
        
        # Show the result
        if st.session_state.result is not None:
            st.markdown(f'<div class="result">You rolled: {st.session_state.result}</div>', unsafe_allow_html=True)

# Handle the JavaScript click event
st.markdown("""
<script>
    window.addEventListener('message', function(event) {
        if (event.data.type === 'dice-click') {
            const buttons = window.parent.document.querySelectorAll('button');
            for (let i = 0; i < buttons.length; i++) {
                if (buttons[i].innerText === 'Roll the dice') {
                    buttons[i].click();
                    break;
                }
            }
        }
    });
</script>
""", unsafe_allow_html=True)

# Hidden button to trigger the roll
if st.button('Roll the dice', key='roll_button', help='Click to roll the dice'):
    roll_dice()

# Show roll history
if st.session_state.roll_history and st.checkbox('Show roll history'):
    st.write("Previous rolls:")
    history_df = st.dataframe({'Roll': st.session_state.roll_history})
