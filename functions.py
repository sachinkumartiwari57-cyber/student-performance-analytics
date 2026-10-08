"""
functions.py
============
Module containing reusable functions for the Student Performance Analytics System.
Includes data loading, validation, performance calculations, statistical analysis,
and report generation using Pandas, NumPy, conditions, and loops.
"""

import os
import pandas as pd
import numpy as np


def load_data(filepath):
    """
    Load student data from a CSV file into a Pandas DataFrame.

    Parameters:
        filepath (str): Path to the students CSV file.

    Returns:
        pd.DataFrame or None: Loaded DataFrame if successful, None otherwise.
    """
    if not os.path.exists(filepath):
        print(f"Error: The dataset file '{filepath}' was not found.")
        return None

    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as error:
        print(f"Error while reading '{filepath}': {error}")
        return None


def validate_data(df, subject_columns, min_records=20):
    """
    Validate the student dataset for completeness, correct types,
    unique IDs, and valid score ranges.

    Parameters:
        df (pd.DataFrame): Input DataFrame to validate.
        subject_columns (list): List of subject column names.
        min_records (int): Minimum number of records expected.

    Returns:
        tuple (bool, str): (True, "Valid") if validation passes,
                           (False, error_message) otherwise.
    """
    if df is None or df.empty:
        return False, "Dataset is empty or could not be loaded."

    if len(df) < min_records:
        return False, f"Dataset must contain at least {min_records} records, found {len(df)}."

    # Validate required base columns
    base_columns = ["Student_ID", "Name", "Department", "Attendance"]
    required_columns = base_columns + subject_columns

    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        return False, f"Missing required column(s): {', '.join(missing_cols)}"

    # Check for duplicate Student_ID values
    if df["Student_ID"].duplicated().any():
        duplicate_ids = df[df["Student_ID"].duplicated()]["Student_ID"].tolist()
        return False, f"Duplicate Student_ID values found: {duplicate_ids}"

    # Check for missing (NaN / null) values
    if df[required_columns].isnull().any().any():
        null_counts = df[required_columns].isnull().sum()
        cols_with_null = null_counts[null_counts > 0].to_dict()
        return False, f"Missing values detected in columns: {cols_with_null}"

    # Validate numeric types and ranges for subject marks (0 - 100)
    for subject in subject_columns:
        if not pd.api.types.is_numeric_dtype(df[subject]):
            return False, f"Column '{subject}' contains non-numeric marks."
        
        marks_array = df[subject].to_numpy()
        if np.any(marks_array < 0) or np.any(marks_array > 100):
            return False, f"Marks in '{subject}' must be between 0 and 100."

    # Validate numeric type and range for Attendance (0 - 100)
    if not pd.api.types.is_numeric_dtype(df["Attendance"]):
        return False, "Column 'Attendance' contains non-numeric values."

    attendance_array = df["Attendance"].to_numpy()
    if np.any(attendance_array < 0) or np.any(attendance_array > 100):
        return False, "Attendance values must be between 0 and 100%."

    return True, "Dataset validated successfully."


def calculate_total_marks(df, subject_columns):
    """
    Calculate total marks across all subjects for each student using NumPy.

    Parameters:
        df (pd.DataFrame): DataFrame containing student records.
        subject_columns (list): List of subject column names.

    Returns:
        np.ndarray: 1D NumPy array containing total marks for each student.
    """
    # Extract marks matrix as a NumPy 2D array
    marks_matrix = df[subject_columns].to_numpy()
    # Compute sum across row axis (axis=1) using NumPy
    total_marks = np.sum(marks_matrix, axis=1)
    return total_marks


def calculate_average_marks(df, subject_columns):
    """
    Calculate average marks across all subjects for each student using NumPy.

    Parameters:
        df (pd.DataFrame): DataFrame containing student records.
        subject_columns (list): List of subject column names.

    Returns:
        np.ndarray: 1D NumPy array of average marks rounded to 2 decimal places.
    """
    # Extract marks matrix as a NumPy 2D array
    marks_matrix = df[subject_columns].to_numpy()
    # Compute mean across row axis (axis=1) using NumPy
    average_marks = np.mean(marks_matrix, axis=1)
    return np.round(average_marks, 2)


