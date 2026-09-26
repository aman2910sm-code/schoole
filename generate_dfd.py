#!/usr/bin/env python3
"""
DFD Level 1 Generator for School Management System.
Generates:
1. school_management_dfd_level1.drawio (Multi-page draw.io XML with Gane & Sarson and Yourdon DeMarco)
2. dfd_level1_gane_sarson.svg (Standalone high-res SVG for Gane & Sarson)
3. dfd_level1_yourdon_demarco.svg (Standalone high-res SVG for Yourdon DeMarco)
4. dfd_level1_viewer.html (Interactive standalone HTML viewer)
"""

import html
import os
import xml.etree.ElementTree as ET

def build_drawio_xml():
    # We will construct standard draw.io / diagrams.net XML
    # Using clean orthogonal layout, robust mxGraph styles
    
    # Page 1: Gane & Sarson Notation
    # Page 2: Yourdon & DeMarco Notation
    
    xml_content = '''<mxfile host="app.diagrams.net" modified="2026-09-26T00:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="gane-sarson" name="DFD Level 1 (Gane &amp; Sarson Notation)">
    <mxGraphModel dx="1600" dy="1100" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1700" pageHeight="1160" background="#FFFFFF" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- ================= DIAGRAM HEADER & TITLE ================= -->
        <mxCell id="title_banner" value="DATA FLOW DIAGRAM (DFD) LEVEL 1: SCHOOL MANAGEMENT SYSTEM&#xa;Notation: Gane &amp; Sarson | Modules: Admin, Teacher, Student, Registrar Office" style="shape=rectangle;fillColor=#1E293B;strokeColor=#0F172A;fontColor=#FFFFFF;fontStyle=1;fontSize=16;align=center;verticalAlign=middle;rounded=1;arcSize=8;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="20" width="1580" height="45" as="geometry" />
        </mxCell>

        <!-- ================= EXTERNAL ENTITIES (Sharp Rectangles) ================= -->
        <!-- Admin Entity -->
        <mxCell id="ent_admin" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;b&gt;Admin&lt;/b&gt;&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(School Administrator)&lt;/i&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontColor=#0F172A;fontSize=12;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="140" width="160" height="90" as="geometry" />
        </mxCell>

        <!-- Registrar Office Entity -->
        <mxCell id="ent_registrar" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;b&gt;Registrar Office&lt;/b&gt;&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Admissions &amp; Records)&lt;/i&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontColor=#0F172A;fontSize=12;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="740" width="160" height="90" as="geometry" />
        </mxCell>

        <!-- Teacher Entity -->
        <mxCell id="ent_teacher" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;b&gt;Teacher&lt;/b&gt;&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Faculty Staff)&lt;/i&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontColor=#0F172A;fontSize=12;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1480" y="140" width="160" height="90" as="geometry" />
        </mxCell>

        <!-- Student Entity -->
        <mxCell id="ent_student" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;b&gt;Student&lt;/b&gt;&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Learner / Enrollee)&lt;/i&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontColor=#0F172A;fontSize=12;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1480" y="740" width="160" height="90" as="geometry" />
        </mxCell>


        <!-- ================= PROCESSES (Gane & Sarson: Rounded Rect with Top ID Band) ================= -->
        <!-- Process 1.0: Admin Management -->
        <mxCell id="p1_group" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="360" y="130" width="220" height="110" as="geometry" />
        </mxCell>
        <mxCell id="p1_box" value="" style="rounded=1;arcSize=14;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#2563EB;strokeWidth=2;shadow=1;" vertex="1" parent="p1_group">
          <mxGeometry x="0" y="0" width="220" height="110" as="geometry" />
        </mxCell>
        <mxCell id="p1_header" value="1.0" style="rounded=1;arcSize=28;whiteSpace=wrap;html=1;fillColor=#BFDBFE;strokeColor=#2563EB;strokeWidth=1.5;fontStyle=1;fontSize=14;fontColor=#1E3A8A;align=center;" vertex="1" parent="p1_group">
          <mxGeometry x="0" y="0" width="220" height="32" as="geometry" />
        </mxCell>
        <mxCell id="p1_label" value="&lt;b&gt;Admin Management&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 11px; color: #475569;&quot;&gt;User Accounts, Settings,&lt;br/&gt;Classes, Grades &amp;amp; Notices&lt;/font&gt;" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=13;fontColor=#0F172A;" vertex="1" parent="p1_group">
          <mxGeometry x="5" y="34" width="210" height="72" as="geometry" />
        </mxCell>

        <!-- Process 4.0: Registrar Office Admissions -->
        <mxCell id="p4_group" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="360" y="730" width="220" height="110" as="geometry" />
        </mxCell>
        <mxCell id="p4_box" value="" style="rounded=1;arcSize=14;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#2563EB;strokeWidth=2;shadow=1;" vertex="1" parent="p4_group">
          <mxGeometry x="0" y="0" width="220" height="110" as="geometry" />
        </mxCell>
        <mxCell id="p4_header" value="4.0" style="rounded=1;arcSize=28;whiteSpace=wrap;html=1;fillColor=#BFDBFE;strokeColor=#2563EB;strokeWidth=1.5;fontStyle=1;fontSize=14;fontColor=#1E3A8A;align=center;" vertex="1" parent="p4_group">
          <mxGeometry x="0" y="0" width="220" height="32" as="geometry" />
        </mxCell>
        <mxCell id="p4_label" value="&lt;b&gt;Registrar Office Management&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 11px; color: #475569;&quot;&gt;Student Admissions, Enrollment&lt;br/&gt;&amp;amp; Demographic Search&lt;/font&gt;" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=13;fontColor=#0F172A;" vertex="1" parent="p4_group">
          <mxGeometry x="5" y="34" width="210" height="72" as="geometry" />
        </mxCell>

        <!-- Process 2.0: Teacher Operations & Grading -->
        <mxCell id="p2_group" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="1120" y="130" width="220" height="110" as="geometry" />
        </mxCell>
        <mxCell id="p2_box" value="" style="rounded=1;arcSize=14;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#2563EB;strokeWidth=2;shadow=1;" vertex="1" parent="p2_group">
          <mxGeometry x="0" y="0" width="220" height="110" as="geometry" />
        </mxCell>
        <mxCell id="p2_header" value="2.0" style="rounded=1;arcSize=28;whiteSpace=wrap;html=1;fillColor=#BFDBFE;strokeColor=#2563EB;strokeWidth=1.5;fontStyle=1;fontSize=14;fontColor=#1E3A8A;align=center;" vertex="1" parent="p2_group">
          <mxGeometry x="0" y="0" width="220" height="32" as="geometry" />
        </mxCell>
        <mxCell id="p2_label" value="&lt;b&gt;Teacher Operations&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 11px; color: #475569;&quot;&gt;Assigned Class Rosters,&lt;br/&gt;Student Grading &amp;amp; Scores&lt;/font&gt;" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=13;fontColor=#0F172A;" vertex="1" parent="p2_group">
          <mxGeometry x="5" y="34" width="210" height="72" as="geometry" />
        </mxCell>

        <!-- Process 3.0: Student Portal -->
        <mxCell id="p3_group" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="1120" y="730" width="220" height="110" as="geometry" />
        </mxCell>
        <mxCell id="p3_box" value="" style="rounded=1;arcSize=14;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#2563EB;strokeWidth=2;shadow=1;" vertex="1" parent="p3_group">
          <mxGeometry x="0" y="0" width="220" height="110" as="geometry" />
        </mxCell>
        <mxCell id="p3_header" value="3.0" style="rounded=1;arcSize=28;whiteSpace=wrap;html=1;fillColor=#BFDBFE;strokeColor=#2563EB;strokeWidth=1.5;fontStyle=1;fontSize=14;fontColor=#1E3A8A;align=center;" vertex="1" parent="p3_group">
          <mxGeometry x="0" y="0" width="220" height="32" as="geometry" />
        </mxCell>
        <mxCell id="p3_label" value="&lt;b&gt;Student Portal Management&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 11px; color: #475569;&quot;&gt;Academic Report Card, Profile,&lt;br/&gt;Credentials &amp;amp; Inquiries&lt;/font&gt;" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=13;fontColor=#0F172A;" vertex="1" parent="p3_group">
          <mxGeometry x="5" y="34" width="210" height="72" as="geometry" />
        </mxCell>


        <!-- ================= DATA STORES (Gane & Sarson: Left ID Box, Open Right Box) ================= -->
        <!-- D1: Admin & Settings -->
        <mxCell id="ds_d1_group" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="725" y="80" width="250" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d1_id" value="D1" style="shape=rectangle;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontStyle=1;fontSize=13;fontColor=#1E3A8A;align=center;verticalAlign=middle;" vertex="1" parent="ds_d1_group">
          <mxGeometry x="0" y="0" width="45" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d1_name" value="&lt;b&gt;Admin &amp;amp; System Settings&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 10px; color: #64748B;&quot;&gt;[admin, setting]&lt;/font&gt;" style="shape=partialRectangle;top=1;left=0;bottom=1;right=0;fillColor=#F8FAFC;strokeColor=#4A7BB0;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=10;verticalAlign=middle;fontSize=12;fontColor=#0F172A;" vertex="1" parent="ds_d1_group">
          <mxGeometry x="45" y="0" width="205" height="46" as="geometry" />
        </mxCell>

        <!-- D2: Teachers -->
        <mxCell id="ds_d2_group" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="725" y="215" width="250" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d2_id" value="D2" style="shape=rectangle;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontStyle=1;fontSize=13;fontColor=#1E3A8A;align=center;verticalAlign=middle;" vertex="1" parent="ds_d2_group">
          <mxGeometry x="0" y="0" width="45" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d2_name" value="&lt;b&gt;Teacher Records&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 10px; color: #64748B;&quot;&gt;[teacher]&lt;/font&gt;" style="shape=partialRectangle;top=1;left=0;bottom=1;right=0;fillColor=#F8FAFC;strokeColor=#4A7BB0;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=10;verticalAlign=middle;fontSize=12;fontColor=#0F172A;" vertex="1" parent="ds_d2_group">
          <mxGeometry x="45" y="0" width="205" height="46" as="geometry" />
        </mxCell>

        <!-- D7: Registrar Office Staff -->
        <mxCell id="ds_d7_group" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="725" y="350" width="250" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d7_id" value="D7" style="shape=rectangle;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontStyle=1;fontSize=13;fontColor=#1E3A8A;align=center;verticalAlign=middle;" vertex="1" parent="ds_d7_group">
          <mxGeometry x="0" y="0" width="45" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d7_name" value="&lt;b&gt;Registrar Staff Records&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 10px; color: #64748B;&quot;&gt;[registrar_office]&lt;/font&gt;" style="shape=partialRectangle;top=1;left=0;bottom=1;right=0;fillColor=#F8FAFC;strokeColor=#4A7BB0;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=10;verticalAlign=middle;fontSize=12;fontColor=#0F172A;" vertex="1" parent="ds_d7_group">
          <mxGeometry x="45" y="0" width="205" height="46" as="geometry" />
        </mxCell>

        <!-- D4: Academic Structure (Classes, Sections, Courses) -->
        <mxCell id="ds_d4_group" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="725" y="485" width="250" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d4_id" value="D4" style="shape=rectangle;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontStyle=1;fontSize=13;fontColor=#1E3A8A;align=center;verticalAlign=middle;" vertex="1" parent="ds_d4_group">
          <mxGeometry x="0" y="0" width="45" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d4_name" value="&lt;b&gt;Academic Structure&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 10px; color: #64748B;&quot;&gt;[grades, section, class, subjects]&lt;/font&gt;" style="shape=partialRectangle;top=1;left=0;bottom=1;right=0;fillColor=#F8FAFC;strokeColor=#4A7BB0;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=10;verticalAlign=middle;fontSize=12;fontColor=#0F172A;" vertex="1" parent="ds_d4_group">
          <mxGeometry x="45" y="0" width="205" height="46" as="geometry" />
        </mxCell>

        <!-- D3: Students -->
        <mxCell id="ds_d3_group" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="725" y="620" width="250" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d3_id" value="D3" style="shape=rectangle;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontStyle=1;fontSize=13;fontColor=#1E3A8A;align=center;verticalAlign=middle;" vertex="1" parent="ds_d3_group">
          <mxGeometry x="0" y="0" width="45" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d3_name" value="&lt;b&gt;Student Records&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 10px; color: #64748B;&quot;&gt;[student]&lt;/font&gt;" style="shape=partialRectangle;top=1;left=0;bottom=1;right=0;fillColor=#F8FAFC;strokeColor=#4A7BB0;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=10;verticalAlign=middle;fontSize=12;fontColor=#0F172A;" vertex="1" parent="ds_d3_group">
          <mxGeometry x="45" y="0" width="205" height="46" as="geometry" />
        </mxCell>

        <!-- D5: Student Scores -->
        <mxCell id="ds_d5_group" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="725" y="755" width="250" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d5_id" value="D5" style="shape=rectangle;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontStyle=1;fontSize=13;fontColor=#1E3A8A;align=center;verticalAlign=middle;" vertex="1" parent="ds_d5_group">
          <mxGeometry x="0" y="0" width="45" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d5_name" value="&lt;b&gt;Scores &amp;amp; Academic Results&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 10px; color: #64748B;&quot;&gt;[student_score]&lt;/font&gt;" style="shape=partialRectangle;top=1;left=0;bottom=1;right=0;fillColor=#F8FAFC;strokeColor=#4A7BB0;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=10;verticalAlign=middle;fontSize=12;fontColor=#0F172A;" vertex="1" parent="ds_d5_group">
          <mxGeometry x="45" y="0" width="205" height="46" as="geometry" />
        </mxCell>

        <!-- D6: Messages -->
        <mxCell id="ds_d6_group" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="725" y="890" width="250" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d6_id" value="D6" style="shape=rectangle;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontStyle=1;fontSize=13;fontColor=#1E3A8A;align=center;verticalAlign=middle;" vertex="1" parent="ds_d6_group">
          <mxGeometry x="0" y="0" width="45" height="46" as="geometry" />
        </mxCell>
        <mxCell id="ds_d6_name" value="&lt;b&gt;Inquiries &amp;amp; Messages&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 10px; color: #64748B;&quot;&gt;[message]&lt;/font&gt;" style="shape=partialRectangle;top=1;left=0;bottom=1;right=0;fillColor=#F8FAFC;strokeColor=#4A7BB0;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=10;verticalAlign=middle;fontSize=12;fontColor=#0F172A;" vertex="1" parent="ds_d6_group">
          <mxGeometry x="45" y="0" width="205" height="46" as="geometry" />
        </mxCell>


        <!-- ================= DATA FLOWS: ADMIN MODULE (1.0) ================= -->
        <!-- Flow: Admin -> 1.0 (Credentials & Config) -->
        <mxCell id="flow_admin_to_p1_1" value="Admin Credentials &amp;amp; School Info" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.25;entryDx=0;entryDy=0;exitX=1;exitY=0.25;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_admin" target="p1_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: Admin -> 1.0 (Staff Creation) -->
        <mxCell id="flow_admin_to_p1_2" value="Staff Accounts &amp;amp; Class Details" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.55;entryDx=0;entryDy=0;exitX=1;exitY=0.55;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_admin" target="p1_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: 1.0 -> Admin (Reports & Inquiries) -->
        <mxCell id="flow_p1_to_admin" value="Admin Dashboard, Metrics &amp;amp; Feedback" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.85;entryDx=0;entryDy=0;exitX=0;exitY=0.85;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="p1_box" target="ent_admin">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: 1.0 <-> D1 (Admin & Settings) -->
        <mxCell id="flow_p1_d1" value="Update &amp;amp; Read System Settings" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.2;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;endArrow=classic;startArrow=classic;" edge="1" parent="1" source="p1_box" target="ds_d1_id">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: 1.0 -> D2 (Teacher Creation) -->
        <mxCell id="flow_p1_d2" value="Create / Update Teacher Profiles" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.6;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="p1_box" target="ds_d2_id">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: 1.0 -> D7 (Registrar Setup) -->
        <mxCell id="flow_p1_d7" value="Manage Registrar Staff Accounts" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=0.9;exitY=1;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="p1_box" target="ds_d7_id">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: 1.0 -> D4 (Setup Classes, Grades) -->
        <mxCell id="flow_p1_d4" value="Configure Classes, Grades &amp;amp; Subjects" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.3;entryDx=0;entryDy=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="p1_box" target="ds_d4_id">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="470" y="499" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: D6 -> 1.0 (Read Inquiries) -->
        <mxCell id="flow_d6_p1" value="Read Feedback &amp;amp; Messages" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.2;entryY=1;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ds_d6_id" target="p1_box">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="320" y="913" />
              <mxPoint x="320" y="320" />
              <mxPoint x="404" y="320" />
            </Array>
          </mxGeometry>
        </mxCell>


        <!-- ================= DATA FLOWS: REGISTRAR OFFICE MODULE (4.0) ================= -->
        <!-- Flow: Registrar -> 4.0 (Auth) -->
        <mxCell id="flow_reg_to_p4_1" value="Staff Login Credentials" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.25;entryDx=0;entryDy=0;exitX=1;exitY=0.25;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_registrar" target="p4_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: Registrar -> 4.0 (Student Data & Search) -->
        <mxCell id="flow_reg_to_p4_2" value="New Student Admission Details &amp;amp; Query" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.55;entryDx=0;entryDy=0;exitX=1;exitY=0.55;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_registrar" target="p4_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: 4.0 -> Registrar (Confirmations) -->
        <mxCell id="flow_p4_to_reg" value="Enrollment Confirmation &amp;amp; Search Results" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.85;entryDx=0;entryDy=0;exitX=0;exitY=0.85;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="p4_box" target="ent_registrar">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: D7 -> 4.0 (Verify Staff) -->
        <mxCell id="flow_d7_p4" value="Verify Registrar Credentials" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.9;entryY=0;entryDx=0;entryDy=0;exitX=0;exitY=0.8;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ds_d7_id" target="p4_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: D4 -> 4.0 (Get Grades & Sections) -->
        <mxCell id="flow_d4_p4" value="Fetch Classes, Grades &amp;amp; Section Lists" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=0;exitY=0.7;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ds_d4_id" target="p4_box">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="470" y="517" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: 4.0 <-> D3 (Save/Read Student Records) -->
        <mxCell id="flow_p4_d3" value="Register / Query Student Demographic Records" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.3;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;startArrow=classic;endArrow=classic;" edge="1" parent="1" source="p4_box" target="ds_d3_id">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>


        <!-- ================= DATA FLOWS: TEACHER MODULE (2.0) ================= -->
        <!-- Flow: Teacher -> 2.0 (Auth) -->
        <mxCell id="flow_teach_to_p2_1" value="Teacher Login Credentials" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.25;entryDx=0;entryDy=0;exitX=0;exitY=0.25;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_teacher" target="p2_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: Teacher -> 2.0 (Marks) -->
        <mxCell id="flow_teach_to_p2_2" value="Student Marks &amp;amp; Exam Assessment Data" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.55;entryDx=0;entryDy=0;exitX=0;exitY=0.55;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_teacher" target="p2_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: 2.0 -> Teacher (Rosters) -->
        <mxCell id="flow_p2_to_teach" value="Assigned Classes, Rosters &amp;amp; Score Confirmations" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.85;entryDx=0;entryDy=0;exitX=1;exitY=0.85;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="p2_box" target="ent_teacher">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: D2 -> 2.0 (Verify Teacher) -->
        <mxCell id="flow_d2_p2" value="Verify Teacher Auth &amp;amp; Assigned Classes" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.3;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ds_d2_name" target="p2_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: D4 -> 2.0 (Subject & Class Info) -->
        <mxCell id="flow_d4_p2" value="Fetch Subject &amp;amp; Class Details" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.3;entryY=1;entryDx=0;entryDy=0;exitX=1;exitY=0.3;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ds_d4_name" target="p2_box">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1186" y="499" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: D3 -> 2.0 (Class Student List) -->
        <mxCell id="flow_d3_p2" value="Retrieve Enrolled Class Student Roster" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.6;entryY=1;entryDx=0;entryDy=0;exitX=1;exitY=0.3;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ds_d3_name" target="p2_box">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1252" y="634" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: 2.0 <-> D5 (Score Records) -->
        <mxCell id="flow_p2_d5" value="Save / Update Student Scores &amp;amp; Fetch Results" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.3;entryDx=0;entryDy=0;exitX=0;exitY=0.7;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;startArrow=classic;endArrow=classic;" edge="1" parent="1" source="p2_box" target="ds_d5_name">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1050" y="207" />
              <mxPoint x="1050" y="769" />
            </Array>
          </mxGeometry>
        </mxCell>


        <!-- ================= DATA FLOWS: STUDENT MODULE (3.0) ================= -->
        <!-- Flow: Student -> 3.0 (Auth & Password) -->
        <mxCell id="flow_stud_to_p3_1" value="Student Login Credentials &amp;amp; New Password" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.25;entryDx=0;entryDy=0;exitX=0;exitY=0.25;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_student" target="p3_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: Student -> 3.0 (Inquiries) -->
        <mxCell id="flow_stud_to_p3_2" value="Contact Messages &amp;amp; Feedback Inquiries" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.55;entryDx=0;entryDy=0;exitX=0;exitY=0.55;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_student" target="p3_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: 3.0 -> Student (Reports & Profile) -->
        <mxCell id="flow_p3_to_stud" value="Student Profile, Enrolled Subjects &amp;amp; Grade Sheet" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.85;entryDx=0;entryDy=0;exitX=1;exitY=0.85;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="p3_box" target="ent_student">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: D3 <-> 3.0 (Auth & Password Update) -->
        <mxCell id="flow_d3_p3" value="Verify Student Auth / Update Password" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.3;entryDx=0;entryDy=0;exitX=1;exitY=0.7;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;startArrow=classic;endArrow=classic;" edge="1" parent="1" source="ds_d3_name" target="p3_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: D4 -> 3.0 (Subject Catalog) -->
        <mxCell id="flow_d4_p3" value="Fetch Enrolled Subject &amp;amp; Class Info" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.4;entryY=0;entryDx=0;entryDy=0;exitX=1;exitY=0.7;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ds_d4_name" target="p3_box">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1208" y="517" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: D5 -> 3.0 (Read Scores) -->
        <mxCell id="flow_d5_p3" value="Read Academic Scores &amp;amp; Exam Results" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.7;entryDx=0;entryDy=0;exitX=1;exitY=0.7;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ds_d5_name" target="p3_box">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: 3.0 -> D6 (Store Inquiry) -->
        <mxCell id="flow_p3_d6" value="Save Inquiry &amp;amp; Message Record" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="p3_box" target="ds_d6_name">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1230" y="913" />
            </Array>
          </mxGeometry>
        </mxCell>


        <!-- ================= LEGEND BOX (Strict DFD Notation) ================= -->
        <mxCell id="legend_group" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="60" y="1000" width="1580" height="120" as="geometry" />
        </mxCell>
        <mxCell id="legend_bg" value="" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#F1F5F9;strokeColor=#CBD5E1;strokeWidth=1.5;shadow=0;" vertex="1" parent="legend_group">
          <mxGeometry x="0" y="0" width="1580" height="120" as="geometry" />
        </mxCell>
        <mxCell id="legend_title" value="&lt;b&gt;GANE &amp;amp; SARSON DFD NOTATION STANDARD (COMPLIANT WITH ATTACHED SPECIFICATION)&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=13;fontColor=#1E293B;" vertex="1" parent="legend_group">
          <mxGeometry x="20" y="10" width="800" height="24" as="geometry" />
        </mxCell>

        <!-- Legend Item 1: External Entity -->
        <mxCell id="leg_ent_sample" value="&lt;b&gt;External Entity&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontSize=11;align=center;verticalAlign=middle;" vertex="1" parent="legend_group">
          <mxGeometry x="30" y="45" width="120" height="50" as="geometry" />
        </mxCell>
        <mxCell id="leg_ent_desc" value="&lt;b&gt;External Entity:&lt;/b&gt; Source or sink of system data outside system boundary (Admin, Teacher, Student, Registrar Office)." style="text;html=1;align=left;verticalAlign=middle;fontSize=11;fontColor=#334155;whiteSpace=wrap;" vertex="1" parent="legend_group">
          <mxGeometry x="160" y="45" width="220" height="50" as="geometry" />
        </mxCell>

        <!-- Legend Item 2: Process -->
        <mxCell id="leg_p_box" value="" style="rounded=1;arcSize=14;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#2563EB;strokeWidth=1.5;" vertex="1" parent="legend_group">
          <mxGeometry x="410" y="45" width="120" height="50" as="geometry" />
        </mxCell>
        <mxCell id="leg_p_header" value="1.0" style="rounded=1;arcSize=28;whiteSpace=wrap;html=1;fillColor=#BFDBFE;strokeColor=#2563EB;strokeWidth=1;fontSize=10;fontStyle=1;align=center;" vertex="1" parent="legend_group">
          <mxGeometry x="410" y="45" width="120" height="18" as="geometry" />
        </mxCell>
        <mxCell id="leg_p_text" value="Process" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;fontStyle=1;" vertex="1" parent="legend_group">
          <mxGeometry x="410" y="63" width="120" height="30" as="geometry" />
        </mxCell>
        <mxCell id="leg_p_desc" value="&lt;b&gt;Process:&lt;/b&gt; Transforms inputs into outputs. Top section denotes Process Number (1.0 - 4.0), bottom is Function Name." style="text;html=1;align=left;verticalAlign=middle;fontSize=11;fontColor=#334155;whiteSpace=wrap;" vertex="1" parent="legend_group">
          <mxGeometry x="540" y="45" width="220" height="50" as="geometry" />
        </mxCell>

        <!-- Legend Item 3: Data Store -->
        <mxCell id="leg_ds_id" value="D1" style="shape=rectangle;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=1.5;fontSize=11;fontStyle=1;align=center;" vertex="1" parent="legend_group">
          <mxGeometry x="790" y="45" width="35" height="50" as="geometry" />
        </mxCell>
        <mxCell id="leg_ds_name" value="Data Store" style="shape=partialRectangle;top=1;left=0;bottom=1;right=0;fillColor=#F8FAFC;strokeColor=#4A7BB0;strokeWidth=1.5;whiteSpace=wrap;html=1;fontSize=11;align=left;spacingLeft=5;fontStyle=1;" vertex="1" parent="legend_group">
          <mxGeometry x="825" y="45" width="95" height="50" as="geometry" />
        </mxCell>
        <mxCell id="leg_ds_desc" value="&lt;b&gt;Data Store:&lt;/b&gt; Persistent database repository. Open right side with left partition for Data Store ID (D1 - D7)." style="text;html=1;align=left;verticalAlign=middle;fontSize=11;fontColor=#334155;whiteSpace=wrap;" vertex="1" parent="legend_group">
          <mxGeometry x="930" y="45" width="230" height="50" as="geometry" />
        </mxCell>

        <!-- Legend Item 4: Data Flow -->
        <mxCell id="leg_flow_line" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=classic;strokeColor=#1E293B;strokeWidth=2;" edge="1" parent="legend_group">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1190" y="70" as="sourcePoint" />
            <mxPoint x="1290" y="70" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_flow_label" value="Data Flow Name" style="edgeLabel;html=1;align=center;verticalAlign=bottom;fontSize=10;fontColor=#0F172A;" vertex="1" connectable="0" parent="leg_flow_line">
          <mxGeometry x="0" y="-3" relative="1" as="geometry" />
        </mxCell>
        <mxCell id="leg_flow_desc" value="&lt;b&gt;Data Flow:&lt;/b&gt; Directed path showing data packet exchange between Entities, Processes, and Data Stores." style="text;html=1;align=left;verticalAlign=middle;fontSize=11;fontColor=#334155;whiteSpace=wrap;" vertex="1" parent="legend_group">
          <mxGeometry x="1310" y="45" width="250" height="50" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>


  <!-- ========================================================================= -->
  <!-- PAGE 2: YOURDON & DEMARCO NOTATION (Column 1 of User Reference Image)   -->
  <!-- ========================================================================= -->
  <diagram id="yourdon-demarco" name="DFD Level 1 (Yourdon &amp; DeMarco Notation)">
    <mxGraphModel dx="1600" dy="1100" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1700" pageHeight="1160" background="#FFFFFF" math="0" shadow="0">
      <root>
        <mxCell id="yd_0" />
        <mxCell id="yd_1" parent="yd_0" />
        
        <!-- ================= DIAGRAM HEADER & TITLE ================= -->
        <mxCell id="yd_title" value="DATA FLOW DIAGRAM (DFD) LEVEL 1: SCHOOL MANAGEMENT SYSTEM&#xa;Notation: Yourdon &amp; DeMarco | Modules: Admin, Teacher, Student, Registrar Office" style="shape=rectangle;fillColor=#1E293B;strokeColor=#0F172A;fontColor=#FFFFFF;fontStyle=1;fontSize=16;align=center;verticalAlign=middle;rounded=1;arcSize=8;shadow=1;" vertex="1" parent="yd_1">
          <mxGeometry x="60" y="20" width="1580" height="45" as="geometry" />
        </mxCell>

        <!-- ================= EXTERNAL ENTITIES (Yellowish Sharp Rectangles) ================= -->
        <!-- Admin Entity -->
        <mxCell id="yd_ent_admin" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;b&gt;Admin&lt;/b&gt;&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(School Administrator)&lt;/i&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="yd_1">
          <mxGeometry x="60" y="140" width="160" height="90" as="geometry" />
        </mxCell>

        <!-- Registrar Office Entity -->
        <mxCell id="yd_ent_registrar" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;b&gt;Registrar Office&lt;/b&gt;&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Admissions &amp; Records)&lt;/i&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="yd_1">
          <mxGeometry x="60" y="740" width="160" height="90" as="geometry" />
        </mxCell>

        <!-- Teacher Entity -->
        <mxCell id="yd_ent_teacher" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;b&gt;Teacher&lt;/b&gt;&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Faculty Staff)&lt;/i&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="yd_1">
          <mxGeometry x="1480" y="140" width="160" height="90" as="geometry" />
        </mxCell>

        <!-- Student Entity -->
        <mxCell id="yd_ent_student" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;b&gt;Student&lt;/b&gt;&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Learner / Enrollee)&lt;/i&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;fontColor=#000000;fontSize=12;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="yd_1">
          <mxGeometry x="1480" y="740" width="160" height="90" as="geometry" />
        </mxCell>


        <!-- ================= PROCESSES (Yourdon DeMarco: Circle / Bubble) ================= -->
        <!-- Process 1.0: Admin Management -->
        <mxCell id="yd_p1" value="&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;b&gt;1.0&lt;/b&gt;&lt;/font&gt;&lt;br/&gt;&lt;b&gt;Admin&lt;br/&gt;Management&lt;/b&gt;" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2.5;fontColor=#000000;fontSize=13;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="yd_1">
          <mxGeometry x="400" y="125" width="120" height="120" as="geometry" />
        </mxCell>

        <!-- Process 4.0: Registrar Office Admissions -->
        <mxCell id="yd_p4" value="&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;b&gt;4.0&lt;/b&gt;&lt;/font&gt;&lt;br/&gt;&lt;b&gt;Registrar&lt;br/&gt;Office&lt;/b&gt;" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2.5;fontColor=#000000;fontSize=13;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="yd_1">
          <mxGeometry x="400" y="725" width="120" height="120" as="geometry" />
        </mxCell>

        <!-- Process 2.0: Teacher Operations & Grading -->
        <mxCell id="yd_p2" value="&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;b&gt;2.0&lt;/b&gt;&lt;/font&gt;&lt;br/&gt;&lt;b&gt;Teacher&lt;br/&gt;Operations&lt;/b&gt;" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2.5;fontColor=#000000;fontSize=13;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="yd_1">
          <mxGeometry x="1170" y="125" width="120" height="120" as="geometry" />
        </mxCell>

        <!-- Process 3.0: Student Portal -->
        <mxCell id="yd_p3" value="&lt;font style=&quot;font-size: 16px;&quot;&gt;&lt;b&gt;3.0&lt;/b&gt;&lt;/font&gt;&lt;br/&gt;&lt;b&gt;Student&lt;br/&gt;Portal&lt;/b&gt;" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2.5;fontColor=#000000;fontSize=13;align=center;verticalAlign=middle;shadow=1;" vertex="1" parent="yd_1">
          <mxGeometry x="1170" y="725" width="120" height="120" as="geometry" />
        </mxCell>


        <!-- ================= DATA STORES (Yourdon DeMarco: Parallel Lines / Open Box) ================= -->
        <!-- D1: Admin & Settings -->
        <mxCell id="yd_ds_d1" value="&lt;b&gt;D1&lt;/b&gt; | Admin &amp;amp; System Settings" style="shape=partialRectangle;top=1;left=1;bottom=1;right=0;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=15;fontSize=12;fontColor=#000000;" vertex="1" parent="yd_1">
          <mxGeometry x="725" y="80" width="250" height="46" as="geometry" />
        </mxCell>

        <!-- D2: Teachers -->
        <mxCell id="yd_ds_d2" value="&lt;b&gt;D2&lt;/b&gt; | Teacher Records" style="shape=partialRectangle;top=1;left=1;bottom=1;right=0;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=15;fontSize=12;fontColor=#000000;" vertex="1" parent="yd_1">
          <mxGeometry x="725" y="215" width="250" height="46" as="geometry" />
        </mxCell>

        <!-- D7: Registrar Office Staff -->
        <mxCell id="yd_ds_d7" value="&lt;b&gt;D7&lt;/b&gt; | Registrar Staff Records" style="shape=partialRectangle;top=1;left=1;bottom=1;right=0;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=15;fontSize=12;fontColor=#000000;" vertex="1" parent="yd_1">
          <mxGeometry x="725" y="350" width="250" height="46" as="geometry" />
        </mxCell>

        <!-- D4: Academic Structure (Classes, Sections, Courses) -->
        <mxCell id="yd_ds_d4" value="&lt;b&gt;D4&lt;/b&gt; | Academic Structure" style="shape=partialRectangle;top=1;left=1;bottom=1;right=0;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=15;fontSize=12;fontColor=#000000;" vertex="1" parent="yd_1">
          <mxGeometry x="725" y="485" width="250" height="46" as="geometry" />
        </mxCell>

        <!-- D3: Students -->
        <mxCell id="yd_ds_d3" value="&lt;b&gt;D3&lt;/b&gt; | Student Records" style="shape=partialRectangle;top=1;left=1;bottom=1;right=0;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=15;fontSize=12;fontColor=#000000;" vertex="1" parent="yd_1">
          <mxGeometry x="725" y="620" width="250" height="46" as="geometry" />
        </mxCell>

        <!-- D5: Student Scores -->
        <mxCell id="yd_ds_d5" value="&lt;b&gt;D5&lt;/b&gt; | Scores &amp;amp; Results" style="shape=partialRectangle;top=1;left=1;bottom=1;right=0;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=15;fontSize=12;fontColor=#000000;" vertex="1" parent="yd_1">
          <mxGeometry x="725" y="755" width="250" height="46" as="geometry" />
        </mxCell>

        <!-- D6: Messages -->
        <mxCell id="yd_ds_d6" value="&lt;b&gt;D6&lt;/b&gt; | Inquiries &amp;amp; Messages" style="shape=partialRectangle;top=1;left=1;bottom=1;right=0;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;whiteSpace=wrap;html=1;align=left;spacingLeft=15;fontSize=12;fontColor=#000000;" vertex="1" parent="yd_1">
          <mxGeometry x="725" y="890" width="250" height="46" as="geometry" />
        </mxCell>


        <!-- ================= DATA FLOWS: ADMIN MODULE (1.0) ================= -->
        <mxCell id="yd_flow_admin_p1_1" value="Admin Credentials &amp;amp; Config" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.25;entryDx=0;entryDy=0;exitX=1;exitY=0.25;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ent_admin" target="yd_p1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_admin_p1_2" value="Staff Accounts &amp;amp; Setup" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.55;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ent_admin" target="yd_p1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_p1_admin" value="Reports &amp;amp; System Metrics" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.85;entryDx=0;entryDy=0;exitX=0;exitY=0.75;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_p1" target="yd_ent_admin">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_p1_d1" value="Update &amp;amp; Read Settings" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.2;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;endArrow=classic;startArrow=classic;" edge="1" parent="yd_1" source="yd_p1" target="yd_ds_d1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_p1_d2" value="Create Teacher Profiles" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.6;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_p1" target="yd_ds_d2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_p1_d7" value="Manage Registrar Accounts" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=0.9;exitY=1;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_p1" target="yd_ds_d7">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_p1_d4" value="Configure Classes &amp;amp; Subjects" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.3;entryDx=0;entryDy=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_p1" target="yd_ds_d4">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="460" y="499" />
            </Array>
          </mxGeometry>
        </mxCell>

        <mxCell id="yd_flow_d6_p1" value="Read Feedback Messages" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.2;entryY=1;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ds_d6" target="yd_p1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="320" y="913" />
              <mxPoint x="320" y="320" />
              <mxPoint x="424" y="320" />
            </Array>
          </mxGeometry>
        </mxCell>


        <!-- ================= DATA FLOWS: REGISTRAR MODULE (4.0) ================= -->
        <mxCell id="yd_flow_reg_p4_1" value="Staff Login Credentials" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.25;entryDx=0;entryDy=0;exitX=1;exitY=0.25;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ent_registrar" target="yd_p4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_reg_p4_2" value="Student Admissions &amp;amp; Queries" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.55;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ent_registrar" target="yd_p4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_p4_reg" value="Admission Confirmations" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.85;entryDx=0;entryDy=0;exitX=0;exitY=0.75;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_p4" target="yd_ent_registrar">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_d7_p4" value="Verify Staff Auth" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.9;entryY=0;entryDx=0;entryDy=0;exitX=0;exitY=0.8;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ds_d7" target="yd_p4">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_d4_p4" value="Fetch Classes &amp;amp; Sections" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=0;exitY=0.7;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ds_d4" target="yd_p4">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="460" y="517" />
            </Array>
          </mxGeometry>
        </mxCell>

        <mxCell id="yd_flow_p4_d3" value="Register / Query Student Records" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;exitX=1;exitY=0.3;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;startArrow=classic;endArrow=classic;" edge="1" parent="yd_1" source="yd_p4" target="yd_ds_d3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>


        <!-- ================= DATA FLOWS: TEACHER MODULE (2.0) ================= -->
        <mxCell id="yd_flow_teach_p2_1" value="Teacher Login Credentials" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.25;entryDx=0;entryDy=0;exitX=0;exitY=0.25;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ent_teacher" target="yd_p2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_teach_p2_2" value="Marks &amp;amp; Exam Assessment" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=0;exitY=0.55;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ent_teacher" target="yd_p2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_p2_teach" value="Assigned Classes &amp;amp; Rosters" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.85;entryDx=0;entryDy=0;exitX=1;exitY=0.75;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_p2" target="yd_ent_teacher">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_d2_p2" value="Verify Teacher Auth" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.3;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ds_d2" target="yd_p2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_d4_p2" value="Fetch Subject Details" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.3;entryY=1;entryDx=0;entryDy=0;exitX=1;exitY=0.3;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ds_d4" target="yd_p2">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1206" y="499" />
            </Array>
          </mxGeometry>
        </mxCell>

        <mxCell id="yd_flow_d3_p2" value="Fetch Enrolled Students" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.6;entryY=1;entryDx=0;entryDy=0;exitX=1;exitY=0.3;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ds_d3" target="yd_p2">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1242" y="634" />
            </Array>
          </mxGeometry>
        </mxCell>

        <mxCell id="yd_flow_p2_d5" value="Save / Fetch Student Scores" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.3;entryDx=0;entryDy=0;exitX=0;exitY=0.7;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;startArrow=classic;endArrow=classic;" edge="1" parent="yd_1" source="yd_p2" target="yd_ds_d5">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1050" y="209" />
              <mxPoint x="1050" y="769" />
            </Array>
          </mxGeometry>
        </mxCell>


        <!-- ================= DATA FLOWS: STUDENT MODULE (3.0) ================= -->
        <mxCell id="yd_flow_stud_p3_1" value="Credentials &amp;amp; Password" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.25;entryDx=0;entryDy=0;exitX=0;exitY=0.25;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ent_student" target="yd_p3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_stud_p3_2" value="Feedback &amp;amp; Messages" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=0;exitY=0.55;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ent_student" target="yd_p3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_p3_stud" value="Profile, Scores &amp;amp; Grades" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.85;entryDx=0;entryDy=0;exitX=1;exitY=0.75;exitDx=0;exitDy=0;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_p3" target="yd_ent_student">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_d3_p3" value="Verify Auth / Update Password" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.3;entryDx=0;entryDy=0;exitX=1;exitY=0.7;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;startArrow=classic;endArrow=classic;" edge="1" parent="yd_1" source="yd_ds_d3" target="yd_p3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_d4_p3" value="Fetch Enrolled Courses" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.4;entryY=0;entryDx=0;entryDy=0;exitX=1;exitY=0.7;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ds_d4" target="yd_p3">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1218" y="517" />
            </Array>
          </mxGeometry>
        </mxCell>

        <mxCell id="yd_flow_d5_p3" value="Read Academic Scores" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.7;entryDx=0;entryDy=0;exitX=1;exitY=0.7;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_ds_d5" target="yd_p3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <mxCell id="yd_flow_p3_d6" value="Save Inquiry Message" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;labelBackgroundColor=#FFFFFF;" edge="1" parent="yd_1" source="yd_p3" target="yd_ds_d6">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1230" y="913" />
            </Array>
          </mxGeometry>
        </mxCell>


        <!-- ================= LEGEND BOX (Yourdon DeMarco) ================= -->
        <mxCell id="yd_legend_group" value="" style="group;" vertex="1" connectable="0" parent="yd_1">
          <mxGeometry x="60" y="1000" width="1580" height="120" as="geometry" />
        </mxCell>
        <mxCell id="yd_legend_bg" value="" style="rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#F1F5F9;strokeColor=#CBD5E1;strokeWidth=1.5;shadow=0;" vertex="1" parent="yd_legend_group">
          <mxGeometry x="0" y="0" width="1580" height="120" as="geometry" />
        </mxCell>
        <mxCell id="yd_legend_title" value="&lt;b&gt;YOURDON &amp;amp; DEMARCO DFD NOTATION STANDARD (COMPLIANT WITH ATTACHED SPECIFICATION)&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=13;fontColor=#1E293B;" vertex="1" parent="yd_legend_group">
          <mxGeometry x="20" y="10" width="800" height="24" as="geometry" />
        </mxCell>

        <!-- Legend Item 1: External Entity -->
        <mxCell id="yd_leg_ent_sample" value="&lt;b&gt;External Entity&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;fontSize=11;align=center;verticalAlign=middle;" vertex="1" parent="yd_legend_group">
          <mxGeometry x="30" y="45" width="120" height="50" as="geometry" />
        </mxCell>
        <mxCell id="yd_leg_ent_desc" value="&lt;b&gt;External Entity:&lt;/b&gt; Source or sink of system data outside system boundary (Admin, Teacher, Student, Registrar Office)." style="text;html=1;align=left;verticalAlign=middle;fontSize=11;fontColor=#334155;whiteSpace=wrap;" vertex="1" parent="yd_legend_group">
          <mxGeometry x="160" y="45" width="220" height="50" as="geometry" />
        </mxCell>

        <!-- Legend Item 2: Process -->
        <mxCell id="yd_leg_p_sample" value="&lt;b&gt;Process&lt;/b&gt;" style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;fontSize=11;align=center;verticalAlign=middle;" vertex="1" parent="yd_legend_group">
          <mxGeometry x="440" y="45" width="50" height="50" as="geometry" />
        </mxCell>
        <mxCell id="yd_leg_p_desc" value="&lt;b&gt;Process (Bubble/Circle):&lt;/b&gt; Transforms inputs to outputs. Process numbering and label inside circle." style="text;html=1;align=left;verticalAlign=middle;fontSize=11;fontColor=#334155;whiteSpace=wrap;" vertex="1" parent="yd_legend_group">
          <mxGeometry x="540" y="45" width="220" height="50" as="geometry" />
        </mxCell>

        <!-- Legend Item 3: Data Store -->
        <mxCell id="yd_leg_ds_sample" value="Data Store" style="shape=partialRectangle;top=1;left=1;bottom=1;right=0;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=2;whiteSpace=wrap;html=1;fontSize=11;align=left;spacingLeft=10;fontStyle=1;" vertex="1" parent="yd_legend_group">
          <mxGeometry x="790" y="45" width="130" height="50" as="geometry" />
        </mxCell>
        <mxCell id="yd_leg_ds_desc" value="&lt;b&gt;Data Store:&lt;/b&gt; Open rectangle / parallel lines storing persistent records (D1 - D7)." style="text;html=1;align=left;verticalAlign=middle;fontSize=11;fontColor=#334155;whiteSpace=wrap;" vertex="1" parent="yd_legend_group">
          <mxGeometry x="930" y="45" width="230" height="50" as="geometry" />
        </mxCell>

        <!-- Legend Item 4: Data Flow -->
        <mxCell id="yd_leg_flow_line" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=classic;strokeColor=#1E293B;strokeWidth=2;" edge="1" parent="yd_legend_group">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1190" y="70" as="sourcePoint" />
            <mxPoint x="1290" y="70" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="yd_leg_flow_label" value="Data Flow Name" style="edgeLabel;html=1;align=center;verticalAlign=bottom;fontSize=10;fontColor=#0F172A;" vertex="1" connectable="0" parent="yd_leg_flow_line">
          <mxGeometry x="0" y="-3" relative="1" as="geometry" />
        </mxCell>
        <mxCell id="yd_leg_flow_desc" value="&lt;b&gt;Data Flow:&lt;/b&gt; Directed arrow indicating movement of specific data items." style="text;html=1;align=left;verticalAlign=middle;fontSize=11;fontColor=#334155;whiteSpace=wrap;" vertex="1" parent="yd_legend_group">
          <mxGeometry x="1310" y="45" width="250" height="50" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml_content


def generate_svg_gane_sarson():
    """Generates an SVG for Gane & Sarson DFD Level 1"""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1700 1160" width="100%" height="100%" style="background-color: #ffffff; font-family: 'Segoe UI', Arial, Helvetica, sans-serif;">
  <defs>
    <!-- Arrow Markers -->
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1E293B" />
    </marker>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563EB" />
    </marker>
    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" flood-color="#000000" />
    </filter>
  </defs>

  <!-- Title Banner -->
  <rect x="60" y="20" width="1580" height="48" rx="8" fill="#1E293B" filter="url(#shadow)"/>
  <text x="850" y="42" fill="#FFFFFF" font-size="16" font-weight="bold" text-anchor="middle" dominant-baseline="middle">DATA FLOW DIAGRAM (DFD) LEVEL 1: SCHOOL MANAGEMENT SYSTEM</text>
  <text x="850" y="58" fill="#94A3B8" font-size="12" text-anchor="middle" dominant-baseline="middle">Gane &amp; Sarson Notation | Four Core Modules: Admin, Teacher, Student, Registrar Office</text>

  <!-- ================= EXTERNAL ENTITIES ================= -->
  <!-- Admin -->
  <g filter="url(#shadow)">
    <rect x="60" y="140" width="160" height="90" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="140" y="165" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle">EXTERNAL ENTITY</text>
    <text x="140" y="190" font-size="18" font-weight="bold" fill="#0F172A" text-anchor="middle">Admin</text>
    <text x="140" y="212" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">(System Admin)</text>
  </g>

  <!-- Registrar Office -->
  <g filter="url(#shadow)">
    <rect x="60" y="740" width="160" height="90" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="140" y="765" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle">EXTERNAL ENTITY</text>
    <text x="140" y="790" font-size="17" font-weight="bold" fill="#0F172A" text-anchor="middle">Registrar Office</text>
    <text x="140" y="812" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">(Admissions / Records)</text>
  </g>

  <!-- Teacher -->
  <g filter="url(#shadow)">
    <rect x="1480" y="140" width="160" height="90" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="1560" y="165" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle">EXTERNAL ENTITY</text>
    <text x="1560" y="190" font-size="18" font-weight="bold" fill="#0F172A" text-anchor="middle">Teacher</text>
    <text x="1560" y="212" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">(Faculty Staff)</text>
  </g>

  <!-- Student -->
  <g filter="url(#shadow)">
    <rect x="1480" y="740" width="160" height="90" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="1560" y="765" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle">EXTERNAL ENTITY</text>
    <text x="1560" y="790" font-size="18" font-weight="bold" fill="#0F172A" text-anchor="middle">Student</text>
    <text x="1560" y="812" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">(Learner / Enrollee)</text>
  </g>


  <!-- ================= PROCESSES (Gane & Sarson) ================= -->
  <!-- Process 1.0 Admin -->
  <g filter="url(#shadow)">
    <rect x="360" y="130" width="220" height="110" rx="14" fill="#F8FAFC" stroke="#2563EB" stroke-width="2"/>
    <path d="M 360 162 L 580 162" stroke="#2563EB" stroke-width="1.5" />
    <path d="M 360 144 A 14 14 0 0 1 374 130 L 566 130 A 14 14 0 0 1 580 144 L 580 162 L 360 162 Z" fill="#BFDBFE"/>
    <text x="470" y="151" font-size="14" font-weight="bold" fill="#1E3A8A" text-anchor="middle">1.0</text>
    <text x="470" y="185" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">Admin Management</text>
    <text x="470" y="205" font-size="11" fill="#64748B" text-anchor="middle">User Accounts, Settings,</text>
    <text x="470" y="222" font-size="11" fill="#64748B" text-anchor="middle">Classes, Grades &amp; Notices</text>
  </g>

  <!-- Process 4.0 Registrar -->
  <g filter="url(#shadow)">
    <rect x="360" y="730" width="220" height="110" rx="14" fill="#F8FAFC" stroke="#2563EB" stroke-width="2"/>
    <path d="M 360 762 L 580 762" stroke="#2563EB" stroke-width="1.5" />
    <path d="M 360 744 A 14 14 0 0 1 374 730 L 566 730 A 14 14 0 0 1 580 744 L 580 762 L 360 762 Z" fill="#BFDBFE"/>
    <text x="470" y="751" font-size="14" font-weight="bold" fill="#1E3A8A" text-anchor="middle">4.0</text>
    <text x="470" y="785" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">Registrar Office Module</text>
    <text x="470" y="805" font-size="11" fill="#64748B" text-anchor="middle">Student Admissions, Enrollment</text>
    <text x="470" y="822" font-size="11" fill="#64748B" text-anchor="middle">&amp; Demographic Search</text>
  </g>

  <!-- Process 2.0 Teacher -->
  <g filter="url(#shadow)">
    <rect x="1120" y="130" width="220" height="110" rx="14" fill="#F8FAFC" stroke="#2563EB" stroke-width="2"/>
    <path d="M 1120 162 L 1340 162" stroke="#2563EB" stroke-width="1.5" />
    <path d="M 1120 144 A 14 14 0 0 1 1134 130 L 1326 130 A 14 14 0 0 1 1340 144 L 1340 162 L 1120 162 Z" fill="#BFDBFE"/>
    <text x="1230" y="151" font-size="14" font-weight="bold" fill="#1E3A8A" text-anchor="middle">2.0</text>
    <text x="1230" y="185" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">Teacher Operations</text>
    <text x="1230" y="205" font-size="11" fill="#64748B" text-anchor="middle">Assigned Class Rosters,</text>
    <text x="1230" y="222" font-size="11" fill="#64748B" text-anchor="middle">Student Grading &amp; Scores</text>
  </g>

  <!-- Process 3.0 Student -->
  <g filter="url(#shadow)">
    <rect x="1120" y="730" width="220" height="110" rx="14" fill="#F8FAFC" stroke="#2563EB" stroke-width="2"/>
    <path d="M 1120 762 L 1340 762" stroke="#2563EB" stroke-width="1.5" />
    <path d="M 1120 744 A 14 14 0 0 1 1134 730 L 1326 730 A 14 14 0 0 1 1340 744 L 1340 762 L 1120 762 Z" fill="#BFDBFE"/>
    <text x="1230" y="751" font-size="14" font-weight="bold" fill="#1E3A8A" text-anchor="middle">3.0</text>
    <text x="1230" y="785" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">Student Portal</text>
    <text x="1230" y="805" font-size="11" fill="#64748B" text-anchor="middle">Academic Report Card, Profile,</text>
    <text x="1230" y="822" font-size="11" fill="#64748B" text-anchor="middle">Credentials &amp; Inquiries</text>
  </g>


  <!-- ================= DATA STORES (Gane & Sarson: Left D# box, Open Right Box) ================= -->
  <!-- D1 -->
  <g>
    <rect x="725" y="80" width="45" height="46" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="747" y="108" font-size="13" font-weight="bold" fill="#1E3A8A" text-anchor="middle">D1</text>
    <path d="M 770 80 L 975 80 M 770 126 L 975 126" stroke="#4A7BB0" stroke-width="2" fill="none"/>
    <rect x="770" y="81" width="205" height="44" fill="#F8FAFC"/>
    <text x="782" y="100" font-size="12" font-weight="bold" fill="#0F172A">Admin &amp; Settings</text>
    <text x="782" y="117" font-size="10" fill="#64748B">[admin, setting]</text>
  </g>

  <!-- D2 -->
  <g>
    <rect x="725" y="215" width="45" height="46" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="747" y="243" font-size="13" font-weight="bold" fill="#1E3A8A" text-anchor="middle">D2</text>
    <path d="M 770 215 L 975 215 M 770 261 L 975 261" stroke="#4A7BB0" stroke-width="2" fill="none"/>
    <rect x="770" y="216" width="205" height="44" fill="#F8FAFC"/>
    <text x="782" y="235" font-size="12" font-weight="bold" fill="#0F172A">Teacher Records</text>
    <text x="782" y="252" font-size="10" fill="#64748B">[teacher]</text>
  </g>

  <!-- D7 -->
  <g>
    <rect x="725" y="350" width="45" height="46" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="747" y="378" font-size="13" font-weight="bold" fill="#1E3A8A" text-anchor="middle">D7</text>
    <path d="M 770 350 L 975 350 M 770 396 L 975 396" stroke="#4A7BB0" stroke-width="2" fill="none"/>
    <rect x="770" y="351" width="205" height="44" fill="#F8FAFC"/>
    <text x="782" y="370" font-size="12" font-weight="bold" fill="#0F172A">Registrar Staff Records</text>
    <text x="782" y="387" font-size="10" fill="#64748B">[registrar_office]</text>
  </g>

  <!-- D4 -->
  <g>
    <rect x="725" y="485" width="45" height="46" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="747" y="513" font-size="13" font-weight="bold" fill="#1E3A8A" text-anchor="middle">D4</text>
    <path d="M 770 485 L 975 485 M 770 531 L 975 531" stroke="#4A7BB0" stroke-width="2" fill="none"/>
    <rect x="770" y="486" width="205" height="44" fill="#F8FAFC"/>
    <text x="782" y="505" font-size="12" font-weight="bold" fill="#0F172A">Academic Structure</text>
    <text x="782" y="522" font-size="10" fill="#64748B">[grades, section, class, subjects]</text>
  </g>

  <!-- D3 -->
  <g>
    <rect x="725" y="620" width="45" height="46" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="747" y="648" font-size="13" font-weight="bold" fill="#1E3A8A" text-anchor="middle">D3</text>
    <path d="M 770 620 L 975 620 M 770 666 L 975 666" stroke="#4A7BB0" stroke-width="2" fill="none"/>
    <rect x="770" y="621" width="205" height="44" fill="#F8FAFC"/>
    <text x="782" y="640" font-size="12" font-weight="bold" fill="#0F172A">Student Records</text>
    <text x="782" y="657" font-size="10" fill="#64748B">[student]</text>
  </g>

  <!-- D5 -->
  <g>
    <rect x="725" y="755" width="45" height="46" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="747" y="783" font-size="13" font-weight="bold" fill="#1E3A8A" text-anchor="middle">D5</text>
    <path d="M 770 755 L 975 755 M 770 801 L 975 801" stroke="#4A7BB0" stroke-width="2" fill="none"/>
    <rect x="770" y="756" width="205" height="44" fill="#F8FAFC"/>
    <text x="782" y="775" font-size="12" font-weight="bold" fill="#0F172A">Scores &amp; Results</text>
    <text x="782" y="792" font-size="10" fill="#64748B">[student_score]</text>
  </g>

  <!-- D6 -->
  <g>
    <rect x="725" y="890" width="45" height="46" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="747" y="918" font-size="13" font-weight="bold" fill="#1E3A8A" text-anchor="middle">D6</text>
    <path d="M 770 890 L 975 890 M 770 936 L 975 936" stroke="#4A7BB0" stroke-width="2" fill="none"/>
    <rect x="770" y="891" width="205" height="44" fill="#F8FAFC"/>
    <text x="782" y="910" font-size="12" font-weight="bold" fill="#0F172A">Inquiries &amp; Messages</text>
    <text x="782" y="927" font-size="10" fill="#64748B">[message]</text>
  </g>


  <!-- ================= DATA FLOWS ================= -->
  <!-- Admin -> 1.0 -->
  <g>
    <path d="M 220 160 L 360 160" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="230" y="148" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="290" y="159" font-size="10" fill="#0F172A" text-anchor="middle">Admin Credentials</text>

    <path d="M 220 185 L 360 185" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="230" y="173" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="290" y="184" font-size="10" fill="#0F172A" text-anchor="middle">Staff Setup &amp; Config</text>

    <path d="M 360 215 L 220 215" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="230" y="203" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="290" y="214" font-size="10" fill="#0F172A" text-anchor="middle">Dashboard &amp; Reports</text>
  </g>

  <!-- 1.0 -> Data Stores -->
  <g>
    <!-- 1.0 <-> D1 -->
    <path d="M 580 150 L 650 150 L 650 103 L 725 103" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" marker-start="url(#arrow-blue)" fill="none"/>
    <rect x="605" y="118" width="105" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="657" y="129" font-size="10" fill="#1E3A8A" text-anchor="middle">Update / Read Config</text>

    <!-- 1.0 -> D2 -->
    <path d="M 580 195 L 670 195 L 670 238 L 725 238" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" fill="none"/>
    <rect x="615" y="210" width="100" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="665" y="221" font-size="10" fill="#1E3A8A" text-anchor="middle">Create Teacher Acc.</text>

    <!-- 1.0 -> D7 -->
    <path d="M 540 240 L 540 373 L 725 373" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" fill="none"/>
    <rect x="560" y="360" width="115" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="617" y="371" font-size="10" fill="#1E3A8A" text-anchor="middle">Manage Registrar Staff</text>

    <!-- 1.0 -> D4 -->
    <path d="M 470 240 L 470 499 L 725 499" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" fill="none"/>
    <rect x="485" y="488" width="145" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="557" y="499" font-size="10" fill="#1E3A8A" text-anchor="middle">Configure Classes &amp; Grades</text>

    <!-- D6 -> 1.0 -->
    <path d="M 725 913 L 320 913 L 320 320 L 404 320 L 404 240" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" fill="none"/>
    <rect x="330" y="308" width="115" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="387" y="319" font-size="10" fill="#1E3A8A" text-anchor="middle">Read Inquiries / Msg</text>
  </g>

  <!-- Registrar -> 4.0 -->
  <g>
    <path d="M 220 760 L 360 760" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="230" y="748" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="290" y="759" font-size="10" fill="#0F172A" text-anchor="middle">Staff Credentials</text>

    <path d="M 220 785 L 360 785" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="230" y="773" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="290" y="784" font-size="10" fill="#0F172A" text-anchor="middle">Student Admissions Data</text>

    <path d="M 360 815 L 220 815" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="230" y="803" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="290" y="814" font-size="10" fill="#0F172A" text-anchor="middle">Enrollment Confirmations</text>
  </g>

  <!-- 4.0 -> Data Stores -->
  <g>
    <!-- D7 -> 4.0 -->
    <path d="M 725 385 L 560 385 L 560 730" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" fill="none"/>
    <rect x="565" y="420" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="625" y="431" font-size="10" fill="#1E3A8A" text-anchor="middle">Verify Registrar Auth</text>

    <!-- D4 -> 4.0 -->
    <path d="M 725 517 L 510 517 L 510 730" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" fill="none"/>
    <rect x="515" y="550" width="130" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="580" y="561" font-size="10" fill="#1E3A8A" text-anchor="middle">Fetch Grade &amp; Section List</text>

    <!-- 4.0 <-> D3 -->
    <path d="M 580 760 L 660 760 L 660 643 L 725 643" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" marker-start="url(#arrow-blue)" fill="none"/>
    <rect x="605" y="695" width="135" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="672" y="706" font-size="10" fill="#1E3A8A" text-anchor="middle">Register / Query Student</text>
  </g>

  <!-- Teacher -> 2.0 -->
  <g>
    <path d="M 1480 160 L 1340 160" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="1350" y="148" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1410" y="159" font-size="10" fill="#0F172A" text-anchor="middle">Teacher Credentials</text>

    <path d="M 1480 185 L 1340 185" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="1350" y="173" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1410" y="184" font-size="10" fill="#0F172A" text-anchor="middle">Student Marks &amp; Scores</text>

    <path d="M 1340 215 L 1480 215" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="1350" y="203" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1410" y="214" font-size="10" fill="#0F172A" text-anchor="middle">Assigned Rosters / Lists</text>
  </g>

  <!-- 2.0 -> Data Stores -->
  <g>
    <!-- D2 -> 2.0 -->
    <path d="M 975 238 L 1050 238 L 1050 165 L 1120 165" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" fill="none"/>
    <rect x="1005" y="185" width="115" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1062" y="196" font-size="10" fill="#1E3A8A" text-anchor="middle">Verify Teacher Auth</text>

    <!-- D4 -> 2.0 -->
    <path d="M 975 499 L 1186 499 L 1186 240" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" fill="none"/>
    <rect x="1060" y="488" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1120" y="499" font-size="10" fill="#1E3A8A" text-anchor="middle">Fetch Subject Details</text>

    <!-- D3 -> 2.0 -->
    <path d="M 975 634 L 1252 634 L 1252 240" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" fill="none"/>
    <rect x="1135" y="623" width="125" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1197" y="634" font-size="10" fill="#1E3A8A" text-anchor="middle">Fetch Class Student List</text>

    <!-- 2.0 <-> D5 -->
    <path d="M 1120 207 L 1025 207 L 1025 769 L 975 769" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" marker-start="url(#arrow-blue)" fill="none"/>
    <rect x="990" y="325" width="140" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1060" y="336" font-size="10" fill="#1E3A8A" text-anchor="middle">Save / Fetch Student Scores</text>
  </g>

  <!-- Student -> 3.0 -->
  <g>
    <path d="M 1480 760 L 1340 760" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="1350" y="748" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1410" y="759" font-size="10" fill="#0F172A" text-anchor="middle">Credentials &amp; Password</text>

    <path d="M 1480 785 L 1340 785" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="1350" y="773" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1410" y="784" font-size="10" fill="#0F172A" text-anchor="middle">Inquiries &amp; Messages</text>

    <path d="M 1340 815 L 1480 815" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="1350" y="803" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1410" y="814" font-size="10" fill="#0F172A" text-anchor="middle">Profile, Scores &amp; Grades</text>
  </g>

  <!-- 3.0 -> Data Stores -->
  <g>
    <!-- D3 <-> 3.0 -->
    <path d="M 975 652 L 1060 652 L 1060 755 L 1120 755" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" marker-start="url(#arrow-blue)" fill="none"/>
    <rect x="1000" y="695" width="145" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1072" y="706" font-size="10" fill="#1E3A8A" text-anchor="middle">Verify Auth / Update Pwd</text>

    <!-- D4 -> 3.0 -->
    <path d="M 975 517 L 1208 517 L 1208 730" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" fill="none"/>
    <rect x="1080" y="550" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1140" y="561" font-size="10" fill="#1E3A8A" text-anchor="middle">Fetch Enrolled Courses</text>

    <!-- D5 -> 3.0 -->
    <path d="M 975 787 L 1120 787" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" fill="none"/>
    <rect x="990" y="776" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1050" y="787" font-size="10" fill="#1E3A8A" text-anchor="middle">Read Scores &amp; Grades</text>

    <!-- 3.0 -> D6 -->
    <path d="M 1230 840 L 1230 913 L 975 913" stroke="#2563EB" stroke-width="1.5" marker-end="url(#arrow-blue)" fill="none"/>
    <rect x="1070" y="902" width="130" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1135" y="913" font-size="10" fill="#1E3A8A" text-anchor="middle">Submit Feedback Inquiry</text>
  </g>


  <!-- ================= LEGEND ================= -->
  <g>
    <rect x="60" y="1000" width="1580" height="120" rx="10" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="80" y="1025" font-size="13" font-weight="bold" fill="#1E293B">GANE &amp; SARSON DFD NOTATION STANDARD (COMPLIANT WITH ATTACHED SPECIFICATION)</text>

    <!-- Entity -->
    <rect x="90" y="1045" width="110" height="48" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="145" y="1074" font-size="12" font-weight="bold" fill="#1E3A8A" text-anchor="middle">Entity</text>
    <text x="215" y="1062" font-size="11" font-weight="bold" fill="#0F172A">External Entity</text>
    <text x="215" y="1078" font-size="10" fill="#475569">Source/Sink of data (Admin, Teacher,</text>
    <text x="215" y="1092" font-size="10" fill="#475569">Student, Registrar Office)</text>

    <!-- Process -->
    <rect x="470" y="1045" width="110" height="48" rx="8" fill="#F8FAFC" stroke="#2563EB" stroke-width="1.5"/>
    <rect x="470" y="1045" width="110" height="18" rx="8" fill="#BFDBFE"/>
    <text x="525" y="1059" font-size="10" font-weight="bold" fill="#1E3A8A" text-anchor="middle">1.0</text>
    <text x="525" y="1080" font-size="11" font-weight="bold" fill="#0F172A" text-anchor="middle">Process</text>
    <text x="595" y="1062" font-size="11" font-weight="bold" fill="#0F172A">Process (Rounded Rect)</text>
    <text x="595" y="1078" font-size="10" fill="#475569">Top bar: Process # (1.0 - 4.0)</text>
    <text x="595" y="1092" font-size="10" fill="#475569">Bottom: Function description</text>

    <!-- Data Store -->
    <rect x="850" y="1045" width="30" height="48" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="1.5"/>
    <text x="865" y="1074" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle">D1</text>
    <path d="M 880 1045 L 960 1045 M 880 1093 L 960 1093" stroke="#4A7BB0" stroke-width="1.5" fill="none"/>
    <rect x="880" y="1046" width="80" height="46" fill="#F8FAFC"/>
    <text x="890" y="1074" font-size="11" font-weight="bold" fill="#0F172A">Data Store</text>
    <text x="980" y="1062" font-size="11" font-weight="bold" fill="#0F172A">Data Store (Open Right)</text>
    <text x="980" y="1078" font-size="10" fill="#475569">Left ID partition (D1 - D7)</text>
    <text x="980" y="1092" font-size="10" fill="#475569">Open-ended database repository</text>

    <!-- Data Flow -->
    <path d="M 1240 1070 L 1330 1070" stroke="#1E293B" stroke-width="1.5" marker-end="url(#arrow)" fill="none"/>
    <rect x="1255" y="1055" width="60" height="14" fill="#FFFFFF"/>
    <text x="1285" y="1066" font-size="10" fill="#0F172A" text-anchor="middle">Data Flow</text>
    <text x="1350" y="1062" font-size="11" font-weight="bold" fill="#0F172A">Data Flow (Directed Arrow)</text>
    <text x="1350" y="1078" font-size="10" fill="#475569">Shows data payload &amp; direction</text>
    <text x="1350" y="1092" font-size="10" fill="#475569">Labeled with noun phrases</text>
  </g>
</svg>'''
    return svg


