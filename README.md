# 🎓 Student Management System & Course Relationship

A beginner-friendly Python project using **SQLAlchemy** and **SQLite** to practice database operations, ORM concepts, and relationships between tables.

This project contains two main parts:

## 📌 Part 1: Student Management System (CRUD)

This section demonstrates how to manage student records using SQLAlchemy ORM.

### Features

- **Create:** Add new students with their names and scores.
- **Read:** Retrieve and display student information.
- **Update:** Modify student names and scores.
- **Delete:** Remove student records from the database.

### Database Structure

**Database:** `StudentData.db`

| Column | Data Type | Description |
|---|---|---|
| id | INTEGER | Primary Key |
| name | STRING | Student Name |
| score | FLOAT | Student Score |

---

## 📌 Part 2: Student-Course Relationship

This section demonstrates how to create and manage a **One-to-Many Relationship** between students and courses using SQLAlchemy.

### Database Structure

**Database:** `CourseData_Relation.db`

**Students Table**

| Column | Data Type | Description |
|---|---|---|
| id | INTEGER | Primary Key |
| name | STRING | Student Name |

**Courses Table**

| Column | Data Type | Description |
|---|---|---|
| id | INTEGER | Primary Key |
| title | STRING | Course Title |
| unit | INTEGER | Course Units |
| student_id | INTEGER | Foreign Key |

### Relationship

- One student can have multiple courses.
- Each course belongs to one student.
- The `student_id` column connects the `courses` table to the `students` table.

### Features

- Create students and courses.
- Retrieve student information and their related courses.
- Define relationships using SQLAlchemy `relationship()`.
- Use `ForeignKey` to maintain referential integrity.
- Prevent courses from being assigned to non-existing students.
- Implement **Cascade Delete** to automatically delete related courses when a student is deleted.
- Enable SQLite Foreign Key constraints using `PRAGMA foreign_keys=ON`.

---

## 🛠️ Technologies Used

- **Python**
- **SQLAlchemy**
- **SQLite**

## 📦 Installation

Install SQLAlchemy using pip:

```bash
pip install sqlalchemy
```

## ▶️ How to Run

1. Clone this repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project directory.

3. Run the Python file:

```bash
python filename.py
```

4. The SQLite databases and tables will be created automatically when the application runs.

## 🎯 Learning Objectives

Through this project, I practiced:

- Working with SQLite databases.
- Using SQLAlchemy ORM.
- Creating database tables and models.
- Performing CRUD operations.
- Understanding Primary Keys and Foreign Keys.
- Implementing One-to-Many relationships.
- Managing related records with Cascade Delete.
- Handling database constraints and relationships.

---

**This project was developed as part of my Python programming course to practice database management and SQLAlchemy ORM concepts.** 🚀
