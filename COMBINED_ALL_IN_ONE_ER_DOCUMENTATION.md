# Unified Entity-Relationship (ER) Documentation: School Management System (`sms_db`)

This documentation accompanies the **Single, Unified All-In-One ER Diagram** created for the **School Management System (`sms_db`)**.

All **12 database tables** have been combined into a **single, unified ER diagram** on one canvas, with complete modeling of all **Primary Key (PK)** and **Foreign Key (FK)** relationships in **Peter Chen's ER Notation**.

---

## 1. Quick Access to Files

| File | Description | How to Open / View |
|---|---|---|
| [**`combined_all_in_one.drawio`**](file:///c:/xampp/htdocs/school-management/combined_all_in_one.drawio) <br>([`school_management_combined_all_in_one.drawio`](file:///c:/xampp/htdocs/school-management/school_management_combined_all_in_one.drawio)) | **Editable draw.io Diagram File** containing all 12 tables and 17 relationships on one unified canvas | Open directly in [diagrams.net](https://app.diagrams.net/), Draw.io desktop app, or VS Code. Fully editable shapes. |
| [**`combined_all_in_one_er.svg`**](file:///c:/xampp/htdocs/school-management/combined_all_in_one_er.svg) | High-resolution standalone vector graphic (SVG) of the single ER diagram | Open in any browser or embed directly into college project reports and documentation. |
| [**`combined_er_viewer.html`**](file:///c:/xampp/htdocs/school-management/combined_er_viewer.html) | Interactive full-screen web viewer with zoom, pan, and direct download buttons | Double-click or open in your browser to inspect the entire diagram with zero loss of quality. |

---

## 2. Diagram Notation & Standards

The diagram strictly conforms to the **reference notation standards**:
- **Format:** **Pure Black & White** (No colors, strictly compliant with college project documentation standards).
- **Entity:** **Rectangles** with bold capitalized entity names.
- **Relationship:** **Diamonds** placed in corridors connecting associated entities.
- **Attributes:** **Ovals / Ellipses** radiating outward around each entity.
- **Primary Key (PK):** Highlighted with bold, underlined text and `(PK)` suffix inside a heavy oval border (e.g., `<u>student_id (PK)</u>`).
- **Foreign Key (FK):** Marked with `(FK)` suffix inside a dashed-border oval (e.g., `grade (FK)`).
- **Connecting Lines:** Solid lines connecting entities to attributes, and entities to relationship diamonds.
- **Cardinality Ratios:** Explicitly labeled multiplicity ratios (`1:1`, `1:N`, `M:N`).

---

## 3. Complete Inventory: All 12 Tables, PKs, and FKs

| # | Table / Entity | Primary Key (PK) | Foreign Keys (FK) & Referencing Tables | All Attributes | Description |
|---|---|---|---|---|---|
| 1 | **`admin`** | `admin_id` | *None* | `admin_id (PK)`, `username`, `password`, `fname`, `lname` | Institutional administrators with top-level system authority. |
| 2 | **`setting`** | `id` | *None* | `id (PK)`, `current_year`, `current_semester`, `school_name`, `slogan`, `about` | Global school identity, active year, and semester config. |
| 3 | **`message`** | `message_id` | *None* | `message_id (PK)`, `sender_full_name`, `sender_email`, `message`, `date_time` | Inquiries and feedback messages submitted by visitors/students. |
| 4 | **`registrar_office`** | `r_user_id` | *None* | `r_user_id (PK)`, `username`, `password`, `fname`, `lname`, `address`, `employee_number`, `date_of_birth`, `phone_number`, `qualification`, `gender`, `email_address`, `date_of_joined` | Staff accounts managing student admissions and records. |
| 5 | **`teacher`** | `teacher_id` | `class` &rarr; `class.class_id`<br>`subjets` &rarr; `subjects.subject_id`<br>`gradeId` &rarr; `grades.grade_id` | `teacher_id (PK)`, `username`, `password`, `class (FK)`, `fname`, `lname`, `subjets (FK)`, `gradeId (FK)`, `address`, `employee_number`, `date_of_birth`, `phone_number`, `qualification`, `gender`, `email_address`, `date_of_joined` | Faculty staff handling instructional classes and student grading. |
| 6 | **`class`** | `class_id` | `grade` &rarr; `grades.grade_id`<br>`section` &rarr; `section.section_id` | `class_id (PK)`, `grade (FK)`, `section (FK)` | Classroom cohorts uniting a Grade tier and a Section letter. |
| 7 | **`student`** | `student_id` | `grade` &rarr; `grades.grade_id`<br>`section` &rarr; `section.section_id`<br>`subjets` &rarr; `subjects.subject_id` | `student_id (PK)`, `username`, `password`, `fname`, `lname`, `grade (FK)`, `section (FK)`, `address`, `gender`, `email_address`, `date_of_birth`, `date_of_joined`, `parent_fname`, `parent_lname`, `parent_phone_number`, `subjets (FK)` | Enrolled learners attending classes and receiving evaluations. |
| 8 | **`courses`** | `course_id` | `grade` &rarr; `grades.grade_id` | `course_id (PK)`, `grade (FK)`, `course_name`, `grade_code`, `course_code` | Academic course offerings linked to grade categories. |
| 9 | **`grades`** | `grade_id` | *None* | `grade_id (PK)`, `grade`, `grade_code` | Academic grade standards (e.g., 'G-1', 'KG-2'). |
| 10 | **`section`** | `section_id` | *None* | `section_id (PK)`, `section` | Division letters (e.g., 'A', 'B', 'C', 'D'). |
| 11 | **`subjects`** | `subject_id` | `grade` &rarr; `grades.grade_id` | `subject_id (PK)`, `subject`, `subject_code`, `grade (FK)` | Academic subjects taught across curriculum levels. |
| 12 | **`student_score`** | `id` | `student_id` &rarr; `student.student_id`<br>`teacher_id` &rarr; `teacher.teacher_id`<br>`subject_id` &rarr; `subjects.subject_id` | `id (PK)`, `semester`, `year`, `student_id (FK)`, `teacher_id (FK)`, `subject_id (FK)`, `results` | Examination marks and evaluation results recorded per student. |

---

## 4. Comprehensive Matrix of All 17 Relationships

Every PK and FK relationship is explicitly modeled with relationship diamonds and multiplicity ratios:

| # | Relationship Diamond | Entity 1 | Entity 2 | Cardinality | Underlying Foreign Key / Semantic Link |
|---|---|---|---|---|---|
| 1 | **`configures`** | `admin` (1) | `setting` (1) | **1 : 1** | One administrator manages the global institutional settings. |
| 2 | **`reviews`** | `admin` (1) | `message` (N) | **1 : N** | Administrator reviews public inquiries and feedback. |
| 3 | **`manages`** | `admin` (1) | `teacher` (N) | **1 : N** | Administrator provisions and oversees teacher accounts. |
| 4 | **`supervises`** | `admin` (1) | `registrar_office` (N) | **1 : N** | Administrator creates and oversees registrar staff accounts. |
| 5 | **`registers`** | `registrar_office` (1) | `student` (N) | **1 : N** | Registrar staff admits and enrolls students into the school. |
| 6 | **`teaches`** | `teacher` (M) | `class` (N) | **M : N** | Faculty teachers instruct multiple assigned class groups (`teacher.class`). |
| 7 | **`enrolled_in`** | `student` (N) | `class` (1) | **N : 1** | Multiple students belong to one instructional class cohort. |
| 8 | **`class_grade`** | `class` (N) | `grades` (1) | **N : 1** | Foreign key: `class.grade` &rarr; `grades.grade_id`. |
| 9 | **`class_section`** | `class` (N) | `section` (1) | **N : 1** | Foreign key: `class.section` &rarr; `section.section_id`. |
| 10 | **`student_grade`** | `student` (N) | `grades` (1) | **N : 1** | Foreign key: `student.grade` &rarr; `grades.grade_id`. |
| 11 | **`student_section`** | `student` (N) | `section` (1) | **N : 1** | Foreign key: `student.section` &rarr; `section.section_id`. |
| 12 | **`defines_course`** | `grades` (1) | `courses` (N) | **1 : N** | Foreign key: `courses.grade` &rarr; `grades.grade_id`. |
| 13 | **`curriculum_for`** | `grades` (1) | `subjects` (N) | **1 : N** | Foreign key: `subjects.grade` &rarr; `grades.grade_id`. |
| 14 | **`instructs`** | `teacher` (1) | `subjects` (N) | **1 : N** | Logical key: `teacher.subjets` &rarr; `subjects.subject_id`. |
| 15 | **`receives_score`** | `student` (1) | `student_score` (N) | **1 : N** | Foreign key: `student_score.student_id` &rarr; `student.student_id`. |
| 16 | **`grades_score`** | `teacher` (1) | `student_score` (N) | **1 : N** | Foreign key: `student_score.teacher_id` &rarr; `teacher.teacher_id`. |
| 17 | **`scored_in`** | `subjects` (1) | `student_score` (N) | **1 : N** | Foreign key: `student_score.subject_id` &rarr; `subjects.subject_id`. |

---

## 5. How to Open and Edit in Draw.io / diagrams.net

1. **Option A: Web Browser ([app.diagrams.net](https://app.diagrams.net/))**
   - Go to [https://app.diagrams.net/](https://app.diagrams.net/).
   - Click **Open Existing Diagram**.
   - Select [`combined_all_in_one.drawio`](file:///c:/xampp/htdocs/school-management/combined_all_in_one.drawio).
   - The complete diagram with all 12 tables and 17 relationships opens on a single canvas. All shapes, text, ovals, and lines are fully editable.

2. **Option B: VS Code Extension**
   - Install the **Draw.io Integration** extension.
   - Click on `combined_all_in_one.drawio` in the VS Code file tree.

3. **Option C: Interactive In-Browser Viewer**
   - Open [`combined_er_viewer.html`](file:///c:/xampp/htdocs/school-management/combined_er_viewer.html) in your browser (Chrome/Edge/Firefox) for full-screen inspection with zoom controls and instant file download.
