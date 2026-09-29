#!/usr/bin/env python3
"""
Generator for School Management System ER Diagram - Part 1
Outputs:
1. School_Management_ER_Part1.drawio (Pure editable Draw.io XML for diagrams.net)
2. School_Management_ER_Part1.svg (Standalone vector graphic for high-res viewing)
3. School_Management_ER_Part1_Viewer.html (Interactive browser viewer)
Domain: Academic Hierarchy & Classroom Organization (grades, section, class)
Source of Truth: DATA_DICTIONARY.md
"""

import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

def generate_part1_drawio():
    # Canvas Dimensions (Landscape: 1400 x 780)
    page_width = 1400
    page_height = 780

    mxfile = ET.Element("mxfile", {
        "host": "app.diagrams.net",
        "modified": "2026-09-29T15:45:00.000Z",
        "agent": "Mozilla/5.0",
        "version": "21.0.0",
        "type": "device"
    })

    diagram = ET.SubElement(mxfile, "diagram", {
        "id": "sms-part1-academic-hierarchy",
        "name": "School Management System - Academic Hierarchy (Part 1)"
    })

    model = ET.SubElement(diagram, "mxGraphModel", {
        "dx": "1400",
        "dy": "780",
        "grid": "1",
        "gridSize": "10",
        "guides": "1",
        "tooltips": "1",
        "connect": "1",
        "arrows": "1",
        "fold": "1",
        "page": "1",
        "pageScale": "1",
        "pageWidth": str(page_width),
        "pageHeight": str(page_height),
        "background": "#FFFFFF",
        "math": "0",
        "shadow": "0"
    })

    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})

    # Helper function to add vertices
    def add_cell(cell_id, value, style, x, y, w, h, parent="1", vertex="1"):
        cell = ET.SubElement(root, "mxCell", {
            "id": cell_id,
            "value": value,
            "style": style,
            "parent": parent,
            "vertex": vertex
        })
        ET.SubElement(cell, "mxGeometry", {
            "x": str(x),
            "y": str(y),
            "width": str(w),
            "height": str(h),
            "as": "geometry"
        })
        return cell

    # Helper function to add edges
    def add_edge(edge_id, value, style, source_id, target_id, parent="1"):
        cell = ET.SubElement(root, "mxCell", {
            "id": edge_id,
            "value": value,
            "style": style,
            "parent": parent,
            "source": source_id,
            "target": target_id,
            "edge": "1"
        })
        ET.SubElement(cell, "mxGeometry", {
            "relative": "1",
            "as": "geometry"
        })
        return cell

    # =========================================================================
    # 1. HEADER / TITLE BANNER
    # =========================================================================
    banner_val = (
        '<div style="font-size: 18px; font-weight: bold; letter-spacing: 0.8px; margin-bottom: 4px;">'
        'SCHOOL MANAGEMENT SYSTEM (<span style="color: #0369a1;">sms_db</span>) — ER DIAGRAM (PART 1)'
        '</div>'
        '<div style="font-size: 12px; color: #475569; font-weight: normal;">'
        '<b>Module 1: Academic Hierarchy &amp; Classroom Organization</b> &nbsp;|&nbsp; '
        'Primary Source of Truth: <b>DATA_DICTIONARY.md</b> &nbsp;|&nbsp; '
        'Strict Foreign Key Referential Integrity'
        '</div>'
    )
    banner_style = (
        "shape=rectangle;rounded=1;arcSize=4;whiteSpace=wrap;html=1;"
        "fillColor=#F8FAFC;strokeColor=#334155;strokeWidth=1.8;"
        "align=center;verticalAlign=middle;fontFamily=Helvetica;fontColor=#0F172A;"
    )
    add_cell("title_banner", banner_val, banner_style, 70, 30, 1260, 65)

    # =========================================================================
    # 2. ENTITIES (RECTANGLES WITH STRUCTURED ATTRIBUTES)
    # =========================================================================
    ent_style = (
        "shape=rectangle;rounded=1;arcSize=4;whiteSpace=wrap;html=1;"
        "fillColor=#FFFFFF;strokeColor=#0F172A;strokeWidth=2;"
        "align=left;verticalAlign=top;spacingLeft=14;spacingRight=14;spacingTop=10;spacingBottom=10;"
        "fontFamily=Helvetica;fontColor=#0F172A;"
    )

    # Table 1: grades (Parent Table 1)
    grades_val = (
        '<div style="text-align: center; font-weight: bold; font-size: 15px; letter-spacing: 0.5px; padding-bottom: 6px; border-bottom: 2px solid #0F172A; margin-bottom: 8px;">grades</div>'
        '<div style="font-size: 12px; line-height: 1.8; font-family: Consolas, \'Courier New\', Courier, monospace;">'
        '<div><u><b>grade_id</b></u> <span style="color: #0369a1; font-weight: bold;">(PK)</span></div>'
        '<div>grade</div>'
        '<div>grade_code</div>'
        '</div>'
    )
    add_cell("ent_grades", grades_val, ent_style, 120, 240, 220, 140)

    # Table 2: class (Associative / Child Table)
    class_val = (
        '<div style="text-align: center; font-weight: bold; font-size: 15px; letter-spacing: 0.5px; padding-bottom: 6px; border-bottom: 2px solid #0F172A; margin-bottom: 8px;">class</div>'
        '<div style="font-size: 12px; line-height: 1.8; font-family: Consolas, \'Courier New\', Courier, monospace;">'
        '<div><u><b>class_id</b></u> <span style="color: #0369a1; font-weight: bold;">(PK)</span></div>'
        '<div><b>grade</b> <span style="color: #b91c1c; font-weight: bold;">(FK)</span></div>'
        '<div><b>section</b> <span style="color: #b91c1c; font-weight: bold;">(FK)</span></div>'
        '</div>'
    )
    add_cell("ent_class", class_val, ent_style, 590, 240, 220, 140)

    # Table 3: section (Parent Table 2)
    section_val = (
        '<div style="text-align: center; font-weight: bold; font-size: 15px; letter-spacing: 0.5px; padding-bottom: 6px; border-bottom: 2px solid #0F172A; margin-bottom: 8px;">section</div>'
        '<div style="font-size: 12px; line-height: 1.8; font-family: Consolas, \'Courier New\', Courier, monospace;">'
        '<div><u><b>section_id</b></u> <span style="color: #0369a1; font-weight: bold;">(PK)</span></div>'
        '<div>section</div>'
        '</div>'
    )
    add_cell("ent_section", section_val, ent_style, 1060, 240, 220, 140)

    # =========================================================================
    # 3. RELATIONSHIP DIAMONDS
    # =========================================================================
    diamond_style = (
        "shape=rhombus;whiteSpace=wrap;html=1;"
        "fillColor=#FFFFFF;strokeColor=#0F172A;strokeWidth=2;"
        "align=center;verticalAlign=middle;fontFamily=Helvetica;fontStyle=1;fontSize=13;fontColor=#0F172A;"
    )

    # Relationship 1: comprises (grades -> class)
    add_cell("rel_comprises", "<b>comprises</b>", diamond_style, 390, 270, 145, 80)

    # Relationship 2: divides (section -> class)
    add_cell("rel_divides", "<b>divides</b>", diamond_style, 865, 270, 145, 80)

    # =========================================================================
    # 4. RELATIONSHIP BADGES / OVERLAYS
    # =========================================================================
    badge_style = (
        "shape=rectangle;rounded=1;arcSize=20;whiteSpace=wrap;html=1;"
        "fillColor=#F1F5F9;strokeColor=#CBD5E1;strokeWidth=1;"
        "align=center;verticalAlign=middle;fontFamily=Helvetica;fontSize=10;fontColor=#334155;fontStyle=1;"
    )
    add_cell("badge_rel1", "1 : N Relationship", badge_style, 412, 238, 100, 22)
    add_cell("badge_rel2", "1 : N Relationship", badge_style, 888, 238, 100, 22)

    # =========================================================================
    # 5. CONNECTING LINES (EDGES) WITH ZERO OVERLAPS
    # =========================================================================
    edge_style = (
        "edgeStyle=none;rounded=0;html=1;endArrow=none;"
        "strokeColor=#0F172A;strokeWidth=2;"
    )

    # Connector 1: grades -> comprises
    add_edge("edge_grades_comprises", "", edge_style, "ent_grades", "rel_comprises")
    # Connector 2: comprises -> class
    add_edge("edge_comprises_class", "", edge_style, "rel_comprises", "ent_class")

    # Connector 3: section -> divides
    add_edge("edge_section_divides", "", edge_style, "ent_section", "rel_divides")
    # Connector 4: divides -> class
    add_edge("edge_divides_class", "", edge_style, "rel_divides", "ent_class")

    # =========================================================================
    # 6. CARDINALITY LABELS ON CONNECTOR SEGMENTS
    # =========================================================================
    card_label_style = (
        "shape=text;html=1;strokeColor=none;fillColor=none;"
        "align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;"
        "fontSize=14;fontStyle=1;fontFamily=Helvetica;fontColor=#0F172A;"
    )
    add_cell("card_grades", "1", card_label_style, 350, 280, 30, 25)
    add_cell("card_class_left", "N", card_label_style, 550, 280, 30, 25)
    add_cell("card_class_right", "N", card_label_style, 825, 280, 30, 25)
    add_cell("card_section", "1", card_label_style, 1020, 280, 30, 25)

    role_label_style = (
        "shape=text;html=1;strokeColor=none;fillColor=none;"
        "align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;"
        "fontSize=10;fontColor=#64748B;fontFamily=Helvetica;"
    )
    add_cell("role_grades", "(Parent Grade)", role_label_style, 325, 315, 80, 20)
    add_cell("role_class_left", "(Cohort)", role_label_style, 540, 315, 55, 20)
    add_cell("role_class_right", "(Cohort)", role_label_style, 810, 315, 55, 20)
    add_cell("role_section", "(Parent Section)", role_label_style, 1000, 315, 85, 20)

    # =========================================================================
    # 7. LOWER PANELS: REFERENTIAL INTEGRITY MATRIX & ER NOTATION LEGEND
    # =========================================================================
    card_fk_val = (
        '<div style="font-weight: bold; font-size: 13px; color: #0F172A; border-bottom: 1.5px solid #CBD5E1; padding-bottom: 5px; margin-bottom: 8px;">'
        'VERIFIED REFERENTIAL INTEGRITY (PK → FK CONSTRAINTS)'
        '</div>'
        '<table style="width: 100%; font-size: 11px; line-height: 1.6; border-collapse: collapse; color: #334155;">'
        '<tr style="background: #F1F5F9;">'
        '<th style="text-align: left; padding: 4px;">Child Table &amp; FK</th>'
        '<th style="text-align: left; padding: 4px;">Referenced Parent &amp; PK</th>'
        '<th style="text-align: center; padding: 4px;">Cardinality</th>'
        '<th style="text-align: left; padding: 4px;">Cascade Rule</th>'
        '</tr>'
        '<tr style="border-bottom: 1px solid #E2E8F0;">'
        '<td style="padding: 5px;"><b>class</b>.<span style="color: #b91c1c;">grade</span></td>'
        '<td style="padding: 5px;"><b>grades</b>.<span style="color: #0369a1;">grade_id</span></td>'
        '<td style="text-align: center; font-weight: bold;">1 : N</td>'
        '<td style="padding: 5px;">ON UPDATE CASCADE</td>'
        '</tr>'
        '<tr>'
        '<td style="padding: 5px;"><b>class</b>.<span style="color: #b91c1c;">section</span></td>'
        '<td style="padding: 5px;"><b>section</b>.<span style="color: #0369a1;">section_id</span></td>'
        '<td style="text-align: center; font-weight: bold;">1 : N</td>'
        '<td style="padding: 5px;">ON UPDATE CASCADE</td>'
        '</tr>'
        '</table>'
        '<div style="margin-top: 8px; font-size: 10.5px; color: #64748B;">'
        '<b>Business Semantics:</b> An instructional classroom cohort (<code>class</code>) is an associative pairing '
        'linking a grade standard (<code>grades</code>) with a physical division (<code>section</code>).'
        '</div>'
    )
    panel_style = (
        "shape=rectangle;rounded=1;arcSize=4;whiteSpace=wrap;html=1;"
        "fillColor=#F8FAFC;strokeColor=#CBD5E1;strokeWidth=1.5;"
        "align=left;verticalAlign=top;spacingLeft=14;spacingRight=14;spacingTop=10;spacingBottom=10;"
        "fontFamily=Helvetica;fontColor=#0F172A;"
    )
    add_cell("panel_fk_matrix", card_fk_val, panel_style, 120, 440, 600, 180)

    card_legend_val = (
        '<div style="font-weight: bold; font-size: 13px; color: #0F172A; border-bottom: 1.5px solid #CBD5E1; padding-bottom: 5px; margin-bottom: 8px;">'
        'ER NOTATION LEGEND &amp; EXTENSIBILITY (PART 1 FOUNDATION)'
        '</div>'
        '<table style="width: 100%; font-size: 11px; line-height: 1.6; border-collapse: collapse; color: #334155;">'
        '<tr>'
        '<td style="width: 140px; padding: 4px;"><b>Rectangle</b></td>'
        '<td style="padding: 4px;">Entity Table containing exact columns from <i>DATA_DICTIONARY.md</i></td>'
        '</tr>'
        '<tr>'
        '<td style="padding: 4px;"><b><span style="color: #0369a1;">(PK)</span></b> Underlined</td>'
        '<td style="padding: 4px;">Primary Key column (Unique, Auto-increment, Not Null)</td>'
        '</tr>'
        '<tr>'
        '<td style="padding: 4px;"><b><span style="color: #b91c1c;">(FK)</span></b> Bold Tag</td>'
        '<td style="padding: 4px;">Foreign Key column maintaining InnoDB relational integrity</td>'
        '</tr>'
        '<tr>'
        '<td style="padding: 4px;"><b>Rhombus / Diamond</b></td>'
        '<td style="padding: 4px;">Semantic relationship connector between parent and child tables</td>'
        '</tr>'
        '<tr>'
        '<td style="padding: 4px;"><b>Cardinality 1 : N</b></td>'
        '<td style="padding: 4px;">One parent record maps to multiple child records (Zero crossing lines)</td>'
        '</tr>'
        '</table>'
        '<div style="margin-top: 8px; font-size: 10.5px; color: #64748B;">'
        '<b>Part 2 Extension Points:</b> <code>grades</code> will connect to <code>subjects</code> &amp; <code>student</code>; '
        '<code>section</code> will connect to <code>student</code>.'
        '</div>'
    )
    add_cell("panel_legend", card_legend_val, panel_style, 760, 440, 520, 180)

    # Bottom Footer Note
    footer_val = (
        '<div style="text-align: center; font-size: 11px; color: #64748B;">'
        'School Management System Database (<code>sms_db</code>) | Editable Draw.io Diagram File | Generated for diagrams.net'
        '</div>'
    )
    add_cell("footer_note", footer_val, "shape=text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;", 70, 645, 1260, 25)

    # Convert to XML string
    raw_xml = ET.tostring(mxfile, encoding="utf-8")
    reparsed = minidom.parseString(raw_xml)
    pretty_xml = reparsed.toprettyxml(indent="  ", encoding="utf-8")

    out_path = r"c:\xampp\htdocs\school-management\School_Management_ER_Part1.drawio"
    with open(out_path, "wb") as f:
        f.write(pretty_xml)

    print(f"Successfully generated Draw.io: {out_path} ({len(pretty_xml)} bytes)")


