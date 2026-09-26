# Entity-Relationship (ER) Diagram Documentation: School Management System & Reference Model

This documentation accompanies the **Chen ER Diagrams** created for your project. The diagram strictly adheres to the **Entity-Relationship notation standards** shown in your reference image:
- **Entity**: Rectangles
- **Relationship**: Diamonds
- **Attribute**: Ovals / Ellipses
- **Primary Key (PK)**: Underlined text inside Ovals
- **Connecting Lines**: Solid connector lines
- **Cardinality**: Explicit ratios (`1:1`, `1:N`, `M:N`)
- **No UML symbols** (no class boxes, no stereotype icons).

---

## 1. Diagram Files Summary

| File | Description | How to Open / View |
|---|---|---|
| [**`school_management_er_diagram.drawio`**](file:///c:/xampp/htdocs/school-management/school_management_er_diagram.drawio) | **Editable draw.io Multi-Page File** containing 3 distinct tabs:<br>• **Tab 1:** School Management System ERD (`sms_db`)<br>• **Tab 2:** Reference E-Commerce ERD (from image examples: User, Products, Orders, Cart)<br>• **Tab 3:** Exact Symbols Reference Table (editable draw.io shapes) | Open directly in [diagrams.net](https://app.diagrams.net/), Draw.io desktop app, or VS Code Draw.io extension. Fully editable shapes. |
| [**`sms_er_diagram.svg`**](file:///c:/xampp/htdocs/school-management/sms_er_diagram.svg) | Standalone vector graphic of the School Management System ERD | High-resolution; open in any browser or embed directly into college project documentation / PDF. |
| [**`ecommerce_er_diagram.svg`**](file:///c:/xampp/htdocs/school-management/ecommerce_er_diagram.svg) | Standalone vector graphic of the Reference E-Commerce ERD | High-resolution view of the example entities from the symbols reference. |
| [**`er_diagram_viewer.html`**](file:///c:/xampp/htdocs/school-management/er_diagram_viewer.html) | Interactive web viewer with tab switcher & quick download button | Double-click or open in your browser to inspect all diagrams interactively. |

---

## 2. Symbols Specification (Referencing Attached Image)

| Symbol Shape | Symbol Name | Meaning & Visual Representation |
|---|---|---|
| **Rectangle** | **Entity** | Represents a real-world object or database entity (e.g., `STUDENT`, `TEACHER`, `USER`). |
| **Diamond** | **Relationship** | Represents an association between two entities (e.g., `Admits`, `Teaches`, `Manages_Cart`). |
| **Oval / Ellipse** | **Attribute** | Represents a property, field, or characteristic of an entity (e.g., `username`, `email`, `fname`). |
| **Underlined Oval** | **Primary Key Attribute** | Unique identifier for an entity with text underlined (e.g., `<u>student_id</u>`, `<u>user_id</u>`). |
| **Solid Line** | **Connecting Line** | Links an entity to its attributes, or an entity to a relationship diamond. |
| **1, N, M Labels** | **Cardinality Ratio** | Quantifies relationship multiplicity (`1:1` one-to-one, `1:N` one-to-many, `M:N` many-to-many). |

---

## 3. Tab 1: School Management System ER Diagram (`sms_db`)

The School Management System ER diagram maps directly to your active MySQL database (`sms_db`) and data dictionary.

### Entities & Attributes

| Entity | Primary Key (PK) | Attributes | Description |
|---|---|---|---|
| **`ADMIN`** | `<u>admin_id</u>` | `username`, `password`, `fname`, `lname` | System administrator overseeing school configuration and users. |
| **`SETTING`** | `<u>id</u>` | `school_name`, `slogan`, `about`, `current_year`, `current_semester` | Institutional identity and global academic calendar config. |
| **`MESSAGE`** | `<u>message_id</u>` | `sender_full_name`, `sender_email`, `message`, `date_time` | Public/student contact queries and feedback sent to admin. |
| **`TEACHER`** | `<u>teacher_id</u>` | `username`, `password`, `fname`, `lname`, `employee_no`, `qualification`, `phone_number`, `email_address`, `gender`, `address` | Faculty staff handling classes, subjects, and student evaluations. |
| **`REGISTRAR_OFFICE`**| `<u>r_user_id</u>` | `username`, `password`, `fname`, `lname`, `employee_no`, `qualification`, `phone_number`, `email_address` | Staff in charge of admissions, enrollments, and demographic records. |
| **`STUDENT`** | `<u>student_id</u>` | `username`, `password`, `fname`, `lname`, `gender`, `email_address`, `address`, `date_of_birth`, `parent_fname`, `parent_phone` | Enrolled learner attending classes and receiving term scores. |
| **`CLASS`** | `<u>class_id</u>` | `grade` (FK), `section` (FK) | Academic classroom division uniting a Grade and a Section. |
| **`GRADE`** | `<u>grade_id</u>` | `grade`, `grade_code` | Academic grade level tier (e.g., Grade 1, Grade 2, KG). |
| **`SECTION`** | `<u>section_id</u>` | `section` | Division within a grade (e.g., Section A, B, C, D). |
| **`SUBJECTS`** | `<u>subject_id</u>` | `subject`, `subject_code`, `grade` (FK) | Course syllabus taught by teachers in specific grades. |
| **`STUDENT_SCORE`** | `<u>id</u>` | `semester`, `year`, `results`, `student_id` (FK), `teacher_id` (FK), `subject_id` (FK) | Term exam evaluations, test marks, and academic grades. |

---

### Relationships & Cardinality Matrix

| Relationship Diamond | Entity 1 | Entity 2 | Cardinality | Business Rule / Description |
|---|---|---|---|---|
| **`Configures`** | `ADMIN` (1) | `SETTING` (1) | **1 : 1** | One administrator manages the global school institutional configuration. |
| **`Reviews`** | `ADMIN` (1) | `MESSAGE` (N) | **1 : N** | One administrator reviews multiple incoming feedback messages. |
| **`Manages`** | `ADMIN` (1) | `TEACHER` (N) | **1 : N** | Administration provisions and manages multiple faculty accounts. |
| **`Supervises`** | `ADMIN` (1) | `REGISTRAR_OFFICE` (N) | **1 : N** | Administration oversees registrar officer accounts. |
| **`Admits`** | `REGISTRAR_OFFICE` (1) | `STUDENT` (N) | **1 : N** | Registrar office admits and enrolls multiple students. |
| **`Teaches`** | `TEACHER` (M) | `CLASS` (N) | **M : N** | Multiple teachers instruct across multiple assigned classes. |
| **`Enrolled_In`** | `STUDENT` (N) | `CLASS` (1) | **N : 1** | Multiple students belong to one specific classroom group. |
| **`Comprises`** | `CLASS` (N) | `GRADE` (1) | **N : 1** | Each class belongs to one designated academic Grade level. |
| **`Divides`** | `CLASS` (N) | `SECTION` (1) | **N : 1** | Each class is partitioned into one designated Section letter. |
| **`Curriculum_Of`** | `GRADE` (1) | `SUBJECTS` (N) | **1 : N** | One grade level curriculum contains multiple academic subjects. |
| **`Instructs`** | `TEACHER` (1) | `SUBJECTS` (N) | **1 : N** | Teachers specialize in and teach one or more subjects. |
| **`Assessed_In`** | `SUBJECTS` (1) | `STUDENT_SCORE` (N) | **1 : N** | A subject has multiple score records recorded across terms. |
| **`Receives`** | `STUDENT` (1) | `STUDENT_SCORE` (N) | **1 : N** | Each student receives multiple exam score reports. |
| **`Evaluates`** | `TEACHER` (1) | `STUDENT_SCORE` (N) | **1 : N** | Teachers evaluate and enter test results for students. |

---

## 4. Tab 2: Reference E-Commerce ER Diagram (Image Examples)

Constructed directly using the sample entities, relationships, and attributes specified in the reference image examples:

* **Entities**:
  * **`USER`**: `<u>user_id</u>` (PK), `name`, `email`, `password`, `address`
  * **`CART`**: `<u>cart_id</u>` (PK), `created_at`
  * **`PRODUCTS`**: `<u>product_id</u>` (PK), `name`, `price`, `description`, `stock`
  * **`ORDERS`**: `<u>order_id</u>` (PK), `order_date`, `total_amount`, `status`
* **Relationships**:
  * **`Manages_Cart`**: `USER` (1) &mdash; `CART` (1)
  * **`Contains_Item`**: `CART` (M) &mdash; `PRODUCTS` (N) with associative attribute `quantity`
  * **`Places_Order`**: `USER` (1) &mdash; `ORDERS` (N)
  * **`Includes_Item`**: `ORDERS` (M) &mdash; `PRODUCTS` (N)

---

## 5. Tab 3: Exact Symbols Table Recreated

A complete, editable replica of the reference table **"Symbols Used in the Above ER Diagram"** has been recreated with editable draw.io shapes inside Tab 3 of [`school_management_er_diagram.drawio`](file:///c:/xampp/htdocs/school-management/school_management_er_diagram.drawio).

---

## 6. How to Open and Edit in Draw.io

1. **Option A: Diagrams.net Online**
   - Visit [https://app.diagrams.net/](https://app.diagrams.net/).
   - Click **Open Existing Diagram**.
   - Browse and select [`school_management_er_diagram.drawio`](file:///c:/xampp/htdocs/school-management/school_management_er_diagram.drawio).
   - Click through the tabs at the bottom:
     - `School Management System ERD`
     - `Reference E-Commerce ERD`
     - `ER Diagram Symbols Reference`

2. **Option B: VS Code Extension**
   - Install the **Draw.io Integration** extension.
   - Click on `school_management_er_diagram.drawio` to open the interactive canvas.

3. **Option C: Interactive In-Browser Viewer**
   - Open [`er_diagram_viewer.html`](file:///c:/xampp/htdocs/school-management/er_diagram_viewer.html) in Chrome/Edge/Firefox to review high-definition vector renders with tab switching and instant file download.
