#!/usr/bin/env python3
"""
Unified Single ER Diagram Generator for School Management System (sms_db)
Adheres strictly to the user reference image symbols:
- Entity: Rectangle
- Relationship: Diamond / Rhombus
- Attribute: Oval / Ellipse
- Primary Key Attribute: Oval with underlined text <u>attribute_id</u> (PK)
- Foreign Key Attribute: Oval with dashed border (FK)
- Connecting Lines: Solid lines with Cardinality (1:1, 1:N, M:N)
- Relatable Relations Only: 15 logical, non-redundant, cleanly routed relations
- Pure Black & White (College Project Documentation Standard)
"""

import os
import math
import xml.etree.ElementTree as ET

def get_orbit_positions(cx, cy, count, rx, ry):
    """
    Distributes attribute ovals around a central entity (cx, cy)
    using elliptical offset calculation with generous spacing to guarantee 0 overlaps.
    """
    positions = []
    
    if count == 16:  # teacher & student (16 attributes: 5 top, 5 bottom, 3 left, 3 right)
        # 5 top with 150px spacing
        for i in range(5):
            positions.append((cx - 300 + i * 150, cy - ry - 35))
        # 3 right with 65px vertical spacing
        for i in range(3):
            positions.append((cx + rx + 85, cy - 65 + i * 65))
        # 5 bottom with 150px spacing
        for i in range(5):
            positions.append((cx - 300 + i * 150, cy + ry + 35))
        # 3 left with 65px vertical spacing
        for i in range(3):
            positions.append((cx - rx - 85, cy - 65 + i * 65))
            
    elif count == 13:  # registrar_office (13 attributes: 4 top, 4 bottom, 2 left, 3 right)
        for i in range(4):
            positions.append((cx - 240 + i * 160, cy - ry - 35))
        for i in range(3):
            positions.append((cx + rx + 85, cy - 65 + i * 65))
        for i in range(4):
            positions.append((cx - 240 + i * 160, cy + ry + 35))
        for i in range(2):
            positions.append((cx - rx - 85, cy - 35 + i * 70))
            
    elif count == 7:  # student_score (7 attributes)
        for i in range(3):
            positions.append((cx - 160 + i * 160, cy - ry - 30))
        positions.append((cx + rx + 85, cy))
        for i in range(3):
            positions.append((cx + 160 - i * 160, cy + ry + 30))
            
    elif count == 6:  # setting (6 attributes: 3 top, 3 bottom)
        for i in range(3):
            positions.append((cx - 160 + i * 160, cy - ry - 30))
        for i in range(3):
            positions.append((cx + 160 - i * 160, cy + ry + 30))
            
    elif count == 5:  # admin, message, courses (5 attributes)
        positions.append((cx - 110, cy - ry - 25))
        positions.append((cx + 110, cy - ry - 25))
        positions.append((cx - rx - 70, cy))
        positions.append((cx - 110, cy + ry + 25))
        positions.append((cx + 110, cy + ry + 25))
        
    elif count == 4:  # subjects (4 attributes)
        positions.append((cx - 110, cy - ry - 25))
        positions.append((cx + 110, cy - ry - 25))
        positions.append((cx + 110, cy + ry + 25))
        positions.append((cx - 110, cy + ry + 25))
        
    elif count == 3:  # grades, class (3 attributes)
        positions.append((cx - 110, cy - ry - 25))
        positions.append((cx + 110, cy - ry - 25))
        positions.append((cx, cy + ry + 25))
        
    elif count == 2:  # section (2 attributes)
        positions.append((cx - 85, cy - ry - 25))
        positions.append((cx + 85, cy - ry - 25))
        
    else:
        for i in range(count):
            angle = (2 * math.pi * i) / count - math.pi / 2
            x = cx + rx * math.cos(angle)
            y = cy + ry * math.sin(angle)
            positions.append((x, y))
            
    return positions


