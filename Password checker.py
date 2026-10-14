import streamlit as st
import re

st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    score = 0
    suggestions = []

    # Check password criteria
    checks = [
        (len(password) >= 8, "At least 8 characters"),
        (bool(re.search(r"[A-Z]", password)), "Uppercase letter"),
        (bool(re.search(r"[a-z]", password)), "Lowercase letter"),
        (bool(re.search(r"[0-9]", password)), "Number"),
        (bool(re.search(r"[^A-Za-z0-9]", password)), "Special character")
    ]

    st.subheader("✅ Password Checklist")

    for passed, message in checks:
        if passed:
            score += 1
            st.write("✅", message)
        else:
            st.write("❌", message)
            suggestions.append(message)

    # Display score and progress
    st.subheader(f"Password Strength Score: {score}/5")
    st.progress(score / 5)

    # Display strength
    if score <= 2:
        st.error("Strength: Weak")
    elif score <= 4:
        st.warning("Strength: Moderate")
    else:
        st.success("Strength: Strong")

    # Display suggestions
    if suggestions:
        st.subheader("💡 Suggestions")
        for suggestion in suggestions:
            st.write("- Add", suggestion.lower())
    else:
        st.success("Great! All criteria are satisfied.")
