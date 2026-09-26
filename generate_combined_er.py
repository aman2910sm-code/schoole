#!/usr/bin/env python3
"""
Generator for Combined ER Diagrams:
1. admin_teacher.drawio / admin_teacher.drowio
2. student_registrar.drawio / student_registrar.drowio
3. High-res SVGs: admin_teacher_er.svg, student_registrar_er.svg
4. combined_er_viewer.html

Strictly complies with the user's reference images:
- Chen ER Diagram Notation
- Pure Black & White (No colors)
- Entity: Rectangles
- Relationship: Diamonds
- Attribute: Ovals / Ellipses connected by solid lines radiating outward
- Constraint labels: (PK) and (FK) only, matching DATA_DICTIONARY.md exactly
"""

import os
import math
import html
import xml.etree.ElementTree as ET

def get_oval_positions(cx, cy, count, rx=190, ry=140):
    """
    Distributes `count` attribute ovals around a central entity (cx, cy).
    Spreads them out in an elliptical orbit so lines radiate nicely without crossing.
    """
    positions = []
    # If 16 attributes (like student and teacher), distribute in two layers or an extended orbit
    if count == 16:
        # 5 top, 5 bottom, 3 left, 3 right
        # Top 5
        for i in range(5):
            x = cx - 220 + i * 110
            y = cy - ry - 25
            positions.append((x, y))
        # Right 3
        for i in range(3):
            x = cx + rx + 30
            y = cy - 60 + i * 60
            positions.append((x, y))
        # Bottom 5
        for i in range(5):
            x = cx - 220 + i * 110
            y = cy + ry + 25
            positions.append((x, y))
        # Left 3
        for i in range(3):
            x = cx - rx - 130
            y = cy - 60 + i * 60
            positions.append((x, y))
    elif count == 13: # Registrar (13 attributes)
        # 4 top, 4 bottom, 2 left, 3 right
        for i in range(4):
            x = cx - 180 + i * 120
            y = cy - ry - 20
            positions.append((x, y))
        for i in range(3):
            x = cx + rx + 25
            y = cy - 60 + i * 60
            positions.append((x, y))
        for i in range(4):
            x = cx - 180 + i * 120
            y = cy + ry + 20
            positions.append((x, y))
        for i in range(2):
            x = cx - rx - 125
            y = cy - 30 + i * 60
            positions.append((x, y))
    elif count == 7: # student_score
        # 3 top, 3 bottom, 1 left
        for i in range(3):
            positions.append((cx - 130 + i * 130, cy - ry - 10))
        positions.append((cx + rx + 15, cy))
        for i in range(3):
            positions.append((cx + 130 - i * 130, cy + ry + 10))
    elif count == 6: # setting
        for i in range(3):
            positions.append((cx - 120 + i * 120, cy - ry))
        for i in range(3):
            positions.append((cx + 120 - i * 120, cy + ry))
    elif count == 5: # admin, courses, message
        for i in range(2):
            positions.append((cx - 80 + i * 160, cy - ry))
        positions.append((cx + rx + 10, cy))
        for i in range(2):
            positions.append((cx + 80 - i * 160, cy + ry))
    elif count == 4: # subjects
        positions.append((cx - 70, cy - ry))
        positions.append((cx + 70, cy - ry))
        positions.append((cx + 70, cy + ry))
        positions.append((cx - 70, cy + ry))
    elif count == 3: # grades, class
        positions.append((cx - 80, cy - ry))
        positions.append((cx + 80, cy - ry))
        positions.append((cx, cy + ry))
    elif count == 2: # section
        positions.append((cx - 60, cy - ry))
        positions.append((cx + 60, cy - ry))
    else:
        for i in range(count):
            angle = (2 * math.pi * i) / count - math.pi / 2
            x = cx + rx * math.cos(angle) - 50
            y = cy + ry * math.sin(angle) - 25
            positions.append((x, y))
            
    return positions


