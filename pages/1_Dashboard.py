import pandas as pd
import plotly.express as px
import streamlit as st

from database import get_assignments, get_attendance, get_exams

st.title("🏠 StudySync AI Dashboard")

# ==========================
# LOAD DATA
# ==========================

assignments = get_assignments()
attendance = get_attendance()
exams = get_exams()

assignments_df = pd.DataFrame(
    assignments,
    columns=[
        "id",
        "title",
        "subject",
        "due_date",
        "priority",
        "status"
    ]
)

attendance_df = pd.DataFrame(
    attendance,
    columns=[
        "id",
        "subject",
        "conducted",
        "attended"
    ]
)

exams_df = pd.DataFrame(
    exams,
    columns=[
        "id",
        "subject",
        "exam_date"
    ]
)

# ==========================
# KPI CARDS
# ==========================

total_assignments = len(assignments_df)

pending_assignments = 0

if not assignments_df.empty:
    pending_assignments = len(
        assignments_df[
            assignments_df["status"] == "Pending"
        ]
    )

total_subjects = len(
    attendance_df["subject"].unique()
) if not attendance_df.empty else 0

avg_attendance = 0

if not attendance_df.empty:

    attendance_df["percentage"] = (
        attendance_df["attended"]
        /
        attendance_df["conducted"]
    ) * 100

    avg_attendance = round(
        attendance_df["percentage"].mean(),
        2
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📝 Assignments",
        total_assignments
    )

with col2:
    st.metric(
        "⏳ Pending",
        pending_assignments
    )

with col3:
    st.metric(
        "📚 Subjects",
        total_subjects
    )

with col4:
    st.metric(
        "📊 Attendance %",
        avg_attendance
    )

st.divider()

# ==========================
# CHARTS
# ==========================

colA, colB = st.columns(2)

with colA:

    st.subheader("📊 Assignment Status")

    if not assignments_df.empty:

        fig = px.pie(
            assignments_df,
            names="status",
            title="Assignments"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:
        st.info("No assignments found")

with colB:

    st.subheader("📈 Attendance")

    if not attendance_df.empty:

        fig = px.bar(
            attendance_df,
            x="subject",
            y="percentage",
            title="Attendance by Subject"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:
        st.info("No attendance records")

st.divider()

# ==========================
# UPCOMING EXAMS
# ==========================

st.subheader("📅 Upcoming Exams")

if exams_df.empty:

    st.info("No exams scheduled")

else:

    st.dataframe(
        exams_df,
        use_container_width=True
    )

st.divider()

# ==========================
# RECENT ASSIGNMENTS
# ==========================

st.subheader("📝 Assignments")

if assignments_df.empty:

    st.info("No assignments added")

else:

    st.dataframe(
        assignments_df,
        use_container_width=True
    )