def get_all_tables_data():
    """
    Returns complete specifications for all 12 tables and 15 relatable relationships.
    Canvas: 3500 x 2500
    """
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
            "cx": 400, "cy": 300, "w": 150, "h": 60,
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
            "cx": 2700, "cy": 300, "w": 190, "h": 65,
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
            "cx": 2700, "cy": 950, "w": 160, "h": 70,
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
        # 1. Admin configures System Setting (1 : 1)
        {"name": "configures", "ent1": "admin", "ent2": "setting", "cx": 750, "cy": 300, "w": 110, "h": 55, "c1": "1", "c2": "1"},
        
        # 2. Admin reviews Visitor Messages (1 : N)
        {"name": "reviews", "ent1": "admin", "ent2": "message", "cx": 1500, "cy": 300, "w": 100, "h": 55, "c1": "1", "c2": "N"},
        
        # 3. Admin manages Teachers (1 : N)
        {"name": "manages", "ent1": "admin", "ent2": "teacher", "cx": 925, "cy": 625, "w": 100, "h": 55, "c1": "1", "c2": "N"},
        
        # 4. Admin supervises Registrar Office (1 : N)
        {"name": "supervises", "ent1": "admin", "ent2": "registrar_office", "cx": 2250, "cy": 180, "w": 110, "h": 55, "c1": "1", "c2": "N"},
        
        # 5. Registrar registers Students (1 : N)
        {"name": "registers", "ent1": "registrar_office", "ent2": "student", "cx": 2700, "cy": 625, "w": 100, "h": 55, "c1": "1", "c2": "N"},
        
        # 6. Teacher teaches Class (M : N)
        {"name": "teaches", "ent1": "teacher", "ent2": "class", "cx": 1175, "cy": 950, "w": 100, "h": 55, "c1": "M", "c2": "N"},
        
        # 7. Student enrolled in Class (N : 1)
        {"name": "enrolled_in", "ent1": "student", "ent2": "class", "cx": 2150, "cy": 950, "w": 110, "h": 55, "c1": "N", "c2": "1"},
        
        # 8. Class has Grade (N : 1) - FK: class.grade -> grades.grade_id
        {"name": "has_grade", "ent1": "class", "ent2": "grades", "cx": 1400, "cy": 1265, "w": 110, "h": 55, "c1": "N", "c2": "1"},
        
        # 9. Class has Section (N : 1) - FK: class.section -> section.section_id
        {"name": "has_section", "ent1": "class", "ent2": "section", "cx": 1825, "cy": 1265, "w": 110, "h": 55, "c1": "N", "c2": "1"},
        
        # 10. Grades offers Courses (1 : N) - FK: courses.grade -> grades.grade_id
        {"name": "offers", "ent1": "grades", "ent2": "courses", "cx": 800, "cy": 1580, "w": 100, "h": 55, "c1": "1", "c2": "N"},
        
        # 11. Grades includes Subjects (1 : N) - FK: subjects.grade -> grades.grade_id
        {"name": "includes", "ent1": "grades", "ent2": "subjects", "cx": 1000, "cy": 1865, "w": 100, "h": 55, "c1": "1", "c2": "N"},
        
        # 12. Teacher instructs Subjects (M : N) - FK: teacher.subjets -> subjects.subject_id
        {"name": "instructs", "ent1": "teacher", "ent2": "subjects", "cx": 680, "cy": 1580, "w": 100, "h": 55, "c1": "M", "c2": "N"},
        
        # 13. Student receives Score (1 : N) - FK: student_score.student_id -> student.student_id
        {"name": "receives", "ent1": "student", "ent2": "student_score", "cx": 2450, "cy": 1600, "w": 110, "h": 55, "c1": "1", "c2": "N"},
        
        # 14. Subjects evaluated in Score (1 : N) - FK: student_score.subject_id -> subjects.subject_id
        {"name": "assessed_in", "ent1": "subjects", "ent2": "student_score", "cx": 1500, "cy": 2150, "w": 110, "h": 55, "c1": "1", "c2": "N"},
        
        # 15. Teacher evaluates Score (1 : N) - FK: student_score.teacher_id -> teacher.teacher_id
        {"name": "evaluates", "ent1": "teacher", "ent2": "student_score", "cx": 1420, "cy": 1550, "w": 110, "h": 55, "c1": "1", "c2": "N"}
    ]

    return {
        "page_w": 3500,
        "page_h": 2500,
        "entities": entities,
        "relationships": relationships
    }


