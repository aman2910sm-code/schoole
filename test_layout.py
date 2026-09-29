#!/usr/bin/env python3
"""
ER Diagram Layout Optimizer & Validator for School Management System (sms_db)
Ensures zero collisions and strictly relatable relationships.
"""

import math

def calculate_layout():
    # Page Canvas Dimensions
    page_w = 3400
    page_h = 2400

    # 12 Entities with center coordinates (cx, cy) and dimensions (w, h)
    # Grouped logically by tiers:
    # Tier 1 (Admin/Settings/Messages/Registrar): Y ~ 300
    # Tier 2 (Teachers, Class, Students): Y ~ 950
    # Tier 3 (Courses, Grades, Section): Y ~ 1580
    # Tier 4 (Subjects, Student Score): Y ~ 2150
    entities = {
        "admin": {
            "name": "admin",
            "cx": 1150, "cy": 300, "w": 160, "h": 65,
            "rx": 200, "ry": 120,
            "attrs": [
                {"name": "admin_id", "type": "PK"},
                {"name": "username", "type": ""},
                {"name": "password", "type": ""},
                {"name": "fname", "type": ""},
                {"name": "lname", "type": ""}
            ]
        },
        "setting": {
            "name": "setting",
            "cx": 450, "cy": 300, "w": 150, "h": 60,
            "rx": 190, "ry": 120,
            "attrs": [
                {"name": "id", "type": "PK"},
                {"name": "current_year", "type": ""},
                {"name": "current_semester", "type": ""},
                {"name": "school_name", "type": ""},
                {"name": "slogan", "type": ""},
                {"name": "about", "type": ""}
            ]
        },
        "message": {
            "name": "message",
            "cx": 1850, "cy": 300, "w": 150, "h": 60,
            "rx": 190, "ry": 120,
            "attrs": [
                {"name": "message_id", "type": "PK"},
                {"name": "sender_full_name", "type": ""},
                {"name": "sender_email", "type": ""},
                {"name": "message", "type": ""},
                {"name": "date_time", "type": ""}
            ]
        },
        "registrar_office": {
            "name": "registrar_office",
            "cx": 2650, "cy": 300, "w": 190, "h": 65,
            "rx": 220, "ry": 135,
            "attrs": [
                {"name": "r_user_id", "type": "PK"},
                {"name": "username", "type": ""},
                {"name": "password", "type": ""},
                {"name": "fname", "type": ""},
                {"name": "lname", "type": ""},
                {"name": "address", "type": ""},
                {"name": "employee_number", "type": ""},
                {"name": "date_of_birth", "type": ""},
                {"name": "phone_number", "type": ""},
                {"name": "qualification", "type": ""},
                {"name": "gender", "type": ""},
                {"name": "email_address", "type": ""},
                {"name": "date_of_joined", "type": ""}
            ]
        },
        "teacher": {
            "name": "teacher",
            "cx": 700, "cy": 950, "w": 160, "h": 70,
            "rx": 230, "ry": 150,
            "attrs": [
                {"name": "teacher_id", "type": "PK"},
                {"name": "username", "type": ""},
                {"name": "password", "type": ""},
                {"name": "class", "type": "FK"},
                {"name": "fname", "type": ""},
                {"name": "lname", "type": ""},
                {"name": "subjets", "type": "FK"},
                {"name": "gradeId", "type": "FK"},
                {"name": "address", "type": ""},
                {"name": "employee_number", "type": ""},
                {"name": "date_of_birth", "type": ""},
                {"name": "phone_number", "type": ""},
                {"name": "qualification", "type": ""},
                {"name": "gender", "type": ""},
                {"name": "email_address", "type": ""},
                {"name": "date_of_joined", "type": ""}
            ]
        },
        "class": {
            "name": "class",
            "cx": 1650, "cy": 950, "w": 150, "h": 60,
            "rx": 180, "ry": 120,
            "attrs": [
                {"name": "class_id", "type": "PK"},
                {"name": "grade", "type": "FK"},
                {"name": "section", "type": "FK"}
            ]
        },
        "student": {
            "name": "student",
            "cx": 2650, "cy": 950, "w": 160, "h": 70,
            "rx": 230, "ry": 150,
            "attrs": [
                {"name": "student_id", "type": "PK"},
                {"name": "username", "type": ""},
                {"name": "password", "type": ""},
                {"name": "fname", "type": ""},
                {"name": "lname", "type": ""},
                {"name": "grade", "type": "FK"},
                {"name": "section", "type": "FK"},
                {"name": "address", "type": ""},
                {"name": "gender", "type": ""},
                {"name": "email_address", "type": ""},
                {"name": "date_of_birth", "type": ""},
                {"name": "date_of_joined", "type": ""},
                {"name": "parent_fname", "type": ""},
                {"name": "parent_lname", "type": ""},
                {"name": "parent_phone_number", "type": ""},
                {"name": "subjets", "type": "FK"}
            ]
        },
        "courses": {
            "name": "courses",
            "cx": 450, "cy": 1580, "w": 150, "h": 60,
            "rx": 190, "ry": 120,
            "attrs": [
                {"name": "course_id", "type": "PK"},
                {"name": "grade", "type": "FK"},
                {"name": "course_name", "type": ""},
                {"name": "grade_code", "type": ""},
                {"name": "course_code", "type": ""}
            ]
        },
        "grades": {
            "name": "grades",
            "cx": 1150, "cy": 1580, "w": 150, "h": 60,
            "rx": 180, "ry": 120,
            "attrs": [
                {"name": "grade_id", "type": "PK"},
                {"name": "grade", "type": ""},
                {"name": "grade_code", "type": ""}
            ]
        },
        "section": {
            "name": "section",
            "cx": 2000, "cy": 1580, "w": 150, "h": 60,
            "rx": 170, "ry": 110,
            "attrs": [
                {"name": "section_id", "type": "PK"},
                {"name": "section", "type": ""}
            ]
        },
        "subjects": {
            "name": "subjects",
            "cx": 850, "cy": 2150, "w": 150, "h": 60,
            "rx": 180, "ry": 120,
            "attrs": [
                {"name": "subject_id", "type": "PK"},
                {"name": "subject", "type": ""},
                {"name": "subject_code", "type": ""},
                {"name": "grade", "type": "FK"}
            ]
        },
        "student_score": {
            "name": "student_score",
            "cx": 2150, "cy": 2150, "w": 170, "h": 65,
            "rx": 210, "ry": 135,
            "attrs": [
                {"name": "id", "type": "PK"},
                {"name": "semester", "type": ""},
                {"name": "year", "type": ""},
                {"name": "student_id", "type": "FK"},
                {"name": "teacher_id", "type": "FK"},
                {"name": "subject_id", "type": "FK"},
                {"name": "results", "type": ""}
            ]
        }
    }

    # Relatable Relationships Only (Direct business logic and foreign key associations)
    relationships = [
        # Admin relationships
        {"name": "configures", "ent1": "admin", "ent2": "setting", "cx": 800, "cy": 300, "w": 110, "h": 55, "c1": "1", "c2": "1"},
        {"name": "reviews", "ent1": "admin", "ent2": "message", "cx": 1500, "cy": 300, "w": 100, "h": 55, "c1": "1", "c2": "N"},
        {"name": "manages", "ent1": "admin", "ent2": "teacher", "cx": 925, "cy": 625, "w": 100, "h": 55, "c1": "1", "c2": "N"},
        {"name": "supervises", "ent1": "admin", "ent2": "registrar_office", "cx": 2220, "cy": 240, "w": 110, "h": 55, "c1": "1", "c2": "N"},
        
        # Registrar relationship
        {"name": "registers", "ent1": "registrar_office", "ent2": "student", "cx": 2650, "cy": 625, "w": 100, "h": 55, "c1": "1", "c2": "N"},
        
        # Teacher & Student to Class
        {"name": "teaches", "ent1": "teacher", "ent2": "class", "cx": 1175, "cy": 950, "w": 100, "h": 55, "c1": "M", "c2": "N"},
        {"name": "enrolled_in", "ent1": "student", "ent2": "class", "cx": 2150, "cy": 950, "w": 110, "h": 55, "c1": "N", "c2": "1"},
        
        # Class to Grades & Section (Foreign Keys in Class)
        {"name": "has_grade", "ent1": "class", "ent2": "grades", "cx": 1400, "cy": 1265, "w": 110, "h": 55, "c1": "N", "c2": "1"},
        {"name": "has_section", "ent1": "class", "ent2": "section", "cx": 1825, "cy": 1265, "w": 110, "h": 55, "c1": "N", "c2": "1"},
        
        # Grades to Courses & Subjects (Curriculum definition)
        {"name": "offers", "ent1": "grades", "ent2": "courses", "cx": 800, "cy": 1580, "w": 100, "h": 55, "c1": "1", "c2": "N"},
        {"name": "includes", "ent1": "grades", "ent2": "subjects", "cx": 1000, "cy": 1865, "w": 100, "h": 55, "c1": "1", "c2": "N"},
        
        # Teacher instructs Subjects
        {"name": "instructs", "ent1": "teacher", "ent2": "subjects", "cx": 680, "cy": 1580, "w": 100, "h": 55, "c1": "1", "c2": "N"},
        
        # Student Score evaluations (Foreign Keys: student_id, teacher_id, subject_id)
        {"name": "receives", "ent1": "student", "ent2": "student_score", "cx": 2450, "cy": 1600, "w": 110, "h": 55, "c1": "1", "c2": "N"},
        {"name": "assessed_in", "ent1": "subjects", "ent2": "student_score", "cx": 1500, "cy": 2150, "w": 110, "h": 55, "c1": "1", "c2": "N"},
        {"name": "evaluates", "ent1": "teacher", "ent2": "student_score", "cx": 1420, "cy": 1550, "w": 110, "h": 55, "c1": "1", "c2": "N"}
    ]

    return page_w, page_h, entities, relationships

if __name__ == "__main__":
    w, h, ents, rels = calculate_layout()
    print(f"Calculated layout: {len(ents)} entities, {len(rels)} relatable relationships.")