def assign_grade(average_mark):
    """
    Assign a letter grade based on the student's average marks.

    Grading Scheme:
        90 - 100 : A+
        80 - 89  : A
        70 - 79  : B
        60 - 69  : C
        50 - 59  : D
        40 - 49  : E
        Below 40 : F

    Parameters:
        average_mark (float): Average mark of the student.

    Returns:
        str: Assigned letter grade.
    """
    if average_mark >= 90.0:
        return "A+"
    elif average_mark >= 80.0:
        return "A"
    elif average_mark >= 70.0:
        return "B"
    elif average_mark >= 60.0:
        return "C"
    elif average_mark >= 50.0:
        return "D"
    elif average_mark >= 40.0:
        return "E"
    else:
        return "F"


def calculate_result(average_mark, subject_marks_list):
    """
    Determine Pass or Fail status for a student.

    Pass Rule:
        A student is PASS only if:
        1. Average marks >= 40
        AND
        2. Student scores at least 40 marks in every subject.
        Otherwise: FAIL.

    Parameters:
        average_mark (float): Average marks of the student.
        subject_marks_list (list or np.ndarray): Marks in all subjects.

    Returns:
        str: "PASS" or "FAIL".
    """
    # Check overall average threshold
    if average_mark < 40.0:
        return "FAIL"

    # Check that every individual subject mark is at least 40
    for mark in subject_marks_list:
        if mark < 40:
            return "FAIL"

    return "PASS"


def calculate_attendance_status(attendance_percentage):
    """
    Determine attendance eligibility status.

    Rule:
        Attendance >= 75% -> "Eligible"
        Attendance < 75%  -> "Short Attendance"

    Parameters:
        attendance_percentage (float): Attendance value in percent.

    Returns:
        str: "Eligible" or "Short Attendance".
    """
    if attendance_percentage >= 75.0:
        return "Eligible"
    else:
        return "Short Attendance"


def add_performance_columns(df, subject_columns):
    """
    Compute and append performance columns to the DataFrame:
    Total_Marks, Average_Marks, Grade, Result, and Attendance_Status.
    Demonstrates meaningful use of loops and conditions alongside Pandas.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        subject_columns (list): List of subject column names.

    Returns:
        pd.DataFrame: DataFrame enriched with new analytical columns.
    """
    df_copy = df.copy()

    # Calculate Total Marks and Average Marks using NumPy functions
    df_copy["Total_Marks"] = calculate_total_marks(df_copy, subject_columns)
    df_copy["Average_Marks"] = calculate_average_marks(df_copy, subject_columns)

    # Use loops to evaluate Grade, Result, and Attendance_Status for each student
    grades = []
    results = []
    attendance_statuses = []

    for index, row in df_copy.iterrows():
        avg = row["Average_Marks"]
        subject_marks = [row[sub] for sub in subject_columns]
        att = row["Attendance"]

        # Assign Grade using conditional logic
        grade = assign_grade(avg)
        grades.append(grade)

        # Determine Result using pass/fail criteria
        result = calculate_result(avg, subject_marks)
        results.append(result)

        # Determine Attendance Eligibility
        att_status = calculate_attendance_status(att)
        attendance_statuses.append(att_status)

    df_copy["Grade"] = grades
    df_copy["Result"] = results
    df_copy["Attendance_Status"] = attendance_statuses

    return df_copy


