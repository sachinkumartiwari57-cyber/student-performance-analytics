# Project Documentation: Student Performance Analytics System

---

## 1. Project Title
**Student Performance Analytics System**

---

## 2. Student Details
- **Name**: [Student Name]
- **Course**: [Course]
- **Branch**: [Branch]
- **Semester**: [Semester]
- **University**: [University]

---

## 3. Objective
The primary objective of this project is to develop an automated, reproducible, and robust academic data analysis system using Python, Pandas, and NumPy. The system processes raw student examination scores and attendance records, performs data validation, calculates academic metrics (total marks, average marks, letter grades, pass/fail status, and attendance eligibility), evaluates cohort-wide statistics, identifies top performers, and generates an exportable audit report.

---

## 4. Problem Statement
In traditional academic management, calculating student grades, evaluating subject-wise passing thresholds, tracking attendance shortfalls, and compiling cohort performance summaries is often conducted manually or through scattered spreadsheets. This introduces substantial risk of:
1. Human error in aggregate marks and percentage calculations.
2. Failure to strictly enforce multi-condition pass/fail rules (e.g., passing average but failing a specific subject).
3. Delays in identifying underperforming subjects and attendance defaulters.
4. Absence of standardized, exportable summary reports for faculty review.

This project delivers an automated, beginner-to-intermediate Python solution that standardizes academic evaluation.

---

## 5. Technologies Used
- **Python (v3.10+)**: Core programming environment.
- **Pandas (v3.0.6 / v2.0+)**: Data manipulation, CSV ingestion, tabular alignment, sorting, and projection.
- **NumPy (v2.5.3 / v1.24+)**: Matrix array computations, vector summation, standard deviation, mean, min/max, and boolean masking.
- **Python Standard Library (`os`, `sys`)**: Operating system file validation, directory management, and system termination.

---

## 6. Dataset Description
The dataset is stored in `students.csv` and contains 25 realistic student records across five academic disciplines.
- **Total Records**: 25 students.
- **Completeness**: No missing values, null values, or duplicate student identifiers.
- **Score Range**: Integer marks between 0 and 100 for each evaluated subject.
- **Attendance Range**: Numeric percentages between 0 and 100%.

### Dataset Schema
| Column | Type | Explanation |
| :--- | :--- | :--- |
| `Student_ID` | String | Unique student roll number / registration ID (STD1001 – STD1025) |
| `Name` | String | Candidate's full name |
| `Department` | String | Branch of study (CS, DS, IT, AIML, ECE) |
| `Python` | Numeric | Score in Python Programming (0–100) |
| `Mathematics` | Numeric | Score in Mathematics (0–100) |
| `Communication` | Numeric | Score in Professional Communication (0–100) |
| `Electronics` | Numeric | Score in Electronics (0–100) |
| `Data_Analysis` | Numeric | Score in Data Analysis (0–100) |
| `Attendance` | Numeric | Percentage of attended sessions (0–100%) |

---

## 7. Implementation
The system is implemented using a modular architecture consisting of:
1. **`students.csv`**: Source data file.
2. **`functions.py`**: Business logic, mathematical processing, data validation, and report writing.
3. **`main.py`**: Execution script coordinating data flow, user display, and export generation.
4. **`output/analysis_report.txt`**: Automatically generated file report.

---

## 8. Project Structure
```text
Student_Performance_Analytics/
│
├── main.py                     # Execution entry point
├── functions.py                # Reusable functions module
├── students.csv                # Student academic dataset
├── requirements.txt            # Package dependencies
├── README.md                   # Project overview and run guide
├── Project_Documentation.md    # Detailed academic documentation
│
└── output/
    └── analysis_report.txt     # Generated analysis report file
```

---

## 9. Python Concepts Used
- **Variables & Data Types**: String formatting, integer and float metrics, booleans, and dictionaries.
- **Collections**: Lists of subjects and records; dictionaries for statistical groupings.
- **Control Structures**: `if-elif-else` branching for grade boundaries, pass/fail status, and validation flags.
- **Iteration**: Meaningful `for` loops across subjects, DataFrame rows, and report sections.
- **Modular Programming**: Separation of concerns into independent functions with docstrings.
- **File Input / Output**: Reading CSV files and writing UTF-8 encoded text reports.
- **Defensive Programming**: Validating dataset boundaries, types, duplicates, and file existence.

---

## 10. NumPy Implementation
NumPy plays a central role in numerical processing:
1. **2D Matrix Conversion**:
   `marks_matrix = df[subject_columns].to_numpy()`
   Converts student marks to a contiguous numerical array.
2. **Vectorized Summation**:
   `total_marks = np.sum(marks_matrix, axis=1)`
   Computes individual student total marks across subjects in a single vectorized pass.