# =========================================================================
# 1. ADMIN + TEACHER ER DIAGRAM
# =========================================================================
def build_admin_teacher_data():
    # Canvas Size: 1800 x 1400
    entities = {
        "admin": {
            "name": "admin",
            "x": 380, "y": 300, "w": 140, "h": 60,
            "attrs": [
                {"name": "admin_id", "type": "PK"},
                {"name": "username", "type": ""},
                {"name": "password", "type": ""},
                {"name": "fname", "type": ""},
                {"name": "lname", "type": ""}
            ],
            "rx": 180, "ry": 120
        },
        "setting": {
            "name": "setting",
            "x": 380, "y": 800, "w": 140, "h": 60,
            "attrs": [
                {"name": "id", "type": "PK"},
                {"name": "current_year", "type": ""},
                {"name": "current_semester", "type": ""},
                {"name": "school_name", "type": ""},
                {"name": "slogan", "type": ""},
                {"name": "about", "type": ""}
            ],
            "rx": 190, "ry": 125
        },
        "message": {
            "name": "message",
            "x": 380, "y": 1200, "w": 140, "h": 60,
            "attrs": [
                {"name": "message_id", "type": "PK"},
                {"name": "sender_full_name", "type": ""},
                {"name": "sender_email", "type": ""},
                {"name": "message", "type": ""},
                {"name": "date_time", "type": ""}
            ],
            "rx": 190, "ry": 120
        },
        "courses": {
            "name": "courses",
            "x": 950, "y": 300, "w": 140, "h": 60,
            "attrs": [
                {"name": "course_id", "type": "PK"},
                {"name": "grade", "type": ""},
                {"name": "course_name", "type": ""},
                {"name": "grade_code", "type": ""},
                {"name": "course_code", "type": ""}
            ],
            "rx": 180, "ry": 120
        },
        "teacher": {
            "name": "teacher",
            "x": 950, "y": 800, "w": 160, "h": 70,
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
            ],
            "rx": 210, "ry": 145
        },
        "subjects": {
            "name": "subjects",
            "x": 950, "y": 1200, "w": 140, "h": 60,
            "attrs": [
                {"name": "subject_id", "type": "PK"},
                {"name": "subject", "type": ""},
                {"name": "subject_code", "type": ""},
                {"name": "grade", "type": "FK"}
            ],
            "rx": 180, "ry": 115
        }
    }

    relationships = [
        {"name": "configures", "ent1": "admin", "ent2": "setting", "x": 380, "y": 550, "w": 110, "h": 60},
        {"name": "reviews", "ent1": "setting", "ent2": "message", "x": 380, "y": 1000, "w": 100, "h": 60},
        {"name": "manages", "ent1": "admin", "ent2": "teacher", "x": 665, "y": 550, "w": 100, "h": 60},
        {"name": "defines", "ent1": "admin", "ent2": "courses", "x": 665, "y": 300, "w": 100, "h": 60},
        {"name": "teaches", "ent1": "teacher", "ent2": "subjects", "x": 950, "y": 1000, "w": 100, "h": 60}
    ]

    return {
        "title": "Combined ER Diagram: Admin & Teacher Modules (sms_db)",
        "page_w": 1550,
        "page_h": 1450,
        "entities": entities,
        "relationships": relationships
    }


