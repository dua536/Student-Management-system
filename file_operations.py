# file_operations.py
import pandas as pd
from config import DEFAULT_COLUMNS

def safe_read_students():
    """Safely read students from Excel file"""
    try:
        df = pd.read_excel("students.xlsx")
        # Ensure all required columns exist
        for col in DEFAULT_COLUMNS:
            if col not in df.columns:
                df[col] = ""
        return df
    except FileNotFoundError:
        # Return empty DataFrame with correct columns
        return pd.DataFrame(columns=DEFAULT_COLUMNS)

def safe_write_students(df):
    """Safely write students to Excel file"""
    # Ensure all required columns exist
    for col in DEFAULT_COLUMNS:
        if col not in df.columns:
            df[col] = ""
    df.to_excel("students.xlsx", index=False)

def safe_append_passed(passed_df):
    """Safely append passed students to passed_students.xlsx"""
    try:
        existing_df = pd.read_excel("passed_students.xlsx")
        combined_df = pd.concat([existing_df, passed_df], ignore_index=True)
    except FileNotFoundError:
        combined_df = passed_df
    combined_df.to_excel("passed_students.xlsx", index=False)
