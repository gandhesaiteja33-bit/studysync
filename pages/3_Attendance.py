import pandas as pd
import streamlit as st

from database import add_attendance, delete_attendance, get_attendance

st.title("📊 Attendance Manager")

st.subheader("➕ Add Attendance")

with st.form("attendance_form"):

    subject = st.text_input("Subject")

    conducted = st.number_input(
        "Classes Conducted",
        min_value=1,
        step=1
    )

    attended = st.number_input(
        "Classes Attended",
        min_value=0,
        step=1
    )

    submit = st.form_submit_button(
        "Save Attendance"
    )

    if submit:

        add_attendance(
            subject,
            conducted,
            attended
        )

        st.success(
            "Attendance Saved"
        )

        st.rerun()

st.divider()

records = get_attendance()

if records:

    df = pd.DataFrame(
        records,
        columns=[
            "ID",
            "Subject",
            "Conducted",
            "Attended"
        ]
    )

    df["Attendance %"] = round(
        (
            df["Attended"]
            /
            df["Conducted"]
        ) * 100,
        2
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    low_attendance = df[
        df["Attendance %"] < 75
    ]

    if not low_attendance.empty:

        st.warning(
            "⚠ Attendance below 75% detected."
        )

        st.dataframe(
            low_attendance,
            use_container_width=True
        )

    record_id = st.selectbox(
        "Delete Record",
        df["ID"]
    )

    if st.button("🗑 Delete"):

        delete_attendance(
            record_id
        )

        st.success(
            "Record Deleted"
        )

        st.rerun()

else:

    st.info(
        "No attendance records found."
    )