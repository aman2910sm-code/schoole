# Data Dictionary: School Management System (`sms_db`)

**Database Name:** `sms_db`  
**RDBMS:** MySQL / MariaDB (InnoDB, `utf8mb4_general_ci`)  
**Total Tables:** **12 Tables**  
**Format Structure:** `Column name | Data Type | Constraint | Description`  

---

## Table Directory

| # | Table Name | Total Columns | Primary Key | Foreign Keys | Description |
|---|---|---|---|---|---|
| 1 | [**`admin`**](#1-admin-table-admin) | 5 | `admin_id` | *None* | System administrators with full administrative authority. |
| 2 | [**`student`**](#2-student-table-student) | 16 | `student_id` | `grade`, `section` | Student demographic records, parental contacts, and enrollments. |
| 3 | [**`teacher`**](#3-teacher-table-teacher) | 16 | `teacher_id` | *None (Logical FKs)* | Faculty teaching staff, qualifications, and assignments. |
| 4 | [**`grades`**](#4-grades-table-grades) | 3 | `grade_id` | *None* | Grade / standard levels (e.g., Kindergarten 'KG', Grade 1 'G'). |
| 5 | [**`section`**](#5-section-table-section) | 2 | `section_id` | *None* | Classroom section letters/divisions (e.g., 'A', 'B', 'C', 'D'). |
| 6 | [**`class`**](#6-class-table-class) | 3 | `class_id` | `grade`, `section` | Classroom cohort pairings combining a Grade and a Section. |
| 7 | [**`subjects`**](#7-subjects-table-subjects) | 4 | `subject_id` | `grade` | Academic subjects assigned to respective grade levels. |
| 8 | [**`courses`**](#8-courses-table-courses) | 5 | `course_id` | *None* | Academic courses categorized by grade code and course code. |
| 9 | [**`student_score`**](#9-student_score-table-student_score) | 7 | `id` | `student_id`, `teacher_id`, `subject_id` | Student test results, exam marks, and academic evaluations. |
| 10 | [**`registrar_office`**](#10-registrar_office-table-registrar_office) | 13 | `r_user_id` | *None* | Registrar office staff managing admissions and demographics. |
| 11 | [**`setting`**](#11-setting-table-setting) | 6 | `id` | *None* | Global school information, current academic year, and semester. |
| 12 | [**`message`**](#12-message-table-message) | 5 | `message_id` | *None* | Public contact form inquiries and feedback sent to administrators. |

---

## 1. ADMIN Table (`admin`)

| Column name | Data Type | Constraint | Description |
|---|---|---|---|
| `admin_id` | `INT(11)` | PRIMARY KEY, AUTO_INCREMENT, NOT NULL | Unique identifier for the administrator account. |
| `username` | `VARCHAR(127)` | NOT NULL | Login username handle for admin authentication. |
| `password` | `VARCHAR(255)` | NOT NULL | Hashed account password (encrypted with bcrypt). |
| `fname` | `VARCHAR(127)` | NOT NULL | First name of the administrator. |
| `lname` | `VARCHAR(127)` | NOT NULL | Last name of the administrator. |

---

## 2. STUDENT Table (`student`)

| Column name | Data Type | Constraint | Description |
|---|---|---|---|
| `student_id` | `INT(11)` | PRIMARY KEY, AUTO_INCREMENT, NOT NULL | Unique identifier for the student. |
| `username` | `VARCHAR(127)` | NOT NULL | Login username handle for the student portal. |
| `password` | `VARCHAR(255)` | NOT NULL | Hashed account password (encrypted with bcrypt). |
| `fname` | `VARCHAR(127)` | NOT NULL | Student's first name. |
| `lname` | `VARCHAR(255)` | NOT NULL | Student's last name. |
| `grade` | `INT(11)` | FOREIGN KEY (`grades.grade_id`), NOT NULL | Reference to the student's enrolled grade level. |
| `section` | `INT(11)` | FOREIGN KEY (`section.section_id`), NOT NULL | Reference to the student's assigned classroom section. |
| `address` | `VARCHAR(31)` | NOT NULL | Residential address or location of the student. |
| `gender` | `VARCHAR(7)` | NOT NULL | Gender of the student ('Male', 'Female'). |
| `email_address` | `VARCHAR(255)` | NOT NULL | Email address of the student. |
| `date_of_birth` | `DATE` | NULL | Date of birth of the student (YYYY-MM-DD). |
| `date_of_joined` | `TIMESTAMP` | NULL, DEFAULT `current_timestamp()` | Registration timestamp when the student was enrolled. |
| `parent_fname` | `VARCHAR(127)` | NOT NULL | First name of parent or legal guardian. |
| `parent_lname` | `VARCHAR(127)` | NOT NULL | Last name of parent or legal guardian. |
| `parent_phone_number` | `VARCHAR(31)` | NOT NULL | Emergency contact phone number for parent/guardian. |
| `subjets` | `VARCHAR(50)` | NULL | Enrolled subject identifier(s) or reference list. |

---

## 3. TEACHER Table (`teacher`)

| Column name | Data Type | Constraint | Description |
|---|---|---|---|
| `teacher_id` | `INT(11)` | PRIMARY KEY, AUTO_INCREMENT, NOT NULL | Unique identifier for the teacher account. |
| `username` | `VARCHAR(127)` | NOT NULL | Login username handle for teacher authentication. |
| `password` | `VARCHAR(255)` | NOT NULL | Hashed account password (encrypted with bcrypt). |
| `class` | `VARCHAR(31)` | NOT NULL | Identifier(s) of class(es) assigned to this teacher. |
| `fname` | `VARCHAR(127)` | NOT NULL | First name of the teacher. |
| `lname` | `VARCHAR(127)` | NOT NULL | Last name of the teacher. |
| `subjets` | `VARCHAR(31)` | NOT NULL | Identifier(s) of subject(s) taught by this teacher. |
| `gradeId` | `INT(11)` | NOT NULL | Grade level ID associated with this teacher. |
| `address` | `VARCHAR(31)` | NOT NULL | Residential address or location of the teacher. |
| `employee_number` | `INT(11)` | NOT NULL | Institutional employee identification number. |
| `date_of_birth` | `DATE` | NULL | Date of birth of the teacher (YYYY-MM-DD). |
| `phone_number` | `VARCHAR(31)` | NOT NULL | Contact telephone/mobile number of the teacher. |
| `qualification` | `VARCHAR(127)` | NOT NULL | Highest educational degree or qualification (e.g., CA, BCA, B.Ed). |
| `gender` | `VARCHAR(7)` | NOT NULL | Gender of the teacher ('Male', 'Female'). |
| `email_address` | `VARCHAR(225)` | NOT NULL | Official contact email address of the teacher. |
| `date_of_joined` | `DATETIME` | NOT NULL, DEFAULT `current_timestamp()` | Date and time when the teacher was onboarded. |

---

## 4. GRADE Table (`grades`)

| Column name | Data Type | Constraint | Description |
|---|---|---|---|
| `grade_id` | `INT(11)` | PRIMARY KEY, AUTO_INCREMENT, NOT NULL | Unique identifier for the grade entry. |
| `grade` | `VARCHAR(31)` | NOT NULL | Numeric or textual designation of grade level (e.g., '1', '2', '3'). |
| `grade_code` | `VARCHAR(7)` | NOT NULL | Category code classification (e.g., 'G' for Grade, 'KG' for Kindergarten). |

---

## 5. SECTION Table (`section`)

| Column name | Data Type | Constraint | Description |
|---|---|---|---|
| `section_id` | `INT(11)` | PRIMARY KEY, AUTO_INCREMENT, NOT NULL | Unique identifier for the section division. |
| `section` | `VARCHAR(7)` | NOT NULL | Section label or division letter (e.g., 'A', 'B', 'C', 'D'). |

---

## 6. CLASS Table (`class`)

| Column name | Data Type | Constraint | Description |
|---|---|---|---|
| `class_id` | `INT(11)` | PRIMARY KEY, AUTO_INCREMENT, NOT NULL | Unique identifier for the classroom instance. |
| `grade` | `INT(11)` | FOREIGN KEY (`grades.grade_id`), NOT NULL | References the grade level associated with this class. |
| `section` | `INT(11)` | FOREIGN KEY (`section.section_id`), NOT NULL | References the section assigned to this class. |

---

## 7. SUBJECTS Table (`subjects`)

| Column name | Data Type | Constraint | Description |
|---|---|---|---|
| `subject_id` | `INT(11)` | PRIMARY KEY, AUTO_INCREMENT, NOT NULL | Unique identifier for the academic subject. |
| `subject` | `VARCHAR(31)` | NOT NULL | Name/title of the subject (e.g., 'English', 'Physics'). |
| `subject_code` | `VARCHAR(31)` | NOT NULL | Standardized code abbreviation (e.g., 'En', 'Phy'). |
| `grade` | `INT(11)` | FOREIGN KEY (`grades.grade_id`), NOT NULL | References the grade level where this subject is taught. |

---

## 8. COURSES Table (`courses`)

| Column name | Data Type | Constraint | Description |
|---|---|---|---|
| `course_id` | `INT(11)` | PRIMARY KEY, AUTO_INCREMENT, NOT NULL | Unique identifier for the academic course. |
| `grade` | `INT(11)` | NOT NULL | Target grade level associated with this course. |
| `course_name` | `VARCHAR(127)` | NOT NULL | Full name/title of the course (e.g., 'English', 'Physics'). |
| `grade_code` | `VARCHAR(31)` | NOT NULL | Category code classification of the grade (e.g., 'G', 'KG'). |
| `course_code` | `VARCHAR(31)` | NOT NULL | Unique subject or course identifier code (e.g., 'eng01', 'Phy01'). |

---

## 9. STUDENT_SCORE Table (`student_score`)

| Column name | Data Type | Constraint | Description |
|---|---|---|---|
| `id` | `INT(11)` | PRIMARY KEY, AUTO_INCREMENT, NOT NULL | Unique identifier for the student score record. |
| `semester` | `VARCHAR(100)` | NOT NULL | Academic semester or term when test/exam was conducted (e.g., 'I', 'II', '\|\|'). |
| `year` | `INT(11)` | NOT NULL | Academic year of examination (e.g., 2025). |
| `student_id` | `INT(11)` | FOREIGN KEY (`student.student_id`), NOT NULL | Reference to the evaluated student (ON DELETE CASCADE, ON UPDATE CASCADE). |
| `teacher_id` | `INT(11)` | FOREIGN KEY (`teacher.teacher_id`), NOT NULL | Reference to the faculty teacher who evaluated the marks. |
| `subject_id` | `INT(11)` | FOREIGN KEY (`subjects.subject_id`), NOT NULL | Reference to the academic subject evaluated. |
| `results` | `VARCHAR(512)` | NOT NULL | Detailed test score results and assessment marks string (e.g., '10 10, 15 20, 30 35'). |

---

## 10. REGISTRAR_OFFICE Table (`registrar_office`)

| Column name | Data Type | Constraint | Description |
|---|---|---|---|
| `r_user_id` | `INT(11)` | PRIMARY KEY, AUTO_INCREMENT, NOT NULL | Unique identifier for the registrar officer account. |
| `username` | `VARCHAR(127)` | NOT NULL | Login username handle for registrar staff authentication. |
| `password` | `VARCHAR(255)` | NOT NULL | Hashed account password (encrypted with bcrypt). |
| `fname` | `VARCHAR(31)` | NOT NULL | First name of the registrar officer. |
| `lname` | `VARCHAR(31)` | NOT NULL | Last name of the registrar officer. |
| `address` | `VARCHAR(31)` | NOT NULL | Residential address or locality of the registrar officer. |
| `employee_number` | `INT(11)` | NOT NULL | Institutional employee identification number. |
| `date_of_birth` | `DATE` | NOT NULL | Date of birth of the registrar officer (YYYY-MM-DD). |
| `phone_number` | `VARCHAR(31)` | NOT NULL | Contact telephone/mobile number. |
| `qualification` | `VARCHAR(31)` | NOT NULL | Educational degree or qualification (e.g., 'BCA'). |
| `gender` | `VARCHAR(7)` | NOT NULL | Gender of the registrar officer ('Male', 'Female'). |
| `email_address` | `VARCHAR(255)` | NOT NULL | Official contact email address. |
| `date_of_joined` | `DATETIME` | NOT NULL, DEFAULT `current_timestamp()` | Date and time when the registrar officer was onboarded. |

---

## 11. SETTING Table (`setting`)

| Column name | Data Type | Constraint | Description |
|---|---|---|---|
| `id` | `INT(11)` | PRIMARY KEY, AUTO_INCREMENT, NOT NULL | Unique identifier for the institutional configuration settings. |
| `current_year` | `INT(11)` | NOT NULL | Active academic school year (e.g., 2026). |
| `current_semester` | `VARCHAR(11)` | NOT NULL | Current active academic semester or term (e.g., 'I', 'II', '\|\|'). |
| `school_name` | `VARCHAR(100)` | NOT NULL | Official registered name of the educational institution. |
| `slogan` | `VARCHAR(300)` | NOT NULL | School motto, mission statement, or promotional tagline. |
| `about` | `TEXT` | NOT NULL | Extended descriptive overview, history, and profile of the school. |

---

## 12. MESSAGE Table (`message`)

| Column name | Data Type | Constraint | Description |
|---|---|---|---|
| `message_id` | `INT(11)` | PRIMARY KEY, AUTO_INCREMENT, NOT NULL | Unique identifier for the incoming contact message. |
| `sender_full_name` | `VARCHAR(100)` | NOT NULL | Full name of the person sending inquiry/feedback. |
| `sender_email` | `VARCHAR(255)` | NOT NULL | Email address of the sender for administrative replies. |
| `message` | `TEXT` | NOT NULL | Body content and details of the message/inquiry. |
| `date_time` | `DATETIME` | NOT NULL, DEFAULT `current_timestamp()` | Timestamp recording when the message was received. |
