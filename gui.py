import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import re
import io
from data_structures import SimpleStack, SimpleQueue, BST
from file_operations import safe_read_students, safe_write_students, safe_append_passed
from config import DEFAULT_COLUMNS

def apply_modern_theme():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Base Styling */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #f8fafc 100%);
        font-family: 'Inter', sans-serif;
        color: #e2e8f0;
    }
    
    .main .block-container {
        padding: 1.5rem;
        max-width: 100%;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        margin: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #06b6d4 100%);
        padding: 2rem 1rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        text-align: center;
        color: white;
        box-shadow: 0 8px 32px rgba(99, 102, 241, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .main-header h1 {
        font-size: 2.2rem;
        margin: 0;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .main-header p {
        font-size: 1rem;
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-weight: 400;
    }
    
    /* Button Styling */
    .stButton>button {
        border-radius: 10px;
        font-weight: 600;
        border: none;
        padding: 0.75rem 1.5rem;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
        background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
    }
    
    /* Secondary Buttons */
    .stButton>button[kind="secondary"] {
        background: linear-gradient(135deg, #475569 0%, #64748b 100%);
        box-shadow: 0 4px 12px rgba(71, 85, 105, 0.3);
    }
    
    .stButton>button[kind="secondary"]:hover {
        background: linear-gradient(135deg, #64748b 0%, #475569 100%);
        box-shadow: 0 6px 20px rgba(71, 85, 105, 0.4);
    }
    
    /* Metric Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(99, 102, 241, 0.4);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #f1f5f9;
        margin: 0;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    .metric-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin: 0.5rem 0 0 0;
        font-weight: 600;
    }
    
    .metric-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
        opacity: 0.9;
    }
    
    /* Section Headers */
    .section-header {
        color: #f1f5f9;
        border-bottom: 2px solid #334155;
        padding-bottom: 0.75rem;
        margin-bottom: 1.5rem;
        font-weight: 700;
        font-size: 1.3rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Dataframe Styling */
    .stDataFrame {
        border-radius: 12px !important;
        border: 1px solid #334155 !important;
        background: rgba(15, 23, 42, 0.8) !important;
        backdrop-filter: blur(10px);
    }
    
    /* Input Fields */
    .stTextInput>div>div>input, 
    .stNumberInput>div>div>input,
    .stSelectbox>div>div>select {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        color: #f1f5f9 !important;
        padding: 0.75rem !important;
    }
    
    .stTextInput>div>div>input:focus, 
    .stNumberInput>div>div>input:focus,
    .stSelectbox>div>div>select:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
    }
    
    /* Expander Styling */
    .streamlit-expanderHeader {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        color: #f1f5f9 !important;
        font-weight: 600;
    }
    
    .streamlit-expanderContent {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid #334155 !important;
        border-top: none !important;
        border-radius: 0 0 8px 8px !important;
    }
    
    /* Success/Warning/Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, #10b98120 0%, #05966920 100%) !important;
        border: 1px solid #10b981 !important;
        border-left: 4px solid #10b981 !important;
        color: #a7f3d0 !important;
        border-radius: 8px;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #f59e0b20 0%, #d9770620 100%) !important;
        border: 1px solid #f59e0b !important;
        border-left: 4px solid #f59e0b !important;
        color: #fde68a !important;
        border-radius: 8px;
    }
    
    .stError {
        background: linear-gradient(135deg, #ef444420 0%, #dc262620 100%) !important;
        border: 1px solid #ef4444 !important;
        border-left: 4px solid #ef4444 !important;
        color: #fecaca !important;
        border-radius: 8px;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #3b82f620 0%, #1d4ed820 100%) !important;
        border: 1px solid #3b82f6 !important;
        border-left: 4px solid #3b82f6 !important;
        color: #93c5fd !important;
        border-radius: 8px;
    }
    
    /* Quick Actions Box */
    .quick-actions-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    /* Navigation Sidebar */
    .css-1d391kg {
        background: rgba(15, 23, 42, 0.9) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid #334155;
    }
    
    /* Scrollbar Styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1e293b;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
    }
    
    /* Text Colors */
    h1, h2, h3, h4, h5, h6 {
        color: #f1f5f9;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
    }
    
    p, label, div {
        color: #e2e8f0;
    }
    
    /* Compact spacing */
    [data-testid="stVerticalBlock"] {
        gap: 0.75rem;
    }
    
    /* Download buttons */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
        box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3) !important;
    }
    
    .stDownloadButton>button:hover {
        background: linear-gradient(135deg, #047857 0%, #059669 100%) !important;
        box-shadow: 0 6px 20px rgba(5, 150, 105, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

def create_metric_card(label, value, icon):
    """Create a modern metric card with glassmorphism effect"""
    return f"""
    <div class="metric-card">
        <div class="metric-icon">{icon}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """

def validate_student_data(id, email):
    """Check if ID or Email already exists before adding student"""
    try:
        df = safe_read_students()
        # Check if ID already exists
        if id in df["ID"].values:
            st.error(f"❌ Student with ID {id} already exists!")
            return False
        # Check if Email already exists
        if email in df["Email"].values:
            st.error(f"❌ Student with email {email} already exists!")
            return False
        return True
    except Exception:
        # If file doesn't exist, no duplicates possible
        return True

def search_by_id():
    """Search student by ID"""
    st.subheader("🔍 Search Student by ID")
    
    try:
        df = safe_read_students()
        if df.empty:
            st.warning("No student records found! Please add students first.")
            return
    except Exception:
        st.warning("No student records found! Please add students first.")
        return
    
    search_id = st.number_input("Enter Student ID to search:", min_value=1, step=1, key="search_id")
    
    if st.button("Search", use_container_width=True):
        # Search for student with matching ID
        result = df[df["ID"] == search_id]
        if not result.empty:
            st.success("🎯 Student Found!")
            st.write("=" * 50)
            for col in result.columns:
                st.write(f"**{col}:** {result[col].values[0]}")
            st.write("=" * 50)
        else:
            st.error(f"❌ No student found with ID: {search_id}")

def search_by_name():
    """Search student by Name (partial match)"""
    st.subheader("🔍 Search Student by Name")
    
    try:
        df = safe_read_students()
        if df.empty:
            st.warning("No student records found! Please add students first.")
            return
    except Exception:
        st.warning("No student records found! Please add students first.")
        return
    
    search_name = st.text_input("Enter Student Name to search:").strip().lower()
    
    if st.button("Search", use_container_width=True):
        if search_name:
            # Search for students with matching name (case-insensitive, partial match)
            result = df[df["Name"].str.lower().str.contains(search_name, na=False)]
            if not result.empty:
                st.success(f"🎯 Found {len(result)} student(s) with name containing '{search_name}':")
                st.dataframe(result, use_container_width=True)
            else:
                st.error(f"❌ No students found with name containing: {search_name}")
        else:
            st.warning("Please enter a name to search.")

def check_duplicates():
    """Check for duplicate IDs and Emails"""
    st.subheader("🔍 Check for Duplicates")
    
    try:
        df = safe_read_students()
        if df.empty:
            st.warning("No student records found! Please add students first.")
            return
    except Exception:
        st.warning("No student records found! Please add students first.")
        return
    
    # Check for duplicate IDs
    duplicate_ids = df[df.duplicated('ID', keep=False)]
    if not duplicate_ids.empty:
        st.error("❌ Duplicate IDs Found:")
        st.dataframe(duplicate_ids[['ID', 'Name']], use_container_width=True)
    else:
        st.success("✅ No duplicate IDs found")
    
    # Check for duplicate Emails
    duplicate_emails = df[df.duplicated('Email', keep=False)]
    if not duplicate_emails.empty:
        st.error("❌ Duplicate Emails Found:")
        st.dataframe(duplicate_emails[['Email', 'Name', 'ID']], use_container_width=True)
    else:
        st.success("✅ No duplicate emails found")

def detect_gender(name_or_email):
    """Simple gender detection based on common name patterns."""
    name = str(name_or_email).lower()
    female_names = ['a', 'i', 'e', 'y', 'ah', 'ra', 'na', 'la', 'ta']
    male_names = ['r', 'n', 'd', 'm', 's', 'l']
    
    # Check typical female name endings
    if any(name.endswith(x) for x in female_names):
        return "Female"
    elif any(name.endswith(x) for x in male_names):
        return "Male"
    else:
        # If unclear, check email clues
        if re.search(r"(miss|ms|mrs)", name):
            return "Female"
        elif re.search(r"(mr|sir)", name):
            return "Male"
        else:
            return "Unknown"

def generate_pass_report():
    """Generate pass report with visualization"""
    st.subheader("📊 Pass Report Analysis")
    
    try:
        df = pd.read_excel("passed_students.xlsx")
    except FileNotFoundError:
        st.warning("⚠️ No passed students sheet found. Please create it first.")
        return
    
    if df.empty:
        st.warning("⚠️ Passed students sheet is empty.")
        return
    
    # Detect gender
    df["Gender"] = df["Name"].apply(detect_gender)
    
    # Summary calculations
    total_students = len(df)
    avg_gpa = round(df["GPA"].mean(), 2) if not df.empty else 0
    max_gpa = df["GPA"].max() if not df.empty else 0
    top_student = df.loc[df["GPA"].idxmax(), "Name"] if not df.empty else "N/A"
    dept_counts = df["Department"].value_counts()
    top_dept = dept_counts.idxmax() if not dept_counts.empty else "N/A"
    gender_counts = df["Gender"].value_counts()
    
    # Calculate GPA ranges
    if not df.empty:
        gpa_ranges = pd.cut(df["GPA"], bins=[0, 2.5, 3.0, 3.5, 4.0], right=False)
        most_common_range = gpa_ranges.value_counts().idxmax() if not gpa_ranges.empty else "N/A"
    else:
        most_common_range = "N/A"
    
    # Display summary in columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Passed Students", total_students)
        st.metric("Average GPA", avg_gpa)
        st.metric("Highest GPA", f"{max_gpa} ({top_student})")
    
    with col2:
        st.metric("Top Department", top_dept)
        st.metric("Gender Distribution", f"Male: {gender_counts.get('Male',0)} | Female: {gender_counts.get('Female',0)}")
        st.metric("Most Common GPA Range", str(most_common_range))
    
    # Plot GPA by Department
    if not df.empty and 'Department' in df.columns and len(df['Department'].unique()) > 0:
        st.subheader("📈 GPA Distribution by Department")
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Group by department and calculate average GPA
        dept_gpa = df.groupby('Department')['GPA'].mean()
        
        ax.bar(dept_gpa.index, dept_gpa.values, color="skyblue")
        ax.axhline(avg_gpa, color="red", linestyle="--", label=f"Average GPA: {avg_gpa}")
        ax.set_xlabel("Department")
        ax.set_ylabel("GPA")
        ax.set_title("Average Passing GPA by Department")
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    
    st.success("✅ Pass report generated successfully!")

def add_student_action(student: dict):
    """Add new student to the system"""
    df = st.session_state.students_df.copy()
    
    # Check if ID already exists
    if student["ID"] in df["ID"].values:
        st.warning(f"ID {student['ID']} already exists.")
        return False
    
    # Add new student
    df = pd.concat([df, pd.DataFrame([student])], ignore_index=True)
    st.session_state.students_df = df
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
        st.session_state.students_df = df.reset_index(drop=True)
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
            st.session_state.students_df = df.reset_index(drop=True)
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
    # Ensure queue is loaded
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
        # Update the main dataframe
        df.loc[df["ID"] == s["ID"], "Seat_Status"] = "Passed"
    
    # Remove passed students from main sheet
    remaining_df = df[df["Seat_Status"] != "Passed"].reset_index(drop=True)
    st.session_state.students_df = remaining_df
    safe_write_students(st.session_state.students_df)
    
    if passed_list:
        passed_df = pd.DataFrame(passed_list)
        safe_append_passed(passed_df)
    
    st.success(f"{len(passed_list)} students marked as Passed!")
    st.rerun()

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
    sorted_df = pd.DataFrame(sorted_students)
    st.session_state.students_df = sorted_df.reset_index(drop=True)
    safe_write_students(st.session_state.students_df)
    st.success("Students sorted by GPA (BST)!")

def calculate_stats():
    """Calculate statistics for overview"""
    df = st.session_state.students_df
    total = len(df)
    passed = len(df[df["Seat_Status"] == "Passed"]) if 'Seat_Status' in df.columns and not df.empty else 0
    avg_gpa = df["GPA"].mean() if not df.empty and not df["GPA"].isna().all() else 0
    queue_size = st.session_state.queue.size() if hasattr(st.session_state, 'queue') else 0
    
    return total, passed, round(avg_gpa, 2), queue_size

def export_to_excel(df, filename):
    """Export dataframe to Excel file in memory"""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Students')
    processed_data = output.getvalue()
    return processed_data

def export_to_csv(df, filename):
    """Export dataframe to CSV file in memory"""
    return df.to_csv(index=False).encode('utf-8')

def main():
    # Apply modern theme
    apply_modern_theme()
    
    # Enhanced Header with Perfect Size
    st.markdown("""
        <div class="main-header">
            <h1>🎓 SMART STUDENT MANAGEMENT</h1>
            <p>Comprehensive Student Tracking & Analytics Dashboard</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 📊 QUICK OVERVIEW - Horizontal Layout with Boxes
    st.markdown('<div class="section-header">📊 QUICK OVERVIEW</div>', unsafe_allow_html=True)
    
    # Calculate stats
    total, passed, avg_gpa, queue_size = calculate_stats()
    
    # Display metrics in horizontal boxes with spacing
    overview_cols = st.columns(4)
    with overview_cols[0]:
        st.markdown(create_metric_card("TOTAL", total, "👨‍🎓"), unsafe_allow_html=True)
    with overview_cols[1]:
        st.markdown(create_metric_card("PASSED", passed, "✅"), unsafe_allow_html=True)
    with overview_cols[2]:
        st.markdown(create_metric_card("GPA AVG", avg_gpa, "📈"), unsafe_allow_html=True)
    with overview_cols[3]:
        st.markdown(create_metric_card("QUEUE", queue_size, "⏳"), unsafe_allow_html=True)
    
    # Add spacing between sections
    st.markdown('<div style="margin-bottom: 1.5rem;"></div>', unsafe_allow_html=True)
    
    # 🚀 QUICK ACTIONS - Horizontal Layout in Box
    st.markdown('<div class="section-header">🚀 QUICK ACTIONS</div>', unsafe_allow_html=True)
    
    # Action buttons in horizontal layout within a box
    st.markdown('<div class="quick-actions-box">', unsafe_allow_html=True)
    action_cols = st.columns(3)
    with action_cols[0]:
        if st.button("🔄 REFRESH DATA", use_container_width=True, key="refresh"):
            st.session_state.students_df = safe_read_students()
            st.success("📊 Data refreshed successfully!")
            st.rerun()
    
    with action_cols[1]:
        if st.button("📥 LOAD QUEUE", use_container_width=True, key="load_queue"):
            load_queue_from_df()
            st.success(f"📋 Queue loaded with {st.session_state.queue.size()} students!")
            st.rerun()
    
    with action_cols[2]:
        if st.button("📊 SORT BY GPA", use_container_width=True, key="sort_gpa"):
            sort_by_gpa_desc_using_bst()
            st.success("🎯 Students sorted by GPA!")
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add spacing between sections
    st.markdown('<div style="margin-bottom: 1.5rem;"></div>', unsafe_allow_html=True)
    
    # Create main layout with Navigation on left and Main Content on right
    nav_col, content_col = st.columns([1, 3])
    
    with nav_col:
        # 🧭 NAVIGATION Section
        st.markdown('<div class="section-header">🧭 NAVIGATION</div>', unsafe_allow_html=True)
        
        # Navigation buttons
        nav_buttons = [
            ("📋 RECORDS", "records"),
            ("➕ ADD", "add"),
            ("⚡ PROCESS", "process"), 
            ("🗑️ DELETE", "delete"),
            ("📊 PASS REPORT", "report")
        ]
        
        for btn_text, view_name in nav_buttons:
            if st.button(btn_text, use_container_width=True, key=f"nav_{view_name}"):
                st.session_state.current_view = view_name
                st.rerun()
    
    with content_col:
        # Main Content Area
        current_view = st.session_state.get('current_view', 'records')
        
        # Content based on current view
        if current_view == "records":
            st.markdown('<div class="section-header">📋 STUDENT RECORDS</div>', unsafe_allow_html=True)
            
            # Add search and utility buttons in expanders
            with st.expander("🔍 SEARCH & UTILITIES", expanded=False):
                util_col1, util_col2, util_col3, util_col4 = st.columns(4)
                
                with util_col1:
                    if st.button("🔍 BY ID", use_container_width=True):
                        st.session_state.show_search_id = True
                
                with util_col2:
                    if st.button("🔍 BY NAME", use_container_width=True):
                        st.session_state.show_search_name = True
                
                with util_col3:
                    if st.button("🔍 CHECK DUPLICATES", use_container_width=True):
                        st.session_state.show_duplicates = True
                
                with util_col4:
                    if st.button("📊 GENERATE REPORT", use_container_width=True):
                        st.session_state.show_report = True
            
            # Export options
            with st.expander("💾 EXPORT DATA", expanded=False):
                export_col1, export_col2 = st.columns(2)
                
                with export_col1:
                    # Export current students
                    if not st.session_state.students_df.empty:
                        excel_data = export_to_excel(st.session_state.students_df, "students.xlsx")
                        st.download_button(
                            label="📥 EXPORT CURRENT STUDENTS (Excel)",
                            data=excel_data,
                            file_name="students.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            use_container_width=True
                        )
                        
                        csv_data = export_to_csv(st.session_state.students_df, "students.csv")
                        st.download_button(
                            label="📥 EXPORT CURRENT STUDENTS (CSV)",
                            data=csv_data,
                            file_name="students.csv",
                            mime="text/csv",
                            use_container_width=True
                        )
                    else:
                        st.warning("No data to export")
                
                with export_col2:
                    # Export passed students
                    try:
                        passed_df = pd.read_excel("passed_students.xlsx")
                        if not passed_df.empty:
                            passed_excel_data = export_to_excel(passed_df, "passed_students.xlsx")
                            st.download_button(
                                label="📥 EXPORT PASSED STUDENTS (Excel)",
                                data=passed_excel_data,
                                file_name="passed_students.xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                use_container_width=True
                            )
                            
                            passed_csv_data = export_to_csv(passed_df, "passed_students.csv")
                            st.download_button(
                                label="📥 EXPORT PASSED STUDENTS (CSV)",
                                data=passed_csv_data,
                                file_name="passed_students.csv",
                                mime="text/csv",
                                use_container_width=True
                            )
                        else:
                            st.warning("No passed students data")
                    except FileNotFoundError:
                        st.warning("No passed students file found")
            
            # Show search by ID if triggered
            if st.session_state.get('show_search_id', False):
                search_by_id()
                if st.button("Close Search", key="close_id"):
                    st.session_state.show_search_id = False
                    st.rerun()
            
            # Show search by name if triggered
            if st.session_state.get('show_search_name', False):
                search_by_name()
                if st.button("Close Search", key="close_name"):
                    st.session_state.show_search_name = False
                    st.rerun()
            
            # Show duplicates if triggered
            if st.session_state.get('show_duplicates', False):
                check_duplicates()
                if st.button("Close Duplicate Check", key="close_dup"):
                    st.session_state.show_duplicates = False
                    st.rerun()
            
            # Show report if triggered
            if st.session_state.get('show_report', False):
                generate_pass_report()
                if st.button("Close Report", key="close_report"):
                    st.session_state.show_report = False
                    st.rerun()
            
            # Display student records
            if not st.session_state.students_df.empty:
                st.dataframe(st.session_state.students_df, use_container_width=True, height=400)
            else:
                st.info("🎯 No student records available. Use 'Add Student' to create records.")
        
        elif current_view == "add":
            st.markdown('<div class="section-header">➕ ADD NEW STUDENT</div>', unsafe_allow_html=True)
            
            # Undo-Redo buttons in Add section
            st.markdown("#### 🔄 Action History")
            undo_col1, undo_col2 = st.columns(2)
            with undo_col1:
                if st.button("↩️ UNDO LAST ACTION", use_container_width=True, key="undo_add"):
                    undo_action()
                    st.rerun()
            with undo_col2:
                if st.button("↪️ REDO LAST ACTION", use_container_width=True, key="redo_add"):
                    redo_action()
                    st.rerun()
            
            st.markdown("---")
            
            with st.form("add_student_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                
                with col1:
                    student_id = st.number_input("🎯 Student ID", min_value=1, step=1)
                    name = st.text_input("👤 Full Name")
                    department = st.text_input("🏛️ Department")
                    semester = st.text_input("📚 Semester")
                    gpa = st.number_input("📊 GPA", min_value=0.0, max_value=4.0, step=0.1, format="%.2f")
                
                with col2:
                    credits_completed = st.number_input("🎓 Credits Completed", min_value=0, step=1)
                    email = st.text_input("📧 Email")
                    contact_no = st.text_input("📞 Contact No")
                    seat_status = st.selectbox("💺 Seat Status", ["Available", "Occupied", "Reserved", "Passed"])
                
                if st.form_submit_button("🎓 ADD STUDENT", use_container_width=True):
                    if validate_student_data(student_id, email):
                        student = {
                            "ID": int(student_id),
                            "Name": name,
                            "Department": department,
                            "Semester": semester,
                            "GPA": float(gpa),
                            "Credits_Completed": int(credits_completed),
                            "Email": email,
                            "Contact_No": contact_no,
                            "Seat_Status": seat_status
                        }
                        if add_student_action(student):
                            st.success("✅ Student added successfully!")
                            st.balloons()
                            st.rerun()
        
        elif current_view == "process":
            st.markdown('<div class="section-header">⚡ BATCH PROCESSING</div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🎯 Queue Management")
                
                # Queue status
                queue_status = st.container()
                with queue_status:
                    if st.session_state.queue.size() > 0:
                        st.success(f"**{st.session_state.queue.size()}** students in processing queue")
                        next_student = st.session_state.queue.get_front()
                        if next_student:
                            st.info(f"""
                            **Next in Line:**
                            - **Name:** {next_student['Name']}
                            - **ID:** {next_student['ID']}
                            - **GPA:** {next_student['GPA']}
                            """)
                    else:
                        st.warning("Queue is empty. Load students to begin processing.")
                
                # Queue operations
                if st.button("🔄 RELOAD QUEUE", use_container_width=True):
                    load_queue_from_df()
                    st.success(f"Queue reloaded with {st.session_state.queue.size()} students!")
                    st.rerun()
            
            with col2:
                st.subheader("⚡ Batch Operations")
                
                if st.session_state.queue.size() > 0:
                    # Handle the case when queue size is 1
                    if st.session_state.queue.size() == 1:
                        pass_count = 1
                        st.info("Only 1 student in queue. This student will be passed.")
                    else:
                        pass_count = st.number_input(
                            "Number of students to mark as passed",
                            min_value=1,
                            max_value=st.session_state.queue.size(),
                            value=1,
                            step=1
                        )
                    
                    if st.button("🎓 MARK AS PASSED", use_container_width=True, type="primary"):
                        pass_students(pass_count)
                        st.rerun()
                else:
                    st.info("Load students into queue to enable batch processing")
        
        elif current_view == "delete":
            st.markdown('<div class="section-header">🗑️ DELETE STUDENT</div>', unsafe_allow_html=True)
            if not st.session_state.students_df.empty:
                st.markdown("### Current Students")
                st.dataframe(st.session_state.students_df[['ID', 'Name', 'Department']], use_container_width=True, height=200)
                
                with st.form("delete_form"):
                    del_id = st.number_input("Enter Student ID to delete", min_value=1, step=1)
                    if st.form_submit_button("⚠️ DELETE STUDENT", use_container_width=True):
                        if delete_student_action(int(del_id)):
                            st.success("✅ Student deleted successfully!")
                            st.rerun()
            else:
                st.info("📝 No students available for deletion.")
        
        elif current_view == "report":
            generate_pass_report()

# Initialize session state
if 'students_df' not in st.session_state:
    st.session_state.students_df = safe_read_students()

if 'undo_stack' not in st.session_state:
    st.session_state.undo_stack = SimpleStack()

if 'redo_stack' not in st.session_state:
    st.session_state.redo_stack = SimpleStack()

if 'queue' not in st.session_state:
    st.session_state.queue = SimpleQueue()

if 'current_view' not in st.session_state:
    st.session_state.current_view = "records"

# Initialize utility view states
if 'show_search_id' not in st.session_state:
    st.session_state.show_search_id = False

if 'show_search_name' not in st.session_state:
    st.session_state.show_search_name = False

if 'show_duplicates' not in st.session_state:
    st.session_state.show_duplicates = False

if 'show_report' not in st.session_state:
    st.session_state.show_report = False

if __name__ == "__main__":
    main()