3. **Vectorized Mean Calculation**:
   `average_marks = np.mean(marks_matrix, axis=1)`
   Computes individual average marks.
4. **Cohort Statistics**:
   `np.mean()`, `np.max()`, `np.min()`, and `np.std()`
   Computes overall class mean, extremes, and marks standard deviation.
5. **Boolean Masking & Counting**:
   `np.count_nonzero(marks >= 40)` and `np.count_nonzero(attendance >= 75)`
   Computes passing students and attendance eligibility rapidly without manual counters.

---

## 11. Pandas Implementation
Pandas provides the foundational tabular infrastructure:
1. **Data Ingestion**: `pd.read_csv("students.csv")`.
2. **Column Validation**: Checking column presence and data types (`pd.api.types.is_numeric_dtype`).
3. **Duplicate Identification**: Detecting duplicate keys using `df["Student_ID"].duplicated()`.
4. **Data Augmentation**: Adding derived columns (`Total_Marks`, `Average_Marks`, `Grade`, `Result`, `Attendance_Status`).
5. **Ranking & Sorting**: `df.sort_values(by="Average_Marks", ascending=False).head(3)`.
6. **Summary Tables**: Creating structured tabular DataFrames for subject-wise analysis.

---

## 12. Functions Used

| Function Name | Location | Purpose |
| :--- | :--- | :--- |
| `load_data(filepath)` | `functions.py` | Safely reads CSV into a Pandas DataFrame with error checking. |
| `validate_data(df, subject_columns, min_records)` | `functions.py` | Performs structural, type, uniqueness, and boundary validation. |
| `calculate_total_marks(df, subject_columns)` | `functions.py` | Computes row-wise total marks using NumPy vectorized summation. |
| `calculate_average_marks(df, subject_columns)` | `functions.py` | Computes row-wise average marks rounded to 2 decimal places. |
| `assign_grade(average_mark)` | `functions.py` | Evaluates grade boundary ladder from A+ to F. |
| `calculate_result(average_mark, subject_marks)` | `functions.py` | Enforces two-tier pass rule (overall average and subject minimums). |
| `calculate_attendance_status(attendance)` | `functions.py` | Evaluates 75% institutional attendance threshold. |
| `add_performance_columns(df, subject_columns)` | `functions.py` | Enriches DataFrame with all derived analytical columns. |
| `get_class_statistics(df, subject_columns)` | `functions.py` | Calculates overall class metrics, dispersion, and pass/fail counts. |
| `get_subject_statistics(df, subject_columns)` | `functions.py` | Computes subject-wise mean, extremes, pass/fail, and best/weakest subjects. |
| `get_top_performers(df, n)` | `functions.py` | Extracts and ranks top N students by average marks. |
| `generate_report(...)` | `functions.py` | Formats and exports complete text report to disk. |
| `run_analytics_system(...)` | `main.py` | Coordinates end-to-end execution and prints formatted console output. |

---

## 13. Loops and Conditions

### Loops
- **Subject-Wise Analysis Loop**: Iterates through each subject (`for subject in subject_columns:`) to compute individual subject statistics (mean, highest mark, lowest mark, pass count, fail count).
- **Row-Wise Evaluation Loop**: Iterates through students (`for _, row in df.iterrows():`) to assign letter grades, verify individual subject marks, and determine attendance eligibility.
- **Output Formatting Loops**: Iterates over data rows to render tabular console text and write report lines.

### Conditions
- **Grading Scale Ladder**: Compares `average_mark` against thresholds [90, 80, 70, 60, 50, 40].
- **Pass/Fail Criteria**:
  ```python
  if average_mark < 40.0:
      return "FAIL"
  for mark in subject_marks_list:
      if mark < 40:
          return "FAIL"
  return "PASS"
  ```
- **Attendance Condition**:
  ```python
  if attendance >= 75.0:
      return "Eligible"
  else:
      return "Short Attendance"
  ```

---

## 14. Grading Logic
The academic grading scheme maps average percentage marks to standardized letter grades:

- **90% – 100%** $\rightarrow$ **A+** (Outstanding)
- **80% – 89%** $\rightarrow$ **A** (Excellent)
- **70% – 79%** $\rightarrow$ **B** (Very Good)
- **60% – 69%** $\rightarrow$ **C** (Good)
- **50% – 59%** $\rightarrow$ **D** (Satisfactory)
- **40% – 49%** $\rightarrow$ **E** (Pass)
- **Below 40%** $\rightarrow$ **F** (Fail)

---

## 15. Pass/Fail Logic
Academic regulations require complete competency across all registered subjects. Therefore, a student is declared **PASS** only if:
1. Their overall average marks are at least **40.0%**.
2. **AND** they have achieved at least **40 marks in every single subject**.