# =========================================================================
# 2. STUDENT + REGISTRAR ER DIAGRAM
# =========================================================================
def build_student_registrar_data():
    entities = {
        "registrar_office": {
            "name": "registrar_office",
            "x": 380, "y": 300, "w": 170, "h": 65,
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
            ],
            "rx": 210, "ry": 135
        },
        "student": {
            "name": "student",
            "x": 380, "y": 800, "w": 160, "h": 70,
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
                {"name": "subjets", "type": ""}
            ],
            "rx": 210, "ry": 145
        },
        "student_score": {
            "name": "student_score",
            "x": 380, "y": 1230, "w": 160, "h": 65,
            "attrs": [
                {"name": "id", "type": "PK"},
                {"name": "semester", "type": ""},
                {"name": "year", "type": ""},
                {"name": "student_id", "type": "FK"},
                {"name": "teacher_id", "type": "FK"},
                {"name": "subject_id", "type": "FK"},
                {"name": "results", "type": ""}
            ],
            "rx": 190, "ry": 125
        },
        "class": {
            "name": "class",
            "x": 950, "y": 800, "w": 140, "h": 60,
            "attrs": [
                {"name": "class_id", "type": "PK"},
                {"name": "grade", "type": "FK"},
                {"name": "section", "type": "FK"}
            ],
            "rx": 170, "ry": 115
        },
        "grades": {
            "name": "grades",
            "x": 950, "y": 450, "w": 140, "h": 60,
            "attrs": [
                {"name": "grade_id", "type": "PK"},
                {"name": "grade", "type": ""},
                {"name": "grade_code", "type": ""}
            ],
            "rx": 170, "ry": 115
        },
        "section": {
            "name": "section",
            "x": 950, "y": 1150, "w": 140, "h": 60,
            "attrs": [
                {"name": "section_id", "type": "PK"},
                {"name": "section", "type": ""}
            ],
            "rx": 160, "ry": 110
        }
    }

    relationships = [
        {"name": "admits", "ent1": "registrar_office", "ent2": "student", "x": 380, "y": 550, "w": 100, "h": 60},
        {"name": "receives", "ent1": "student", "ent2": "student_score", "x": 380, "y": 1015, "w": 100, "h": 60},
        {"name": "enrolled_in", "ent1": "student", "ent2": "class", "x": 665, "y": 800, "w": 110, "h": 60},
        {"name": "comprises", "ent1": "class", "ent2": "grades", "x": 950, "y": 625, "w": 105, "h": 60},
        {"name": "divides", "ent1": "class", "ent2": "section", "x": 950, "y": 975, "w": 100, "h": 60}
    ]

    return {
        "title": "Combined ER Diagram: Student & Registrar Modules (sms_db)",
        "page_w": 1550,
        "page_h": 1450,
        "entities": entities,
        "relationships": relationships
    }


