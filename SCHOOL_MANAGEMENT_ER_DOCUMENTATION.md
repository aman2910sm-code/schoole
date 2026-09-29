# School Management System (sms_db) — Unified Entity-Relationship (ER) Documentation

This document provides the complete structural specification for the **Unified School Management System (sms_db) ER Diagram**. The diagram combines all **12 database tables** into a **single, unified ER diagram** using **Peter Chen ER Notation** and **pure Black & White** styling as specified in the reference guidelines.

---

## 1. Symbol Notation Guide (As Specified in Reference Image)

| Symbol | Draw.io Shape | Description & Formatting | Usage in SMS ER Diagram |
| :--- | :--- | :--- | :--- |
| **Entity** | Rectangle | Solid black border (`strokeWidth=2.5`), white fill, bold uppercase title. | Represents database tables (e.g., `ADMIN`, `TEACHER`, `STUDENT`). |
| **Relationship** | Diamond (Rhombus) | Solid black border (`strokeWidth=2.0`), white fill, bold verb label. | Connects related entities (e.g., `teaches`, `enrolled_in`). |
| **Regular Attribute** | Oval (Ellipse) | Thin black border (`strokeWidth=1.2`), white fill, normal text. | Entity properties (e.g., `fname`, `lname`, `email_address`). |
| **Primary Key (PK)** | Oval (Ellipse) | Thick black border (`strokeWidth=2.5`), **underlined text** + `(PK)`. | Unique row identifiers (e.g., `<u>admin_id</u> (PK)`). |
| **Foreign Key (FK)** | Oval (Ellipse) | **Dashed border** (`strokeDasharray=3 3`), labeled with `(FK)`. | Relational keys referencing other tables (e.g., `grade (FK)`). |
| **Connecting Line** | Solid Line | Clean black connecting lines (`strokeWidth=1.2` for attributes, `1.8` for relationships). | Associates attributes with entities, and entities with relationships. |
| **Cardinality** | Text Badges | Labeled multiplicity ratios (`1:1`, `1:N`, `M:N`). | Quantifies relational mapping between entities. |

---

## 2. Complete Database Table Inventory (12 Tables, 85 Attributes)

| Table / Entity | Primary Key (PK) | Foreign Keys (FK) | Additional Attributes | Total Attributes |
| :--- | :--- | :--- | :--- | :---: |
| **`admin`** | `admin_id` | *None* | `username`, `password`, `fname`, `lname` | **5** |
| **`setting`** | `id` | *None* | `current_year`, `current_semester`, `school_name`, `slogan`, `about` | **6** |
| **`message`** | `message_id` | *None* | `sender_full_name`, `sender_email`, `message`, `date_time` | **5** |
| **`registrar_office`** | `r_user_id` | *None* | `username`, `password`, `fname`, `lname`, `address`, `employee_number`, `date_of_birth`, `phone_number`, `qualification`, `gender`, `email_address`, `date_of_joined` | **13** |
| **`teacher`** | `teacher_id` | `class`, `subjets`, `gradeId` | `username`, `password`, `fname`, `lname`, `address`, `employee_number`, `date_of_birth`, `phone_number`, `qualification`, `gender`, `email_address`, `date_of_joined` | **16** |
| **`class`** | `class_id` | `grade`, `section` | *None* | **3** |
| **`student`** | `student_id` | `grade`, `section`, `subjets` | `username`, `password`, `fname`, `lname`, `address`, `gender`, `email_address`, `date_of_birth`, `date_of_joined`, `parent_fname`, `parent_lname`, `parent_phone_number` | **16** |
| **`courses`** | `course_id` | `grade` | `course_name`, `grade_code`, `course_code` | **5** |
| **`grades`** | `grade_id` | *None* | `grade`, `grade_code` | **3** |
| **`section`** | `section_id` | *None* | `section` | **2** |
| **`subjects`** | `subject_id` | `grade` | `subject`, `subject_code` | **4** |
| **`student_score`** | `id` | `student_id`, `teacher_id`, `subject_id` | `semester`, `year`, `results` | **7** |

---

## 3. Relatable Relationships Matrix (15 Natural Business & FK Relations)

To ensure the diagram is clean, intuitive, and readable for college project submission, only **direct, relatable relationships** are modeled, eliminating redundant cross-connections:

| # | Relationship Name | Entity 1 | Cardinality 1 | Entity 2 | Cardinality 2 | Business Meaning & Schema Reference |
| :-: | :--- | :--- | :-: | :--- | :-: | :--- |
| **1** | **`configures`** | `admin` | **1** | `setting` | **1** | Admin configures school settings (name, slogan, year, semester). |
| **2** | **`reviews`** | `admin` | **1** | `message` | **N** | Admin reviews visitor messages received by the portal. |
| **3** | **`manages`** | `admin` | **1** | `teacher` | **N** | Admin oversees and manages academic teaching personnel. |
| **4** | **`supervises`** | `admin` | **1** | `registrar_office` | **N** | Admin supervises registrar office staff members. |
| **5** | **`registers`** | `registrar_office` | **1** | `student` | **N** | Registrar office admits and registers student records. |
| **6** | **`teaches`** | `teacher` | **M** | `class` | **N** | Teacher is assigned to instruct classes (`teacher.class`). |
| **7** | **`enrolled_in`** | `student` | **N** | `class` | **1** | Students are enrolled into their respective classes. |
| **8** | **`has_grade`** | `class` | **N** | `grades` | **1** | Class belongs to a grade level (`class.grade -> grades.grade_id`). |
| **9** | **`has_section`** | `class` | **N** | `section` | **1** | Class belongs to a specific section (`class.section -> section.section_id`). |
| **10**| **`offers`** | `grades` | **1** | `courses` | **N** | Grade curriculum offers specific courses (`courses.grade -> grades.grade_id`). |
| **11**| **`includes`** | `grades` | **1** | `subjects` | **N** | Grade curriculum contains subjects (`subjects.grade -> grades.grade_id`). |
| **12**| **`instructs`** | `teacher` | **M** | `subjects` | **N** | Teacher instructs subjects (`teacher.subjets -> subjects.subject_id`). |
| **13**| **`receives`** | `student` | **1** | `student_score` | **N** | Student receives grades/scores (`student_score.student_id -> student.student_id`). |
| **14**| **`evaluates`** | `teacher` | **1** | `student_score` | **N** | Teacher submits assessment scores (`student_score.teacher_id -> teacher.teacher_id`). |
| **15**| **`assessed_in`** | `subjects` | **1** | `student_score` | **N** | Subject is evaluated in the score record (`student_score.subject_id -> subjects.subject_id`). |

---

## 4. Generated Project Deliverables

| File Name | File Path | Purpose |
| :--- | :--- | :--- |
| **`School_Management_Unified_ER.drawio`** | `c:\xampp\htdocs\school-management\School_Management_Unified_ER.drawio` | **Brand new native Draw.io diagram file** containing all 12 tables and 15 relatable relations on a single canvas. |
| **`School_Management_Unified_ER.svg`** | `c:\xampp\htdocs\school-management\School_Management_Unified_ER.svg` | Scalable high-resolution vector graphic for insertion into PDF/Word project reports. |
| **`School_Management_ER_Viewer.html`** | `c:\xampp\htdocs\school-management\School_Management_ER_Viewer.html` | Interactive browser viewer with zoom controls, pan navigation, and instant `.drawio` download. |