def build_unified_drawio_xml():
    """
    Builds the complete, 100% valid Draw.io XML for diagrams.net.
    Conforms to Peter Chen ER standard with exact symbol definitions:
    1. Entities (Rectangles)
    2. Attributes (Ovals with Underline for PK, dashed for FK)
    3. Relationships (Diamonds)
    4. Connecting lines with Cardinality
    5. Legend bar
    """
    data = get_all_tables_data()
    entities = data["entities"]
    relationships = data["relationships"]
    page_w = data["page_w"]
    page_h = data["page_h"]

    lines = []
    lines.append('<mxfile host="app.diagrams.net" modified="2026-09-29T00:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">')
    lines.append('  <diagram id="unified-sms-er" name="School Management System ERD">')
    lines.append(f'    <mxGraphModel dx="2800" dy="2000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{page_w}" pageHeight="{page_h}" background="#FFFFFF" math="0" shadow="0">')
    lines.append('      <root>')
    lines.append('        <mxCell id="0" />')
    lines.append('        <mxCell id="1" parent="0" />')

    # Top Header Title Banner
    lines.append('        <!-- ================= TITLE BANNER ================= -->')
    lines.append(f'        <mxCell id="title_banner" value="&lt;b style=&quot;font-size: 20px;&quot;&gt;UNIFIED ENTITY-RELATIONSHIP (ER) DIAGRAM — SCHOOL MANAGEMENT SYSTEM (sms_db)&lt;/b&gt;&lt;br/&gt;&lt;span style=&quot;font-size: 13px; color: #333333;&quot;&gt;Complete Relational Architecture Covering All 12 Database Tables | Peter Chen Notation Standard | Pure Black &amp;amp; White (College Project Documentation)&lt;/span&gt;" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2.5;fontColor=#000000;align=center;verticalAlign=middle;rounded=0;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="60" y="30" width="{page_w - 120}" height="70" as="geometry" />')
    lines.append('        </mxCell>')

    # 1. ENTITY VERTICES
    lines.append('        <!-- ================= ENTITY VERTICES ================= -->')
    for ename, edata in entities.items():
        eid = f"ent_{ename}"
        ex = edata["cx"] - edata["w"] // 2
        ey = edata["cy"] - edata["h"] // 2
        ew = edata["w"]
        eh = edata["h"]
        lines.append(f'        <mxCell id="{eid}" value="&lt;b&gt;{ename.upper()}&lt;/b&gt;" style="shape=rectangle;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2.5;fontColor=#000000;fontSize=15;align=center;verticalAlign=middle;" vertex="1" parent="1">')
        lines.append(f'          <mxGeometry x="{ex}" y="{ey}" width="{ew}" height="{eh}" as="geometry" />')
        lines.append('        </mxCell>')

    # 2. ATTRIBUTE VERTICES
    lines.append('        <!-- ================= ATTRIBUTE VERTICES ================= -->')
    for ename, edata in entities.items():
        attrs = edata["attrs"]
        positions = get_orbit_positions(edata["cx"], edata["cy"], len(attrs), edata["rx"], edata["ry"])
        for aidx, attr in enumerate(attrs):
            aid = f"att_{ename}_{aidx}_{attr['name']}"
            ax, ay = positions[aidx]
            aname = attr["name"]
            atype = attr["type"]

            # Reference Image style: PK is underlined; FK has dashed border
            if atype == "PK":
                label = f"&lt;u&gt;&lt;b&gt;{aname}&lt;/b&gt; (PK)&lt;/u&gt;"
                astyle = "shape=ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2.5;fontSize=11;fontColor=#000000;align=center;verticalAlign=middle;"
                aw = max(95, len(aname) * 8 + 42)
            elif atype == "FK":
                label = f"{aname} (FK)"
                astyle = "shape=ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontSize=11;fontColor=#000000;strokeDasharray=3 3;align=center;verticalAlign=middle;"
                aw = max(85, len(aname) * 8 + 36)
            else:
                label = aname
                astyle = "shape=ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;fontColor=#000000;align=center;verticalAlign=middle;"
                aw = max(75, len(aname) * 8 + 26)

            ah = 36
            acx = int(ax - aw / 2)
            acy = int(ay - ah / 2)

            lines.append(f'        <mxCell id="{aid}" value="{label}" style="{astyle}" vertex="1" parent="1">')
            lines.append(f'          <mxGeometry x="{acx}" y="{acy}" width="{aw}" height="{ah}" as="geometry" />')
            lines.append('        </mxCell>')

    # 3. RELATIONSHIP VERTICES (Diamonds)
    lines.append('        <!-- ================= RELATIONSHIP VERTICES ================= -->')
    for idx, rel in enumerate(relationships):
        rid = f"rel_{idx}_{rel['name']}"
        rx = int(rel["cx"] - rel["w"] / 2)
        ry = int(rel["cy"] - rel["h"] / 2)
        rname = rel["name"]
        lines.append(f'        <mxCell id="{rid}" value="&lt;b&gt;{rname}&lt;/b&gt;" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=middle;" vertex="1" parent="1">')
        lines.append(f'          <mxGeometry x="{rx}" y="{ry}" width="{rel["w"]}" height="{rel["h"]}" as="geometry" />')
        lines.append('        </mxCell>')

    # 4. ATTRIBUTE CONNECTING LINES (Edges)
    lines.append('        <!-- ================= ATTRIBUTE CONNECTING LINES ================= -->')
    for ename, edata in entities.items():
        eid = f"ent_{ename}"
        attrs = edata["attrs"]
        for aidx, attr in enumerate(attrs):
            aid = f"att_{ename}_{aidx}_{attr['name']}"
            lines.append(f'        <mxCell id="line_{aid}" style="endArrow=none;strokeColor=#000000;strokeWidth=1.2;" edge="1" parent="1" source="{eid}" target="{aid}">')
            lines.append('          <mxGeometry relative="1" as="geometry" />')
            lines.append('        </mxCell>')

    # 5. RELATIONSHIP CONNECTING LINES (Edges with Cardinality)
    lines.append('        <!-- ================= RELATIONSHIP CONNECTING LINES ================= -->')
    for idx, rel in enumerate(relationships):
        rid = f"rel_{idx}_{rel['name']}"
        e1_id = f"ent_{rel['ent1']}"
        e2_id = f"ent_{rel['ent2']}"
        c1 = rel.get("c1", "1")
        c2 = rel.get("c2", "N")

        # Line from ent1 to relationship diamond
        lines.append(f'        <mxCell id="line_{rid}_1" value="{c1}" style="endArrow=none;strokeColor=#000000;strokeWidth=1.8;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;fontColor=#000000;" edge="1" parent="1" source="{e1_id}" target="{rid}">')
        lines.append('          <mxGeometry relative="1" as="geometry" />')
        lines.append('        </mxCell>')

        # Line from relationship diamond to ent2
        lines.append(f'        <mxCell id="line_{rid}_2" value="{c2}" style="endArrow=none;strokeColor=#000000;strokeWidth=1.8;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;fontColor=#000000;" edge="1" parent="1" source="{rid}" target="{e2_id}">')
        lines.append('          <mxGeometry relative="1" as="geometry" />')
        lines.append('        </mxCell>')

    # 6. LEGEND BAR (Bottom)
    leg_y = page_h - 130
    lines.append('        <!-- ================= NOTATION LEGEND ================= -->')
    lines.append(f'        <mxCell id="legend_bg" value="" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2.5;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="60" y="{leg_y}" width="{page_w - 120}" height="90" as="geometry" />')
    lines.append('        </mxCell>')
    lines.append(f'        <mxCell id="legend_title" value="&lt;b&gt;PETER CHEN ER DIAGRAM NOTATION LEGEND (COLLEGE PROJECT STANDARD)&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=13;fontColor=#000000;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="80" y="{leg_y + 10}" width="600" height="20" as="geometry" />')
    lines.append('        </mxCell>')
    
    # Legend Item: Entity
    lines.append(f'        <mxCell id="leg_ent" value="&lt;b&gt;ENTITY&lt;/b&gt;" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;fontSize=11;fontColor=#000000;align=center;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="90" y="{leg_y + 40}" width="90" height="35" as="geometry" />')
    lines.append('        </mxCell>')
    lines.append(f'        <mxCell id="leg_ent_desc" value="Entity / Database Table" style="text;html=1;fontSize=11;fontColor=#000000;align=left;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="190" y="{leg_y + 47}" width="140" height="20" as="geometry" />')
    lines.append('        </mxCell>')

    # Legend Item: Relationship
    lines.append(f'        <mxCell id="leg_rel" value="&lt;b&gt;Rel&lt;/b&gt;" style="shape=rhombus;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;fontSize=11;fontColor=#000000;align=center;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="360" y="{leg_y + 35}" width="70" height="42" as="geometry" />')
    lines.append('        </mxCell>')
    lines.append(f'        <mxCell id="leg_rel_desc" value="Relationship (Diamond)" style="text;html=1;fontSize=11;fontColor=#000000;align=left;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="440" y="{leg_y + 47}" width="150" height="20" as="geometry" />')
    lines.append('        </mxCell>')

    # Legend Item: Attribute
    lines.append(f'        <mxCell id="leg_att" value="attribute" style="shape=ellipse;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=11;fontColor=#000000;align=center;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="620" y="{leg_y + 40}" width="80" height="34" as="geometry" />')
    lines.append('        </mxCell>')
    lines.append(f'        <mxCell id="leg_att_desc" value="Regular Attribute" style="text;html=1;fontSize=11;fontColor=#000000;align=left;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="710" y="{leg_y + 47}" width="120" height="20" as="geometry" />')
    lines.append('        </mxCell>')

    # Legend Item: Primary Key
    lines.append(f'        <mxCell id="leg_pk" value="&lt;u&gt;&lt;b&gt;id (PK)&lt;/b&gt;&lt;/u&gt;" style="shape=ellipse;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2.5;fontSize=11;fontColor=#000000;align=center;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="870" y="{leg_y + 40}" width="85" height="34" as="geometry" />')
    lines.append('        </mxCell>')
    lines.append(f'        <mxCell id="leg_pk_desc" value="Primary Key (Underlined + PK)" style="text;html=1;fontSize=11;fontColor=#000000;align=left;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="965" y="{leg_y + 47}" width="180" height="20" as="geometry" />')
    lines.append('        </mxCell>')

    # Legend Item: Foreign Key
    lines.append(f'        <mxCell id="leg_fk" value="fk_id (FK)" style="shape=ellipse;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;strokeDasharray=3 3;fontSize=11;fontColor=#000000;align=center;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="1190" y="{leg_y + 40}" width="85" height="34" as="geometry" />')
    lines.append('        </mxCell>')
    lines.append(f'        <mxCell id="leg_fk_desc" value="Foreign Key (Dashed + FK)" style="text;html=1;fontSize=11;fontColor=#000000;align=left;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="1285" y="{leg_y + 47}" width="180" height="20" as="geometry" />')
    lines.append('        </mxCell>')

    # Legend Item: Cardinality
    lines.append(f'        <mxCell id="leg_card" value="1 : N" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1;fontSize=11;fontStyle=1;fontColor=#000000;align=center;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="1510" y="{leg_y + 42}" width="50" height="30" as="geometry" />')
    lines.append('        </mxCell>')
    lines.append(f'        <mxCell id="leg_card_desc" value="Cardinality Multiplicity (1:1, 1:N, M:N)" style="text;html=1;fontSize=11;fontColor=#000000;align=left;" vertex="1" parent="1">')
    lines.append(f'          <mxGeometry x="1570" y="{leg_y + 47}" width="240" height="20" as="geometry" />')
    lines.append('        </mxCell>')

    lines.append('      </root>')
    lines.append('    </mxGraphModel>')
    lines.append('  </diagram>')
    lines.append('</mxfile>')

    return '\n'.join(lines)


