import streamlit as st
import pandas as pd
import random

st.title("🍺 BJCP Beer Styles Flashcard Quiz")

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv("styles.csv")
    return df

data = load_data()

# Initialize session state variables
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total' not in st.session_state:
    st.session_state.total = 0
if 'current_style' not in st.session_state:
    st.session_state.current_style = None
if 'current_examples' not in st.session_state:
    st.session_state.current_examples = None
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False

def next_question():
    row = data.sample().iloc[0]
    st.session_state.current_style = row['Style']
    st.session_state.current_examples = row['Commercial_Examples']
    st.session_state.show_answer = False

# Button to load next question
if st.button("🎲 Next Beer Style"):
    next_question()

if st.session_state.current_style:
    st.markdown(f"### 🎤 **Beer Style:** {st.session_state.current_style}")
    if st.button("Reveal Examples"):
        st.session_state.show_answer = True

    if st.session_state.show_answer:
        st.markdown(f"🍻 **Examples:** {st.session_state.current_examples}")
        col1, col2 = st.columns(2)
        if col1.button("✅ Correct"):
            st.session_state.score += 1
            st.session_state.total += 1
            next_question()
        if col2.button("❌ Incorrect"):
            st.session_state.total += 1
            next_question()

# Display score
st.sidebar.header("Your Score")
st.sidebar.write(f"{st.session_state.score} out of {st.session_state.total}")

st.sidebar.info("Click 'Next Beer Style' to begin or continue quizzing yourself!")
