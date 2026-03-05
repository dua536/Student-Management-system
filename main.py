import streamlit as st
import pandas as pd
import io
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now import your modules
from data_structures import SimpleStack, SimpleQueue, BST
from file_operations import safe_read_students, safe_append_passed
from student_operations import (
    add_student_action, delete_student_action, undo_action, redo_action,
    load_queue_from_df, pass_students, sort_by_gpa_desc_using_bst
)
from utils import apply_modern_theme
from config import DEFAULT_COLUMNS, PASSED_FILE

# Initialize session state
if "undo_stack" not in st.session_state:
    st.session_state.undo_stack = SimpleStack()
if "redo_stack" not in st.session_state:
    st.session_state.redo_stack = SimpleStack()
if "queue" not in st.session_state:
    st.session_state.queue = SimpleQueue()
if "bst" not in st.session_state:
    st.session_state.bst = BST()
if "students_df" not in st.session_state:
    st.session_state.students_df = safe_read_students()

# Set page config and apply theme
st.set_page_config(
    page_title="Smart Student Management System",
    layout="wide",
    page_icon="🎓"
)
apply_modern_theme()

# Header
st.markdown("<h1>Smart Student Management System</h1>", unsafe_allow_html=True)

# Quick Stats
if not st.session_state.students_df.empty:
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Students", len(st.session_state.students_df))
    with col2:
        passed = len(st.session_state.students_df[st.session_state.students_df['Seat_Status'] == 'Passed'])
        st.metric("Passed", passed)
    with col3:
        st.metric("Avg GPA", f"{st.session_state.students_df['GPA'].mean():.2f}")
    with col4:
        st.metric("Queue", st.session_state.queue.size())

# Sidebar
with st.sidebar:
    st.header("Quick Actions")

    if st.button("🔄 Refresh Data"):
        st.session_state.students_df = safe_read_students()
        st.success("Data refreshed!")
    
    if st.button("📊 Sort by GPA (BST)"):
        sort_by_gpa_desc_using_bst()

    if st.button("🔄 Load Queue"):
        load_queue_from_df()
        st.success("Queue loaded!")

    st.header("History")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("↩️ Undo"):
            undo_action()
    with col2:
        if st.button("↪️ Redo"):
            redo_action()

    st.header("Export")
    buffer = io.BytesIO()
    st.session_state.students_df.to_excel(buffer, index=False)
    st.download_button("📁 Download Excel", data=buffer, file_name="students.xlsx")

# Main Content Tabs
tab1, tab2, tab3, tab4 = st.tabs(['View Students', 'Add Student', 'Delete Student', 'Process Queue'])

with tab1:
    st.subheader("Student Records")
    st.dataframe(st.session_state.students_df, use_container_width=True)

with tab2:
    st.subheader("Add New Student")
    with st.form("add_form"):
        col1, col2 = st.columns(2)
        with col1:
            id_val = st.number_input("ID", min_value=1, step=1)
            name = st.text_input("Name")
            dept = st.text_input("Department")
            sem = st.text_input("Semester")
        with col2:
            gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, step=0.1)
            credits = st.number_input("Credits", min_value=0, step=1)
            email = st.text_input("Email")
            contact = st.text_input("Contact")
            status = st.selectbox("Status", ["Active", "Passed", "Pending"])
        
        if st.form_submit_button("+ Add Student"):
            student = {
                "ID": int(id_val), "Name": name, "Department": dept,
                "Semester": sem, "GPA": gpa, "Credits_Completed": credits,
                "Email": email, "Contact_No": contact, "Seat_Status": status
            }
            if add_student_action(student):
                st.success(f"Added {name}!")

with tab3:
    st.subheader("Delete Student")
    with st.form("delete_form"):
        del_id = st.number_input("Student ID to delete", min_value=1, step=1)
        if st.form_submit_button("🗑️ Delete"):
            if delete_student_action(int(del_id)):
                st.success(f"Deleted ID {del_id}!")

with tab4:
    st.subheader("Process Students Queue")
    col1, col2 = st.columns([2, 1])
    with col1:
        count = st.slider("Students to pass", 1, 50, 5)
        if st.button("Process Students"):
            pass_students(count)
    with col2:
        st.metric("Queue Size", st.session_state.queue.size())

# Passed Students Section
st.markdown("---")
st.subheader("Passed Students")
if PASSED_FILE.exists():
    try:
        df_passed = pd.read_excel(PASSED_FILE)
        if not df_passed.empty:
            st.dataframe(df_passed, use_container_width=True)
            st.download_button(
                "Download Passed List",
                data=df_passed.to_csv(index=False).encode(),
                file_name="passed_students.csv"
            )
    except:
        st.info("No passed students yet")
else:
    st.info("No passed students archive yet")