def generate_unified_svg():
    """
    Generates a crisp, high-resolution SVG matching the Chen ER Diagram exactly.
    """
    data = get_all_tables_data()
    entities = data["entities"]
    relationships = data["relationships"]
    page_w = data["page_w"]
    page_h = data["page_h"]

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {page_w} {page_h}" width="100%" height="100%" style="background-color: #ffffff; font-family: \'Segoe UI\', Arial, Helvetica, sans-serif;">')
    lines.append('  <style>')
    lines.append('    .ent-rect { fill: #ffffff; stroke: #000000; stroke-width: 2.5px; }')
    lines.append('    .ent-text { font-size: 16px; font-weight: bold; fill: #000000; text-anchor: middle; dominant-baseline: middle; letter-spacing: 0.5px; }')
    lines.append('    .rel-dia { fill: #ffffff; stroke: #000000; stroke-width: 2px; }')
    lines.append('    .rel-text { font-size: 12px; font-weight: bold; fill: #000000; text-anchor: middle; dominant-baseline: middle; }')
    lines.append('    .att-reg { fill: #ffffff; stroke: #000000; stroke-width: 1.2px; }')
    lines.append('    .att-pk { fill: #ffffff; stroke: #000000; stroke-width: 2.5px; }')
    lines.append('    .att-fk { fill: #ffffff; stroke: #000000; stroke-width: 1.5px; stroke-dasharray: 4,3; }')
    lines.append('    .att-text { font-size: 11px; fill: #000000; text-anchor: middle; dominant-baseline: middle; }')
    lines.append('    .att-pk-text { font-size: 11px; font-weight: bold; text-decoration: underline; fill: #000000; text-anchor: middle; dominant-baseline: middle; }')
    lines.append('    .att-fk-text { font-size: 11px; font-weight: 600; fill: #000000; text-anchor: middle; dominant-baseline: middle; }')
    lines.append('    .conn-line { stroke: #000000; stroke-width: 1.2px; }')
    lines.append('    .rel-line { stroke: #000000; stroke-width: 1.8px; }')
    lines.append('    .card-label { font-size: 13px; font-weight: bold; fill: #000000; }')
    lines.append('  </style>')

    # Defs: Filters and drop shadow
    lines.append('  <defs>')
    lines.append('    <filter id="card-badge" x="0" y="0" width="100%" height="100%">')
    lines.append('      <feFlood flood-color="#ffffff"/>')
    lines.append('      <feComposite in="SourceGraphic"/>')
    lines.append('    </filter>')
    lines.append('  </defs>')

    # Title Banner
    lines.append(f'  <!-- Title Banner -->')
    lines.append(f'  <rect x="60" y="30" width="{page_w - 120}" height="70" fill="#ffffff" stroke="#000000" stroke-width="2.5" />')
    lines.append(f'  <text x="{page_w / 2}" y="57" text-anchor="middle" font-size="20px" font-weight="bold" fill="#000000">UNIFIED ENTITY-RELATIONSHIP (ER) DIAGRAM — SCHOOL MANAGEMENT SYSTEM (sms_db)</text>')
    lines.append(f'  <text x="{page_w / 2}" y="82" text-anchor="middle" font-size="13px" fill="#333333">Complete Relational Architecture Covering All 12 Database Tables | Peter Chen Notation Standard | Pure Black &amp; White (College Project Standard)</text>')

    # 1. Attribute Connecting Lines (Entity Center -> Attribute Center)
    lines.append('  <!-- Attribute Connecting Lines -->')
    for ename, edata in entities.items():
        ecx, ecy = edata["cx"], edata["cy"]
        attrs = edata["attrs"]
        positions = get_orbit_positions(ecx, ecy, len(attrs), edata["rx"], edata["ry"])
        for idx, (ax, ay) in enumerate(positions):
            lines.append(f'  <line x1="{ecx}" y1="{ecy}" x2="{int(ax)}" y2="{int(ay)}" class="conn-line" />')

    # 2. Relationship Connecting Lines (Entity Center -> Rel Diamond Center -> Entity Center)
    lines.append('  <!-- Relationship Connecting Lines -->')
    for rel in relationships:
        e1 = entities[rel["ent1"]]
        e2 = entities[rel["ent2"]]
        rx, ry = rel["cx"], rel["cy"]
        
        # Line 1: ent1 to diamond
        lines.append(f'  <line x1="{e1["cx"]}" y1="{e1["cy"]}" x2="{rx}" y2="{ry}" class="rel-line" />')
        # Line 2: diamond to ent2
        lines.append(f'  <line x1="{rx}" y1="{ry}" x2="{e2["cx"]}" y2="{e2["cy"]}" class="rel-line" />')

        # Cardinality Badges
        m1x = (e1["cx"] * 0.6 + rx * 0.4)
        m1y = (e1["cy"] * 0.6 + ry * 0.4)
        m2x = (e2["cx"] * 0.6 + rx * 0.4)
        m2y = (e2["cy"] * 0.6 + ry * 0.4)

        lines.append(f'  <rect x="{int(m1x - 12)}" y="{int(m1y - 12)}" width="24" height="24" fill="#ffffff" stroke="#000000" stroke-width="1" />')
        lines.append(f'  <text x="{int(m1x)}" y="{int(m1y)}" text-anchor="middle" dominant-baseline="middle" class="card-label">{rel.get("c1", "1")}</text>')

        lines.append(f'  <rect x="{int(m2x - 12)}" y="{int(m2y - 12)}" width="24" height="24" fill="#ffffff" stroke="#000000" stroke-width="1" />')
        lines.append(f'  <text x="{int(m2x)}" y="{int(m2y)}" text-anchor="middle" dominant-baseline="middle" class="card-label">{rel.get("c2", "N")}</text>')

    # 3. Entity Boxes (Rectangles)
    lines.append('  <!-- Entity Rectangles -->')
    for ename, edata in entities.items():
        ex = edata["cx"] - edata["w"] // 2
        ey = edata["cy"] - edata["h"] // 2
        lines.append(f'  <rect x="{ex}" y="{ey}" width="{edata["w"]}" height="{edata["h"]}" class="ent-rect" />')
        lines.append(f'  <text x="{edata["cx"]}" y="{edata["cy"]}" class="ent-text">{ename.upper()}</text>')

    # 4. Attribute Ovals (Ellipses)
    lines.append('  <!-- Attribute Ellipses -->')
    for ename, edata in entities.items():
        attrs = edata["attrs"]
        positions = get_orbit_positions(edata["cx"], edata["cy"], len(attrs), edata["rx"], edata["ry"])
        for idx, attr in enumerate(attrs):
            ax, ay = positions[idx]
            aname = attr["name"]
            atype = attr["type"]

            if atype == "PK":
                rx_val = max(48, len(aname) * 4 + 21)
                ry_val = 18
                lines.append(f'  <ellipse cx="{int(ax)}" cy="{int(ay)}" rx="{rx_val}" ry="{ry_val}" class="att-pk" />')
                lines.append(f'  <text x="{int(ax)}" y="{int(ay)}" class="att-pk-text">{aname} (PK)</text>')
            elif atype == "FK":
                rx_val = max(43, len(aname) * 4 + 18)
                ry_val = 18
                lines.append(f'  <ellipse cx="{int(ax)}" cy="{int(ay)}" rx="{rx_val}" ry="{ry_val}" class="att-fk" />')
                lines.append(f'  <text x="{int(ax)}" y="{int(ay)}" class="att-fk-text">{aname} (FK)</text>')
            else:
                rx_val = max(38, len(aname) * 4 + 13)
                ry_val = 18
                lines.append(f'  <ellipse cx="{int(ax)}" cy="{int(ay)}" rx="{rx_val}" ry="{ry_val}" class="att-reg" />')
                lines.append(f'  <text x="{int(ax)}" y="{int(ay)}" class="att-text">{aname}</text>')

    # 5. Relationship Diamonds (Rhombus)
    lines.append('  <!-- Relationship Diamonds -->')
    for rel in relationships:
        rx, ry = rel["cx"], rel["cy"]
        rw, rh = rel["w"], rel["h"]
        p1 = f"{rx},{ry - rh//2}"
        p2 = f"{rx + rw//2},{ry}"
        p3 = f"{rx},{ry + rh//2}"
        p4 = f"{rx - rw//2},{ry}"
        lines.append(f'  <polygon points="{p1} {p2} {p3} {p4}" class="rel-dia" />')
        lines.append(f'  <text x="{rx}" y="{ry}" class="rel-text">{rel["name"]}</text>')

    # 6. Legend Bar
    leg_y = page_h - 130
    lines.append('  <!-- Legend Bar -->')
    lines.append(f'  <rect x="60" y="{leg_y}" width="{page_w - 120}" height="90" fill="#ffffff" stroke="#000000" stroke-width="2.5" />')
    lines.append(f'  <text x="80" y="{leg_y + 24}" font-size="13px" font-weight="bold" fill="#000000">PETER CHEN ER DIAGRAM NOTATION LEGEND (COLLEGE PROJECT STANDARD)</text>')

    # Entity legend
    lines.append(f'  <rect x="90" y="{leg_y + 40}" width="90" height="35" class="ent-rect" />')
    lines.append(f'  <text x="135" y="{leg_y + 58}" class="ent-text" font-size="11px">ENTITY</text>')
    lines.append(f'  <text x="190" y="{leg_y + 62}" font-size="12px" fill="#000000">Entity / Database Table</text>')

    # Rel legend
    rx = 395
    ry = leg_y + 57
    rw = 70
    rh = 40
    lines.append(f'  <polygon points="{rx},{ry - rh//2} {rx + rw//2},{ry} {rx},{ry + rh//2} {rx - rw//2},{ry}" class="rel-dia" />')
    lines.append(f'  <text x="{rx}" y="{ry}" class="rel-text">Rel</text>')
    lines.append(f'  <text x="445" y="{leg_y + 62}" font-size="12px" fill="#000000">Relationship (Diamond)</text>')

    # Regular Attribute legend
    lines.append(f'  <ellipse cx="660" cy="{leg_y + 57}" rx="40" ry="17" class="att-reg" />')
    lines.append(f'  <text x="660" y="{leg_y + 57}" class="att-text">attribute</text>')
    lines.append(f'  <text x="710" y="{leg_y + 62}" font-size="12px" fill="#000000">Regular Attribute</text>')

    # PK legend
    lines.append(f'  <ellipse cx="910" cy="{leg_y + 57}" rx="45" ry="17" class="att-pk" />')
    lines.append(f'  <text x="910" y="{leg_y + 57}" class="att-pk-text">id (PK)</text>')
    lines.append(f'  <text x="965" y="{leg_y + 62}" font-size="12px" fill="#000000">Primary Key (Underlined + PK)</text>')

    # FK legend
    lines.append(f'  <ellipse cx="1230" cy="{leg_y + 57}" rx="45" ry="17" class="att-fk" />')
    lines.append(f'  <text x="1230" y="{leg_y + 57}" class="att-fk-text">fk_id (FK)</text>')
    lines.append(f'  <text x="1285" y="{leg_y + 62}" font-size="12px" fill="#000000">Foreign Key (Dashed + FK)</text>')

    # Cardinality legend
    lines.append(f'  <rect x="1510" y="{leg_y + 44}" width="50" height="26" fill="#ffffff" stroke="#000000" stroke-width="1.2" />')
    lines.append(f'  <text x="1535" y="{leg_y + 57}" text-anchor="middle" dominant-baseline="middle" font-size="12px" font-weight="bold" fill="#000000">1 : N</text>')
    lines.append(f'  <text x="1570" y="{leg_y + 62}" font-size="12px" fill="#000000">Cardinality Multiplicity (1:1, 1:N, M:N)</text>')

    lines.append('</svg>')
    return '\n'.join(lines)