def get_class_statistics(df, subject_columns):
    """
    Calculate comprehensive class-level performance statistics using NumPy and Pandas.

    Parameters:
        df (pd.DataFrame): Processed DataFrame with analytical columns.
        subject_columns (list): List of subject columns.

    Returns:
        dict: Summary metrics for the class.
    """
    total_students = len(df)
    averages_array = df["Average_Marks"].to_numpy()

    # NumPy calculations for class averages and extremes
    overall_class_average = float(np.round(np.mean(averages_array), 2))
    highest_average = float(np.max(averages_array))
    lowest_average = float(np.min(averages_array))

    # Highest and lowest performing student records
    highest_idx = df["Average_Marks"].idxmax()
    lowest_idx = df["Average_Marks"].idxmin()

    highest_student = {
        "Student_ID": df.loc[highest_idx, "Student_ID"],
        "Name": df.loc[highest_idx, "Name"],
        "Average_Marks": df.loc[highest_idx, "Average_Marks"],
        "Grade": df.loc[highest_idx, "Grade"],
        "Result": df.loc[highest_idx, "Result"],
    }

    lowest_student = {
        "Student_ID": df.loc[lowest_idx, "Student_ID"],
        "Name": df.loc[lowest_idx, "Name"],
        "Average_Marks": df.loc[lowest_idx, "Average_Marks"],
        "Grade": df.loc[lowest_idx, "Grade"],
        "Result": df.loc[lowest_idx, "Result"],
    }

    # Pass / Fail counts and percentages
    passed_count = int(np.count_nonzero(df["Result"].to_numpy() == "PASS"))
    failed_count = int(np.count_nonzero(df["Result"].to_numpy() == "FAIL"))
    pass_percentage = round((passed_count / total_students) * 100, 2)
    fail_percentage = round((failed_count / total_students) * 100, 2)

    # Attendance statistics
    attendance_array = df["Attendance"].to_numpy()
    average_attendance = float(np.round(np.mean(attendance_array), 2))
    eligible_attendance_count = int(np.count_nonzero(attendance_array >= 75))
    short_attendance_count = int(np.count_nonzero(attendance_array < 75))

    # 2D NumPy array across all subject marks
    all_marks_matrix = df[subject_columns].to_numpy()
    marks_overall_mean = float(np.round(np.mean(all_marks_matrix), 2))
    marks_overall_max = int(np.max(all_marks_matrix))
    marks_overall_min = int(np.min(all_marks_matrix))
    marks_std_dev = float(np.round(np.std(all_marks_matrix), 2))

    return {
        "total_students": total_students,
        "overall_class_average": overall_class_average,
        "highest_average": highest_average,
        "lowest_average": lowest_average,
        "highest_student": highest_student,
        "lowest_student": lowest_student,
        "passed_count": passed_count,
        "failed_count": failed_count,
        "pass_percentage": pass_percentage,
        "fail_percentage": fail_percentage,
        "average_attendance": average_attendance,
        "eligible_attendance_count": eligible_attendance_count,
        "short_attendance_count": short_attendance_count,
        "marks_overall_mean": marks_overall_mean,
        "marks_overall_max": marks_overall_max,
        "marks_overall_min": marks_overall_min,
        "marks_std_dev": marks_std_dev,
    }


def get_subject_statistics(df, subject_columns):
    """
    Calculate subject-wise metrics (average, highest, lowest, pass count)
    using loops and NumPy functions, and identify the best and weakest subjects.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        subject_columns (list): List of subject column names.

    Returns:
        dict: Contains a summary DataFrame of subject metrics, best subject, and weakest subject.
    """
    records = []

    # Meaningful loop over subjects
    for subject in subject_columns:
        subject_array = df[subject].to_numpy()

        sub_avg = float(np.round(np.mean(subject_array), 2))
        sub_high = int(np.max(subject_array))
        sub_low = int(np.min(subject_array))
        sub_passed = int(np.count_nonzero(subject_array >= 40))
        sub_failed = int(np.count_nonzero(subject_array < 40))

        records.append({
            "Subject": subject,
            "Average": sub_avg,
            "Highest": sub_high,
            "Lowest": sub_low,
            "Passed": sub_passed,
            "Failed": sub_failed
        })

    summary_df = pd.DataFrame(records)

    # Determine best and weakest subjects based on average score
    best_idx = summary_df["Average"].idxmax()
    weakest_idx = summary_df["Average"].idxmin()

    best_subject = summary_df.loc[best_idx, "Subject"]
    best_subject_avg = summary_df.loc[best_idx, "Average"]

    weakest_subject = summary_df.loc[weakest_idx, "Subject"]
    weakest_subject_avg = summary_df.loc[weakest_idx, "Average"]

    return {
        "summary_df": summary_df,
        "best_subject": best_subject,
        "best_subject_avg": best_subject_avg,
        "weakest_subject": weakest_subject,
        "weakest_subject_avg": weakest_subject_avg
    }


