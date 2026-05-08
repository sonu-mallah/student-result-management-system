Student Result Management System
A CLI-based Student Result Management System built in Python with complete CRUD operations, grade calculation, leaderboard, and statistics dashboard.
Features

Add student with duplicate roll number prevention and input validation
View all students
Update student marks (auto grade recalculation)
Delete student with confirmation
Search by name or roll number (partial search supported)
Leaderboard sorted by marks with rank
Statistics dashboard (topper, average, pass percentage, grade-wise count)
JSON-based persistent storage

Tech Stack

Language: Python
Storage: JSON (File-based persistent database)
Interface: CLI (Command Line Interface)

How to Run
Make sure Python is installed on your system.
bashpython main.py
Project Structure
student-result-management-system/
│
├── main.py          # Main application file
├── students.json    # Auto-generated database file
└── README.md        # Project documentation
Concepts Used

CRUD Operations
File Handling (JSON)
Input Validation
Sorting Algorithm 
Search Algorithm (partial match)
Dictionary and List data structures
Modular programming with functions