def build_viewer_html(drawio_filename="School_Management_Unified_ER.drawio"):
    """
    Creates an interactive HTML viewer with zoom/pan and download button.
    """
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>School Management System — Unified ER Diagram Viewer</title>
  <style>
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }}
    body {{
      background: #0f172a;
      color: #f8fafc;
      overflow: hidden;
      height: 100vh;
      display: flex;
      flex-direction: column;
    }}
    header {{
      background: #1e293b;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #334155;
      z-index: 10;
    }}
    .header-title h1 {{
      font-size: 17px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .badge {{
      font-size: 11px;
      padding: 3px 8px;
      border-radius: 9999px;
      background: #059669;
      color: #ffffff;
      font-weight: 600;
    }}
    .header-title p {{
      font-size: 12px;
      color: #94a3b8;
      margin-top: 2px;
    }}
    .actions {{
      display: flex;
      gap: 10px;
      align-items: center;
    }}
    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      border: 1px solid #475569;
      background: #334155;
      color: #ffffff;
      transition: all 0.2s;
    }}
    .btn:hover {{
      background: #475569;
    }}
    .btn-primary {{
      background: #2563eb;
      border-color: #3b82f6;
    }}
    .btn-primary:hover {{
      background: #1d4ed8;
    }}
    .viewport {{
      flex: 1;
      overflow: auto;
      padding: 24px;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      background: #090d16;
    }}
    .sheet-card {{
      background: #ffffff;
      border-radius: 8px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6);
      width: 100%;
      max-width: 3500px;
      transform-origin: top center;
      transition: transform 0.15s ease-out;
    }}
    object {{
      display: block;
      width: 100%;
      height: 2500px;
    }}
    .zoom-controls {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      display: flex;
      gap: 6px;
      background: rgba(30, 41, 59, 0.9);
      padding: 6px;
      border-radius: 8px;
      border: 1px solid #475569;
      backdrop-filter: blur(8px);
      z-index: 20;
    }}
    .zoom-btn {{
      background: #1e293b;
      color: white;
      border: 1px solid #334155;
      padding: 8px 12px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
      font-weight: bold;
    }}
    .zoom-btn:hover {{
      background: #334155;
    }}
  </style>