def generate_svg_yourdon():
    """Generates an SVG for Yourdon DeMarco DFD Level 1"""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1700 1160" width="100%" height="100%" style="background-color: #ffffff; font-family: 'Segoe UI', Arial, Helvetica, sans-serif;">
  <defs>
    <!-- Arrow Markers -->
    <marker id="yd-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#1E293B" />
    </marker>
    <marker id="yd-arrow-blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#B45309" />
    </marker>
    <!-- Drop Shadow Filter -->
    <filter id="yd-shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" flood-color="#000000" />
    </filter>
  </defs>

  <!-- Title Banner -->
  <rect x="60" y="20" width="1580" height="48" rx="8" fill="#1E293B" filter="url(#yd-shadow)"/>
  <text x="850" y="42" fill="#FFFFFF" font-size="16" font-weight="bold" text-anchor="middle" dominant-baseline="middle">DATA FLOW DIAGRAM (DFD) LEVEL 1: SCHOOL MANAGEMENT SYSTEM</text>
  <text x="850" y="58" fill="#FCD34D" font-size="12" text-anchor="middle" dominant-baseline="middle">Yourdon &amp; DeMarco Notation | Four Core Modules: Admin, Teacher, Student, Registrar Office</text>

  <!-- ================= EXTERNAL ENTITIES (Yellowish Sharp Rectangles) ================= -->
  <!-- Admin -->
  <g filter="url(#yd-shadow)">
    <rect x="60" y="140" width="160" height="90" fill="#FFF2CC" stroke="#D6B656" stroke-width="2"/>
    <text x="140" y="165" font-size="11" font-weight="bold" fill="#78350F" text-anchor="middle">EXTERNAL ENTITY</text>
    <text x="140" y="190" font-size="18" font-weight="bold" fill="#0F172A" text-anchor="middle">Admin</text>
    <text x="140" y="212" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">(System Admin)</text>
  </g>

  <!-- Registrar Office -->
  <g filter="url(#yd-shadow)">
    <rect x="60" y="740" width="160" height="90" fill="#FFF2CC" stroke="#D6B656" stroke-width="2"/>
    <text x="140" y="765" font-size="11" font-weight="bold" fill="#78350F" text-anchor="middle">EXTERNAL ENTITY</text>
    <text x="140" y="790" font-size="17" font-weight="bold" fill="#0F172A" text-anchor="middle">Registrar Office</text>
    <text x="140" y="812" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">(Admissions / Records)</text>
  </g>

  <!-- Teacher -->
  <g filter="url(#yd-shadow)">
    <rect x="1480" y="140" width="160" height="90" fill="#FFF2CC" stroke="#D6B656" stroke-width="2"/>
    <text x="1560" y="165" font-size="11" font-weight="bold" fill="#78350F" text-anchor="middle">EXTERNAL ENTITY</text>
    <text x="1560" y="190" font-size="18" font-weight="bold" fill="#0F172A" text-anchor="middle">Teacher</text>
    <text x="1560" y="212" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">(Faculty Staff)</text>
  </g>

  <!-- Student -->
  <g filter="url(#yd-shadow)">
    <rect x="1480" y="740" width="160" height="90" fill="#FFF2CC" stroke="#D6B656" stroke-width="2"/>
    <text x="1560" y="765" font-size="11" font-weight="bold" fill="#78350F" text-anchor="middle">EXTERNAL ENTITY</text>
    <text x="1560" y="790" font-size="18" font-weight="bold" fill="#0F172A" text-anchor="middle">Student</text>
    <text x="1560" y="812" font-size="11" font-style="italic" fill="#475569" text-anchor="middle">(Learner / Enrollee)</text>
  </g>


  <!-- ================= PROCESSES (Yourdon DeMarco: Circle / Bubble) ================= -->
  <!-- Process 1.0 Admin -->
  <g filter="url(#yd-shadow)">
    <circle cx="460" cy="185" r="60" fill="#FFF2CC" stroke="#D6B656" stroke-width="2.5"/>
    <text x="460" y="165" font-size="16" font-weight="bold" fill="#78350F" text-anchor="middle">1.0</text>
    <text x="460" y="185" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">Admin</text>
    <text x="460" y="202" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">Management</text>
  </g>

  <!-- Process 4.0 Registrar -->
  <g filter="url(#yd-shadow)">
    <circle cx="460" cy="785" r="60" fill="#FFF2CC" stroke="#D6B656" stroke-width="2.5"/>
    <text x="460" y="765" font-size="16" font-weight="bold" fill="#78350F" text-anchor="middle">4.0</text>
    <text x="460" y="785" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">Registrar</text>
    <text x="460" y="802" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">Office</text>
  </g>

  <!-- Process 2.0 Teacher -->
  <g filter="url(#yd-shadow)">
    <circle cx="1230" cy="185" r="60" fill="#FFF2CC" stroke="#D6B656" stroke-width="2.5"/>
    <text x="1230" y="165" font-size="16" font-weight="bold" fill="#78350F" text-anchor="middle">2.0</text>
    <text x="1230" y="185" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">Teacher</text>
    <text x="1230" y="202" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">Operations</text>
  </g>

  <!-- Process 3.0 Student -->
  <g filter="url(#yd-shadow)">
    <circle cx="1230" cy="785" r="60" fill="#FFF2CC" stroke="#D6B656" stroke-width="2.5"/>
    <text x="1230" y="765" font-size="16" font-weight="bold" fill="#78350F" text-anchor="middle">3.0</text>
    <text x="1230" y="785" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">Student</text>
    <text x="1230" y="802" font-size="13" font-weight="bold" fill="#0F172A" text-anchor="middle">Portal</text>
  </g>


  <!-- ================= DATA STORES (Yourdon DeMarco: Open-Ended Box) ================= -->
  <!-- D1 -->
  <g>
    <path d="M 975 80 L 725 80 L 725 126 L 975 126" stroke="#D6B656" stroke-width="2" fill="none"/>
    <rect x="726" y="81" width="248" height="44" fill="#FFF2CC"/>
    <text x="740" y="100" font-size="12" font-weight="bold" fill="#78350F">D1 | Admin &amp; System Settings</text>
    <text x="740" y="117" font-size="10" fill="#64748B">[admin, setting]</text>
  </g>

  <!-- D2 -->
  <g>
    <path d="M 975 215 L 725 215 L 725 261 L 975 261" stroke="#D6B656" stroke-width="2" fill="none"/>
    <rect x="726" y="216" width="248" height="44" fill="#FFF2CC"/>
    <text x="740" y="235" font-size="12" font-weight="bold" fill="#78350F">D2 | Teacher Records</text>
    <text x="740" y="252" font-size="10" fill="#64748B">[teacher]</text>
  </g>

  <!-- D7 -->
  <g>
    <path d="M 975 350 L 725 350 L 725 396 L 975 396" stroke="#D6B656" stroke-width="2" fill="none"/>
    <rect x="726" y="351" width="248" height="44" fill="#FFF2CC"/>
    <text x="740" y="370" font-size="12" font-weight="bold" fill="#78350F">D7 | Registrar Staff Records</text>
    <text x="740" y="387" font-size="10" fill="#64748B">[registrar_office]</text>
  </g>

  <!-- D4 -->
  <g>
    <path d="M 975 485 L 725 485 L 725 531 L 975 531" stroke="#D6B656" stroke-width="2" fill="none"/>
    <rect x="726" y="486" width="248" height="44" fill="#FFF2CC"/>
    <text x="740" y="505" font-size="12" font-weight="bold" fill="#78350F">D4 | Academic Structure</text>
    <text x="740" y="522" font-size="10" fill="#64748B">[grades, section, class, subjects]</text>
  </g>

  <!-- D3 -->
  <g>
    <path d="M 975 620 L 725 620 L 725 666 L 975 666" stroke="#D6B656" stroke-width="2" fill="none"/>
    <rect x="726" y="621" width="248" height="44" fill="#FFF2CC"/>
    <text x="740" y="640" font-size="12" font-weight="bold" fill="#78350F">D3 | Student Records</text>
    <text x="740" y="657" font-size="10" fill="#64748B">[student]</text>
  </g>

  <!-- D5 -->
  <g>
    <path d="M 975 755 L 725 755 L 725 801 L 975 801" stroke="#D6B656" stroke-width="2" fill="none"/>
    <rect x="726" y="756" width="248" height="44" fill="#FFF2CC"/>
    <text x="740" y="775" font-size="12" font-weight="bold" fill="#78350F">D5 | Scores &amp; Results</text>
    <text x="740" y="792" font-size="10" fill="#64748B">[student_score]</text>
  </g>

  <!-- D6 -->
  <g>
    <path d="M 975 890 L 725 890 L 725 936 L 975 936" stroke="#D6B656" stroke-width="2" fill="none"/>
    <rect x="726" y="891" width="248" height="44" fill="#FFF2CC"/>
    <text x="740" y="910" font-size="12" font-weight="bold" fill="#78350F">D6 | Inquiries &amp; Messages</text>
    <text x="740" y="927" font-size="10" fill="#64748B">[message]</text>
  </g>


  <!-- ================= DATA FLOWS ================= -->
  <!-- Admin -> 1.0 -->
  <g>
    <path d="M 220 160 L 402 160" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="245" y="148" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="305" y="159" font-size="10" fill="#0F172A" text-anchor="middle">Admin Credentials</text>

    <path d="M 220 185 L 400 185" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="245" y="173" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="305" y="184" font-size="10" fill="#0F172A" text-anchor="middle">Staff Setup &amp; Config</text>

    <path d="M 402 210 L 220 210" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="245" y="202" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="305" y="213" font-size="10" fill="#0F172A" text-anchor="middle">Dashboard &amp; Reports</text>
  </g>

  <!-- 1.0 -> Data Stores -->
  <g>
    <path d="M 515 160 L 650 160 L 650 103 L 725 103" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" marker-start="url(#yd-arrow-blue)" fill="none"/>
    <rect x="605" y="118" width="105" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="657" y="129" font-size="10" fill="#78350F" text-anchor="middle">Update / Read Config</text>

    <path d="M 520 185 L 670 185 L 670 238 L 725 238" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" fill="none"/>
    <rect x="615" y="210" width="100" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="665" y="221" font-size="10" fill="#78350F" text-anchor="middle">Create Teacher Acc.</text>

    <path d="M 505 225 L 540 225 L 540 373 L 725 373" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" fill="none"/>
    <rect x="560" y="360" width="115" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="617" y="371" font-size="10" fill="#78350F" text-anchor="middle">Manage Registrar Staff</text>

    <path d="M 460 245 L 460 499 L 725 499" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" fill="none"/>
    <rect x="485" y="488" width="145" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="557" y="499" font-size="10" fill="#78350F" text-anchor="middle">Configure Classes &amp; Grades</text>

    <path d="M 725 913 L 320 913 L 320 320 L 420 320 L 420 238" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" fill="none"/>
    <rect x="330" y="308" width="115" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="387" y="319" font-size="10" fill="#78350F" text-anchor="middle">Read Inquiries / Msg</text>
  </g>

  <!-- Registrar -> 4.0 -->
  <g>
    <path d="M 220 760 L 402 760" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="245" y="748" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="305" y="759" font-size="10" fill="#0F172A" text-anchor="middle">Staff Credentials</text>

    <path d="M 220 785 L 400 785" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="245" y="773" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="305" y="784" font-size="10" fill="#0F172A" text-anchor="middle">Student Admissions Data</text>

    <path d="M 402 810 L 220 810" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="245" y="802" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="305" y="813" font-size="10" fill="#0F172A" text-anchor="middle">Enrollment Confirmations</text>
  </g>

  <!-- 4.0 -> Data Stores -->
  <g>
    <path d="M 725 385 L 560 385 L 560 740 L 505 740" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" fill="none"/>
    <rect x="565" y="420" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="625" y="431" font-size="10" fill="#78350F" text-anchor="middle">Verify Registrar Auth</text>

    <path d="M 725 517 L 510 517 L 510 728" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" fill="none"/>
    <rect x="515" y="550" width="130" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="580" y="561" font-size="10" fill="#78350F" text-anchor="middle">Fetch Grade &amp; Section List</text>

    <path d="M 515 760 L 660 760 L 660 643 L 725 643" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" marker-start="url(#yd-arrow-blue)" fill="none"/>
    <rect x="605" y="695" width="135" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="672" y="706" font-size="10" fill="#78350F" text-anchor="middle">Register / Query Student</text>
  </g>

  <!-- Teacher -> 2.0 -->
  <g>
    <path d="M 1480 160 L 1288 160" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="1335" y="148" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1395" y="159" font-size="10" fill="#0F172A" text-anchor="middle">Teacher Credentials</text>

    <path d="M 1480 185 L 1290 185" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="1335" y="173" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1395" y="184" font-size="10" fill="#0F172A" text-anchor="middle">Student Marks &amp; Scores</text>

    <path d="M 1288 210 L 1480 210" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="1335" y="202" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1395" y="213" font-size="10" fill="#0F172A" text-anchor="middle">Assigned Rosters / Lists</text>
  </g>

  <!-- 2.0 -> Data Stores -->
  <g>
    <path d="M 975 238 L 1050 238 L 1050 165 L 1172 165" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" fill="none"/>
    <rect x="1005" y="185" width="115" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1062" y="196" font-size="10" fill="#78350F" text-anchor="middle">Verify Teacher Auth</text>

    <path d="M 975 499 L 1186 499 L 1186 240" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" fill="none"/>
    <rect x="1060" y="488" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1120" y="499" font-size="10" fill="#78350F" text-anchor="middle">Fetch Subject Details</text>

    <path d="M 975 634 L 1252 634 L 1252 243" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" fill="none"/>
    <rect x="1135" y="623" width="125" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1197" y="634" font-size="10" fill="#78350F" text-anchor="middle">Fetch Class Student List</text>

    <path d="M 1172 207 L 1025 207 L 1025 769 L 975 769" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" marker-start="url(#yd-arrow-blue)" fill="none"/>
    <rect x="990" y="325" width="140" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1060" y="336" font-size="10" fill="#78350F" text-anchor="middle">Save / Fetch Student Scores</text>
  </g>

  <!-- Student -> 3.0 -->
  <g>
    <path d="M 1480 760 L 1288 760" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="1335" y="748" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1395" y="759" font-size="10" fill="#0F172A" text-anchor="middle">Credentials &amp; Password</text>

    <path d="M 1480 785 L 1290 785" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="1335" y="773" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1395" y="784" font-size="10" fill="#0F172A" text-anchor="middle">Inquiries &amp; Messages</text>

    <path d="M 1288 810 L 1480 810" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="1335" y="802" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1395" y="813" font-size="10" fill="#0F172A" text-anchor="middle">Profile, Scores &amp; Grades</text>
  </g>

  <!-- 3.0 -> Data Stores -->
  <g>
    <path d="M 975 652 L 1060 652 L 1060 755 L 1172 755" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" marker-start="url(#yd-arrow-blue)" fill="none"/>
    <rect x="1000" y="695" width="145" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1072" y="706" font-size="10" fill="#78350F" text-anchor="middle">Verify Auth / Update Pwd</text>

    <path d="M 975 517 L 1208 517 L 1208 728" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" fill="none"/>
    <rect x="1080" y="550" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1140" y="561" font-size="10" fill="#78350F" text-anchor="middle">Fetch Enrolled Courses</text>

    <path d="M 975 787 L 1170 787" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" fill="none"/>
    <rect x="990" y="776" width="120" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1050" y="787" font-size="10" fill="#78350F" text-anchor="middle">Read Scores &amp; Grades</text>

    <path d="M 1230 845 L 1230 913 L 975 913" stroke="#B45309" stroke-width="1.5" marker-end="url(#yd-arrow-blue)" fill="none"/>
    <rect x="1070" y="902" width="130" height="15" fill="#FFFFFF" opacity="0.95"/>
    <text x="1135" y="913" font-size="10" fill="#78350F" text-anchor="middle">Submit Feedback Inquiry</text>
  </g>


  <!-- ================= LEGEND ================= -->
  <g>
    <rect x="60" y="1000" width="1580" height="120" rx="10" fill="#F1F5F9" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="80" y="1025" font-size="13" font-weight="bold" fill="#1E293B">YOURDON &amp; DEMARCO DFD NOTATION STANDARD (COMPLIANT WITH ATTACHED SPECIFICATION)</text>

    <!-- Entity -->
    <rect x="90" y="1045" width="110" height="48" fill="#FFF2CC" stroke="#D6B656" stroke-width="2"/>
    <text x="145" y="1074" font-size="12" font-weight="bold" fill="#78350F" text-anchor="middle">Entity</text>
    <text x="215" y="1062" font-size="11" font-weight="bold" fill="#0F172A">External Entity</text>
    <text x="215" y="1078" font-size="10" fill="#475569">Source/Sink of data (Admin, Teacher,</text>
    <text x="215" y="1092" font-size="10" fill="#475569">Student, Registrar Office)</text>

    <!-- Process -->
    <circle cx="525" cy="1069" r="24" fill="#FFF2CC" stroke="#D6B656" stroke-width="2"/>
    <text x="525" y="1073" font-size="10" font-weight="bold" fill="#78350F" text-anchor="middle">Process</text>
    <text x="575" y="1062" font-size="11" font-weight="bold" fill="#0F172A">Process (Circle / Bubble)</text>
    <text x="575" y="1078" font-size="10" fill="#475569">Numbered circle representing</text>
    <text x="575" y="1092" font-size="10" fill="#475569">system functional transformations</text>

    <!-- Data Store -->
    <path d="M 960 1045 L 870 1045 L 870 1093 L 960 1093" stroke="#D6B656" stroke-width="2" fill="none"/>
    <rect x="871" y="1046" width="88" height="46" fill="#FFF2CC"/>
    <text x="880" y="1074" font-size="11" font-weight="bold" fill="#78350F">Data Store</text>
    <text x="980" y="1062" font-size="11" font-weight="bold" fill="#0F172A">Data Store (Open-Ended Box)</text>
    <text x="980" y="1078" font-size="10" fill="#475569">Two parallel lines with left cap</text>
    <text x="980" y="1092" font-size="10" fill="#475569">Persistent database storage (D1-D7)</text>

    <!-- Data Flow -->
    <path d="M 1240 1070 L 1330 1070" stroke="#1E293B" stroke-width="1.5" marker-end="url(#yd-arrow)" fill="none"/>
    <rect x="1255" y="1055" width="60" height="14" fill="#FFFFFF"/>
    <text x="1285" y="1066" font-size="10" fill="#0F172A" text-anchor="middle">Data Flow</text>
    <text x="1350" y="1062" font-size="11" font-weight="bold" fill="#0F172A">Data Flow (Directed Arrow)</text>
    <text x="1350" y="1078" font-size="10" fill="#475569">Shows data payload &amp; direction</text>
    <text x="1350" y="1092" font-size="10" fill="#475569">Labeled with noun phrases</text>
  </g>
</svg>'''
    return svg


def generate_interactive_html():
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DFD Level 1: School Management System</title>
  <style>
    :root {
      --bg: #0F172A;
      --card-bg: #1E293B;
      --text: #F8FAFC;
      --text-muted: #94A3B8;
      --primary: #38BDF8;
      --primary-hover: #0EA5E9;
      --border: #334155;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }
    header {
      background: var(--card-bg);
      border-bottom: 1px solid var(--border);
      padding: 12px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .header-left h1 {
      font-size: 1.15rem;
      font-weight: 700;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .header-left p {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 2px;
    }
    .tabs-group {
      display: flex;
      background: #0F172A;
      padding: 4px;
      border-radius: 8px;
      border: 1px solid var(--border);
      gap: 4px;
    }
    .tab-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 6px 14px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      border-radius: 6px;
      transition: all 0.2s;
    }
    .tab-btn.active {
      background: #2563EB;
      color: #FFFFFF;
      box-shadow: 0 2px 6px rgba(37, 99, 235, 0.4);
    }
    .header-actions {
      display: flex;
      gap: 8px;
      align-items: center;
    }
    .btn {
      background: var(--card-bg);
      color: #F8FAFC;
      border: 1px solid var(--border);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      transition: all 0.15s;
    }
    .btn:hover {
      background: #334155;
      border-color: #64748B;
    }
    .btn-primary {
      background: #2563EB;
      border-color: #3B82F6;
      color: #FFFFFF;
    }
    .btn-primary:hover {
      background: #1D4ED8;
    }
    .viewport {
      flex: 1;
      position: relative;
      overflow: hidden;
      background: #E2E8F0;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .diagram-container {
      width: 100%;
      height: 100%;
      overflow: auto;
      display: flex;
      justify-content: center;
      align-items: flex-start;
      padding: 24px;
    }
    .diagram-container svg {
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.2);
      border-radius: 8px;
      background: #FFFFFF;
      max-width: 1700px;
      width: 100%;
      height: auto;
    }
    .controls {
      position: absolute;
      bottom: 20px;
      right: 20px;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 8px;
      padding: 6px;
      display: flex;
      gap: 6px;
      z-index: 10;
    }
    .ctrl-btn {
      background: #1E293B;
      color: #FFFFFF;
      border: 1px solid #334155;
      width: 32px;
      height: 32px;
      border-radius: 6px;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: pointer;
      font-size: 14px;
      font-weight: bold;
    }
    .ctrl-btn:hover {
      background: #334155;
    }
  </style>
</head>
<body>
  <header>
    <div class="header-left">
      <h1>School Management System &bull; DFD Level 1</h1>
      <p>Modules: Admin, Teacher, Student, Registrar Office &bull; No UML Symbols &bull; Compliant with Specification</p>
    </div>
    <div class="tabs-group">
      <button class="tab-btn active" onclick="switchTab('gane-sarson')">Gane &amp; Sarson Notation</button>
      <button class="tab-btn" onclick="switchTab('yourdon')">Yourdon &amp; DeMarco Notation</button>
    </div>
    <div class="header-actions">
      <a href="school_management_dfd_level1.drawio" download class="btn btn-primary" title="Download editable draw.io diagram file">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
        Download .drawio
      </a>
      <a href="https://app.diagrams.net/" target="_blank" class="btn" title="Open diagrams.net online editor">
        Open in draw.io
      </a>
    </div>
  </header>

  <div class="viewport">
    <div class="diagram-container" id="container-gs">
      <iframe src="dfd_level1_gane_sarson.svg" style="width: 1700px; height: 1160px; border: none; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.25);"></iframe>
    </div>
    <div class="diagram-container" id="container-yd" style="display: none;">
      <iframe src="dfd_level1_yourdon_demarco.svg" style="width: 1700px; height: 1160px; border: none; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.25);"></iframe>
    </div>
  </div>

  <script>
    function switchTab(notation) {
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      if (notation === 'gane-sarson') {
        document.querySelectorAll('.tab-btn')[0].classList.add('active');
        document.getElementById('container-gs').style.display = 'flex';
        document.getElementById('container-yd').style.display = 'none';
      } else {
        document.querySelectorAll('.tab-btn')[1].classList.add('active');
        document.getElementById('container-gs').style.display = 'none';
        document.getElementById('container-yd').style.display = 'flex';
      }
    }
  </script>
</body>
</html>'''
    return html_content


def main():
    workspace = r"c:\xampp\htdocs\school-management"
    
    # 1. Generate draw.io XML file
    drawio_file = os.path.join(workspace, "school_management_dfd_level1.drawio")
    print(f"Writing {drawio_file}...")
    with open(drawio_file, "w", encoding="utf-8") as f:
        f.write(build_drawio_xml())
    
    # 2. Generate SVG 1 (Gane & Sarson)
    svg_gs_file = os.path.join(workspace, "dfd_level1_gane_sarson.svg")
    print(f"Writing {svg_gs_file}...")
    with open(svg_gs_file, "w", encoding="utf-8") as f:
        f.write(generate_svg_gane_sarson())
        
    # 3. Generate SVG 2 (Yourdon & DeMarco)
    svg_yd_file = os.path.join(workspace, "dfd_level1_yourdon_demarco.svg")
    print(f"Writing {svg_yd_file}...")
    with open(svg_yd_file, "w", encoding="utf-8") as f:
        f.write(generate_svg_yourdon())
        
    # 4. Generate Interactive HTML Viewer
    html_file = os.path.join(workspace, "dfd_level1_viewer.html")
    print(f"Writing {html_file}...")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(generate_interactive_html())

    print("All diagram files successfully generated!")

if __name__ == "__main__":
    main()
