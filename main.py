"""
main.py
=======
Student Performance Analytics System
------------------------------------
Main execution script and entry point.
Coordinates data loading, validation, analytical computations,
console reporting, and report export.
"""

import os
import sys
from functions import (
    load_data,
    validate_data,
    add_performance_columns,
    get_class_statistics,
    get_subject_statistics,
    get_top_performers,
    generate_report,
)


def run_analytics_system(csv_path="students.csv", output_report_path="output/analysis_report.txt"):
    """
    Execute the end-to-end Student Performance Analytics workflow.

    Parameters:
        csv_path (str): Path to input CSV data file.
        output_report_path (str): Path to target output report text file.
    """
    print("\n" + "=" * 80)
    print("                     STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 80)

    # 1. Load Dataset
    print("\n[INFO] Loading dataset from:", csv_path)
    df = load_data(csv_path)
    if df is None:
        print("[ERROR] Failed to load data. Exiting system.")
        sys.exit(1)

    # Automatically identify subject columns (non-metadata columns)
    metadata_columns = {"Student_ID", "Name", "Department", "Attendance"}
    subject_columns = [col for col in df.columns if col not in metadata_columns]

    # 2. Validate Dataset
    is_valid, validation_msg = validate_data(df, subject_columns, min_records=20)
    if not is_valid:
        print(f"[ERROR] Validation failed: {validation_msg}")
        sys.exit(1)

    # 3. Process Student Performance (Add analytical columns)
    processed_df = add_performance_columns(df, subject_columns)

    # 4. Compute Statistical Summaries
    class_stats = get_class_statistics(processed_df, subject_columns)
    subject_stats = get_subject_statistics(processed_df, subject_columns)
    top_performers = get_top_performers(processed_df, n=3)

    # =========================================================================
    # DISPLAY FORMATTED CONSOLE OUTPUT
    # =========================================================================

    # 1. DATASET INFORMATION
    print("\n" + "=" * 80)
    print("1. DATASET INFORMATION")
    print("-" * 80)
    print(f"Total Student Records  : {len(df)}")
    print(f"Total Columns          : {len(df.columns)}")
    print(f"Columns in Dataset     : {list(df.columns)}")
    print(f"Identified Subjects    : {subject_columns}")
    print(f"Missing Values         : None detected (Clean Dataset)")

    # 2. STUDENT PERFORMANCE
    print("\n" + "=" * 80)
    print("2. STUDENT PERFORMANCE")
    print("-" * 80)
    display_cols = ["Student_ID", "Name", "Total_Marks", "Average_Marks", "Grade", "Result", "Attendance_Status"]
    header = f"{'Student_ID':<12} {'Name':<22} {'Total':<8} {'Average':<10} {'Grade':<8} {'Result':<8} {'Attendance_Status'}"
    print(header)
    print("-" * 80)
    for _, row in processed_df[display_cols].iterrows():
        print(
            f"{row['Student_ID']:<12} {row['Name']:<22} {row['Total_Marks']:<8} "
            f"{row['Average_Marks']:<10.2f} {row['Grade']:<8} {row['Result']:<8} {row['Attendance_Status']}"
        )

    # 3. CLASS PERFORMANCE SUMMARY
    print("\n" + "=" * 80)
    print("3. CLASS PERFORMANCE SUMMARY")
    print("-" * 80)
    print(f"Overall Class Average  : {class_stats['overall_class_average']:.2f}")
    print(f"Highest Average Mark   : {class_stats['highest_average']:.2f}")
    print(f"Lowest Average Mark    : {class_stats['lowest_average']:.2f}")
    print(f"Class-wide Marks Mean  : {class_stats['marks_overall_mean']:.2f}")
    print(f"Marks Std. Deviation   : {class_stats['marks_std_dev']:.2f}")
    h_student = class_stats['highest_student']
    l_student = class_stats['lowest_student']
    print(f"Highest Performer      : {h_student['Name']} ({h_student['Student_ID']}) - {h_student['Average_Marks']}% [Grade: {h_student['Grade']}]")
    print(f"Lowest Performer       : {l_student['Name']} ({l_student['Student_ID']}) - {l_student['Average_Marks']}% [Grade: {l_student['Grade']}]")

    # 4. SUBJECT-WISE PERFORMANCE
    print("\n" + "=" * 80)
    print("4. SUBJECT-WISE PERFORMANCE")
    print("-" * 80)
    sub_header = f"{'Subject':<18} {'Average':<10} {'Highest':<10} {'Lowest':<10} {'Passed':<8} {'Failed':<8}"
    print(sub_header)
    print("-" * 80)
    for _, sub_row in subject_stats["summary_df"].iterrows():
        print(
            f"{sub_row['Subject']:<18} {sub_row['Average']:<10.2f} {sub_row['Highest']:<10} "
            f"{sub_row['Lowest']:<10} {sub_row['Passed']:<8} {sub_row['Failed']:<8}"
        )
    print("-" * 80)
    print(f"Best Performing Subject    : {subject_stats['best_subject']} (Average: {subject_stats['best_subject_avg']:.2f})")
    print(f"Weakest Performing Subject : {subject_stats['weakest_subject']} (Average: {subject_stats['weakest_subject_avg']:.2f})")

    # 5. TOP 3 PERFORMERS
    print("\n" + "=" * 80)
    print("5. TOP 3 PERFORMERS")
    print("-" * 80)
    top_header = f"{'Rank':<6} {'Student Name':<24} {'Average Marks':<16} {'Grade':<8} {'Result'}"
    print(top_header)
    print("-" * 80)
    for _, t_row in top_performers.iterrows():
        print(
            f"{t_row['Rank']:<6} {t_row['Name']:<24} {t_row['Average_Marks']:<16.2f} "
            f"{t_row['Grade']:<8} {t_row['Result']}"
        )

    # 6. PASS/FAIL ANALYSIS
    print("\n" + "=" * 80)
    print("6. PASS/FAIL ANALYSIS")
    print("-" * 80)
    print(f"Total Students Evaluated   : {class_stats['total_students']}")
    print(f"Number of Passed Students  : {class_stats['passed_count']}")
    print(f"Number of Failed Students  : {class_stats['failed_count']}")
    print(f"Pass Percentage            : {class_stats['pass_percentage']:.2f}%")
    print(f"Fail Percentage            : {class_stats['fail_percentage']:.2f}%")

    # 7. ATTENDANCE ANALYSIS
    print("\n" + "=" * 80)
    print("7. ATTENDANCE ANALYSIS")
    print("-" * 80)
    print(f"Class Average Attendance   : {class_stats['average_attendance']:.2f}%")
    print(f"Eligible Attendance (>= 75%): {class_stats['eligible_attendance_count']} students")
    print(f"Short Attendance (< 75%)   : {class_stats['short_attendance_count']} students")

    # 8. FINAL CONCLUSION
    print("\n" + "=" * 80)
    print("8. FINAL CONCLUSION")
    print("-" * 80)
    print(f"- The cohort demonstrated a solid academic average of {class_stats['overall_class_average']:.2f} marks.")
    print(f"- {class_stats['pass_percentage']:.2f}% of students satisfied all pass criteria (>=40 marks in every subject and overall).")
    print(f"- The leading subject was '{subject_stats['best_subject']}' with an average score of {subject_stats['best_subject_avg']:.2f}.")
    print(f"- The subject '{subject_stats['weakest_subject']}' had the lowest average ({subject_stats['weakest_subject_avg']:.2f}), requiring extra tutorials.")
    print(f"- {class_stats['short_attendance_count']} students have Short Attendance (<75%) and need remedial attendance notice.")
    print("=" * 80)

    # 9. Generate Report File
    report_saved = generate_report(processed_df, class_stats, subject_stats, top_performers, output_report_path)
    if report_saved:
        print(f"\n[SUCCESS] Detailed analysis report saved to: '{output_report_path}'")
    else:
        print(f"\n[WARNING] Could not save analysis report to: '{output_report_path}'")

    print("\n" + "=" * 80)
    print("               ANALYSIS EXECUTION SUCCESSFULLY COMPLETED")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    run_analytics_system()
