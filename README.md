# Student Performance Analytics System

A Python-based academic data analysis system designed to evaluate, summarize, and report student academic performance and attendance records using Pandas, NumPy, and core Python programming constructs.

---

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Project Objective](#2-project-objective)
3. [Problem Statement](#3-problem-statement)
4. [Technologies Used](#4-technologies-used)
5. [Python Concepts Used](#5-python-concepts-used)
6. [Project Structure](#6-project-structure)
7. [Dataset Description](#7-dataset-description)
8. [Dataset Columns](#8-dataset-columns)
9. [Grading System](#9-grading-system)
10. [Pass/Fail Logic](#10-passfail-logic)
11. [Attendance Logic](#11-attendance-logic)
12. [How the Program Works](#12-how-the-program-works)
13. [Step-by-Step Code Logic](#13-step-by-step-code-logic)
14. [Role of Pandas](#14-role-of-pandas)
15. [Role of NumPy](#15-role-of-numpy)
16. [Role of Functions](#16-role-of-functions)
17. [Role of Loops](#17-role-of-loops)
18. [Analysis Performed](#18-analysis-performed)
19. [Output Generated](#19-output-generated)
20. [How to Install Requirements](#20-how-to-install-requirements)
21. [How to Run the Project](#21-how-to-run-the-project)
22. [Example Commands](#22-example-commands)
23. [Expected Output](#23-expected-output)
24. [Important Findings](#24-important-findings)
25. [Learning Outcomes](#25-learning-outcomes)
26. [Challenges and Solutions](#26-challenges-and-solutions)
27. [Future Improvements](#27-future-improvements)
28. [GitHub Repository](#28-github-repository)

---

## 1. Project Overview
The **Student Performance Analytics System** is an educational, reproducible data analysis tool developed for academic evaluation. It reads raw student examination marks and attendance metrics from a CSV file, performs data validation, calculates aggregate statistics, assigns letter grades, evaluates pass/fail status, detects top performers, and generates a structured summary report both on the terminal console and as an exported text file.

---

## 2. Project Objective
- To automate student grade computation and performance analysis using Python.
- To demonstrate practical applications of NumPy and Pandas for data manipulation.
- To implement clean, modular, and reusable Python functions.
- To provide academic mentors and institutions with immediate insights into class performance, subject difficulty, and attendance eligibility.

---

## 3. Problem Statement
Educational institutions often handle student records across multiple subjects manually or using fragmented spreadsheets. This leads to:
- Calculation errors in total marks and percentage averages.
- Inconsistent grade allocation.
- Inability to quickly identify struggling students or subjects requiring pedagogical intervention.
- Difficulties tracking students with short attendance.

This project solves these issues by providing a deterministic, automated, and easy-to-explain analytics pipeline.

---

## 4. Technologies Used
- **Python 3.x**: Primary programming language.
- **Pandas**: High-performance DataFrame library for CSV ingestion, table manipulation, filtering, and sorting.
- **NumPy**: Numerical computation library for multidimensional array calculations, statistics (mean, std, min, max), and boolean masking.
- **Standard Library (`os`, `sys`)**: File path resolution, directory creation, and clean exit handling.

---

## 5. Python Concepts Used
- **Variables & Data Types**: Strings, integers, floating-point numbers, lists, dictionaries, tuples, and booleans.
- **Conditional Statements (`if-elif-else`)**: Grading boundaries, pass/fail evaluation, and attendance checks.
- **Loops (`for` loops & iteration)**: Row-wise student evaluations, subject-wise statistics processing, and formatted table printing.
- **Functions & Modularity**: Separation of concerns into reusable functions with parameter passing and return values.
- **File I/O**: Reading CSV datasets and writing generated analysis reports to disk.
- **Error Handling**: Graceful error messages on missing files, improper data, and invalid schema.

---

## 6. Project Structure

```text
Student_Performance_Analytics/
│
├── main.py                     # Entry point orchestrating the analytics pipeline
├── functions.py                # Reusable analytical functions and business logic
├── students.csv                # Primary dataset containing 25 student records
├── requirements.txt            # Minimal required dependencies (pandas, numpy)
├── README.md                   # Comprehensive project documentation and usage guide
├── Project_Documentation.md    # Detailed academic submission report
│
└── output/
    └── analysis_report.txt     # Generated text report exported after analysis
```

---

## 7. Dataset Description
The dataset (`students.csv`) contains **25 realistic student records** across diverse academic departments (Computer Science, Data Science, AI & Machine Learning, Information Technology, Electronics & Communication). It has:
- Zero missing values.
- Unique Student IDs (`STD1001` through `STD1025`).
- Numeric scores between 0 and 100 for all subjects.
- Numeric attendance percentages between 0 and 100.
- Realistic score variance to test high performers, regular passing students, borderline cases, and failing conditions.

---

## 8. Dataset Columns

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `Student_ID` | String | Unique identifier for each student (e.g., STD1001) |
| `Name` | String | Full student name |
| `Department` | String | Academic department/branch |
| `Python` | Integer | Marks obtained in Python (0–100) |
| `Mathematics` | Integer | Marks obtained in Mathematics (0–100) |
| `Communication` | Integer | Marks obtained in Communication (0–100) |
| `Electronics` | Integer | Marks obtained in Electronics (0–100) |
| `Data_Analysis` | Integer | Marks obtained in Data Analysis (0–100) |
| `Attendance` | Integer | Class attendance percentage (0–100%) |

---

## 9. Grading System
The grading logic classifies a student based on their calculated **Average Marks**:

| Average Marks Range | Grade | Performance Description |
| :---: | :---: | :--- |
| **90 – 100** | **A+** | Outstanding |
| **80 – 89** | **A** | Excellent |
| **70 – 79** | **B** | Very Good |
| **60 – 69** | **C** | Good |
| **50 – 59** | **D** | Satisfactory |
| **40 – 49** | **E** | Pass / Marginal |
| **Below 40** | **F** | Fail |

---

## 10. Pass/Fail Logic
A student is awarded a status of **PASS** if and only if both conditions are met:
1. **Average Marks $\ge$ 40.0**
2. **Every individual subject mark $\ge$ 40**

If a student scores below 40 marks in even one subject, their status is set to **FAIL**, regardless of how high their average marks may be.

---

## 11. Attendance Logic
Institutional eligibility is calculated independently of marks:
- **Attendance $\ge$ 75%** $\rightarrow$ **Eligible**
- **Attendance < 75%** $\rightarrow$ **Short Attendance** (Requires attendance counseling/advisory notice)

---

## 12. How the Program Works
1. When `main.py` is executed, it loads `students.csv` using the `load_data()` function.
2. The `validate_data()` function ensures the schema is intact, no duplicate IDs exist, marks are within valid ranges, and at least 20 records exist.
3. Subject columns are dynamically detected from non-metadata fields.
4. Total marks, average marks, letter grades, pass/fail status, and attendance statuses are computed and appended to the DataFrame.
5. NumPy is utilized to compute class-wide aggregate metrics (overall mean, standard deviation, max, min).
6. Subject-level statistics are calculated to determine the best-performing and weakest-performing subjects.
7. Top 3 students by average marks are ranked.
8. The console displays 8 organized analytical sections.
9. An export report is generated and saved to `output/analysis_report.txt`.

---

## 13. Step-by-Step Code Logic

### Step 1: Load Dataset (`load_data`)
- **Action**: Reads `students.csv` into a Pandas DataFrame using `pd.read_csv()`.
- **Why Required**: Loads raw tabular data from secondary storage into memory for analytical manipulation.

### Step 2: Validate Dataset (`validate_data`)
- **Action**: Verifies file existence, minimum row count (>= 20), column presence, absence of duplicate IDs, numeric types, and 0–100 boundary ranges.
- **Why Required**: Prevents runtime errors, crashes, or skewed mathematical computations caused by corrupted input.

### Step 3: Identify Subject Columns
- **Action**: Dynamically filters columns that are not student metadata (`Student_ID`, `Name`, `Department`, `Attendance`).
- **Why Required**: Allows the system to scale and adapt to different subject lists without hardcoding subject names in calculations.

### Step 4: Calculate Total Marks (`calculate_total_marks`)
- **Action**: Converts subject marks to a 2D NumPy array and applies row-wise summation (`np.sum(axis=1)`).
- **Why Required**: Attendance must not be added to examination marks; NumPy ensures vectorized addition.

### Step 5: Calculate Average Marks (`calculate_average_marks`)
- **Action**: Computes row-wise mean using `np.mean(axis=1)` and rounds to 2 decimal places.
- **Why Required**: Serves as the core normalized metric for assigning letter grades and ranking students.

### Step 6: Assign Letter Grades (`assign_grade`)
- **Action**: Evaluates average marks through a deterministic `if-elif-else` ladder matching institutional grading bands (A+ to F).
- **Why Required**: Provides standard categorical classification for report cards.

### Step 7: Check Pass/Fail Status (`calculate_result`)
- **Action**: Verifies that the student's average is >= 40 and that every individual subject mark is >= 40.
- **Why Required**: Enforces academic rigor where no student can clear an academic semester if they have failed any subject.

### Step 8: Check Attendance Eligibility (`calculate_attendance_status`)
- **Action**: Checks if attendance percentage is >= 75%.
- **Why Required**: Tracks institutional compliance separate from exam grades.

### Step 9: Perform Class-Level Analysis (`get_class_statistics`)
- **Action**: Computes class average, highest/lowest scores, pass count, fail count, pass percentage, fail percentage, and marks standard deviation using NumPy.
- **Why Required**: Gives faculty a high-level overview of batch performance and dispersion.

### Step 10: Perform Subject-Wise Analysis (`get_subject_statistics`)
- **Action**: Iterates over each subject with a `for` loop to compute mean, maximum, minimum, pass count, and fail count.
- **Why Required**: Pinpoints specific curriculum areas where students excel or need remedial support.

### Step 11: Identify Top 3 Performers (`get_top_performers`)
- **Action**: Sorts DataFrame descending by `Average_Marks` using Pandas `.sort_values()` and selects the top 3.
- **Why Required**: Identifies merit students for academic honors and scholarships.

### Step 12: Print Final Results to Console
- **Action**: Formats all sections into clean, readable terminal tables with clear section headers.
- **Why Required**: Delivers immediate, readable feedback to the user without inspecting code or raw data.

### Step 13: Save Analysis Report (`generate_report`)
- **Action**: Writes the formatted analysis to `output/analysis_report.txt`.
- **Why Required**: Creates a permanent, exportable academic audit record for archiving.

---

## 14. Role of Pandas
Pandas is central to managing tabular data:
- **`pd.read_csv()`**: Fast and structured CSV ingestion.
- **`df[columns]`**: Column slicing and projection.
- **`df.sort_values(by="Average_Marks", ascending=False)`**: High-speed sorting of student records.
- **`df.copy()`**: Safe non-destructive DataFrame operations.
- **Column Assignment**: Adding `Total_Marks`, `Average_Marks`, `Grade`, `Result`, and `Attendance_Status`.
- **`df.iterrows()`**: Clean iteration over rows when creating tabular reports.

---

## 15. Role of NumPy
NumPy is used meaningfully for numerical computing:
- **`df[subject_columns].to_numpy()`**: Converts tabular slices into high-performance 2D numeric matrices.
- **`np.sum(matrix, axis=1)`**: Computes row-wise total marks across subjects.
- **`np.mean(matrix, axis=1)` / `np.mean(array)`**: Computes student averages, class averages, and subject averages.
- **`np.max(array)` & `np.min(array)`**: Finds highest and lowest marks in arrays.
- **`np.std(matrix)`**: Computes class-wide marks standard deviation to measure score spread.
- **`np.count_nonzero(condition)`**: Vectorized counting of passing and failing students.
- **`np.round()`**: Precision rounding for statistics.

---

## 16. Role of Functions
Modular design keeps code clean and testable:
- `load_data(filepath)`: Isolates dataset loading and file validation.
- `validate_data(df, subject_columns)`: Centralizes data sanity checks.
- `calculate_total_marks(df, subject_columns)`: Reusable total marks calculation.
- `calculate_average_marks(df, subject_columns)`: Reusable average marks calculation.
- `assign_grade(average_mark)`: Pure function mapping average mark to letter grade.
- `calculate_result(average_mark, subject_marks)`: Enforces pass/fail criteria.
- `calculate_attendance_status(attendance)`: Maps attendance percentage to status.
- `add_performance_columns(df, subject_columns)`: Enriches DataFrame with derived metrics.
- `get_class_statistics(df, subject_columns)`: Gathers overall batch statistics.
- `get_subject_statistics(df, subject_columns)`: Computes subject-specific metrics.
- `get_top_performers(df, n=3)`: Extracts ranked top performers.
- `generate_report(df, class_stats, subject_stats, top_performers, output_filepath)`: Formats and exports report.

---

## 17. Role of Loops
Loops are used where iteration is meaningful:
- **Subject Iteration**: A `for subject in subject_columns:` loop computes individual statistics (mean, min, max, pass/fail) for each subject dynamically.
- **Student Performance Mapping**: Iterates through rows to evaluate multi-condition pass/fail status and assign grades.
- **Table Printing & File Generation**: Iterates through records to render aligned, formatted tables for both terminal and file export.

---

## 18. Analysis Performed
1. Total student count.
2. Overall class average across all students.
3. Highest and lowest average marks in the class.
4. Student-wise total marks, average marks, grade, and pass/fail result.
5. Subject-wise average, highest mark, lowest mark, pass count, and fail count.
6. Identification of the best-performing and weakest-performing subjects.
7. Top 3 ranked performers with average marks and grades.
8. Class pass count, fail count, pass percentage, and fail percentage.
9. Attendance analysis: average attendance, eligible count (>=75%), and short attendance count (<75%).
10. Marks standard deviation measuring score dispersion.

---

## 19. Output Generated
1. **Console Output**: Terminal display divided into 8 numbered sections with formatted tables.
2. **Text File Export**: Exported report file at `output/analysis_report.txt` containing complete academic findings.

---

## 20. How to Install Requirements
Ensure Python 3.10+ is installed. Install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 21. How to Run the Project
Navigate to the project root directory and execute `main.py`:

```bash
python main.py
```

---

## 22. Example Commands

```bash
# Check Python installation
python --version

# Install dependencies
pip install -r requirements.txt

# Run the complete analysis system
python main.py

# View the generated report in Windows PowerShell
Get-Content output/analysis_report.txt

# Or view in command prompt
type output\analysis_report.txt
```

---

## 23. Expected Output

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
...
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

## 24. Important Findings
- **High Overall Success**: 84.00% of students passed the semester.
- **Top Performers**: Priya Patel and Divya Menon both achieved the highest average of 91.80% (Grade A+).
- **Strongest Subject**: `Data_Analysis` demonstrated the highest class average (71.64).
- **Subject Needing Attention**: `Electronics` had the lowest average (65.64) and lowest individual score (28), indicating a need for tutorial review.
- **Subject-Failure Rule Impact**: Students like Devendra Kumar (average 54.00%) and Siddharth Malhotra (average 51.40%) failed the semester because they scored under 40 marks in a specific subject (Mathematics and Electronics, respectively).
- **Attendance Concerns**: 5 students recorded attendance below 75%, requiring administrative advisory notices.

---

## 25. Learning Outcomes
- Gained hands-on experience in structuring an end-to-end Python data analysis project.
- Learned to use Pandas for DataFrame transformations, sorting, and tabular data handling.
- Mastered NumPy operations for vectorized operations, multi-dimensional array math, and statistics.
- Learned proper defensive programming: file validation, boundary checks, and informative error handling.
- Understood clean separation of concerns by isolating reusable functions from main execution scripts.

---

## 26. Challenges and Solutions
| Challenge | Solution |
| :--- | :--- |
| Enforcing strict pass rule (both average >= 40 and all individual subjects >= 40). | Implemented `calculate_result()` that checks both the average threshold and iterates across all subject scores. |
| Avoiding accidental addition of attendance into total marks. | Dynamically isolated `subject_columns` from non-subject metadata before matrix summation. |
| Cross-platform console formatting on Windows. | Replaced non-ASCII bullet characters with standard ASCII hyphens to ensure clean rendering. |
| Generating permanent export without hardcoding output values. | Implemented `generate_report()` which writes dynamically computed metrics into `output/analysis_report.txt`. |

---

## 27. Future Improvements
- **Data Visualization**: Adding Matplotlib/Seaborn bar charts and histograms for grade distribution.
- **Interactive CLI / GUI**: Building an interactive menu or Streamlit web interface for custom queries.
- **Multi-Semester Analysis**: Expanding data schema to track student performance across multiple terms.
- **Automated PDF Export**: Generating styled PDF report cards with institutional letterhead.

---


