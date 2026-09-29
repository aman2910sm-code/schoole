# Combined Entity-Relationship (ER) Documentation: School Management System

This documentation provides a comprehensive structural guide for the **Combined Chen ER Diagrams** generated for the School Management System (`sms_db`):
1. [**`admin_registrar.drawio`**](file:///c:/xampp/htdocs/school-management/admin_registrar.drawio) (or [`admin_registrar.drowio`](file:///c:/xampp/htdocs/school-management/admin_registrar.drowio)) &mdash; Admin & Registrar Modules (5 Tables)
2. [**`student_teacher.drawio`**](file:///c:/xampp/htdocs/school-management/student_teacher.drawio) (or [`student_teacher.drowio`](file:///c:/xampp/htdocs/school-management/student_teacher.drowio)) &mdash; Student & Teacher Modules (7 Tables)
3. [**`combined_er_viewer.html`**](file:///c:/xampp/htdocs/school-management/combined_er_viewer.html) &mdash; Interactive In-Browser Tabbed Viewer

---

## 1. Ground Truth Constraint Mapping (from `DATA_DICTIONARY.md`)

Before generating the diagrams, an exhaustive analysis of [`DATA_DICTIONARY.md`](file:///c:/xampp/htdocs/school-management/DATA_DICTIONARY.md) was performed. Every relationship in the ER diagrams is strictly backed by an explicit foreign key. Where no foreign key exists in the database schema, the entity is drawn as a standalone entity with radiating attribute ovals (matching `admin_users` and `time_slots` in reference Image 1).

### Complete Mapping: `TABLE → PK → FK → REFERENCED TABLE → REFERENCED PK`

| # | Table | Primary Key (PK) | Foreign Key (FK) | Referenced Table | Referenced PK | Diagram Location |
|---|---|---|---|---|---|---|
| 1 | **`admin`** | `admin_id` | *None* | *None* | *None* | `admin_registrar.drawio` |
| 2 | **`registrar_office`** | `r_user_id` | *None* | *None* | *None* | `admin_registrar.drawio` |
| 3 | **`setting`** | `id` | *None* | *None* | *None* | `admin_registrar.drawio` |
| 4 | **`courses`** | `course_id` | *None* | *None* | *None* | `admin_registrar.drawio` |
| 5 | **`message`** | `message_id` | *None* | *None* | *None* | `admin_registrar.drawio` |
| 6 | **`teacher`** | `teacher_id` | *None* | *None* | *None* | `student_teacher.drawio` |
| 7 | **`grades`** | `grade_id` | *None* | *None* | *None* | `student_teacher.drawio` |
| 8 | **`section`** | `section_id` | *None* | *None* | *None* | `student_teacher.drawio` |
| 9 | **`subjects`** | `subject_id` | `grade` | `grades` | `grade_id` | `student_teacher.drawio` |
| 10 | **`class`** | `class_id` | `grade` | `grades` | `grade_id` | `student_teacher.drawio` |
| 11 | **`class`** | `class_id` | `section` | `section` | `section_id` | `student_teacher.drawio` |
| 12 | **`student`** | `student_id` | `grade` | `grades` | `grade_id` | `student_teacher.drawio` |
| 13 | **`student`** | `student_id` | `section` | `section` | `section_id` | `student_teacher.drawio` |
| 14 | **`student_score`** | `id` | `student_id` | `student` | `student_id` | `student_teacher.drawio` |
| 15 | **`student_score`** | `id` | `teacher_id` | `teacher` | `teacher_id` | `student_teacher.drawio` |
| 16 | **`student_score`** | `id` | `subject_id` | `subjects` | `subject_id` | `student_teacher.drawio` |

---

## 2. File Directory

| Diagram Name | Draw.io File (diagrams.net) | Alternative Extension | Standalone High-Res SVG | Interactive Viewer |
|---|---|---|---|---|
| **Admin & Registrar ER** | [**`admin_registrar.drawio`**](file:///c:/xampp/htdocs/school-management/admin_registrar.drawio) | [**`admin_registrar.drowio`**](file:///c:/xampp/htdocs/school-management/admin_registrar.drowio) | [**`admin_registrar_er.svg`**](file:///c:/xampp/htdocs/school-management/admin_registrar_er.svg) | [**`combined_er_viewer.html`**](file:///c:/xampp/htdocs/school-management/combined_er_viewer.html) (Tab 1) |
| **Student & Teacher ER** | [**`student_teacher.drawio`**](file:///c:/xampp/htdocs/school-management/student_teacher.drawio) | [**`student_teacher.drowio`**](file:///c:/xampp/htdocs/school-management/student_teacher.drowio) | [**`student_teacher_er.svg`**](file:///c:/xampp/htdocs/school-management/student_teacher_er.svg) | [**`combined_er_viewer.html`**](file:///c:/xampp/htdocs/school-management/combined_er_viewer.html) (Tab 2) |

---

## 3. Diagram Details & Visual Notation

Both diagrams use strict **Chen ER Notation** and **Pure Black & White** styling as specified:
- **Entity**: Rectangle with bold table name (`fillColor=#FFFFFF`, `strokeColor=#000000`).
- **Relationship**: Diamond with relation verb (`fillColor=#FFFFFF`, `strokeColor=#000000`).
- **Attribute**: Oval / Ellipse with attribute name (`fillColor=#FFFFFF`, `strokeColor=#000000`).
- **Primary Key (PK)**: Underlined text and explicit `(PK)` tag (e.g., `<u>student_id</u><br/>(PK)`).
- **Foreign Key (FK)**: Attribute name with explicit `(FK)` tag (e.g., `grade<br/>(FK)`).
- **Connectors**: Solid lines linking attributes to entities and entities to relationship diamonds.

---

### Diagram 1: `admin_registrar.drawio` (5 Tables, Standalone Architecture)

In MySQL/MariaDB schema `sms_db`, administrative, registrar, configuration, courses, and inquiry messages operate as independent management records. Since no foreign keys link these tables together, they are drawn cleanly as standalone entities with radiating attribute ovals (matching the standalone reference entities `admin_users` and `time_slots` in reference Image 1):

1. **`admin` (5 attributes):**
   - `admin_id` **(PK)**
   - `username`, `password`, `fname`, `lname`
2. **`registrar_office` (13 attributes):**
   - `r_user_id` **(PK)**
   - `username`, `password`, `fname`, `lname`, `address`, `employee_number`, `date_of_birth`, `phone_number`, `qualification`, `gender`, `email_address`, `date_of_joined`
3. **`setting` (6 attributes):**
   - `id` **(PK)**
   - `current_year`, `current_semester`, `school_name`, `slogan`, `about`
4. **`courses` (5 attributes):**
   - `course_id` **(PK)**
   - `grade`, `course_name`, `grade_code`, `course_code`
5. **`message` (5 attributes):**
   - `message_id` **(PK)**
   - `sender_full_name`, `sender_email`, `message`, `date_time`

---

### Diagram 2: `student_teacher.drawio` (7 Tables, 8 Explicit FK Relationships)

This diagram forms the complete relational core of the academic management system:

1. **`teacher` (16 attributes):**
   - `teacher_id` **(PK)**
   - `username`, `password`, `class`, `fname`, `lname`, `subjets`, `gradeId`, `address`, `employee_number`, `date_of_birth`, `phone_number`, `qualification`, `gender`, `email_address`, `date_of_joined`
2. **`student` (16 attributes):**
   - `student_id` **(PK)**
   - `grade` **(FK)** &rarr; `grades.grade_id`
   - `section` **(FK)** &rarr; `section.section_id`
   - `username`, `password`, `fname`, `lname`, `address`, `gender`, `email_address`, `date_of_birth`, `date_of_joined`, `parent_fname`, `parent_lname`, `parent_phone_number`, `subjets`
3. **`student_score` (7 attributes):**
   - `id` **(PK)**
   - `student_id` **(FK)** &rarr; `student.student_id`
   - `teacher_id` **(FK)** &rarr; `teacher.teacher_id`
   - `subject_id` **(FK)** &rarr; `subjects.subject_id`
   - `semester`, `year`, `results`
4. **`subjects` (4 attributes):**
   - `subject_id` **(PK)**
   - `grade` **(FK)** &rarr; `grades.grade_id`
   - `subject`, `subject_code`
5. **`grades` (3 attributes):**
   - `grade_id` **(PK)**
   - `grade`, `grade_code`
6. **`section` (2 attributes):**
   - `section_id` **(PK)**
   - `section`
7. **`class` (3 attributes):**
   - `class_id` **(PK)**
   - `grade` **(FK)** &rarr; `grades.grade_id`
   - `section` **(FK)** &rarr; `section.section_id`

#### The 8 Relationships (Diamonds):
1. **`scores_for`**: Links `student_score` &harr; `student` via `student_score.student_id = student.student_id`.
2. **`graded_by`**: Links `student_score` &harr; `teacher` via `student_score.teacher_id = teacher.teacher_id`.
3. **`evaluated_in`**: Links `student_score` &harr; `subjects` via `student_score.subject_id = subjects.subject_id`.
4. **`curriculum_of`**: Links `subjects` &harr; `grades` via `subjects.grade = grades.grade_id`.
5. **`in_grade`**: Links `student` &harr; `grades` via `student.grade = grades.grade_id`.
6. **`in_section`**: Links `student` &harr; `section` via `student.section = section.section_id`.
7. **`has_grade`**: Links `class` &harr; `grades` via `class.grade = grades.grade_id`.
8. **`has_section`**: Links `class` &harr; `section` via `class.section = section.section_id`.
