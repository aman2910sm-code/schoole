# Database Documentation: School Management System (`sms_db`)

**Database Name:** `sms_db`  
**RDBMS:** MySQL / MariaDB (Default Engine: `InnoDB`, Charset: `utf8mb4`, Collation: `utf8mb4_general_ci`)  
**Host / Connection:** `localhost:3306` via PDO (`DB_connection.php`)  
**Total Tables:** **12 Tables**

---

## 1. Executive Summary & Table Inventory

The School Management System database (`sms_db`) contains **12 relational tables** categorized into 5 logical modules:

```
                                  sms_db (12 Tables)
                                           │
  ┌──────────────────┬─────────────────────┼─────────────────────┬──────────────────┐
  ▼                  ▼                     ▼                     ▼                  ▼
User Roles & Auth  Academic Hierarchy   Curriculum/Courses   Academic Evaluation  System & Messaging
├─ admin           ├─ grades             ├─ subjects          └─ student_score    ├─ setting
├─ teacher         ├─ section            └─ courses                               └─ message
├─ student         └─ class
└─ registrar_office
```

### Table Directory & Statistics

| # | Table Name | Total Columns | Primary Key | Foreign Keys | Sample Records | Description |
|---|---|---|---|---|---|---|
| 1 | [**`admin`**](#1-admin-table) | 5 | `admin_id` | *None* | 1 | System administrators with full administrative authority. |
| 2 | [**`class`**](#2-class-table) | 3 | `class_id` | `grade`, `section` | 7 | Specific classroom cohorts combining a Grade and a Section. |
| 3 | [**`courses`**](#3-courses-table) | 5 | `course_id` | *None* | 2 | Academic courses categorized by grade code and course code. |
| 4 | [**`grades`**](#4-grades-table) | 3 | `grade_id` | *None* | 5 | Grade / standard levels (e.g., Kindergarten 'KG', Grade 1 'G'). |
| 5 | [**`message`**](#5-message-table) | 5 | `message_id` | *None* | 2 | Public inquiries and contact messages submitted to admin. |
| 6 | [**`registrar_office`**](#6-registrar_office-table) | 13 | `r_user_id` | *None* | 3 | Registrar staff accounts handling admissions and demographics. |
| 7 | [**`section`**](#7-section-table) | 2 | `section_id` | *None* | 4 | Classroom sections/divisions (e.g., 'A', 'B', 'C', 'D'). |
| 8 | [**`setting`**](#8-setting-table) | 6 | `id` | *None* | 1 | Global school configuration, semester, and academic year. |
| 9 | [**`student`**](#9-student-table) | 16 | `student_id` | `grade`, `section` | 4 | Student profiles, parent info, and class enrollments. |
| 10 | [**`student_score`**](#10-student_score-table) | 7 | `id` | `student_id`, `teacher_id`, `subject_id` | 1 | Exam scores and evaluations recorded per student and subject. |
| 11 | [**`subjects`**](#11-subjects-table) | 4 | `subject_id` | `grade` | 2 | Academic subjects assigned to respective grade levels. |
| 12 | [**`teacher`**](#12-teacher-table) | 16 | `teacher_id` | *None (Logical FKs)* | 2 | Faculty teachers, qualification, subject & grade assignments. |

---

## 2. Entity-Relationship (ER) Architecture

```mermaid
erDiagram
    ADMIN {
        int admin_id PK
        varchar username
        varchar password
        varchar fname
        varchar lname
    }

    SETTING {
        int id PK
        int current_year
        varchar current_semester
        varchar school_name
        varchar slogan
        text about
    }

    MESSAGE {
        int message_id PK
        varchar sender_full_name
        varchar sender_email
        text message
        datetime date_time
    }

    GRADES {
        int grade_id PK
        varchar grade
        varchar grade_code
    }

    SECTION {
        int section_id PK
        varchar section
    }

    CLASS {
        int class_id PK
        int grade FK
        int section FK
    }

    SUBJECTS {
        int subject_id PK
        varchar subject
        varchar subject_code
        int grade FK
    }

    COURSES {
        int course_id PK
        int grade
        varchar course_name
        varchar grade_code
        varchar course_code
    }

    TEACHER {
        int teacher_id PK
        varchar username
        varchar password
        varchar class
        varchar fname
        varchar lname
        varchar subjets
        int gradeId
        varchar address
        int employee_number
        date date_of_birth
        varchar phone_number
        varchar qualification
        varchar gender
        varchar email_address
        datetime date_of_joined
    }

    REGISTRAR_OFFICE {
        int r_user_id PK
        varchar username
        varchar password
        varchar fname
        varchar lname
        varchar address
        int employee_number
        date date_of_birth
        varchar phone_number
        varchar qualification
        varchar gender
        varchar email_address
        datetime date_of_joined
    }

    STUDENT {
        int student_id PK
        varchar username
        varchar password
        varchar fname
        varchar lname
        int grade FK
        int section FK
        varchar address
        varchar gender
        varchar email_address
        date date_of_birth
        timestamp date_of_joined
        varchar parent_fname
        varchar parent_lname
        varchar parent_phone_number
        varchar subjets
    }

    STUDENT_SCORE {
        int id PK
        varchar semester
        int year
        int student_id FK
        int teacher_id FK
        int subject_id FK
        varchar results
    }

    GRADES ||--o{ CLASS : "contains (grade_id -> grade)"
    SECTION ||--o{ CLASS : "partitions (section_id -> section)"
    GRADES ||--o{ SUBJECTS : "curriculum (grade_id -> grade)"
    GRADES ||--o{ STUDENT : "enrolled in (grade_id -> grade)"
    SECTION ||--o{ STUDENT : "assigned to (section_id -> section)"
    STUDENT ||--o{ STUDENT_SCORE : "receives (student_id -> student_id)"
    TEACHER ||--o{ STUDENT_SCORE : "grades (teacher_id -> teacher_id)"
    SUBJECTS ||--o{ STUDENT_SCORE : "evaluated in (subject_id -> subject_id)"
```

---

## 3. Comprehensive Schema Details (All 12 Tables)

### 1. `admin` Table
Stores login accounts for institutional administrators with top-level system privileges.

| Column Name | Data Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| `admin_id` | `INT(11)` | No | *AUTO_INCREMENT* | **PRIMARY KEY** | Unique identifier for the administrator account. |
| `username` | `VARCHAR(127)` | No | *None* | | Username for administrator login authentication. |
| `password` | `VARCHAR(255)` | No | *None* | | Hashed password (PHP `password_hash` bcrypt). |
| `fname` | `VARCHAR(127)` | No | *None* | | First name of administrator. |
| `lname` | `VARCHAR(127)` | No | *None* | | Last name of administrator. |

---

### 2. `class` Table
Represents an instructional classroom combining an academic grade level and a section.

| Column Name | Data Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| `class_id` | `INT(11)` | No | *AUTO_INCREMENT* | **PRIMARY KEY** | Unique class identifier. |
| `grade` | `INT(11)` | No | *None* | **KEY**, **FK** -> `grades(grade_id)` | Academic grade level. Cascades on update. |
| `section` | `INT(11)` | No | *None* | **KEY**, **FK** -> `section(section_id)` | Section division. Cascades on update. |

* **Foreign Key Constraints:**
  * `fk_class_grade`: `FOREIGN KEY (grade) REFERENCES grades(grade_id) ON UPDATE CASCADE`
  * `fk_class_section`: `FOREIGN KEY (section) REFERENCES section(section_id) ON UPDATE CASCADE`

---

### 3. `courses` Table
Maintains catalog of academic courses categorized by grade code and course code.

| Column Name | Data Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| `course_id` | `INT(11)` | No | *AUTO_INCREMENT* | **PRIMARY KEY** | Unique course identifier. |
| `grade` | `INT(11)` | No | *None* | | Target grade level for course. |
| `course_name` | `VARCHAR(127)` | No | *None* | | Full course title (e.g., 'English', 'Physics'). |
| `grade_code` | `VARCHAR(31)` | No | *None* | | Grade classification code (e.g., 'G', 'KG'). |
| `course_code` | `VARCHAR(31)` | No | *None* | | Subject/Course identifier code (e.g., 'eng01', 'Phy01'). |

---

### 4. `grades` Table
Stores academic levels and tier designations within the school.

| Column Name | Data Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| `grade_id` | `INT(11)` | No | *AUTO_INCREMENT* | **PRIMARY KEY** | Unique identifier for grade entry. |
| `grade` | `VARCHAR(31)` | No | *None* | | Grade title/number (e.g., '1', '2', '3', '4'). |
| `grade_code` | `VARCHAR(7)` | No | *None* | | Classification code ('G' for primary/secondary, 'KG' for Kindergarten). |

---

### 5. `message` Table
Stores contact inquiries and feedback received from website visitors or users.

| Column Name | Data Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| `message_id` | `INT(11)` | No | *AUTO_INCREMENT* | **PRIMARY KEY** | Unique identifier for the message. |
| `sender_full_name` | `VARCHAR(100)` | No | *None* | | Full name of the sender. |
| `sender_email` | `VARCHAR(255)` | No | *None* | | Email address for replying to the sender. |
| `message` | `TEXT` | No | *None* | | Message body / inquiry content. |
| `date_time` | `DATETIME` | No | `current_timestamp()` | | Timestamp when message was submitted. |

---

### 6. `registrar_office` Table
Stores user credentials and demographic details for registrar personnel.

| Column Name | Data Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| `r_user_id` | `INT(11)` | No | *AUTO_INCREMENT* | **PRIMARY KEY** | Unique registrar account identifier. |
| `username` | `VARCHAR(127)` | No | *None* | | Login username handle. |
| `password` | `VARCHAR(255)` | No | *None* | | Hashed password string (bcrypt). |
| `fname` | `VARCHAR(31)` | No | *None* | | First name. |
| `lname` | `VARCHAR(31)` | No | *None* | | Last name. |
| `address` | `VARCHAR(31)` | No | *None* | | Residential address. |
| `employee_number` | `INT(11)` | No | *None* | | Official employee registration number. |
| `date_of_birth` | `DATE` | No | *None* | | Date of birth (YYYY-MM-DD). |
| `phone_number` | `VARCHAR(31)` | No | *None* | | Contact telephone/mobile number. |
| `qualification` | `VARCHAR(31)` | No | *None* | | Academic qualification (e.g., 'BCA'). |
| `gender` | `VARCHAR(7)` | No | *None* | | Gender ('Male', 'Female'). |
| `email_address` | `VARCHAR(255)` | No | *None* | | Contact email address. |
| `date_of_joined` | `DATETIME` | No | `current_timestamp()` | | Date and time when hired/registered. |

---

### 7. `section` Table
Contains section classifications (e.g., A, B, C, D) used to partition classes and students.

| Column Name | Data Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| `section_id` | `INT(11)` | No | *AUTO_INCREMENT* | **PRIMARY KEY** | Unique section identifier. |
| `section` | `VARCHAR(7)` | No | *None* | | Section designation label (e.g., 'A', 'B', 'C', 'D'). |

---

### 8. `setting` Table
Contains global school system variables and institutional details.

| Column Name | Data Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| `id` | `INT(11)` | No | *AUTO_INCREMENT* | **PRIMARY KEY** | Unique identifier for configuration row. |
| `current_year` | `INT(11)` | No | *None* | | Active academic year (e.g., `2026`). |
| `current_semester` | `VARCHAR(11)` | No | *None* | | Active term/semester (e.g., 'I', 'II', '||'). |
| `school_name` | `VARCHAR(100)` | No | *None* | | Official institution name (e.g., 'Raino School'). |
| `slogan` | `VARCHAR(300)` | No | *None* | | Institution motto or promotional slogan. |
| `about` | `TEXT` | No | *None* | | School descriptive overview and mission statement. |

---

### 9. `student` Table
Stores student enrollment details, parent contacts, credentials, and class assignments.

| Column Name | Data Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| `student_id` | `INT(11)` | No | *AUTO_INCREMENT* | **PRIMARY KEY** | Unique student identifier. |
| `username` | `VARCHAR(127)` | No | *None* | | Username for student portal login. |
| `password` | `VARCHAR(255)` | No | *None* | | Hashed password string (bcrypt). |
| `fname` | `VARCHAR(127)` | No | *None* | | Student's first name. |
| `lname` | `VARCHAR(255)` | No | *None* | | Student's last name. |
| `grade` | `INT(11)` | No | *None* | **KEY**, **FK** -> `grades(grade_id)` | Enrolled grade level. Cascades on update. |
| `section` | `INT(11)` | No | *None* | **KEY**, **FK** -> `section(section_id)` | Assigned class section. Cascades on update. |
| `address` | `VARCHAR(31)` | No | *None* | | Residential location. |
| `gender` | `VARCHAR(7)` | No | *None* | | Gender ('Male', 'Female'). |
| `email_address` | `VARCHAR(255)` | No | *None* | | Student email address. |
| `date_of_birth` | `DATE` | Yes | `NULL` | | Date of birth (YYYY-MM-DD). |
| `date_of_joined` | `TIMESTAMP` | Yes | `current_timestamp()` | | Timestamp when student joined/enrolled. |
| `parent_fname` | `VARCHAR(127)` | No | *None* | | First name of parent or legal guardian. |
| `parent_lname` | `VARCHAR(127)` | No | *None* | | Last name of parent or legal guardian. |
| `parent_phone_number` | `VARCHAR(31)` | No | *None* | | Contact telephone for parent/guardian. |
| `subjets` | `VARCHAR(50)` | Yes | `NULL` | | Enrolled subject IDs (comma-separated or single ID). |

* **Foreign Key Constraints:**
  * `fk_student_grade`: `FOREIGN KEY (grade) REFERENCES grades(grade_id) ON UPDATE CASCADE`
  * `fk_student_section`: `FOREIGN KEY (section) REFERENCES section(section_id) ON UPDATE CASCADE`

---

### 10. `student_score` Table
Tracks academic marks, test evaluations, and semester exam grades for students.

| Column Name | Data Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| `id` | `INT(11)` | No | *AUTO_INCREMENT* | **PRIMARY KEY** | Unique score record identifier. |
| `semester` | `VARCHAR(100)` | No | *None* | | Academic semester (e.g., 'I', 'II', '||'). |
| `year` | `INT(11)` | No | *None* | | Academic year of examination (e.g., 2025). |
| `student_id` | `INT(11)` | No | *None* | **KEY**, **FK** -> `student(student_id)` | Student evaluated. Cascade Delete & Update. |
| `teacher_id` | `INT(11)` | No | *None* | **KEY**, **FK** -> `teacher(teacher_id)` | Faculty teacher who recorded the evaluation. |
| `subject_id` | `INT(11)` | No | *None* | **KEY**, **FK** -> `subjects(subject_id)` | Academic subject evaluated. |
| `results` | `VARCHAR(512)` | No | *None* | | Assessment results / score pairs (e.g., '10 10, 15 20, 30 35'). |

* **Foreign Key Constraints:**
  * `fk_score_student`: `FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE`
  * `fk_score_teacher`: `FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON UPDATE CASCADE`
  * `fk_score_subject`: `FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON UPDATE CASCADE`

---

### 11. `subjects` Table
Maintains course curriculum items tied to specific academic grades.

| Column Name | Data Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| `subject_id` | `INT(11)` | No | *AUTO_INCREMENT* | **PRIMARY KEY** | Unique subject identifier. |
| `subject` | `VARCHAR(31)` | No | *None* | | Name of the subject (e.g., 'English', 'Physics'). |
| `subject_code` | `VARCHAR(31)` | No | *None* | | Standard code abbreviation (e.g., 'En', 'Phy'). |
| `grade` | `INT(11)` | No | *None* | **KEY**, **FK** -> `grades(grade_id)` | Associated grade level. Cascades on update. |

* **Foreign Key Constraints:**
  * `fk_subjects_grade`: `FOREIGN KEY (grade) REFERENCES grades(grade_id) ON UPDATE CASCADE`

---

### 12. `teacher` Table
Maintains faculty profiles, assigned classes, subjects taught, and credentials.

| Column Name | Data Type | Nullable | Default | Constraints | Description |
|---|---|---|---|---|---|
| `teacher_id` | `INT(11)` | No | *AUTO_INCREMENT* | **PRIMARY KEY** | Unique teacher identifier. |
| `username` | `VARCHAR(127)` | No | *None* | | Login username handle. |
| `password` | `VARCHAR(255)` | No | *None* | | Hashed password string (bcrypt). |
| `class` | `VARCHAR(31)` | No | *None* | | Associated class ID(s) assigned to teacher. |
| `fname` | `VARCHAR(127)` | No | *None* | | Faculty first name. |
| `lname` | `VARCHAR(127)` | No | *None* | | Faculty last name. |
| `subjets` | `VARCHAR(31)` | No | *None* | | Associated subject ID(s) taught by teacher. |
| `gradeId` | `INT(11)` | No | *None* | | Grade level ID associated with teacher. |
| `address` | `VARCHAR(31)` | No | *None* | | Residential address. |
| `employee_number` | `INT(11)` | No | *None* | | Institutional employee registration ID. |
| `date_of_birth` | `DATE` | Yes | `NULL` | | Date of birth (YYYY-MM-DD). |
| `phone_number` | `VARCHAR(31)` | No | *None* | | Contact telephone/mobile number. |
| `qualification` | `VARCHAR(127)` | No | *None* | | Highest degree (e.g., 'CA', 'BCA', 'B.Ed'). |
| `gender` | `VARCHAR(7)` | No | *None* | | Gender ('Male', 'Female'). |
| `email_address` | `VARCHAR(225)` | No | *None* | | Official faculty email address. |
| `date_of_joined` | `DATETIME` | No | `current_timestamp()` | | Date and time when teacher joined. |

---

## 4. Foreign Key Constraints & Referential Integrity Matrix

| Child Table | Foreign Key Column | Referenced Parent Table | Referenced Column | ON DELETE | ON UPDATE | Constraint Name |
|---|---|---|---|---|---|---|
| `class` | `grade` | `grades` | `grade_id` | RESTRICT | CASCADE | `fk_class_grade` |
| `class` | `section` | `section` | `section_id` | RESTRICT | CASCADE | `fk_class_section` |
| `student` | `grade` | `grades` | `grade_id` | RESTRICT | CASCADE | `fk_student_grade` |
| `student` | `section` | `section` | `section_id` | RESTRICT | CASCADE | `fk_student_section` |
| `student_score` | `student_id` | `student` | `student_id` | **CASCADE** | CASCADE | `fk_score_student` |
| `student_score` | `teacher_id` | `teacher` | `teacher_id` | RESTRICT | CASCADE | `fk_score_teacher` |
| `student_score` | `subject_id` | `subjects` | `subject_id` | RESTRICT | CASCADE | `fk_score_subject` |
| `subjects` | `grade` | `grades` | `grade_id` | RESTRICT | CASCADE | `fk_subjects_grade` |

---

## 5. Database Connection Specifications

Configured in [`DB_connection.php`](file:///c:/xampp/htdocs/school-management/DB_connection.php):

```php
<?php 
$sName = "localhost";
$uName = "root";
$pass  = "";
$db_name = "sms_db";

try {
    $conn = new PDO("mysql:host=$sName;dbname=$db_name", $uName, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e){
    echo "Connection failed: ". $e->getMessage();
    exit;
}
```

---

## 6. How to Import or Reset the Database

1. Ensure MySQL is running in XAMPP Control Panel.
2. Open phpMyAdmin at `http://localhost/phpmyadmin/` or open terminal:
   ```powershell
   # Using MySQL CLI
   C:\xampp\mysql\bin\mysql.exe -u root -e "CREATE DATABASE IF NOT EXISTS sms_db;"
   C:\xampp\mysql\bin\mysql.exe -u root sms_db < "c:\xampp\htdocs\school-management\sms_db (1).sql"
   ```
3. Alternatively, import [`sms_db (1).sql`](file:///c:/xampp/htdocs/school-management/sms_db%20%281%29.sql) directly via phpMyAdmin's **Import** tab.