</head>
<body>

  <header>
    <div class="header-title">
      <h1>
        Unified School Management System ER Diagram
        <span class="badge">All 12 Tables Combined</span>
      </h1>
      <p>Peter Chen Notation &bull; Pure Black &amp; White &bull; All PKs and FKs Linked &bull; College Project Documentation</p>
    </div>

    <div class="actions">
      <a href="{drawio_filename}" download class="btn btn-primary" title="Download editable draw.io diagram">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
        Download .drawio
      </a>
      <a href="https://app.diagrams.net/" target="_blank" class="btn" title="Open diagrams.net online editor">
        Open in draw.io
      </a>
    </div>
  </header>

  <div class="viewport" id="viewport">
    <div class="sheet-card" id="card">
      <object data="School_Management_Unified_ER.svg" type="image/svg+xml" id="svg-object"></object>
    </div>
  </div>

  <div class="zoom-controls">
    <button class="zoom-btn" onclick="zoomIn()" title="Zoom In">+</button>
    <button class="zoom-btn" onclick="zoomOut()" title="Zoom Out">&minus;</button>
    <button class="zoom-btn" onclick="resetZoom()" title="Reset Zoom">100%</button>
  </div>

  <script>
    let scale = 1.0;
    const card = document.getElementById('card');

    function zoomIn() {{
      scale += 0.15;
      applyZoom();
    }}
    function zoomOut() {{
      if (scale > 0.3) {{
        scale -= 0.15;
        applyZoom();
      }}
    }}
    function resetZoom() {{
      scale = 1.0;
      applyZoom();
    }}
    function applyZoom() {{
      card.style.transform = `scale(${{scale}})`;
      card.style.transformOrigin = 'top center';
    }}
  </script>
