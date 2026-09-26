# Combined Entity-Relationship (ER) Documentation: School Management System

This documentation accompanies the **Combined Chen ER Diagrams** generated for the School Management System (`sms_db`):
1. [**`admin_teacher.drawio`**](file:///c:/xampp/htdocs/school-management/admin_teacher.drawio) (or [`admin_teacher.drowio`](file:///c:/xampp/htdocs/school-management/admin_teacher.drowio)) &mdash; Admin & Teacher Modules
2. [**`student_registrar.drawio`**](file:///c:/xampp/htdocs/school-management/student_registrar.drawio) (or [`student_registrar.drowio`](file:///c:/xampp/htdocs/school-management/student_registrar.drowio)) &mdash; Student & Registrar Modules
3. [**`combined_er_viewer.html`**](file:///c:/xampp/htdocs/school-management/combined_er_viewer.html) &mdash; Interactive In-Browser Tabbed Viewer

The diagrams strictly adhere to the **reference notation standards** shown in your reference image:
- **Pure Black & White (No Colors)**
- **Entity:** Rectangles with bold entity name inside
- **Relationship:** Diamonds linking associated entities
- **Attributes:** Ovals / Ellipses connected by solid lines radiating outward
- **Key Constraints:** Explicit `(PK)` for Primary Keys and `(FK)` for Foreign Keys
- **Exact Data Dictionary Match:** 100% of all columns from [`DATA_DICTIONARY.md`](file:///c:/xampp/htdocs/school-management/DATA_DICTIONARY.md) are included

---

## 1. Quick Access to Files

| Diagram Name | Draw.io File (diagrams.net) | Standalone Vector Graphic | Interactive Viewer |
|---|---|---|---|
| **Admin & Teacher ER** | [**`admin_teacher.drawio`**](file:///c:/xampp/htdocs/school-management/admin_teacher.drawio) <br>([`admin_teacher.drowio`](file:///c:/xampp/htdocs/school-management/admin_teacher.drowio)) | [**`admin_teacher_er.svg`**](file:///c:/xampp/htdocs/school-management/admin_teacher_er.svg) | [**`combined_er_viewer.html`**](file:///c:/xampp/htdocs/school-management/combined_er_viewer.html) (Tab 1) |
| **Student & Registrar ER** | [**`student_registrar.drawio`**](file:///c:/xampp/htdocs/school-management/student_registrar.drawio) <br>([`student_registrar.drowio`](file:///c:/xampp/htdocs/school-management/student_registrar.drowio)) | [**`student_registrar_er.svg`**](file:///c:/xampp/htdocs/school-management/student_registrar_er.svg) | [**`combined_er_viewer.html`**](file:///c:/xampp/htdocs/school-management/combined_er_viewer.html) (Tab 2) |

---

## 2. Diagram 1: Admin & Teacher Combined ER (`admin_teacher.drawio`)

Covers 6 tables related to system administration, faculty roster, and academic curriculum:

### 1. `admin` Entity (5 Attributes)
- `admin_id` **(PK)**
- `username`
- `password`
- `fname`
- `lname`

### 2. `setting` Entity (6 Attributes)
- `id` **(PK)**
- `current_year`
- `current_semester`
- `school_name`
- `slogan`
- `about`

### 3. `message` Entity (5 Attributes)
- `message_id` **(PK)**
- `sender_full_name`
- `sender_email`
- `message`
- `date_time`

### 4. `courses` Entity (5 Attributes)
- `course_id` **(PK)**
- `grade`
- `course_name`
- `grade_code`
- `course_code`

### 5. `teacher` Entity (16 Attributes)
- `teacher_id` **(PK)**
- `username`
- `password`
- `class` **(FK)**
- `fname`
- `lname`
- `subjets` **(FK)**
- `gradeId` **(FK)**
- `address`
- `employee_number`
- `date_of_birth`
- `phone_number`
- `qualification`
- `gender`
- `email_address`
- `date_of_joined`

### 6. `subjects` Entity (4 Attributes)
- `subject_id` **(PK)**
- `subject`
- `subject_code`
- `grade` **(FK)**

### Relationships (Diamonds):
- **`configures`**: `admin` &mdash; `setting`
- **`reviews`**: `admin` / `setting` &mdash; `message`
- **`manages`**: `admin` &mdash; `teacher`
- **`defines`**: `admin` &mdash; `courses`
- **`teaches`**: `teacher` &mdash; `subjects`

---

## 3. Diagram 2: Student & Registrar Combined ER (`student_registrar.drawio`)

Covers 6 tables related to student admissions, class grouping, grading, and evaluations:

### 1. `registrar_office` Entity (13 Attributes)
- `r_user_id` **(PK)**
- `username`
- `password`
- `fname`
- `lname`
- `address`
- `employee_number`
- `date_of_birth`
- `phone_number`
- `qualification`
- `gender`
- `email_address`
- `date_of_joined`

### 2. `student` Entity (16 Attributes)
- `student_id` **(PK)**
- `username`
- `password`
- `fname`
- `lname`
- `grade` **(FK)**
- `section` **(FK)**
- `address`
- `gender`
- `email_address`
- `date_of_birth`
- `date_of_joined`
- `parent_fname`
- `parent_lname`
- `parent_phone_number`
- `subjets`

### 3. `student_score` Entity (7 Attributes)
- `id` **(PK)**
- `semester`
- `year`
- `student_id` **(FK)**
- `teacher_id` **(FK)**
- `subject_id` **(FK)**
- `results`

### 4. `class` Entity (3 Attributes)
- `class_id` **(PK)**
- `grade` **(FK)**
- `section` **(FK)**

### 5. `grades` Entity (3 Attributes)
- `grade_id` **(PK)**
- `grade`
- `grade_code`

### 6. `section` Entity (2 Attributes)
- `section_id` **(PK)**
- `section`

### Relationships (Diamonds):
- **`admits`**: `registrar_office` &mdash; `student`
- **`receives`**: `student` &mdash; `student_score`
- **`enrolled_in`**: `student` &mdash; `class`
- **`comprises`**: `class` &mdash; `grades`
- **`divides`**: `class` &mdash; `section`

---

## 4. How to Open and Edit

1. **Browser Interactive Viewer:** Open [**`combined_er_viewer.html`**](file:///c:/xampp/htdocs/school-management/combined_er_viewer.html) to toggle between both diagrams and view them in full vector resolution with download options.
2. **In Draw.io / Diagrams.net:** Navigate to [diagrams.net](https://app.diagrams.net/) &rarr; **Open Existing Diagram** &rarr; select [`admin_teacher.drawio`](file:///c:/xampp/htdocs/school-management/admin_teacher.drawio) or [`student_registrar.drawio`](file:///c:/xampp/htdocs/school-management/student_registrar.drawio).
3. **In VS Code:** Open either `.drawio` file with the VS Code Draw.io extension installed.