If a student scores less than 40 marks in any subject, they are awarded **FAIL** regardless of how high their average or total score is.

---

## 16. Attendance Logic
Class attendance is monitored independently of examination performance:
- **Attendance $\ge$ 75%**: Student is classified as **Eligible**.
- **Attendance < 75%**: Student is classified as **Short Attendance** and flagged for institutional counseling.

---

## 17. Data Analysis
The system computes the following analytical findings from `students.csv`:

1. **Cohort Size**: 25 evaluated students.
2. **Overall Class Average**: 69.47 marks.
3. **Highest Student Average**: 91.80% (Priya Patel, Divya Menon).
4. **Lowest Student Average**: 33.00% (Harsh Vardhan).
5. **Class-Wide Marks Spread**: Mean = 69.47, Standard Deviation = 18.09.
6. **Pass / Fail Breakdown**:
   - Passed: 21 students (84.00%)
   - Failed: 4 students (16.00%)
7. **Subject Performance**:
   - Best Subject: **Data_Analysis** (Class Average: 71.64, Highest: 96)
   - Weakest Subject: **Electronics** (Class Average: 65.64, Lowest: 28)
8. **Attendance Status**:
   - Class Average Attendance: 82.00%
   - Eligible (>= 75%): 20 students (80.00%)
   - Short Attendance (< 75%): 5 students (20.00%)

---

## 18. Key Features
- **Dynamic Subject Detection**: Automatically identifies academic subjects without hardcoding.
- **Comprehensive Data Validation**: Verifies record counts, duplicate IDs, types, and score bounds.
- **Accurate Business Logic**: Enforces multi-criteria pass/fail rules without bugs.
- **Clear Console Dashboard**: Divides results into 8 well-organized visual sections.
- **Exportable Audit Report**: Creates an automatic, human-readable text report at `output/analysis_report.txt`.
- **Zero Heavy Dependencies**: Lightweight, beginner-friendly, requiring only Pandas and NumPy.

---

## 19. Output / Results

