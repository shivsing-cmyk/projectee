import streamlit as st

st.title("My Calculator")

num1 = st.number_input("Enter 1st no.")
num2 = st.number_input("Enter 2nd no.")

operation = st.selectbox(
    "Choose an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            st.error("Cannot divide by zero!")
        else:
            result = num1 / num2

    if operation != "Division" or num2 != 0:
        st.success(f"Result: {result}")