def generate_part1_svg():
    """Generates a standalone, beautiful SVG file for immediate preview."""
    svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 750" width="1400" height="750" style="background:#FFFFFF; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- TITLE BANNER -->
  <g transform="translate(70, 30)">
    <rect width="1260" height="68" rx="6" fill="#F8FAFC" stroke="#334155" stroke-width="1.8" filter="url(#shadow)"/>
    <text x="630" y="32" text-anchor="middle" font-size="18" font-weight="bold" fill="#0F172A">
      SCHOOL MANAGEMENT SYSTEM (<tspan fill="#0284C7">sms_db</tspan>) — ER DIAGRAM (PART 1)
    </text>
    <text x="630" y="52" text-anchor="middle" font-size="12" fill="#475569">
      <tspan font-weight="bold">Module 1: Academic Hierarchy &amp; Classroom Organization</tspan> | Primary Source of Truth: <tspan font-weight="bold">DATA_DICTIONARY.md</tspan> | Strict Foreign Key Referential Integrity
    </text>
  </g>

  <!-- CONNECTING RELATIONSHIP LINES -->
  <!-- Line 1: grades to comprises -->
  <line x1="340" y1="310" x2="390" y2="310" stroke="#0F172A" stroke-width="2.2"/>
  <!-- Line 2: comprises to class -->
  <line x1="535" y1="310" x2="590" y2="310" stroke="#0F172A" stroke-width="2.2"/>
  <!-- Line 3: class to divides -->
  <line x1="810" y1="310" x2="865" y2="310" stroke="#0F172A" stroke-width="2.2"/>
  <!-- Line 4: divides to section -->
  <line x1="1010" y1="310" x2="1060" y2="310" stroke="#0F172A" stroke-width="2.2"/>

  <!-- CARDINALITY & ROLES ON LINES -->
  <!-- grades side -->
  <text x="365" y="300" text-anchor="middle" font-size="16" font-weight="bold" fill="#0F172A">1</text>
  <text x="365" y="330" text-anchor="middle" font-size="10" fill="#64748B">(Grade)</text>

  <!-- class left side -->
  <text x="562" y="300" text-anchor="middle" font-size="16" font-weight="bold" fill="#0F172A">N</text>
  <text x="562" y="330" text-anchor="middle" font-size="10" fill="#64748B">(Cohort)</text>

  <!-- class right side -->
  <text x="838" y="300" text-anchor="middle" font-size="16" font-weight="bold" fill="#0F172A">N</text>
  <text x="838" y="330" text-anchor="middle" font-size="10" fill="#64748B">(Cohort)</text>

  <!-- section side -->
  <text x="1035" y="300" text-anchor="middle" font-size="16" font-weight="bold" fill="#0F172A">1</text>
  <text x="1035" y="330" text-anchor="middle" font-size="10" fill="#64748B">(Section)</text>

  <!-- RELATIONSHIP BADGES (ABOVE DIAMONDS) -->
  <rect x="412.5" y="238" width="100" height="22" rx="11" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
  <text x="462.5" y="253" text-anchor="middle" font-size="10" font-weight="bold" fill="#334155">1 : N Relationship</text>

  <rect x="887.5" y="238" width="100" height="22" rx="11" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1"/>
  <text x="937.5" y="253" text-anchor="middle" font-size="10" font-weight="bold" fill="#334155">1 : N Relationship</text>

  <!-- RELATIONSHIP DIAMONDS -->
  <!-- comprises diamond -->
  <g transform="translate(390, 270)">
    <polygon points="72.5,0 145,40 72.5,80 0,40" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.2" filter="url(#shadow)"/>
    <text x="72.5" y="45" text-anchor="middle" font-size="13" font-weight="bold" fill="#0F172A">comprises</text>
  </g>

  <!-- divides diamond -->
  <g transform="translate(865, 270)">
    <polygon points="72.5,0 145,40 72.5,80 0,40" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.2" filter="url(#shadow)"/>
    <text x="72.5" y="45" text-anchor="middle" font-size="13" font-weight="bold" fill="#0F172A">divides</text>
  </g>

  <!-- ENTITY 1: grades -->
  <g transform="translate(120, 240)">
    <rect width="220" height="140" rx="4" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.2" filter="url(#shadow)"/>
    <rect width="220" height="34" rx="4" fill="#F8FAFC" stroke="#0F172A" stroke-width="2.2"/>
    <line x1="0" y1="34" x2="220" y2="34" stroke="#0F172A" stroke-width="2"/>
    <text x="110" y="23" text-anchor="middle" font-size="14" font-weight="bold" fill="#0F172A">grades</text>

    <!-- Attributes -->
    <text x="18" y="60" font-size="12" font-family="Consolas, monospace" fill="#0F172A">
      <tspan font-weight="bold" text-decoration="underline">grade_id</tspan> <tspan fill="#0284C7" font-weight="bold">(PK)</tspan>
    </text>
    <text x="18" y="85" font-size="12" font-family="Consolas, monospace" fill="#334155">grade</text>
    <text x="18" y="110" font-size="12" font-family="Consolas, monospace" fill="#334155">grade_code</text>
  </g>

  <!-- ENTITY 2: class (Associative / Junction Entity) -->
  <g transform="translate(590, 240)">
    <rect width="220" height="140" rx="4" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.2" filter="url(#shadow)"/>
    <rect width="220" height="34" rx="4" fill="#F8FAFC" stroke="#0F172A" stroke-width="2.2"/>
    <line x1="0" y1="34" x2="220" y2="34" stroke="#0F172A" stroke-width="2"/>
    <text x="110" y="23" text-anchor="middle" font-size="14" font-weight="bold" fill="#0F172A">class</text>

    <!-- Attributes -->
    <text x="18" y="60" font-size="12" font-family="Consolas, monospace" fill="#0F172A">
      <tspan font-weight="bold" text-decoration="underline">class_id</tspan> <tspan fill="#0284C7" font-weight="bold">(PK)</tspan>
    </text>
    <text x="18" y="85" font-size="12" font-family="Consolas, monospace" fill="#0F172A">
      <tspan font-weight="bold">grade</tspan> <tspan fill="#B91C1C" font-weight="bold">(FK)</tspan>
    </text>
    <text x="18" y="110" font-size="12" font-family="Consolas, monospace" fill="#0F172A">
      <tspan font-weight="bold">section</tspan> <tspan fill="#B91C1C" font-weight="bold">(FK)</tspan>
    </text>
  </g>

  <!-- ENTITY 3: section -->
  <g transform="translate(1060, 240)">
    <rect width="220" height="140" rx="4" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.2" filter="url(#shadow)"/>
    <rect width="220" height="34" rx="4" fill="#F8FAFC" stroke="#0F172A" stroke-width="2.2"/>
    <line x1="0" y1="34" x2="220" y2="34" stroke="#0F172A" stroke-width="2"/>
    <text x="110" y="23" text-anchor="middle" font-size="14" font-weight="bold" fill="#0F172A">section</text>

    <!-- Attributes -->
    <text x="18" y="60" font-size="12" font-family="Consolas, monospace" fill="#0F172A">
      <tspan font-weight="bold" text-decoration="underline">section_id</tspan> <tspan fill="#0284C7" font-weight="bold">(PK)</tspan>
    </text>
    <text x="18" y="85" font-size="12" font-family="Consolas, monospace" fill="#334155">section</text>
  </g>

  <!-- LOWER PANELS: REFERENTIAL INTEGRITY & ER NOTATION LEGEND -->
  <!-- Panel 1: FK Matrix -->
  <g transform="translate(120, 440)">
    <rect width="600" height="180" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="20" y="28" font-size="13" font-weight="bold" fill="#0F172A">VERIFIED REFERENTIAL INTEGRITY (PK → FK CONSTRAINTS)</text>
    <line x1="20" y1="36" x2="580" y2="36" stroke="#CBD5E1" stroke-width="1"/>

    <!-- Table header -->
    <rect x="20" y="46" width="560" height="24" fill="#F1F5F9" rx="3"/>
    <text x="30" y="62" font-size="11" font-weight="bold" fill="#334155">Child Table &amp; FK</text>
    <text x="180" y="62" font-size="11" font-weight="bold" fill="#334155">Referenced Parent &amp; PK</text>
    <text x="350" y="62" font-size="11" font-weight="bold" fill="#334155">Cardinality</text>
    <text x="440" y="62" font-size="11" font-weight="bold" fill="#334155">Cascade Rule</text>

    <!-- Row 1 -->
    <text x="30" y="88" font-size="11" font-family="Consolas, monospace" fill="#0F172A">class.<tspan fill="#B91C1C" font-weight="bold">grade</tspan></text>
    <text x="180" y="88" font-size="11" font-family="Consolas, monospace" fill="#0F172A">grades.<tspan fill="#0284C7" font-weight="bold">grade_id</tspan></text>
    <text x="375" y="88" text-anchor="middle" font-size="11" font-weight="bold" fill="#0F172A">1 : N</text>
    <text x="440" y="88" font-size="11" fill="#475569">ON UPDATE CASCADE</text>
    <line x1="20" y1="98" x2="580" y2="98" stroke="#E2E8F0" stroke-width="1"/>

    <!-- Row 2 -->
    <text x="30" y="118" font-size="11" font-family="Consolas, monospace" fill="#0F172A">class.<tspan fill="#B91C1C" font-weight="bold">section</tspan></text>
    <text x="180" y="118" font-size="11" font-family="Consolas, monospace" fill="#0F172A">section.<tspan fill="#0284C7" font-weight="bold">section_id</tspan></text>
    <text x="375" y="118" text-anchor="middle" font-size="11" font-weight="bold" fill="#0F172A">1 : N</text>
    <text x="440" y="118" font-size="11" fill="#475569">ON UPDATE CASCADE</text>

    <!-- Explanatory note -->
    <text x="20" y="152" font-size="10.5" fill="#64748B">
      <tspan font-weight="bold">Business Semantics:</tspan> An instructional classroom cohort (class) is an associative pairing linking
    </text>
    <text x="20" y="168" font-size="10.5" fill="#64748B">
      a grade standard (grades) with a physical section division (section).
    </text>
  </g>

  <!-- Panel 2: Legend -->
  <g transform="translate(760, 440)">
    <rect width="520" height="180" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)"/>
    <text x="20" y="28" font-size="13" font-weight="bold" fill="#0F172A">ER NOTATION LEGEND &amp; EXTENSIBILITY (PART 1)</text>
    <line x1="20" y1="36" x2="500" y2="36" stroke="#CBD5E1" stroke-width="1"/>

    <text x="20" y="60" font-size="11" font-weight="bold" fill="#0F172A">Rectangle Box</text>
    <text x="160" y="60" font-size="11" fill="#475569">Entity Table with exact columns from DATA_DICTIONARY.md</text>

    <text x="20" y="82" font-size="11" font-weight="bold" fill="#0284C7">(PK) Underline</text>
    <text x="160" y="82" font-size="11" fill="#475569">Primary Key (Unique, Auto-increment, Not Null)</text>

    <text x="20" y="104" font-size="11" font-weight="bold" fill="#B91C1C">(FK) Tag</text>
    <text x="160" y="104" font-size="11" fill="#475569">Foreign Key column maintaining InnoDB referential integrity</text>

    <text x="20" y="126" font-size="11" font-weight="bold" fill="#0F172A">Rhombus / Diamond</text>
    <text x="160" y="126" font-size="11" fill="#475569">Semantic relationship connector between parent and child</text>

    <text x="20" y="148" font-size="11" font-weight="bold" fill="#0F172A">Cardinality 1 : N</text>
    <text x="160" y="148" font-size="11" fill="#475569">One parent record maps to multiple child records</text>

    <text x="20" y="170" font-size="10.5" fill="#64748B">
      <tspan font-weight="bold">Part 2 Extension:</tspan> grades connects to subjects &amp; student; section connects to student.
    </text>
  </g>

  <!-- FOOTER -->
  <text x="700" y="660" text-anchor="middle" font-size="11" fill="#64748B">
    School Management System Database (sms_db) | Editable Draw.io Diagram File: School_Management_ER_Part1.drawio | Open in diagrams.net
  </text>
</svg>"""

    svg_path = r"c:\xampp\htdocs\school-management\School_Management_ER_Part1.svg"
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Successfully generated SVG: {svg_path} ({len(svg_content)} bytes)")


def generate_viewer_html():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>School Management System — ER Diagram Part 1 Viewer</title>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    body {
      background: #0f172a;
      color: #f8fafc;
      overflow: hidden;
      height: 100vh;
      display: flex;
      flex-direction: column;
    }
    header {
      background: #1e293b;
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #334155;
      z-index: 10;
    }
    .header-title h1 {
      font-size: 17px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .badge {
      font-size: 11px;
      padding: 3px 8px;
      border-radius: 9999px;
      background: #059669;
      color: #ffffff;
      font-weight: 600;
    }
    .header-title p {
      font-size: 12px;
      color: #94a3b8;
      margin-top: 2px;
    }
    .actions {
      display: flex;
      gap: 10px;
      align-items: center;
    }
    .btn {
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
    }
    .btn:hover {
      background: #475569;
    }
    .btn-primary {
      background: #2563eb;
      border-color: #3b82f6;
    }
    .btn-primary:hover {
      background: #1d4ed8;
    }
    .viewport {
      flex: 1;
      overflow: auto;
      padding: 24px;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      background: #090d16;
    }
    .sheet-card {
      background: #ffffff;
      border-radius: 8px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6);
      width: 100%;
      max-width: 1400px;
    }
    img {
      display: block;
      width: 100%;
      height: auto;
    }
  </style>
</head>
<body>
  <header>
    <div class="header-title">
      <h1>School Management System — ER Diagram Part 1 <span class="badge">Academic Hierarchy</span></h1>
      <p>Editable File: School_Management_ER_Part1.drawio | Tables: grades, section, class | Source: DATA_DICTIONARY.md</p>
    </div>
    <div class="actions">
      <a href="School_Management_ER_Part1.drawio" download class="btn btn-primary">Download .drawio File</a>
      <a href="https://app.diagrams.net/" target="_blank" class="btn">Open in diagrams.net</a>
    </div>
  </header>

  <div class="viewport">
    <div class="sheet-card">
      <img src="School_Management_ER_Part1.svg" alt="School Management ER Diagram Part 1" />
    </div>
  </div>
</body>
</html>"""
    html_path = r"c:\xampp\htdocs\school-management\School_Management_ER_Part1_Viewer.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully generated HTML Viewer: {html_path} ({len(html_content)} bytes)")


if __name__ == "__main__":
    generate_part1_drawio()
    generate_part1_svg()
    generate_viewer_html()
