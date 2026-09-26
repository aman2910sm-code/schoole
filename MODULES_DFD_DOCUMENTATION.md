# Module Data Flow Diagrams (DFD) — Level 1 Functional Decomposition

This documentation covers the **Level 1 Functional Decomposition Data Flow Diagrams (DFDs)** for all modules of the **School Management System (`sms_db`)**.

The diagrams strictly mirror the **exact format and layout of your reference report image**:
- **Black & White / Grayscale Only:** Clean, professional academic report format without colors.
- **Left Column:** A single tall vertical **External Entity box** (sharp rectangle with vertical title).
- **Middle Column:** A vertical sequence of **Process Ovals** (`1.1`, `1.2`, etc.).
- **Right Column:** Open-ended **Data Store boxes** (`[   Table Name   `) aligned with each process.
- **Data Flow Arrows:**
  - **Upper line ($\rightarrow$):** Input data flow from Entity &rarr; Process, and Process &rarr; Data Store.
  - **Lower line ($\leftarrow$):** Output/Feedback flow from Data Store &rarr; Process, and Process &rarr; Entity.
- **Report Frame:** Professional double-line page border, header, centered subheader, figure caption, and page numbering.

---

## 1. Quick Access to Diagram Files

| Module | Draw.io File | Standalone Vector SVG | Interactive Web Viewer |
|---|---|---|---|
| **Admin Module** | [**`admin.drawio`**](file:///c:/xampp/htdocs/school-management/admin.drawio) <br>([`admin.drowio`](file:///c:/xampp/htdocs/school-management/admin.drowio)) | [**`admin_dfd.svg`**](file:///c:/xampp/htdocs/school-management/admin_dfd.svg) | [**`dfd_modules_viewer.html`**](file:///c:/xampp/htdocs/school-management/dfd_modules_viewer.html) (Tab 1) |
| **Teacher Module** | [**`teacher.drawio`**](file:///c:/xampp/htdocs/school-management/teacher.drawio) <br>([`teacher.drowio`](file:///c:/xampp/htdocs/school-management/teacher.drowio)) | [**`teacher_dfd.svg`**](file:///c:/xampp/htdocs/school-management/teacher_dfd.svg) | [**`dfd_modules_viewer.html`**](file:///c:/xampp/htdocs/school-management/dfd_modules_viewer.html) (Tab 2) |
| **Student Module** | [**`student.drawio`**](file:///c:/xampp/htdocs/school-management/student.drawio) <br>([`student.drowio`](file:///c:/xampp/htdocs/school-management/student.drowio)) | [**`student_dfd.svg`**](file:///c:/xampp/htdocs/school-management/student_dfd.svg) | [**`dfd_modules_viewer.html`**](file:///c:/xampp/htdocs/school-management/dfd_modules_viewer.html) (Tab 3) |
| **Registrar Module** | [**`registrar.drawio`**](file:///c:/xampp/htdocs/school-management/registrar.drawio) <br>([`registrar.drowio`](file:///c:/xampp/htdocs/school-management/registrar.drowio), [`registarar.drowio`](file:///c:/xampp/htdocs/school-management/registarar.drowio)) | [**`registrar_dfd.svg`**](file:///c:/xampp/htdocs/school-management/registrar_dfd.svg) | [**`dfd_modules_viewer.html`**](file:///c:/xampp/htdocs/school-management/dfd_modules_viewer.html) (Tab 4) |

---

## 2. Module Specifications

### 1. Admin Module (`admin.drawio` / `admin_dfd.svg`)
* **External Entity:** `ADMIN` (Tall left box)
* **Processes (Ovals) & Data Stores (Right Boxes):**
  1. `1.1 Login` &harr; `Admins Table` (`check admin` / `reply`, `login credentials` / `response`)
  2. `1.2 Manage Settings` &harr; `Settings Table` (`update settings` / `reply`, `school details` / `response`)
  3. `1.3 Manage Teachers` &harr; `Teachers Table` (`add/update/delete` / `reply`, `teacher details` / `response`)
  4. `1.4 Manage Registrar` &harr; `Registrar Table` (`add/update/delete` / `reply`, `registrar details` / `response`)
  5. `1.5 Manage Classes` &harr; `Class Table` (`add/update/delete` / `reply`, `class & grade details` / `response`)
  6. `1.6 Manage Courses` &harr; `Courses Table` (`add/update/delete` / `reply`, `course & subject data` / `response`)
  7. `1.7 View Inquiries` &harr; `Inquiries Table` (`view/status` / `reply`, `inquiry request` / `response`)
* **Figure Caption:** *Figure 6.1: Level 1 DFD of Admin Module*

---

### 2. Teacher Module (`teacher.drawio` / `teacher_dfd.svg`)
* **External Entity:** `TEACHER` (Tall left box)
* **Processes (Ovals) & Data Stores (Right Boxes):**
  1. `2.1 Login` &harr; `Teachers Table` (`check teacher` / `reply`, `login credentials` / `response`)
  2. `2.2 View Classes` &harr; `Class Table` (`fetch classes` / `reply`, `class request` / `response`)
  3. `2.3 View Students` &harr; `Students Table` (`fetch students` / `reply`, `roster request` / `response`)
  4. `2.4 Manage Scores` &harr; `Scores Table` (`add/update marks` / `reply`, `student marks data` / `response`)
  5. `2.5 Manage Profile` &harr; `Teachers Table` (`update profile` / `reply`, `profile update data` / `response`)
* **Figure Caption:** *Figure 6.2: Level 1 DFD of Teacher Module*

---

### 3. Student Module (`student.drawio` / `student_dfd.svg`)
* **External Entity:** `STUDENT` (Tall left box)
* **Processes (Ovals) & Data Stores (Right Boxes):**
  1. `3.1 Login` &harr; `Students Table` (`check student` / `reply`, `login credentials` / `response`)
  2. `3.2 View Profile` &harr; `Students Table` (`fetch details` / `reply`, `profile request` / `response`)
  3. `3.3 View Results` &harr; `Scores Table` (`fetch scores` / `reply`, `results request` / `response`)
  4. `3.4 Send Inquiry` &harr; `Inquiries Table` (`store inquiry` / `reply`, `inquiry details` / `response`)
  5. `3.5 Manage Password` &harr; `Students Table` (`update password` / `reply`, `password update data` / `response`)
* **Figure Caption:** *Figure 6.3: Level 1 DFD of Student Module*

---

### 4. Registrar Office Module (`registrar.drawio` / `registrar_dfd.svg`)
* **External Entity:** `REGISTRAR` (Tall left box)
* **Processes (Ovals) & Data Stores (Right Boxes):**
  1. `4.1 Login` &harr; `Registrar Table` (`check registrar` / `reply`, `login credentials` / `response`)
  2. `4.2 Student Admission` &harr; `Students Table` (`insert student` / `reply`, `admission details` / `response`)
  3. `4.3 Assign Class` &harr; `Class Table` (`update class` / `reply`, `class assign details` / `response`)
  4. `4.4 Search Students` &harr; `Students Table` (`fetch records` / `reply`, `search query` / `response`)
  5. `4.5 Manage Profile` &harr; `Registrar Table` (`update profile` / `reply`, `profile update data` / `response`)
* **Figure Caption:** *Figure 6.4: Level 1 DFD of Registrar Module*

---

## 3. How to View and Edit the Diagrams

1. **In-Browser Interactive Viewer:** Open [**`dfd_modules_viewer.html`**](file:///c:/xampp/htdocs/school-management/dfd_modules_viewer.html) directly in any browser. It displays the white report sheets side-by-side with tab buttons and quick `.drawio` download links.
2. **In Draw.io / Diagrams.net:** Go to [diagrams.net](https://app.diagrams.net/), select **Open Existing Diagram**, and open `admin.drawio`, `teacher.drawio`, `student.drawio`, or `registrar.drawio`.
3. **In VS Code:** Open any `.drawio` file directly with the Draw.io extension installed.