def get_top_performers(df, n=3):
    """
    Retrieve the top N students ranked by Average_Marks.

    Parameters:
        df (pd.DataFrame): DataFrame with Average_Marks column.
        n (int): Number of top performers to extract.

    Returns:
        pd.DataFrame: Sorted DataFrame of top N students with assigned ranks.
    """
    top_df = df.sort_values(by="Average_Marks", ascending=False).head(n).copy()
    top_df.reset_index(drop=True, inplace=True)
    top_df["Rank"] = range(1, len(top_df) + 1)
    return top_df


def generate_report(df, class_stats, subject_stats, top_performers, output_filepath):
    """
    Generate a formatted academic analysis report and save it to a text file.

    Parameters:
        df (pd.DataFrame): Processed student DataFrame.
        class_stats (dict): Class statistics dictionary.
        subject_stats (dict): Subject statistics dictionary.
        top_performers (pd.DataFrame): Top performing students.
        output_filepath (str): Target text file path.

    Returns:
        bool: True if file was saved successfully, False otherwise.
    """
    try:
        output_dir = os.path.dirname(output_filepath)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        lines = []
        lines.append("=" * 80)
        lines.append("           STUDENT PERFORMANCE ANALYTICS SYSTEM - ACADEMIC REPORT")
        lines.append("=" * 80)
        lines.append("")

        # 1. Dataset Information
        lines.append("1. DATASET INFORMATION")
        lines.append("-" * 80)
        lines.append(f"Total Student Records  : {class_stats['total_students']}")
        lines.append(f"Class-wide Marks Mean  : {class_stats['marks_overall_mean']}")
        lines.append(f"Marks Std. Deviation   : {class_stats['marks_std_dev']}")
        lines.append(f"Overall Highest Mark   : {class_stats['marks_overall_max']}")
        lines.append(f"Overall Lowest Mark    : {class_stats['marks_overall_min']}")
        lines.append("")

        # 2. Student Performance Table
        lines.append("2. STUDENT-WISE PERFORMANCE")
        lines.append("-" * 80)
        table_cols = ["Student_ID", "Name", "Total_Marks", "Average_Marks", "Grade", "Result", "Attendance_Status"]
        header_str = f"{'Student_ID':<12} {'Name':<22} {'Total':<8} {'Average':<10} {'Grade':<8} {'Result':<8} {'Attendance_Status'}"
        lines.append(header_str)
        lines.append("-" * 80)
        for _, row in df[table_cols].iterrows():
            lines.append(
                f"{row['Student_ID']:<12} {row['Name']:<22} {row['Total_Marks']:<8} "
                f"{row['Average_Marks']:<10.2f} {row['Grade']:<8} {row['Result']:<8} {row['Attendance_Status']}"
            )
        lines.append("")

        # 3. Class Performance Summary
        lines.append("3. CLASS PERFORMANCE SUMMARY")
        lines.append("-" * 80)
        lines.append(f"Overall Class Average  : {class_stats['overall_class_average']:.2f}")
        lines.append(f"Highest Average Score  : {class_stats['highest_average']:.2f}")
        lines.append(f"Lowest Average Score   : {class_stats['lowest_average']:.2f}")
        h_stu = class_stats['highest_student']
        l_stu = class_stats['lowest_student']
        lines.append(f"Highest Performer      : {h_stu['Name']} ({h_stu['Student_ID']}) - Avg: {h_stu['Average_Marks']} (Grade: {h_stu['Grade']})")
        lines.append(f"Lowest Performer       : {l_stu['Name']} ({l_stu['Student_ID']}) - Avg: {l_stu['Average_Marks']} (Grade: {l_stu['Grade']})")
        lines.append("")

        # 4. Subject-Wise Performance
        lines.append("4. SUBJECT-WISE PERFORMANCE")
        lines.append("-" * 80)
        sub_header = f"{'Subject':<18} {'Average':<10} {'Highest':<10} {'Lowest':<10} {'Passed':<8} {'Failed':<8}"
        lines.append(sub_header)
        lines.append("-" * 80)
        for _, sub_row in subject_stats["summary_df"].iterrows():
            lines.append(
                f"{sub_row['Subject']:<18} {sub_row['Average']:<10.2f} {sub_row['Highest']:<10} "
                f"{sub_row['Lowest']:<10} {sub_row['Passed']:<8} {sub_row['Failed']:<8}"
            )
        lines.append("-" * 80)
        lines.append(f"Best Performing Subject    : {subject_stats['best_subject']} (Average: {subject_stats['best_subject_avg']:.2f})")
        lines.append(f"Weakest Performing Subject : {subject_stats['weakest_subject']} (Average: {subject_stats['weakest_subject_avg']:.2f})")
        lines.append("")

        # 5. Top 3 Performers
        lines.append("5. TOP 3 PERFORMERS")
        lines.append("-" * 80)
        top_header = f"{'Rank':<6} {'Student Name':<24} {'Average Marks':<16} {'Grade':<8} {'Result'}"
        lines.append(top_header)
        lines.append("-" * 80)
        for _, t_row in top_performers.iterrows():
            lines.append(
                f"{t_row['Rank']:<6} {t_row['Name']:<24} {t_row['Average_Marks']:<16.2f} "
                f"{t_row['Grade']:<8} {t_row['Result']}"
            )
        lines.append("")

        # 6. Pass / Fail Analysis
        lines.append("6. PASS / FAIL ANALYSIS")
        lines.append("-" * 80)
        lines.append(f"Number of Passed Students  : {class_stats['passed_count']}")
        lines.append(f"Number of Failed Students  : {class_stats['failed_count']}")
        lines.append(f"Pass Percentage            : {class_stats['pass_percentage']:.2f}%")
        lines.append(f"Fail Percentage            : {class_stats['fail_percentage']:.2f}%")
        lines.append("")

        # 7. Attendance Analysis
        lines.append("7. ATTENDANCE ANALYSIS")
        lines.append("-" * 80)
        lines.append(f"Class Average Attendance   : {class_stats['average_attendance']:.2f}%")
        lines.append(f"Eligible (>= 75%) Count    : {class_stats['eligible_attendance_count']} students")
        lines.append(f"Short Attendance (< 75%)   : {class_stats['short_attendance_count']} students")
        lines.append("")

        # 8. Final Conclusion
        lines.append("8. FINAL CONCLUSION")
        lines.append("-" * 80)
        lines.append(f"- The batch has an overall academic average of {class_stats['overall_class_average']:.2f} marks.")
        lines.append(f"- {class_stats['pass_percentage']:.2f}% of students successfully passed all subjects and met the criteria.")
        lines.append(f"- Subject '{subject_stats['best_subject']}' exhibited the highest performance across the cohort.")
        lines.append(f"- Subject '{subject_stats['weakest_subject']}' showed lower averages, indicating area for academic support.")
        lines.append(f"- {class_stats['short_attendance_count']} student(s) require attendance counseling to meet institutional criteria.")
        lines.append("=" * 80)

        report_content = "\n".join(lines) + "\n"
        with open(output_filepath, "w", encoding="utf-8") as file:
            file.write(report_content)

        return True

    except Exception as err:
        print(f"Error while generating report file: {err}")
        return False
