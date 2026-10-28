
import streamlit as st
import numpy as np
import pandas as pd

# App title
st.title("🎓 Student Marks Calculator")

st.write("Enter student details and calculate marks.")

# Input student details
name = st.text_input("Enter Student Name")
marks = st.number_input(
    "Enter Marks (0-100)",
    min_value=0,
    max_value=100,
    step=1
)

# Create an empty DataFrame
if "students" not in st.session_state:
    st.session_state.students = pd.DataFrame(
        columns=["Name", "Marks"]
    )

# Add student
if st.button("Add Student"):
    if name.strip():
        new_student = pd.DataFrame({
            "Name": [name],
            "Marks": [marks]
        })

        st.session_state.students = pd.concat(
            [st.session_state.students, new_student],
            ignore_index=True
        )

        st.success("Student added successfully!")
    else:
        st.warning("Please enter a student name.")

# Display student table
st.subheader("📋 Student Records")
df = st.session_state.students
st.dataframe(df)

# Calculate statistics
if not df.empty:
    # Convert marks into a NumPy array
    marks_array = df["Marks"].to_numpy()

    average = np.mean(marks_array)
    highest = np.max(marks_array)
    lowest = np.min(marks_array)

    # Display results
    st.subheader("📊 Marks Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric("Average Marks", f"{average:.2f}")
    col2.metric("Highest Marks", highest)
    col3.metric("Lowest Marks", lowest)

    # Add grades using Pandas
    df["Grade"] = np.where(
        df["Marks"] >= 90, "A",
        np.where(
            df["Marks"] >= 75, "B",
            np.where(df["Marks"] >= 50, "C", "F")
        )
    )

    st.subheader("🏆 Student Grades")
    st.dataframe(df)

    # Show students who passed
    passed = df[df["Marks"] >= 50]

    st.write("Number of students:", len(df))
    st.write("Students passed:", len(passed))
    st.write("Students failed:", len(df) - len(passed))

    # Show highest-scoring student(s)
    st.subheader("🌟 Top Scorer(s)")
    top_students = df[df["Marks"] == highest]
    st.dataframe(top_students)