# =========================================================================
# XML GENERATOR (Draw.io)
# =========================================================================
def generate_drawio_xml(data, diagram_id):
    page_w = data["page_w"]
    page_h = data["page_h"]
    title = data["title"]
    entities = data["entities"]
    relationships = data["relationships"]

    esc_title = html.escape(title)

    xml = f'''<mxfile host="app.diagrams.net" modified="2026-09-26T00:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="{diagram_id}" name="{esc_title}">
    <mxGraphModel dx="1600" dy="1200" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{page_w}" pageHeight="{page_h}" background="#FFFFFF" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Banner (Black and White) -->
        <mxCell id="title" value="&lt;b&gt;{esc_title}&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 11px;&quot;&gt;Chen ER Notation | Entities: Rectangles | Relationships: Diamonds | Attributes: Ovals | PK and FK Constraints&lt;/font&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=14;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="60" y="30" width="{page_w - 120}" height="50" as="geometry" />
        </mxCell>
'''

    cell_id = 100

    # 1. Render Entities and their Attribute Ovals
    for e_key, e_val in entities.items():
        ex, ey, ew, eh = e_val["x"], e_val["y"], e_val["w"], e_val["h"]
        e_name = e_val["name"]
        attrs = e_val["attrs"]
        rx, ry = e_val["rx"], e_val["ry"]
        
        # Center of entity
        cx = ex + ew / 2
        cy = ey + eh / 2

        # Entity Rectangle
        e_cid = f"ent_{e_key}"
        xml += f'''
        <!-- Entity: {e_name} -->
        <mxCell id="{e_cid}" value="&lt;b&gt;{e_name}&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.8;fontColor=#000000;fontSize=13;fontStyle=1;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="{ex}" y="{ey}" width="{ew}" height="{eh}" as="geometry" />
        </mxCell>
'''
        # Calculate attribute positions
        attr_positions = get_oval_positions(cx, cy, len(attrs), rx, ry)

        for i, attr in enumerate(attrs):
            ax, ay = attr_positions[i]
            # Width and height of oval
            aw, ah = 105, 42
            attr_name = attr["name"]
            attr_type = attr["type"]
            
            if attr_type == "PK":
                attr_label = f"&lt;u&gt;{attr_name}&lt;/u&gt;&lt;br/&gt;&lt;b&gt;(PK)&lt;/b&gt;"
            elif attr_type == "FK":
                attr_label = f"{attr_name}&lt;br/&gt;&lt;b&gt;(FK)&lt;/b&gt;"
            else:
                attr_label = attr_name

            a_cid = f"attr_{e_key}_{i}"
            xml += f'''
        <mxCell id="{a_cid}" value="{attr_label}" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontColor=#000000;fontSize=10;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="{ax}" y="{ay}" width="{aw}" height="{ah}" as="geometry" />
        </mxCell>
        <!-- Connector Line from Entity to Attribute -->
        <mxCell id="edge_{e_key}_{i}" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1;" edge="1" parent="1" source="{e_cid}" target="{a_cid}">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
'''

    # 2. Render Relationships (Diamonds) and Connectors to Entities
    for r_idx, rel in enumerate(relationships):
        rx, ry, rw, rh = rel["x"], rel["y"], rel["w"], rel["h"]
        r_name = rel["name"]
        ent1_id = f"ent_{rel['ent1']}"
        ent2_id = f"ent_{rel['ent2']}"
        rel_cid = f"rel_{r_idx}"

        xml += f'''
        <!-- Relationship: {r_name} ({rel['ent1']} <-> {rel['ent2']}) -->
        <mxCell id="{rel_cid}" value="&lt;b&gt;{r_name}&lt;/b&gt;" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontColor=#000000;fontSize=11;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="{rx}" y="{ry}" width="{rw}" height="{rh}" as="geometry" />
        </mxCell>
        <!-- Line: {rel['ent1']} to Relationship -->
        <mxCell id="rel_edge_1_{r_idx}" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.5;" edge="1" parent="1" source="{ent1_id}" target="{rel_cid}">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Line: {rel['ent2']} to Relationship -->
        <mxCell id="rel_edge_2_{r_idx}" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.5;" edge="1" parent="1" source="{ent2_id}" target="{rel_cid}">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
'''

    # 3. Legend Box at Bottom (Pure Black & White)
    legend_y = page_h - 90
    xml += f'''
        <!-- Legend Box (Image 2 Symbols Reference Compliance) -->
        <mxCell id="legend_box" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;" vertex="1" parent="1">
          <mxGeometry x="60" y="{legend_y}" width="{page_w - 120}" height="65" as="geometry" />
        </mxCell>
        <mxCell id="leg_t" value="&lt;b&gt;ER SYMBOLS REFERENCE (Standard Chen Notation - Black &amp;amp; White)&lt;/b&gt;" style="text;html=1;align=center;verticalAlign=middle;fontSize=11;fontColor=#000000;" vertex="1" parent="legend_box">
          <mxGeometry x="10" y="2" width="{page_w - 140}" height="18" as="geometry" />
        </mxCell>
        <!-- Entity -->
        <mxCell id="leg_e" value="Entity" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=9;fontStyle=1;" vertex="1" parent="legend_box">
          <mxGeometry x="80" y="24" width="70" height="30" as="geometry" />
        </mxCell>
        <mxCell id="leg_e_t" value="&lt;b&gt;Rectangle:&lt;/b&gt; Entity" style="text;html=1;fontSize=10;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="155" y="24" width="130" height="30" as="geometry" />
        </mxCell>
        <!-- Relationship -->
        <mxCell id="leg_r" value="Rel" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=9;fontStyle=1;" vertex="1" parent="legend_box">
          <mxGeometry x="320" y="20" width="45" height="38" as="geometry" />
        </mxCell>
        <mxCell id="leg_r_t" value="&lt;b&gt;Diamond:&lt;/b&gt; Relationship" style="text;html=1;fontSize=10;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="370" y="24" width="150" height="30" as="geometry" />
        </mxCell>
        <!-- Attribute -->
        <mxCell id="leg_a" value="attr" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=9;" vertex="1" parent="legend_box">
          <mxGeometry x="540" y="24" width="55" height="30" as="geometry" />
        </mxCell>
        <mxCell id="leg_a_t" value="&lt;b&gt;Oval:&lt;/b&gt; Attribute" style="text;html=1;fontSize=10;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="600" y="24" width="120" height="30" as="geometry" />
        </mxCell>
        <!-- PK -->
        <mxCell id="leg_pk" value="&lt;u&gt;id&lt;/u&gt;&lt;br/&gt;&lt;b&gt;(PK)&lt;/b&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=8;" vertex="1" parent="legend_box">
          <mxGeometry x="740" y="22" width="55" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_pk_t" value="&lt;b&gt;Underlined Oval (PK):&lt;/b&gt; Primary Key" style="text;html=1;fontSize=10;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="800" y="24" width="200" height="30" as="geometry" />
        </mxCell>
        <!-- FK -->
        <mxCell id="leg_fk" value="ref&lt;br/&gt;&lt;b&gt;(FK)&lt;/b&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontSize=8;" vertex="1" parent="legend_box">
          <mxGeometry x="1030" y="22" width="55" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_fk_t" value="&lt;b&gt;Oval (FK):&lt;/b&gt; Foreign Key" style="text;html=1;fontSize=10;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="1090" y="24" width="160" height="30" as="geometry" />
        </mxCell>
        <!-- Connecting Line -->
        <mxCell id="leg_line" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.2;" edge="1" parent="legend_box">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1270" y="39" as="sourcePoint" />
            <mxPoint x="1330" y="39" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_line_t" value="&lt;b&gt;Line:&lt;/b&gt; Connection" style="text;html=1;fontSize=10;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="1340" y="24" width="120" height="30" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml


# =========================================================================
# SVG GENERATOR
# =========================================================================
def generate_svg(data):
    page_w = data["page_w"]
    page_h = data["page_h"]
    title = data["title"]
    entities = data["entities"]
    relationships = data["relationships"]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {page_w} {page_h}" width="100%" height="100%" style="background:#ffffff; font-family: 'Times New Roman', Times, serif;">
  <!-- Title -->
  <rect x="60" y="25" width="{page_w - 120}" height="55" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="{page_w/2}" y="50" font-size="16" font-weight="bold" text-anchor="middle" fill="#000000">{html.escape(title)}</text>
  <text x="{page_w/2}" y="68" font-size="11" font-style="italic" text-anchor="middle" fill="#000000">Chen ER Notation | Entities: Rectangles | Relationships: Diamonds | Attributes: Ovals | Constraints: (PK) and (FK)</text>
'''

    # First draw connector lines to attributes
    for e_key, e_val in entities.items():
        ex, ey, ew, eh = e_val["x"], e_val["y"], e_val["w"], e_val["h"]
        attrs = e_val["attrs"]
        rx, ry = e_val["rx"], e_val["ry"]
        cx = ex + ew / 2
        cy = ey + eh / 2
        attr_positions = get_oval_positions(cx, cy, len(attrs), rx, ry)

        for i, (ax, ay) in enumerate(attr_positions):
            aw, ah = 105, 42
            acx = ax + aw / 2
            acy = ay + ah / 2
            svg += f'  <line x1="{cx}" y1="{cy}" x2="{acx}" y2="{acy}" stroke="#000000" stroke-width="1" />\n'

    # Connector lines between entities and relationships
    for rel in relationships:
        rx, ry, rw, rh = rel["x"], rel["y"], rel["w"], rel["h"]
        rcx = rx + rw / 2
        rcy = ry + rh / 2
        ent1 = entities[rel["ent1"]]
        ent2 = entities[rel["ent2"]]
        e1cx = ent1["x"] + ent1["w"] / 2
        e1cy = ent1["y"] + ent1["h"] / 2
        e2cx = ent2["x"] + ent2["w"] / 2
        e2cy = ent2["y"] + ent2["h"] / 2

        svg += f'  <line x1="{e1cx}" y1="{e1cy}" x2="{rcx}" y2="{rcy}" stroke="#000000" stroke-width="1.8" />\n'
        svg += f'  <line x1="{e2cx}" y1="{e2cy}" x2="{rcx}" y2="{rcy}" stroke="#000000" stroke-width="1.8" />\n'

    # Now render relationship diamonds (white fill to cover lines)
    for rel in relationships:
        rx, ry, rw, rh = rel["x"], rel["y"], rel["w"], rel["h"]
        rcx = rx + rw / 2
        rcy = ry + rh / 2
        points = f"{rcx},{ry} {rx+rw},{rcy} {rcx},{ry+rh} {rx},{rcy}"
        svg += f'''
  <!-- Relationship Diamond: {rel['name']} -->
  <polygon points="{points}" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="{rcx}" y="{rcy + 4}" font-size="11" font-weight="bold" text-anchor="middle" fill="#000000">{rel['name']}</text>
'''

    # Render entities (rectangles with white fill)
    for e_key, e_val in entities.items():
        ex, ey, ew, eh = e_val["x"], e_val["y"], e_val["w"], e_val["h"]
        cx = ex + ew / 2
        cy = ey + eh / 2
        svg += f'''
  <!-- Entity: {e_val['name']} -->
  <rect x="{ex}" y="{ey}" width="{ew}" height="{eh}" fill="#ffffff" stroke="#000000" stroke-width="2" />
  <text x="{cx}" y="{cy + 5}" font-size="13" font-weight="bold" text-anchor="middle" fill="#000000">{e_val['name']}</text>
'''

    # Render attribute ovals
    for e_key, e_val in entities.items():
        ex, ey, ew, eh = e_val["x"], e_val["y"], e_val["w"], e_val["h"]
        attrs = e_val["attrs"]
        rx, ry = e_val["rx"], e_val["ry"]
        cx = ex + ew / 2
        cy = ey + eh / 2
        attr_positions = get_oval_positions(cx, cy, len(attrs), rx, ry)

        for i, (ax, ay) in enumerate(attr_positions):
            aw, ah = 105, 42
            acx = ax + aw / 2
            acy = ay + ah / 2
            attr = attrs[i]
            attr_name = attr["name"]
            attr_type = attr["type"]

            svg += f'''
  <ellipse cx="{acx}" cy="{acy}" rx="{aw/2}" ry="{ah/2}" fill="#ffffff" stroke="#000000" stroke-width="1.2" />'''
            if attr_type == "PK":
                svg += f'''
  <text x="{acx}" y="{acy - 2}" font-size="10" text-decoration="underline" text-anchor="middle" fill="#000000">{attr_name}</text>
  <text x="{acx}" y="{acy + 10}" font-size="9" font-weight="bold" text-anchor="middle" fill="#000000">(PK)</text>'''
            elif attr_type == "FK":
                svg += f'''
  <text x="{acx}" y="{acy - 2}" font-size="10" text-anchor="middle" fill="#000000">{attr_name}</text>
  <text x="{acx}" y="{acy + 10}" font-size="9" font-weight="bold" text-anchor="middle" fill="#000000">(FK)</text>'''
            else:
                svg += f'''
  <text x="{acx}" y="{acy + 4}" font-size="10" text-anchor="middle" fill="#000000">{attr_name}</text>'''

    # Legend Box at Bottom
    leg_y = page_h - 90
    svg += f'''
  <!-- Legend Box -->
  <rect x="60" y="{leg_y}" width="{page_w - 120}" height="65" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="{page_w/2}" y="{leg_y + 16}" font-size="11" font-weight="bold" text-anchor="middle" fill="#000000">ER SYMBOLS REFERENCE (Standard Chen Notation - Black &amp; White)</text>

  <!-- Entity -->
  <rect x="90" y="{leg_y + 26}" width="70" height="28" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="125" y="{leg_y + 44}" font-size="9" font-weight="bold" text-anchor="middle" fill="#000000">Entity</text>
  <text x="170" y="{leg_y + 44}" font-size="10" fill="#000000"><tspan font-weight="bold">Rectangle:</tspan> Entity</text>

  <!-- Relationship -->
  <polygon points="340,{leg_y+24} 360,{leg_y+40} 340,{leg_y+56} 320,{leg_y+40}" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="340" y="{leg_y + 44}" font-size="8" font-weight="bold" text-anchor="middle" fill="#000000">Rel</text>
  <text x="375" y="{leg_y + 44}" font-size="10" fill="#000000"><tspan font-weight="bold">Diamond:</tspan> Relationship</text>

  <!-- Attribute -->
  <ellipse cx="570" cy="{leg_y + 40}" rx="28" ry="14" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="570" y="{leg_y + 44}" font-size="9" text-anchor="middle" fill="#000000">attr</text>
  <text x="610" y="{leg_y + 44}" font-size="10" fill="#000000"><tspan font-weight="bold">Oval:</tspan> Attribute</text>

  <!-- PK -->
  <ellipse cx="765" cy="{leg_y + 40}" rx="30" ry="16" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="765" y="{leg_y + 36}" font-size="8" text-decoration="underline" text-anchor="middle" fill="#000000">id</text>
  <text x="765" y="{leg_y + 48}" font-size="8" font-weight="bold" text-anchor="middle" fill="#000000">(PK)</text>
  <text x="810" y="{leg_y + 44}" font-size="10" fill="#000000"><tspan font-weight="bold">Underlined Oval (PK):</tspan> Primary Key</text>

  <!-- FK -->
  <ellipse cx="1060" cy="{leg_y + 40}" rx="30" ry="16" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="1060" y="{leg_y + 36}" font-size="8" text-anchor="middle" fill="#000000">ref</text>
  <text x="1060" y="{leg_y + 48}" font-size="8" font-weight="bold" text-anchor="middle" fill="#000000">(FK)</text>
  <text x="1105" y="{leg_y + 44}" font-size="10" fill="#000000"><tspan font-weight="bold">Oval (FK):</tspan> Foreign Key</text>

  <!-- Line -->
  <line x1="1280" y1="{leg_y + 40}" x2="1335" y2="{leg_y + 40}" stroke="#000000" stroke-width="1.5" />
  <text x="1350" y="{leg_y + 44}" font-size="10" fill="#000000"><tspan font-weight="bold">Line:</tspan> Connector</text>
</svg>'''
    return svg


