# Student-Management-System-with-Custom-Exceptions
Python OOPs based Student Management System with custom exceptions, file handling, and class performance analysis




# Student Management System (Python OOPs)

A Python project demonstrating **Object-Oriented Programming (OOPs)** concepts with custom exceptions, file handling, and student data analysis.

---

## 🚀 Features
- Custom Exceptions:
  - `StudentsNotFoundError`
  - `MarksError`
  - `SubjectMissing`
  - `LoadData`
- Classes:
  - `Person`
  - `Student`
  - `Teacher`
  - `SchoolManager`
- Student operations:
  - Add / Update / Delete student
  - Add new subject and update marks
  - Calculate total marks, percentage, and grade
- Teacher info management
- Save & Load student data using CSV
- Analyze class performance (average, highest, lowest marks, subject coverage)

---

## 🛠️ Technologies Used
- Python 3.x
- OOPs concepts (Encapsulation, Inheritance, Polymorphism, Abstraction)
- File Handling (CSV, TXT)

## 📂 Project Structure
├── student_manager.py         # Main project file
├── student.csv                # Sample student data (CSV) 
└── README.md                  # Documentation



---

## 📊 Sample Data
```python
student_lists = [
    {"ROLL_NO": 1, "NAME": "Ali", "MARKS": {"Math": 95, "Science": 80}},
    {"ROLL_NO": 2, "NAME": "Sara", "MARKS": {"Math": 70, "English": 85}},
    {"ROLL_NO": 3, "NAME": "John", "MARKS": {"Science": 60, "History": 75}},
    {"ROLL_NO": 4, "NAME": "Aman", "MARKS": {"Math": 40, "Science": 30, "English": 50 , "Python": 45}}
]

## 📈 Example Output

```text
Loaded Students: [{'ROLL_NO': 1, 'NAME': 'Ali', 'MARKS': {'Math': 95, 'Science': 80}}, 
                  {'ROLL_NO': 2, 'NAME': 'Sara', 'MARKS': {'Math': 70, 'English': 85}}, 
                  {'ROLL_NO': 3, 'NAME': 'John', 'MARKS': {'Science': 60, 'History': 75}}, 
                  {'ROLL_NO': 4, 'NAME': 'Aman', 'MARKS': {'Math': 40, 'Science': 30, 'English': 50, 'Python': 45}}]
============================================================
TOTAL STUDENT IS --> 4
SUBJECT COVERAGE --> {'Math': 3, 'Science': 3, 'English': 2, 'History': 1, 'Python': 1}
STUDENT ANALYZES DATA --> [
    {'ROLL_NO': 1, 'TOTAL MARKS': 175, 'PERCENTAGE': 87.5, 'GRADE': 'A'},
    {'ROLL_NO': 2, 'TOTAL MARKS': 155, 'PERCENTAGE': 77.5, 'GRADE': 'B'},
    {'ROLL_NO': 3, 'TOTAL MARKS': 135, 'PERCENTAGE': 67.5, 'GRADE': 'B'},
    {'ROLL_NO': 4, 'TOTAL MARKS': 165, 'PERCENTAGE': 55.0, 'GRADE': 'C'}
]
CLASS DATA --> {
    'AVG MARKS FOR ALL CLASS': 157.5,
    'HIGHEST MARKS FOR ALL CLASS IS': 175,
    'LOWEST MARKS FOR ALL CLASS IS ': 135
}
