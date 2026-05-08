# Student Result Management System

A CLI-based Student Result Management System built using Python and JSON file handling.

This project allows users to manage student records with features like CRUD operations, leaderboard ranking, grade calculation, and statistics analysis.

---

# Features

- Add Student Records
- Prevent Duplicate Roll Numbers
- Update Student Marks
- Automatic Grade Calculation
- Delete Student Records
- Search by Name or Roll Number
- Leaderboard with Rank System
- Statistics Dashboard
- Persistent JSON Storage
- Input Validation and Error Handling

---

# Grade Criteria

| Marks Range | Grade | Result |
|-------------|-------|--------|
| 90 - 100 | A+ | Pass |
| 80 - 89 | A | Pass |
| 70 - 79 | B | Pass |
| 60 - 69 | C | Pass |
| 50 - 59 | D | Pass |
| 40 - 49 | E | Pass |
| Below 40 | Fail | Fail |

---

# Tech Stack

- Python
- JSON
- File Handling
- CLI (Command Line Interface)

---

# Project Structure

```bash
student-result-management-system/
│
├── main.py
├── students.json
└── README.md
```

---

# How to Run

```bash
python main.py
```

---

# Sample Student Record

```json
{
  "roll": "101",
  "name": "Sonu",
  "marks": 85,
  "grade": "A",
  "result": "Pass",
  "percentage": 85.0
}
```

---

# Concepts Used

- CRUD Operations
- Sorting and Ranking
- Functions and Modular Programming
- JSON File Handling
- Input Validation
- Conditional Logic

---

# Future Improvements

- GUI Version
- Database Integration
- Login Authentication
- Export Results to CSV/PDF

---

# Author

Sonu Mallah