# =========================================================================
# COMBINED ER VIEWER HTML
# =========================================================================
def generate_viewer_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Combined ER Diagrams: Admin-Teacher & Student-Registrar | School Management System</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background: #475569;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
    }
    header {
      width: 100%;
      background: #1e293b;
      padding: 14px 24px;
      box-sizing: border-box;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #ffffff;
      border-bottom: 2px solid #334155;
    }
    .header-title h1 {
      margin: 0;
      font-size: 1.15rem;
    }
    .header-title p {
      margin: 4px 0 0 0;
      font-size: 0.8rem;
      color: #94a3b8;
    }
    .nav-tabs {
      display: flex;
      gap: 8px;
    }
    .nav-btn {
      background: #334155;
      color: #cbd5e1;
      border: 1px solid #475569;
      padding: 7px 18px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 600;
      transition: all 0.2s;
    }
    .nav-btn:hover {
      background: #475569;
      color: #ffffff;
    }
    .nav-btn.active {
      background: #ffffff;
      color: #0f172a;
      border-color: #ffffff;
    }
    .actions a {
      background: #2563eb;
      color: #ffffff;
      padding: 8px 16px;
      border-radius: 6px;
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .actions a:hover {
      background: #1d4ed8;
    }
    main {
      padding: 30px 10px;
      width: 100%;
      max-width: 1580px;
      display: flex;
      justify-content: center;
    }
    .sheet-card {
      background: #ffffff;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
      width: 100%;
      border-radius: 4px;
      overflow: hidden;
      padding: 10px;
    }
    .panel {
      display: none;
      width: 100%;
    }
    .panel.active {
      display: block;
    }
    .panel object, .panel img {
      width: 100%;
      display: block;
    }
  </style>
</head>
<body>

  <header>
    <div class="header-title">
      <h1>School Management System — Combined ER Diagrams (Chen Notation)</h1>
      <p>Pure Black &amp; White | Entities: Rectangles | Attributes: Ovals with (PK) &amp; (FK) | Relationships: Diamonds</p>
    </div>

    <div class="nav-tabs">
      <button class="nav-btn active" onclick="showTab('admin_teacher')">1. Admin &amp; Teacher ER</button>
      <button class="nav-btn" onclick="showTab('student_registrar')">2. Student &amp; Registrar ER</button>
    </div>

    <div class="actions">
      <a id="download-drawio" href="admin_teacher.drawio" download>Download .drawio</a>
    </div>
  </header>

  <main>
    <div class="sheet-card">
      <div id="tab-admin_teacher" class="panel active">
        <object data="admin_teacher_er.svg" type="image/svg+xml"></object>
      </div>
      <div id="tab-student_registrar" class="panel">
        <object data="student_registrar_er.svg" type="image/svg+xml"></object>
      </div>
    </div>
  </main>

  <script>
    function showTab(name) {
      document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));

      event.target.classList.add('active');
      document.getElementById('tab-' + name).classList.add('active');
      document.getElementById('download-drawio').href = name + '.drawio';
      document.getElementById('download-drawio').setAttribute('download', name + '.drawio');
    }
  </script>
