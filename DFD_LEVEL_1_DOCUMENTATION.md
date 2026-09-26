# Data Flow Diagram (DFD) Level 1: School Management System

This document provides complete documentation and architectural specifications for the **DFD Level 1 diagram** created for the **School Management System (`sms_db`)**.

The diagram has been built strictly adhering to the user's attached notation reference (conforming to **Gane & Sarson** and **Yourdon & DeMarco** standards) with **NO UML symbols**.

---

## 1. Diagram Files Summary

| File Name | Description | How to Use |
|---|---|---|
| [`school_management_dfd_level1.drawio`](file:///c:/xampp/htdocs/school-management/school_management_dfd_level1.drawio) | **Native draw.io Multi-Page File** containing two complete diagram tabs:<br>• Tab 1: **Gane & Sarson Notation**<br>• Tab 2: **Yourdon & DeMarco Notation** | Open directly in [diagrams.net](https://app.diagrams.net/), Draw.io desktop app, or VS Code Draw.io extension. Fully editable. |
| [`dfd_level1_gane_sarson.svg`](file:///c:/xampp/htdocs/school-management/dfd_level1_gane_sarson.svg) | Standalone vector graphic of Gane & Sarson DFD Level 1 | View in any web browser, embed in PDF reports, or print in high resolution. |
| [`dfd_level1_yourdon_demarco.svg`](file:///c:/xampp/htdocs/school-management/dfd_level1_yourdon_demarco.svg) | Standalone vector graphic of Yourdon & DeMarco DFD Level 1 | View in any web browser or documentation. |
| [`dfd_level1_viewer.html`](file:///c:/xampp/htdocs/school-management/dfd_level1_viewer.html) | Interactive web viewer with tab switcher & quick download | Double-click or open in browser to inspect both diagram notations instantly. |

---

## 2. DFD Symbol Compliance (Referencing Attached Image)

As mandated, standard DFD modeling rules are strictly followed without mixing UML elements (no stick figures, no class diagrams, no use-case stereotypes):

| DFD Element | Gane & Sarson Notation (Tab 1 / Column 2) | Yourdon & DeMarco Notation (Tab 2 / Column 1) | Function in this System |
|---|---|---|---|
| **External Entity** | Sharp-cornered rectangle (`#DAE8FC`, blue) | Sharp-cornered rectangle (`#FFF2CC`, yellow) | Sources and sinks of information outside the software boundary: `Admin`, `Teacher`, `Student`, `Registrar Office`. |
| **Process** | Rounded rectangle with top partition for Process ID (`1.0`, `2.0`, `3.0`, `4.0`) and lower compartment for function description | Circle / Bubble with process ID and name inside | System functional transformations converting data inputs into outputs. |
| **Data Store** | Open-ended rectangle on the right, with a vertical line dividing the ID (`D1`-`D7`) on the left | Open-ended rectangle / two horizontal parallel lines with left cap | Persistent database repositories corresponding to physical MySQL tables in `sms_db`. |
| **Data Flow** | Solid line with directional arrow head and descriptive noun-phrase label | Solid line with directional arrow head and descriptive noun-phrase label | Shows the movement of data packets between Entities, Processes, and Data Stores. |

---

## 3. Four Core Modules & Processes Breakdown

### Module 1: Admin Module (Process `1.0 Admin Management`)
* **Primary External Entity:** `Admin` (System Administrator)
* **Underlying Database Tables:** `admin`, `setting`, `teacher`, `registrar_office`, `grades`, `section`, `class`, `subjects`, `message`
* **Core Functions:**
  1. Authenticates administrative login credentials.
  2. Configures institution settings (school name, slogan, academic year, current semester).
  3. Creates, updates, and deletes `Teacher` accounts (`teacher-add.php`, `teacher-edit.php`).
  4. Creates, updates, and deletes `Registrar Office` staff accounts (`registrar-office-add.php`).
  5. Manages academic foundation: Grades (`grade-add.php`), Sections (`section-add.php`), Classes (`class-add.php`), and Subjects/Courses (`course-add.php`).
  6. Reviews student and public contact feedback messages (`message.php`).
* **Input Data Flows:**
  * `Admin Credentials & School Info` (from `Admin`)
  * `Staff Accounts & Class Details` (from `Admin`)
  * `Read Feedback & Messages` (from `D6 Inquiries & Messages`)
  * `Read Settings` (from `D1 Admin & System Settings`)
* **Output Data Flows:**
  * `Admin Dashboard, Metrics & Feedback` (to `Admin`)
  * `Update System Settings` (to `D1 Admin & System Settings`)
  * `Create / Update Teacher Profiles` (to `D2 Teacher Records`)
  * `Manage Registrar Staff Accounts` (to `D7 Registrar Staff Records`)
  * `Configure Classes, Grades & Subjects` (to `D4 Academic Structure`)

---

### Module 2: Teacher Module (Process `2.0 Teacher Operations`)
* **Primary External Entity:** `Teacher` (Faculty Member)
* **Underlying Database Tables:** `teacher`, `class`, `section`, `student`, `student_score`, `subjects`
* **Core Functions:**
  1. Authenticates teacher login credentials against employee records.
  2. Retrieves assigned classes and grade levels (`classes.php`).
  3. Accesses enrolled student rosters for assigned classes (`students_of_class.php`, `student.php`).
  4. Records and modifies student scores and examination marks across semesters (`student-grade.php`).
* **Input Data Flows:**
  * `Teacher Login Credentials` (from `Teacher`)
  * `Student Marks & Exam Assessment Data` (from `Teacher`)
  * `Verify Teacher Auth & Assigned Classes` (from `D2 Teacher Records`)
  * `Fetch Subject & Class Details` (from `D4 Academic Structure`)
  * `Retrieve Enrolled Class Student Roster` (from `D3 Student Records`)
  * `Fetch Existing Scores` (from `D5 Scores & Academic Results`)
* **Output Data Flows:**
  * `Assigned Classes, Rosters & Score Confirmations` (to `Teacher`)
  * `Save / Update Student Scores` (to `D5 Scores & Academic Results`)

---

### Module 3: Student Module (Process `3.0 Student Portal`)
* **Primary External Entity:** `Student` (Learner / Enrollee)
* **Underlying Database Tables:** `student`, `student_score`, `grades`, `class`, `section`, `subjects`, `message`
* **Core Functions:**
  1. Authenticates student login credentials.
  2. Allows student to update/change portal login password (`pass.php`).
  3. Displays student demographic and enrollment profile (`index.php`).
  4. Displays academic evaluation, term scores, and results report card (`grade.php`).
  5. Allows students to send contact inquiries and feedback to administration (`home.php` contact form).
* **Input Data Flows:**
  * `Student Login Credentials & New Password` (from `Student`)
  * `Contact Messages & Feedback Inquiries` (from `Student`)
  * `Verify Student Auth & Profile Data` (from `D3 Student Records`)
  * `Fetch Enrolled Subject & Class Info` (from `D4 Academic Structure`)
  * `Read Academic Scores & Exam Results` (from `D5 Scores & Academic Results`)
* **Output Data Flows:**
  * `Student Profile, Enrolled Subjects & Grade Sheet` (to `Student`)
  * `Update Student Password` (to `D3 Student Records`)
  * `Save Inquiry & Message Record` (to `D6 Inquiries & Messages`)

---

### Module 4: Registrar Office Module (Process `4.0 Registrar Office Management`)
* **Primary External Entity:** `Registrar Office` (Admissions / Records Staff)
* **Underlying Database Tables:** `registrar_office`, `student`, `grades`, `section`, `class`
* **Core Functions:**
  1. Authenticates registrar officer credentials against staff roster.
  2. Processes new student admissions and enrollment registration (`student-add.php`).
  3. Assigns students to designated grades, sections, and classes.
  4. Performs student record searches and view demographic profiles (`student-search.php`, `student.php`, `student-view.php`).
* **Input Data Flows:**
  * `Staff Login Credentials` (from `Registrar Office`)
  * `New Student Admission Details & Query` (from `Registrar Office`)
  * `Verify Registrar Credentials` (from `D7 Registrar Staff Records`)
  * `Fetch Classes, Grades & Section Lists` (from `D4 Academic Structure`)
  * `Retrieve Student Demographic Records` (from `D3 Student Records`)
* **Output Data Flows:**
  * `Enrollment Confirmation & Search Results` (to `Registrar Office`)
  * `Register / Update Student Demographic Records` (to `D3 Student Records`)

---

## 4. Data Stores Reference (Physical to Logical Mapping)

| Store ID | Data Store Name | MySQL Tables Covered | Key Fields Stored |
|---|---|---|---|
| **D1** | **Admin & System Settings** | `admin`, `setting` | `admin_id`, `username`, `password`, `school_name`, `slogan`, `current_year`, `current_semester` |
| **D2** | **Teacher Records** | `teacher` | `teacher_id`, `username`, `class`, `subjets`, `gradeId`, `employee_number`, `qualification` |
| **D3** | **Student Records** | `student` | `student_id`, `username`, `fname`, `lname`, `grade`, `section`, `address`, `parent_phone_number` |
| **D4** | **Academic Structure** | `grades`, `section`, `class`, `subjects`, `courses` | `grade_id`, `grade_code`, `section_id`, `section`, `class_id`, `subject_id`, `course_name` |
| **D5** | **Scores & Academic Results** | `student_score` | `id`, `semester`, `year`, `student_id`, `teacher_id`, `subject_id`, `results` |
| **D6** | **Inquiries & Messages** | `message` | `message_id`, `sender_full_name`, `sender_email`, `message`, `date_time` |
| **D7** | **Registrar Staff Records** | `registrar_office` | `r_user_id`, `username`, `fname`, `lname`, `employee_number`, `qualification`, `email_address` |

---

## 5. DFD Structural Integrity Rules Validated

1. **No Entity-to-Entity Flows:** External entities never exchange data directly; all communication passes through a transformation process.
2. **No Entity-to-Data Store Flows:** External entities cannot directly read or write to data stores; all updates are validated by processes (`1.0`, `2.0`, `3.0`, `4.0`).
3. **No Store-to-Store Flows:** Data cannot move between stores without process logic.
4. **Conservation of Data (No Black Holes or Miracles):** Every process has both defined incoming and outgoing flows with clear noun-phrase descriptors.
5. **No UML Stereotypes:** Uses exclusively standard DFD syntax (circles/rounded rectangles, parallel/open boxes, sharp entity rectangles, directional flow arrows).

---

## 6. How to Open and Edit in Draw.io

1. **Option A: Web Browser ([app.diagrams.net](https://app.diagrams.net/))**
   - Go to [https://app.diagrams.net/](https://app.diagrams.net/)
   - Click **Open Existing Diagram**
   - Select `school_management_dfd_level1.drawio` from `c:\xampp\htdocs\school-management\`
   - You will see two tabs at the bottom:
     - `DFD Level 1 (Gane & Sarson Notation)`
     - `DFD Level 1 (Yourdon & DeMarco Notation)`

2. **Option B: VS Code Extension**
   - Install the **Draw.io Integration** extension by *Henning Dieterichs*.
   - Click on `school_management_dfd_level1.drawio` in VS Code file explorer.
   - The interactive canvas will render immediately.

3. **Option C: Immediate In-Browser Preview**
   - Open [`dfd_level1_viewer.html`](file:///c:/xampp/htdocs/school-management/dfd_level1_viewer.html) in your browser (Chrome/Edge/Firefox) to view both diagrams side-by-side or tabbed with full resolution.
