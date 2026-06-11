import pandas as pd
import streamlit as st

from database import (
    add_assignment,
    delete_assignment,
    get_assignments,
    mark_assignment_complete,
)

st.title("📝 Assignments")

# ======================
# ADD ASSIGNMENT
# ======================

st.subheader("➕ Add Assignment")

with st.form("assignment_form"):

    title = st.text_input(
        "Assignment Title"
    )

    subject = st.text_input(
        "Subject"
    )

    due_date = st.date_input(
        "Due Date"
    )

    priority = st.selectbox(
        "Priority",
        ["Low", "Medium", "High"]
    )

    submit = st.form_submit_button(
        "Add Assignment"
    )

    if submit:

        add_assignment(
            title,
            subject,
            str(due_date),
            priority
        )

        st.success(
            "Assignment Added Successfully"
        )

        st.rerun()

# ======================
# VIEW ASSIGNMENTS
# ======================

st.divider()

st.subheader("📋 Assignment List")

assignments = get_assignments()

if assignments:

    df = pd.DataFrame(
        assignments,
        columns=[
            "ID",
            "Title",
            "Subject",
            "Due Date",
            "Priority",
            "Status"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    st.subheader("⚙ Assignment Actions")

    assignment_id = st.selectbox(
        "Select Assignment ID",
        df["ID"]
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "✅ Mark Complete"
        ):

            mark_assignment_complete(
                assignment_id
            )

            st.success(
                "Assignment Completed"
            )

            st.rerun()

    with col2:

        if st.button(
            "🗑 Delete Assignment"
        ):

            delete_assignment(
                assignment_id
            )

            st.success(
                "Assignment Deleted"
            )

            st.rerun()

else:

    st.info(
        "No assignments available."
    )