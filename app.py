import streamlit as st

# Set page config
st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

# Custom CSS for better UI
st.markdown("""
    <style>
        .result {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #4b4b4b;
        }
        .stNumberInput > div > div {
            background-color: #f7f7f7 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #4b8bbe;'>🧮 My Calculator</h1>", unsafe_allow_html=True)

# Input section
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("🔢 Enter the first number", value=0.0)
with col2:
    num2 = st.number_input("🔢 Enter the second number", value=0.0)

# Operation selection
operation = st.radio("📌 Choose an operation:", ["Add ➕", "Subtract ➖", "Multiply ✖️", "Divide ➗"], horizontal=True)

# Calculate on button click
if st.button("Calculate"):
    try:
        if operation.startswith("Add"):
            result = num1 + num2
            op_symbol = "+"
        elif operation.startswith("Subtract"):
            result = num1 - num2
            op_symbol = "-"
        elif operation.startswith("Multiply"):
            result = num1 * num2
            op_symbol = "×"
        elif operation.startswith("Divide"):
            if num2 == 0:
                st.error("❌ Cannot divide by zero!")
                result = None
            else:
                result = num1 / num2
                op_symbol = "÷"

        if result is not None:
            st.markdown(f"<div class='result'>{num1} {op_symbol} {num2} = {round(result, 4)}</div>", unsafe_allow_html=True)
            # Save to session state
            if "history" not in st.session_state:
                st.session_state.history = []
            st.session_state.history.append(f"{num1} {op_symbol} {num2} = {round(result, 4)}")

    except Exception as e:
        st.error(f"Unexpected error: {e}")

# History log
if "history" in st.session_state and st.session_state.history:
    with st.expander("📜 View Calculation History"):
        for item in reversed(st.session_state.history[-10:]):
            st.markdown(f"- {item}")
