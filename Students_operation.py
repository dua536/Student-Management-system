import pandas as pd
import streamlit as st
from data_structures import SimpleStack, SimpleQueue, BST
from file_operations import safe_read_students, safe_write_students, safe_append_passed
from config import DEFAULT_COLUMNS

def add_student_action(student: dict):
    """Add new student to the system"""
    df = st.session_state.students_df.copy()
    
    # Check if ID already exists
    if student["ID"] in df["ID"].values:
        st.warning(f"ID {student['ID']} already exists.")
        return False
    
    # Add new student
    df = pd.concat([df, pd.DataFrame([student])], ignore_index=True)
    st.session_state.students_df = df[DEFAULT_COLUMNS]
    safe_write_students(st.session_state.students_df)
    st.session_state.undo_stack.push(("add", student))
    st.session_state.redo_stack.clear()
    return True

def delete_student_action(student_id: int):
    """Delete student from the system"""
    df = st.session_state.students_df.copy()
    
    # Check if student exists
    if student_id not in df["ID"].values:
        st.warning(f"ID {student_id} not found.")
        return False
    
    # Delete student
    deleted_row = df[df["ID"] == student_id].iloc[0].to_dict()
    df = df[df["ID"] != student_id]
    st.session_state.students_df = df.reset_index(drop=True)
    safe_write_students(st.session_state.students_df)
    st.session_state.undo_stack.push(("delete", deleted_row))
    st.session_state.redo_stack.clear()
    return True

def undo_action():
    """Undo the last action"""
    if st.session_state.undo_stack.is_empty():
        st.info("Nothing to undo.")
        return
    
    action, data = st.session_state.undo_stack.pop()
    df = st.session_state.students_df.copy()
    
    if action == "add":
        # Remove added student
        df = df[df["ID"] != data["ID"]]
        st.session_state.students_df = df.reset_index(drop=True)
        st.session_state.redo_stack.push(("add", data))
    elif action == "delete":
        # Restore deleted student
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
        st.session_state.students_df = df[DEFAULT_COLUMNS].reset_index(drop=True)
        st.session_state.redo_stack.push(("delete", data))
    
    safe_write_students(st.session_state.students_df)
    st.success("Undo performed.")

def redo_action():
    """Redo the last undone action"""
    if st.session_state.redo_stack.is_empty():
        st.info("Nothing to redo.")
        return
    
    action, data = st.session_state.redo_stack.pop()
    df = st.session_state.students_df.copy()
    
    if action == "add":
        if data["ID"] in df["ID"].values:
            st.warning("Redo add conflict: ID already exists.")
        else:
            df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
            st.session_state.students_df = df[DEFAULT_COLUMNS].reset_index(drop=True)
            st.session_state.undo_stack.push(("add", data))
    elif action == "delete":
        df = df[df["ID"] != data["ID"]]
        st.session_state.students_df = df.reset_index(drop=True)
        st.session_state.undo_stack.push(("delete", data))
    
    safe_write_students(st.session_state.students_df)
    st.success("Redo performed.")

def load_queue_from_df():
    """Load students into queue"""
    st.session_state.queue.clear()
    df = st.session_state.students_df
    for _, row in df.iterrows():
        st.session_state.queue.enqueue(row.to_dict())

def pass_students(count: int):
    """Mark students as passed"""
    if st.session_state.queue.size() == 0:
        load_queue_from_df()
    
    if st.session_state.queue.size() == 0:
        st.warning("No students to pass.")
        return
    
    if count > st.session_state.queue.size():
        st.warning(f"Only {st.session_state.queue.size()} students available.")
        return
    
    passed_list = []
    df = st.session_state.students_df.copy()
    
    for _ in range(count):
        s = st.session_state.queue.dequeue()
        if not isinstance(s, dict):
            continue
        s["Seat_Status"] = "Passed"
        passed_list.append(s)
        df.loc[df["ID"] == s["ID"], "Seat_Status"] = "Passed"
    
    # Remove passed students from main sheet
    remaining_df = df[df["Seat_Status"] != "Passed"].reset_index(drop=True)
    st.session_state.students_df = remaining_df[DEFAULT_COLUMNS]
    safe_write_students(st.session_state.students_df)
    
    if passed_list:
        passed_df = pd.DataFrame(passed_list)[DEFAULT_COLUMNS]
        safe_append_passed(passed_df)
    
    st.success(f"{len(passed_list)} students marked as Passed!")

def sort_by_gpa_desc_using_bst():
    """Sort students by GPA using BST"""
    df = safe_read_students()
    if df.empty:
        st.info("No students to sort.")
        return
    
    bst = BST()
    for _, row in df.iterrows():
        try:
            gpa_val = float(row["GPA"])
        except Exception:
            gpa_val = float(".inf")
        bst.insert((gpa_val, row.to_dict()))
    
    nodes = bst.inorder()
    nodes.reverse()  # Highest GPA first
    sorted_students = [n[1] for n in nodes]
    sorted_df = pd.DataFrame(sorted_students)[DEFAULT_COLUMNS]
    st.session_state.students_df = sorted_df.reset_index(drop=True)
    safe_write_students(st.session_state.students_df)
    st.success("Students sorted by GPA (BST)!")
