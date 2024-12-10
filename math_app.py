import streamlit as st
import random

# Initialize session state variables
if "number1" not in st.session_state:
    st.session_state.number1 = random.randint(1, 10)
if "number2" not in st.session_state:
    st.session_state.number2 = random.randint(1, 10)
if "operation" not in st.session_state:
    st.session_state.operation = random.choice(["*", "/"])
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""

# Function to generate new problem
def generate_new_problem():
    st.session_state.number1 = random.randint(1, 10)
    st.session_state.number2 = random.randint(1, 10)
    st.session_state.operation = random.choice(["*", "/"])
    st.session_state.feedback = ""
    st.session_state.user_answer = ""

# Display the problem
number1 = st.session_state.number1
number2 = st.session_state.number2
operation = st.session_state.operation

if operation == "*":
    correct_answer = number1 * number2
elif operation == "/":
    # Ensure the division is always an integer
    correct_answer = number1
    number1 = number1 * number2  # Adjust to make division clean

st.markdown(
    f"<h1 style='font-size: 36px;'>Solve this problem:</h1>", unsafe_allow_html=True
)
st.markdown(
    f"<h2 style='font-size: 32px; color: blue;'>{number1} {operation} {number2} = ?</h2>",
    unsafe_allow_html=True,
)

# Input for the kid's answer
user_answer = st.text_input("Enter your answer:", st.session_state.user_answer)

# Check the answer
if st.button("Submit"):
    if user_answer.isdigit():
        if int(user_answer) == correct_answer:
            st.session_state.feedback = "Well done! 🎉"
        else:
            st.session_state.feedback = "Try again! ❌"
    else:
        st.session_state.feedback = "Please enter a valid number."

# Display feedback
st.markdown(
    f"<h3 style='font-size: 28px; color: green;'>{st.session_state.feedback}</h3>",
    unsafe_allow_html=True,
)

# Button to continue to the next problem
if st.session_state.feedback == "Well done! 🎉" and st.button("Next Problem"):
    generate_new_problem()
