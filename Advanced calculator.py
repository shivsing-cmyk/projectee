import streamlit as st
import math

st.title("🧮 My Calculator")

num1 = st.number_input("Enter 1st number")
num2 = st.number_input("Enter 2nd number")

operation = st.selectbox(
    "Choose an operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Square Root"
    ]
)

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
            st.stop()
        result = num1 / num2

    elif operation == "Power":
        result = num1 ** num2

    elif operation == "Square Root":
        if num1 < 0:
            st.error("Cannot find square root of a negative number!")
            st.stop()
        result = math.sqrt(num1)

    st.success(f"Result: {result}")

# Extra buttons
st.divider()

if st.button("Show Number 1 Squared"):
    st.info(f"{num1}² = {num1 ** 2}")

if st.button("Show Number 2 Squared"):
    st.info(f"{num2}² = {num2 ** 2}")