### Console Execution Output
```text
================================================================================
                     STUDENT PERFORMANCE ANALYTICS SYSTEM
================================================================================

[INFO] Loading dataset from: students.csv

================================================================================
1. DATASET INFORMATION
--------------------------------------------------------------------------------
Total Student Records  : 25
Total Columns          : 9
Columns in Dataset     : ['Student_ID', 'Name', 'Department', 'Python', 'Mathematics', 'Communication', 'Electronics', 'Data_Analysis', 'Attendance']
Identified Subjects    : ['Python', 'Mathematics', 'Communication', 'Electronics', 'Data_Analysis']
Missing Values         : None detected (Clean Dataset)

================================================================================
2. STUDENT PERFORMANCE
--------------------------------------------------------------------------------
Student_ID   Name                   Total    Average    Grade    Result   Attendance_Status
--------------------------------------------------------------------------------
STD1001      Aarav Sharma           455      91.00      A+       PASS     Eligible
STD1002      Priya Patel            459      91.80      A+       PASS     Eligible
STD1003      Rohan Mehta            385      77.00      B        PASS     Eligible
STD1004      Ananya Verma           435      87.00      A        PASS     Eligible
STD1005      Vikram Singh           309      61.80      C        PASS     Eligible
STD1006      Sneha Rao              403      80.60      A        PASS     Eligible
STD1007      Rahul Nair             231      46.20      E        PASS     Short Attendance
STD1008      Neha Gupta             450      90.00      A+       PASS     Eligible
STD1009      Aditya Joshi           293      58.60      D        PASS     Eligible
STD1010      Pooja Kulkarni         370      74.00      B        PASS     Eligible
STD1011      Devendra Kumar         270      54.00      D        FAIL     Short Attendance
STD1012      Kavita Iyer            411      82.20      A        PASS     Eligible
STD1013      Arjun Reddy            350      70.00      B        PASS     Eligible
STD1014      Tanvi Deshmukh         260      52.00      D        PASS     Eligible
STD1015      Sameer Khan            190      38.00      F        FAIL     Short Attendance
STD1016      Ritu Choudhary         370      74.00      B        PASS     Eligible
STD1017      Manav Bansal           427      85.40      A        PASS     Eligible
STD1018      Ishita Sen             349      69.80      C        PASS     Eligible
STD1019      Kunal Kapoor           210      42.00      E        PASS     Short Attendance
STD1020      Divya Menon            459      91.80      A+       PASS     Eligible
STD1021      Siddharth Malhotra     257      51.40      D        FAIL     Eligible
STD1022      Riya Sen               396      79.20      B        PASS     Eligible
STD1023      Harsh Vardhan          165      33.00      F        FAIL     Short Attendance
STD1024      Shalini Mishra         425      85.00      A        PASS     Eligible
STD1025      Varun Bhatt            355      71.00      B        PASS     Eligible

================================================================================
3. CLASS PERFORMANCE SUMMARY
--------------------------------------------------------------------------------
Overall Class Average  : 69.47
Highest Average Mark   : 91.80
Lowest Average Mark    : 33.00
Class-wide Marks Mean  : 69.47
Marks Std. Deviation   : 18.09
Highest Performer      : Priya Patel (STD1002) - 91.8% [Grade: A+]
Lowest Performer       : Harsh Vardhan (STD1023) - 33.0% [Grade: F]

================================================================================
4. SUBJECT-WISE PERFORMANCE
--------------------------------------------------------------------------------
Subject            Average    Highest    Lowest     Passed   Failed  
--------------------------------------------------------------------------------
Python             70.80      95         35         23       2       
Mathematics        67.72      94         30         22       3       
Communication      71.56      94         38         24       1       
Electronics        65.64      90         28         22       3       
Data_Analysis      71.64      96         34         24       1       
--------------------------------------------------------------------------------
Best Performing Subject    : Data_Analysis (Average: 71.64)
Weakest Performing Subject : Electronics (Average: 65.64)

================================================================================
5. TOP 3 PERFORMERS
--------------------------------------------------------------------------------
Rank   Student Name             Average Marks    Grade    Result
--------------------------------------------------------------------------------
1      Priya Patel              91.80            A+       PASS
2      Divya Menon              91.80            A+       PASS
3      Aarav Sharma             91.00            A+       PASS

================================================================================
6. PASS/FAIL ANALYSIS
--------------------------------------------------------------------------------
Total Students Evaluated   : 25
Number of Passed Students  : 21
Number of Failed Students  : 4
Pass Percentage            : 84.00%
Fail Percentage            : 16.00%

================================================================================
7. ATTENDANCE ANALYSIS
--------------------------------------------------------------------------------
Class Average Attendance   : 82.00%
Eligible Attendance (>= 75%): 20 students
Short Attendance (< 75%)   : 5 students

================================================================================
8. FINAL CONCLUSION
--------------------------------------------------------------------------------
- The cohort demonstrated a solid academic average of 69.47 marks.
- 84.00% of students satisfied all pass criteria (>=40 marks in every subject and overall).
- The leading subject was 'Data_Analysis' with an average score of 71.64.
- The subject 'Electronics' had the lowest average (65.64), requiring extra tutorials.
- 5 students have Short Attendance (<75%) and need remedial attendance notice.
================================================================================

[SUCCESS] Detailed analysis report saved to: 'output/analysis_report.txt'
```

---

## 20. Final Outcome
The project successfully delivers an automated system capable of loading any compliant student marks CSV, running data validation, computing individual and aggregate performance metrics, and creating an academic audit report. The solution adheres strictly to foundational Python concepts, making it ideal for academic submission and viva presentations.

---

## 21. Challenges Faced
1. **Handling Subject Failure Edge Cases**: A student may achieve a satisfactory overall average (e.g., > 50%) but still score below 40 in one subject.
2. **Preventing Attendance Contamination**: Ensuring attendance percentage is strictly isolated from academic mark sums.
3. **Data Integrity Verification**: Ensuring the system catches missing values, negative scores, or scores over 100 gracefully.
4. **Terminal Character Encoding**: Ensuring formatting characters render cleanly across all terminal environments.

---

## 22. Solutions
1. Developed `calculate_result()` which combines `average_mark >= 40.0` with an iterative verification ensuring every individual subject score $\ge 40$.
2. Separated metadata columns from subject columns dynamically, ensuring summation operates only on validated subject columns.
3. Built `validate_data()` to inspect schema, row count, uniqueness, and value boundaries before mathematical execution begins.
4. Adopted standard ASCII character formatting for all console tables and reports.

---

## 23. Learning Outcomes
- Acquired proficiency in organizing a real-world Python project with separation of concerns.
- Mastered the complementary roles of Pandas (tabular management) and NumPy (fast vectorized math).
- Developed defensive coding patterns for dataset validation.
- Gained experience generating automated, professional documentation and text-based reports.

---

## 24. Future Scope
- **Interactive Graphical Interface**: Integrating Tkinter, PyQt, or Streamlit for graphical CSV selection and interactive dashboards.
- **Visual Analytics**: Generating automated distribution charts and grade pie charts using Matplotlib.
- **Database Integration**: Connecting to SQLite or PostgreSQL for multi-term historical tracking.
- **Automated Grade Card Generation**: Generating individual student PDF report cards.

---

## 25. GitHub Repository
[To be added after GitHub upload]