</body>
</html>'''


def main():
    workspace = r"c:\xampp\htdocs\school-management"
    print("Generating Combined ER Diagrams in:", workspace)

    # 1. Admin + Teacher
    at_data = build_admin_teacher_data()
    at_xml = generate_drawio_xml(at_data, "admin-teacher-er")
    ET.fromstring(at_xml)  # Validate well-formed XML
    
    with open(os.path.join(workspace, "admin_teacher.drawio"), "w", encoding="utf-8") as f:
        f.write(at_xml)
    with open(os.path.join(workspace, "admin_teacher.drowio"), "w", encoding="utf-8") as f:
        f.write(at_xml)
    print("[OK] Generated and validated admin_teacher.drawio and admin_teacher.drowio")

    at_svg = generate_svg(at_data)
    ET.fromstring(at_svg)  # Validate well-formed SVG
    with open(os.path.join(workspace, "admin_teacher_er.svg"), "w", encoding="utf-8") as f:
        f.write(at_svg)
    print("[OK] Generated and validated admin_teacher_er.svg")

    # 2. Student + Registrar
    sr_data = build_student_registrar_data()
    sr_xml = generate_drawio_xml(sr_data, "student-registrar-er")
    ET.fromstring(sr_xml)  # Validate well-formed XML

    with open(os.path.join(workspace, "student_registrar.drawio"), "w", encoding="utf-8") as f:
        f.write(sr_xml)
    with open(os.path.join(workspace, "student_registrar.drowio"), "w", encoding="utf-8") as f:
        f.write(sr_xml)
    print("[OK] Generated and validated student_registrar.drawio and student_registrar.drowio")

    sr_svg = generate_svg(sr_data)
    ET.fromstring(sr_svg)  # Validate well-formed SVG
    with open(os.path.join(workspace, "student_registrar_er.svg"), "w", encoding="utf-8") as f:
        f.write(sr_svg)
    print("[OK] Generated and validated student_registrar_er.svg")

    # 3. Viewer
    with open(os.path.join(workspace, "combined_er_viewer.html"), "w", encoding="utf-8") as f:
        f.write(generate_viewer_html())
    print("[OK] Generated combined_er_viewer.html")

if __name__ == "__main__":
    main()
