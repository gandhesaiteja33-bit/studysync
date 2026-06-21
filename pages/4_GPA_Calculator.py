import streamlit as st

st.title("🎓 GPA Calculator")

st.subheader("Calculate GPA")

num_subjects = st.number_input("Number of Subjects", min_value=1, max_value=15, value=5)

grades = []
credits = []

grade_points = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5, "F": 0}

for i in range(num_subjects):
    st.markdown(f"### Subject {i + 1}")

    grade = st.selectbox(f"Grade {i + 1}", list(grade_points.keys()), key=f"grade{i}")

    credit = st.number_input(
        f"Credits {i + 1}", min_value=1, max_value=10, value=3, key=f"credit{i}"
    )

    grades.append(grade)
    credits.append(credit)

if st.button("Calculate GPA"):
    total_points = 0
    total_credits = 0

    for g, c in zip(grades, credits):
        total_points += grade_points[g] * c
        total_credits += c

    gpa = total_points / total_credits

    st.success(f"Your GPA is {gpa:.2f}")