</body>
</html>'''


def main():
    workspace = r"c:\xampp\htdocs\school-management"

    print("Generating Unified ER Diagram XML...")
    drawio_content = build_unified_drawio_xml()
    
    # Target files
    target_files = [
        "School_Management_Unified_ER.drawio",
        "school_management_combined_all_in_one.drawio",
        "combined_all_in_one.drawio",
        "combined_er.drawio"
    ]

    for fn in target_files:
        path = os.path.join(workspace, fn)
        print(f"Writing {path}...")
        with open(path, "w", encoding="utf-8") as f:
            f.write(drawio_content)

    print("Generating Unified ER Diagram SVG...")
    svg_content = generate_unified_svg()
    for sfn in ["School_Management_Unified_ER.svg", "combined_all_in_one_er.svg"]:
        spath = os.path.join(workspace, sfn)
        print(f"Writing {spath}...")
        with open(spath, "w", encoding="utf-8") as f:
            f.write(svg_content)

    print("Generating Interactive HTML Viewer...")
    html_content = build_viewer_html("School_Management_Unified_ER.drawio")
    for hfn in ["School_Management_ER_Viewer.html", "combined_er_viewer.html"]:
        hpath = os.path.join(workspace, hfn)
        print(f"Writing {hpath}...")
        with open(hpath, "w", encoding="utf-8") as f:
            f.write(html_content)

    print("Validating XML syntax of generated draw.io files...")
    for fn in target_files:
        path = os.path.join(workspace, fn)
        tree = ET.parse(path)
        root = tree.getroot()
        cells = root.findall('.//mxCell')
        print(f"  [OK] {fn}: 100% Valid XML ({len(cells)} cells).")

    print("\nAll files successfully generated and verified!")


if __name__ == "__main__":
    main()
