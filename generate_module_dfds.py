#!/usr/bin/env python3
"""
Generator for Module-Specific Data Flow Diagrams (DFDs)
Strictly adheres to the user-provided DFD Shapes:
1. External Entity: Rectangle
2. Process: Oval / Ellipse
3. Data Store: Two Parallel Horizontal Lines
4. Data Flow: Solid Arrow Line

Files Generated:
- admin.drawio / admin.drowio
- teacher.drawio / teacher.drowio
- student.drawio / student.drowio
- registrar.drawio / registrar.drowio / registarar.drowio
- Standalone SVGs: admin_dfd.svg, teacher_dfd.svg, student_dfd.svg, registrar_dfd.svg
- dfd_modules_viewer.html
"""

import os
import shutil
import html

# Common style definitions for draw.io
STYLE_ENTITY = "rounded=0;whiteSpace=wrap;html=1;fillColor=#EBF3FB;strokeColor=#2563EB;strokeWidth=2;fontColor=#0F172A;fontSize=13;fontStyle=1;align=center;verticalAlign=middle;shadow=1;"
STYLE_ENTITY_SECONDARY = "rounded=0;whiteSpace=wrap;html=1;fillColor=#F1F5F9;strokeColor=#475569;strokeWidth=2;fontColor=#0F172A;fontSize=13;fontStyle=1;align=center;verticalAlign=middle;shadow=1;"
STYLE_PROCESS = "ellipse;whiteSpace=wrap;html=1;fillColor=#FFFBEB;strokeColor=#D97706;strokeWidth=2;fontColor=#78350F;fontSize=12;align=center;verticalAlign=middle;shadow=1;"
# Two parallel horizontal lines for Data Store
STYLE_DATASTORE = "shape=partialRectangle;top=1;bottom=1;left=0;right=0;fillColor=#F8FAFC;strokeColor=#334155;strokeWidth=2;whiteSpace=wrap;html=1;fontColor=#0F172A;fontSize=12;fontStyle=1;align=center;verticalAlign=middle;"
STYLE_FLOW = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;labelBackgroundColor=#FFFFFF;"
STYLE_FLOW_BIDIR = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=classic;startArrow=classic;strokeColor=#2563EB;strokeWidth=1.5;fontSize=11;fontColor=#1E3A8A;labelBackgroundColor=#FFFFFF;"

def generate_admin_drawio():
    xml = '''<mxfile host="app.diagrams.net" modified="2026-09-26T00:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="admin-module-dfd" name="Admin Module DFD">
    <mxGraphModel dx="1600" dy="1100" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1650" pageHeight="1150" background="#FFFFFF" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Banner -->
        <mxCell id="title" value="DATA FLOW DIAGRAM (DFD): ADMIN MODULE&#xa;School Management System (sms_db) | Standard Shapes: Entity (Rectangle), Process (Oval), Data Store (Parallel Lines)" style="shape=rectangle;fillColor=#1E293B;strokeColor=#0F172A;fontColor=#FFFFFF;fontStyle=1;fontSize=15;align=center;verticalAlign=middle;rounded=1;arcSize=6;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1550" height="46" as="geometry" />
        </mxCell>

        <!-- ================= EXTERNAL ENTITIES (Rectangles) ================= -->
        <!-- Primary Admin Entity -->
        <mxCell id="ent_admin" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 15px;&quot;&gt;Admin&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(School Administrator)&lt;/i&gt;" style="''' + STYLE_ENTITY + '''" vertex="1" parent="1">
          <mxGeometry x="50" y="380" width="160" height="110" as="geometry" />
        </mxCell>

        <!-- Secondary Entity: Public Visitor -->
        <mxCell id="ent_visitor" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 14px;&quot;&gt;Public Visitor / Parent&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Contact Inquiries)&lt;/i&gt;" style="''' + STYLE_ENTITY_SECONDARY + '''" vertex="1" parent="1">
          <mxGeometry x="50" y="860" width="160" height="85" as="geometry" />
        </mxCell>

        <!-- Secondary Entity: Teacher -->
        <mxCell id="ent_teacher" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 14px;&quot;&gt;Teacher Staff&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Receives Login Info)&lt;/i&gt;" style="''' + STYLE_ENTITY_SECONDARY + '''" vertex="1" parent="1">
          <mxGeometry x="1440" y="310" width="160" height="80" as="geometry" />
        </mxCell>

        <!-- Secondary Entity: Registrar Office -->
        <mxCell id="ent_registrar" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 14px;&quot;&gt;Registrar Staff&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Receives Login Info)&lt;/i&gt;" style="''' + STYLE_ENTITY_SECONDARY + '''" vertex="1" parent="1">
          <mxGeometry x="1440" y="470" width="160" height="80" as="geometry" />
        </mxCell>


        <!-- ================= PROCESSES (Ovals / Ellipses) ================= -->
        <!-- Process 1.1 -->
        <mxCell id="p1_1" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;1.1&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Admin Login &amp;amp;&lt;br/&gt;Authentication&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="360" y="100" width="150" height="100" as="geometry" />
        </mxCell>

        <!-- Process 1.2 -->
        <mxCell id="p1_2" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;1.2&lt;/b&gt;&lt;br/&gt;&lt;b&gt;School Settings&lt;br/&gt;Configuration&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="360" y="240" width="150" height="100" as="geometry" />
        </mxCell>

        <!-- Process 1.3 -->
        <mxCell id="p1_3" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;1.3&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Teacher Account &amp;amp;&lt;br/&gt;Subject Assignment&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="360" y="380" width="150" height="100" as="geometry" />
        </mxCell>

        <!-- Process 1.4 -->
        <mxCell id="p1_4" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;1.4&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Registrar Staff&lt;br/&gt;Account Setup&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="360" y="520" width="150" height="100" as="geometry" />
        </mxCell>

        <!-- Process 1.5 -->
        <mxCell id="p1_5" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;1.5&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Academic Structure&lt;br/&gt;(Grades &amp;amp; Sections)&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="360" y="660" width="150" height="100" as="geometry" />
        </mxCell>

        <!-- Process 1.6 -->
        <mxCell id="p1_6" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;1.6&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Course &amp;amp; Subject&lt;br/&gt;Curriculum Setup&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="360" y="790" width="150" height="100" as="geometry" />
        </mxCell>

        <!-- Process 1.7 -->
        <mxCell id="p1_7" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;1.7&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Feedback Inquiries&lt;br/&gt;&amp;amp; Message Review&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="360" y="920" width="150" height="100" as="geometry" />
        </mxCell>


        <!-- ================= DATA STORES (Two Parallel Horizontal Lines) ================= -->
        <!-- D1: admin table -->
        <mxCell id="ds_admin" value="&lt;b&gt;D1&lt;/b&gt; | admin (Admin Credentials &amp;amp; Profiles)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="125" width="310" height="46" as="geometry" />
        </mxCell>

        <!-- D2: setting table -->
        <mxCell id="ds_setting" value="&lt;b&gt;D2&lt;/b&gt; | setting (School Name, Slogan, Term, Year)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="265" width="310" height="46" as="geometry" />
        </mxCell>

        <!-- D3: teacher table -->
        <mxCell id="ds_teacher" value="&lt;b&gt;D3&lt;/b&gt; | teacher (Faculty Roster &amp;amp; Subject Allocations)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="405" width="310" height="46" as="geometry" />
        </mxCell>

        <!-- D4: registrar_office table -->
        <mxCell id="ds_reg" value="&lt;b&gt;D4&lt;/b&gt; | registrar_office (Staff Profiles &amp;amp; Logins)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="545" width="310" height="46" as="geometry" />
        </mxCell>

        <!-- D5: grades, section, class tables -->
        <mxCell id="ds_structure" value="&lt;b&gt;D5&lt;/b&gt; | grades &amp;amp; section &amp;amp; class (Classroom Cohorts)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="685" width="310" height="46" as="geometry" />
        </mxCell>

        <!-- D6: subjects & courses tables -->
        <mxCell id="ds_courses" value="&lt;b&gt;D6&lt;/b&gt; | subjects &amp;amp; courses (Academic Curriculum)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="815" width="310" height="46" as="geometry" />
        </mxCell>

        <!-- D7: message table -->
        <mxCell id="ds_message" value="&lt;b&gt;D7&lt;/b&gt; | message (Inquiries, Feedback &amp;amp; Sender Email)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="945" width="310" height="46" as="geometry" />
        </mxCell>


        <!-- ================= DATA FLOWS (Directed Solid Arrows) ================= -->
        <!-- Flow: Admin -> 1.1 Auth -->
        <mxCell id="f_admin_p1_1" value="Admin Credentials (user, pass)" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_admin" target="p1_1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="270" y="400" />
              <mxPoint x="270" y="150" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 1.1 <-> D1 -->
        <mxCell id="f_p1_1_d1" value="Validate Auth / Establish Admin Session" style="''' + STYLE_FLOW_BIDIR + '''" edge="1" parent="1" source="p1_1" target="ds_admin">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: 1.1 -> Admin Return Dashboard -->
        <mxCell id="f_p1_1_admin" value="Login Token &amp;amp; Admin Dashboard" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p1_1" target="ent_admin">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="290" y="170" />
              <mxPoint x="290" y="420" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Admin -> 1.2 Settings -->
        <mxCell id="f_admin_p1_2" value="School Name, Slogan &amp;amp; Year Config" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_admin" target="p1_2">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="260" y="430" />
              <mxPoint x="260" y="290" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 1.2 <-> D2 -->
        <mxCell id="f_p1_2_d2" value="Read &amp;amp; Update School Settings" style="''' + STYLE_FLOW_BIDIR + '''" edge="1" parent="1" source="p1_2" target="ds_setting">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: Admin -> 1.3 Teacher Management -->
        <mxCell id="f_admin_p1_3" value="Teacher Details (name, qualification, subjects)" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_admin" target="p1_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: 1.3 <-> D3 -->
        <mxCell id="f_p1_3_d3" value="Insert / Edit / Delete Faculty Record" style="''' + STYLE_FLOW_BIDIR + '''" edge="1" parent="1" source="p1_3" target="ds_teacher">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: D3 -> Teacher Entity -->
        <mxCell id="f_d3_teacher" value="Account Provisioned Notice" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_teacher" target="ent_teacher">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1280" y="428" />
              <mxPoint x="1280" y="350" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Admin -> 1.4 Registrar Management -->
        <mxCell id="f_admin_p1_4" value="Registrar Staff Registration Info" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_admin" target="p1_4">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="260" y="460" />
              <mxPoint x="260" y="570" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 1.4 <-> D4 -->
        <mxCell id="f_p1_4_d4" value="Manage Registrar Staff Accounts" style="''' + STYLE_FLOW_BIDIR + '''" edge="1" parent="1" source="p1_4" target="ds_reg">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: D4 -> Registrar Entity -->
        <mxCell id="f_d4_reg" value="Staff Credentials Granted" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_reg" target="ent_registrar">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1280" y="568" />
              <mxPoint x="1280" y="510" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Admin -> 1.5 Academic Structure -->
        <mxCell id="f_admin_p1_5" value="Grades, Sections &amp;amp; Class Pairs" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_admin" target="p1_5">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="250" y="480" />
              <mxPoint x="250" y="710" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 1.5 <-> D5 -->
        <mxCell id="f_p1_5_d5" value="Add / Update Grades, Sections &amp;amp; Classes" style="''' + STYLE_FLOW_BIDIR + '''" edge="1" parent="1" source="p1_5" target="ds_structure">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: Admin -> 1.6 Curriculum -->
        <mxCell id="f_admin_p1_6" value="Course Code, Title &amp;amp; Target Grade" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_admin" target="p1_6">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="230" y="490" />
              <mxPoint x="230" y="840" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 1.6 <-> D6 -->
        <mxCell id="f_p1_6_d6" value="Store / Update Course &amp;amp; Subject Catalog" style="''' + STYLE_FLOW_BIDIR + '''" edge="1" parent="1" source="p1_6" target="ds_courses">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: Visitor -> 1.7 Feedback -->
        <mxCell id="f_vis_p1_7" value="Contact Form Feedback &amp;amp; Queries" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_visitor" target="p1_7">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="280" y="902" />
              <mxPoint x="280" y="970" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 1.7 -> D7 -->
        <mxCell id="f_p1_7_d7" value="Store Inquiries &amp;amp; Messages" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p1_7" target="ds_message">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: D7 -> 1.7 -> Admin -->
        <mxCell id="f_d7_p1_7" value="Read Feedback Messages" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_message" target="p1_7">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="670" y="980" />
              <mxPoint x="670" y="980" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="f_p1_7_admin" value="Inquiries List &amp;amp; Messages to Admin" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p1_7" target="ent_admin">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="210" y="990" />
              <mxPoint x="210" y="490" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- ================= DFD SHAPE LEGEND (Exact match to Reference Image) ================= -->
        <mxCell id="legend_box" value="" style="rounded=1;arcSize=4;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#CBD5E1;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="50" y="1050" width="1550" height="70" as="geometry" />
        </mxCell>
        <mxCell id="leg_title" value="&lt;b&gt;DFD SHAPES USED IN THIS DIAGRAM (Standard Reference)&lt;/b&gt;" style="text;html=1;align=center;verticalAlign=middle;fontSize=12;fontColor=#0F172A;" vertex="1" parent="legend_box">
          <mxGeometry x="10" y="2" width="1530" height="20" as="geometry" />
        </mxCell>
        <!-- Legend 1: Entity -->
        <mxCell id="leg_ent" value="External Entity" style="''' + STYLE_ENTITY + '''fontSize=10;" vertex="1" parent="legend_box">
          <mxGeometry x="120" y="26" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_ent_desc" value="&lt;b&gt;Rectangle:&lt;/b&gt; Source/Sink of data" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="230" y="26" width="200" height="34" as="geometry" />
        </mxCell>
        <!-- Legend 2: Process -->
        <mxCell id="leg_proc" value="Process" style="''' + STYLE_PROCESS + '''fontSize=10;" vertex="1" parent="legend_box">
          <mxGeometry x="510" y="24" width="80" height="38" as="geometry" />
        </mxCell>
        <mxCell id="leg_proc_desc" value="&lt;b&gt;Oval:&lt;/b&gt; Transforms inputs to outputs" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="600" y="26" width="220" height="34" as="geometry" />
        </mxCell>
        <!-- Legend 3: Data Store -->
        <mxCell id="leg_ds" value="Data Store" style="''' + STYLE_DATASTORE + '''fontSize=10;" vertex="1" parent="legend_box">
          <mxGeometry x="890" y="28" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="leg_ds_desc" value="&lt;b&gt;Parallel Lines:&lt;/b&gt; DB Table / Storage" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="1000" y="26" width="220" height="34" as="geometry" />
        </mxCell>
        <!-- Legend 4: Flow -->
        <mxCell id="leg_flow" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=classic;strokeColor=#1E293B;strokeWidth=2;" edge="1" parent="legend_box">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1290" y="43" as="sourcePoint" />
            <mxPoint x="1360" y="43" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_flow_desc" value="&lt;b&gt;Solid Arrow:&lt;/b&gt; Movement of data" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="1380" y="26" width="180" height="34" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml

def generate_teacher_drawio():
    xml = '''<mxfile host="app.diagrams.net" modified="2026-09-26T00:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="teacher-module-dfd" name="Teacher Module DFD">
    <mxGraphModel dx="1600" dy="1100" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1650" pageHeight="1100" background="#FFFFFF" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Banner -->
        <mxCell id="title" value="DATA FLOW DIAGRAM (DFD): TEACHER MODULE&#xa;School Management System (sms_db) | Standard Shapes: Entity (Rectangle), Process (Oval), Data Store (Parallel Lines)" style="shape=rectangle;fillColor=#1E293B;strokeColor=#0F172A;fontColor=#FFFFFF;fontStyle=1;fontSize=15;align=center;verticalAlign=middle;rounded=1;arcSize=6;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1550" height="46" as="geometry" />
        </mxCell>

        <!-- ================= EXTERNAL ENTITIES (Rectangles) ================= -->
        <!-- Primary Entity: Teacher -->
        <mxCell id="ent_teacher" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 15px;&quot;&gt;Teacher&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Faculty Member)&lt;/i&gt;" style="''' + STYLE_ENTITY + '''" vertex="1" parent="1">
          <mxGeometry x="50" y="380" width="160" height="110" as="geometry" />
        </mxCell>

        <!-- Secondary Entity: Student (Recipient of results) -->
        <mxCell id="ent_student" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 14px;&quot;&gt;Student&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Evaluated Learner)&lt;/i&gt;" style="''' + STYLE_ENTITY_SECONDARY + '''" vertex="1" parent="1">
          <mxGeometry x="1440" y="580" width="160" height="90" as="geometry" />
        </mxCell>

        <!-- ================= PROCESSES (Ovals / Ellipses) ================= -->
        <!-- Process 2.1 -->
        <mxCell id="p2_1" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;2.1&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Teacher Login &amp;amp;&lt;br/&gt;Authentication&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="120" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- Process 2.2 -->
        <mxCell id="p2_2" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;2.2&lt;/b&gt;&lt;br/&gt;&lt;b&gt;View Assigned&lt;br/&gt;Classes &amp;amp; Subjects&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="270" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- Process 2.3 -->
        <mxCell id="p2_3" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;2.3&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Student Class Roster&lt;br/&gt;Retrieval&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="420" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- Process 2.4 -->
        <mxCell id="p2_4" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;2.4&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Student Exam Marks&lt;br/&gt;&amp;amp; Score Evaluation&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="570" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- Process 2.5 -->
        <mxCell id="p2_5" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;2.5&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Teacher Profile &amp;amp;&lt;br/&gt;Password Update&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="730" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- ================= DATA STORES (Two Parallel Horizontal Lines) ================= -->
        <!-- D1: teacher -->
        <mxCell id="ds_teach" value="&lt;b&gt;D1&lt;/b&gt; | teacher (Faculty Profiles, Login &amp;amp; Assignments)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="145" width="330" height="46" as="geometry" />
        </mxCell>

        <!-- D2: class & subjects -->
        <mxCell id="ds_class_subj" value="&lt;b&gt;D2&lt;/b&gt; | class &amp;amp; subjects (Classrooms, Grades, Subject Code)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="295" width="330" height="46" as="geometry" />
        </mxCell>

        <!-- D3: student -->
        <mxCell id="ds_stud" value="&lt;b&gt;D3&lt;/b&gt; | student (Enrolled Students by Grade &amp;amp; Section)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="445" width="330" height="46" as="geometry" />
        </mxCell>

        <!-- D4: student_score -->
        <mxCell id="ds_score" value="&lt;b&gt;D4&lt;/b&gt; | student_score (Semester Exam Marks &amp;amp; Evaluations)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="595" width="330" height="46" as="geometry" />
        </mxCell>

        <!-- D5: setting -->
        <mxCell id="ds_setting" value="&lt;b&gt;D5&lt;/b&gt; | setting (Current Academic Year &amp;amp; Semester)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="755" width="330" height="46" as="geometry" />
        </mxCell>


        <!-- ================= DATA FLOWS (Directed Solid Arrows) ================= -->
        <!-- Flow: Teacher -> 2.1 Auth -->
        <mxCell id="f_teach_p2_1" value="Teacher Credentials (username, password)" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_teacher" target="p2_1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="280" y="400" />
              <mxPoint x="280" y="170" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 2.1 <-> D1 -->
        <mxCell id="f_p2_1_d1" value="Verify Teacher Credentials &amp;amp; Status" style="''' + STYLE_FLOW_BIDIR + '''" edge="1" parent="1" source="p2_1" target="ds_teach">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: 2.1 -> Teacher Dashboard -->
        <mxCell id="f_p2_1_teach" value="Teacher Dashboard Access &amp;amp; Profile Info" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p2_1" target="ent_teacher">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="300" y="190" />
              <mxPoint x="300" y="420" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Teacher -> 2.2 Classes -->
        <mxCell id="f_teach_p2_2" value="Request Assigned Classes &amp;amp; Syllabus" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_teacher" target="p2_2">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="260" y="430" />
              <mxPoint x="260" y="320" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: D2 -> 2.2 -->
        <mxCell id="f_d2_p2_2" value="Retrieve Class Cohorts &amp;amp; Subject Names" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_class_subj" target="p2_2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: 2.2 -> Teacher -->
        <mxCell id="f_p2_2_teach" value="Display Assigned Classes &amp;amp; Subjects" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p2_2" target="ent_teacher">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="290" y="340" />
              <mxPoint x="290" y="440" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Teacher -> 2.3 Roster -->
        <mxCell id="f_teach_p2_3" value="Select Class ID &amp;amp; Section Division" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_teacher" target="p2_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: D3 -> 2.3 -->
        <mxCell id="f_d3_p2_3" value="Fetch Enrolled Students by Class/Grade" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_stud" target="p2_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: 2.3 -> Teacher -->
        <mxCell id="f_p2_3_teach" value="Display Student Class Roster List" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p2_3" target="ent_teacher">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="280" y="480" />
              <mxPoint x="280" y="470" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Teacher -> 2.4 Scores -->
        <mxCell id="f_teach_p2_4" value="Submit Student Exam Scores &amp;amp; Marks String" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_teacher" target="p2_4">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="260" y="470" />
              <mxPoint x="260" y="620" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: D5 -> 2.4 -->
        <mxCell id="f_d5_p2_4" value="Fetch Current Semester &amp;amp; Year" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_setting" target="p2_4">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="680" y="778" />
              <mxPoint x="680" y="650" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 2.4 <-> D4 -->
        <mxCell id="f_p2_4_d4" value="Insert / Update student_score Record" style="''' + STYLE_FLOW_BIDIR + '''" edge="1" parent="1" source="p2_4" target="ds_score">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: 2.4 -> Teacher Feedback -->
        <mxCell id="f_p2_4_teach" value="Score Saved Confirmation" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p2_4" target="ent_teacher">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="290" y="640" />
              <mxPoint x="290" y="485" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: D4 -> Student Entity -->
        <mxCell id="f_d4_stud" value="Published Grades &amp;amp; Scores Visible to Student" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_score" target="ent_student">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: Teacher -> 2.5 Password -->
        <mxCell id="f_teach_p2_5" value="Change Password Request (old, new pass)" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_teacher" target="p2_5">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="240" y="485" />
              <mxPoint x="240" y="780" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 2.5 -> D1 -->
        <mxCell id="f_p2_5_d1" value="Update Hashed Password in teacher Table" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p2_5" target="ds_teach">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="750" y="780" />
              <mxPoint x="750" y="170" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 2.5 -> Teacher Success -->
        <mxCell id="f_p2_5_teach" value="Password Updated Successfully" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p2_5" target="ent_teacher">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="220" y="800" />
              <mxPoint x="220" y="490" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- ================= DFD SHAPE LEGEND ================= -->
        <mxCell id="legend_box" value="" style="rounded=1;arcSize=4;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#CBD5E1;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="50" y="980" width="1550" height="70" as="geometry" />
        </mxCell>
        <mxCell id="leg_title" value="&lt;b&gt;DFD SHAPES USED IN THIS DIAGRAM (Standard Reference)&lt;/b&gt;" style="text;html=1;align=center;verticalAlign=middle;fontSize=12;fontColor=#0F172A;" vertex="1" parent="legend_box">
          <mxGeometry x="10" y="2" width="1530" height="20" as="geometry" />
        </mxCell>
        <mxCell id="leg_ent" value="External Entity" style="''' + STYLE_ENTITY + '''fontSize=10;" vertex="1" parent="legend_box">
          <mxGeometry x="120" y="26" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_ent_desc" value="&lt;b&gt;Rectangle:&lt;/b&gt; Source/Sink of data" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="230" y="26" width="200" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_proc" value="Process" style="''' + STYLE_PROCESS + '''fontSize=10;" vertex="1" parent="legend_box">
          <mxGeometry x="510" y="24" width="80" height="38" as="geometry" />
        </mxCell>
        <mxCell id="leg_proc_desc" value="&lt;b&gt;Oval:&lt;/b&gt; Transforms inputs to outputs" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="600" y="26" width="220" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_ds" value="Data Store" style="''' + STYLE_DATASTORE + '''fontSize=10;" vertex="1" parent="legend_box">
          <mxGeometry x="890" y="28" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="leg_ds_desc" value="&lt;b&gt;Parallel Lines:&lt;/b&gt; DB Table / Storage" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="1000" y="26" width="220" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_flow" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=classic;strokeColor=#1E293B;strokeWidth=2;" edge="1" parent="legend_box">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1290" y="43" as="sourcePoint" />
            <mxPoint x="1360" y="43" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_flow_desc" value="&lt;b&gt;Solid Arrow:&lt;/b&gt; Movement of data" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="1380" y="26" width="180" height="34" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml

def generate_student_drawio():
    xml = '''<mxfile host="app.diagrams.net" modified="2026-09-26T00:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="student-module-dfd" name="Student Module DFD">
    <mxGraphModel dx="1600" dy="1100" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1650" pageHeight="1100" background="#FFFFFF" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Banner -->
        <mxCell id="title" value="DATA FLOW DIAGRAM (DFD): STUDENT MODULE&#xa;School Management System (sms_db) | Standard Shapes: Entity (Rectangle), Process (Oval), Data Store (Parallel Lines)" style="shape=rectangle;fillColor=#1E293B;strokeColor=#0F172A;fontColor=#FFFFFF;fontStyle=1;fontSize=15;align=center;verticalAlign=middle;rounded=1;arcSize=6;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1550" height="46" as="geometry" />
        </mxCell>

        <!-- ================= EXTERNAL ENTITIES (Rectangles) ================= -->
        <!-- Primary Entity: Student -->
        <mxCell id="ent_student" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 15px;&quot;&gt;Student&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Learner / Enrollee)&lt;/i&gt;" style="''' + STYLE_ENTITY + '''" vertex="1" parent="1">
          <mxGeometry x="50" y="380" width="160" height="110" as="geometry" />
        </mxCell>

        <!-- Secondary Entity: School Admin / Support -->
        <mxCell id="ent_admin" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 14px;&quot;&gt;Admin / Support&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Receives Inquiries)&lt;/i&gt;" style="''' + STYLE_ENTITY_SECONDARY + '''" vertex="1" parent="1">
          <mxGeometry x="1440" y="590" width="160" height="85" as="geometry" />
        </mxCell>

        <!-- ================= PROCESSES (Ovals / Ellipses) ================= -->
        <!-- Process 3.1 -->
        <mxCell id="p3_1" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;3.1&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Student Login &amp;amp;&lt;br/&gt;Authentication&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="120" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- Process 3.2 -->
        <mxCell id="p3_2" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;3.2&lt;/b&gt;&lt;br/&gt;&lt;b&gt;View Demographic&lt;br/&gt;&amp;amp; Enrollment Profile&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="270" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- Process 3.3 -->
        <mxCell id="p3_3" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;3.3&lt;/b&gt;&lt;br/&gt;&lt;b&gt;View Academic Scores&lt;br/&gt;&amp;amp; Report Card&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="430" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- Process 3.4 -->
        <mxCell id="p3_4" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;3.4&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Submit Feedback &amp;amp;&lt;br/&gt;Contact Inquiries&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="580" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- Process 3.5 -->
        <mxCell id="p3_5" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;3.5&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Password Change &amp;amp;&lt;br/&gt;Account Security&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="730" width="160" height="100" as="geometry" />
        </mxCell>


        <!-- ================= DATA STORES (Two Parallel Horizontal Lines) ================= -->
        <!-- D1: student -->
        <mxCell id="ds_stud" value="&lt;b&gt;D1&lt;/b&gt; | student (Credentials, Demographics, Parents &amp;amp; Classes)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="145" width="340" height="46" as="geometry" />
        </mxCell>

        <!-- D2: class, grades, section -->
        <mxCell id="ds_class" value="&lt;b&gt;D2&lt;/b&gt; | class &amp;amp; grades &amp;amp; section (Classroom Details &amp;amp; Standard)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="295" width="340" height="46" as="geometry" />
        </mxCell>

        <!-- D3: student_score -->
        <mxCell id="ds_score" value="&lt;b&gt;D3&lt;/b&gt; | student_score (Semester Evaluations &amp;amp; Exam Marks)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="445" width="340" height="46" as="geometry" />
        </mxCell>

        <!-- D4: subjects -->
        <mxCell id="ds_subj" value="&lt;b&gt;D4&lt;/b&gt; | subjects (Subject Names, Codes &amp;amp; Grade Level)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="520" width="340" height="46" as="geometry" />
        </mxCell>

        <!-- D5: message -->
        <mxCell id="ds_msg" value="&lt;b&gt;D5&lt;/b&gt; | message (Submitted Inquiries, Feedback &amp;amp; Timestamps)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="650" width="340" height="46" as="geometry" />
        </mxCell>


        <!-- ================= DATA FLOWS (Directed Solid Arrows) ================= -->
        <!-- Flow: Student -> 3.1 Auth -->
        <mxCell id="f_stud_p3_1" value="Student Credentials (username, password)" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_student" target="p3_1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="280" y="400" />
              <mxPoint x="280" y="170" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 3.1 <-> D1 -->
        <mxCell id="f_p3_1_d1" value="Validate Student Auth &amp;amp; Establish Session" style="''' + STYLE_FLOW_BIDIR + '''" edge="1" parent="1" source="p3_1" target="ds_stud">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: 3.1 -> Student Dashboard -->
        <mxCell id="f_p3_1_stud" value="Student Portal Access Granted" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p3_1" target="ent_student">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="300" y="190" />
              <mxPoint x="300" y="420" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Student -> 3.2 Profile Request -->
        <mxCell id="f_stud_p3_2" value="Request Demographic &amp;amp; Class Details" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_student" target="p3_2">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="260" y="430" />
              <mxPoint x="260" y="320" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: D1 -> 3.2 -->
        <mxCell id="f_d1_p3_2" value="Retrieve Student Personal &amp;amp; Parent Info" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_stud" target="p3_2">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="750" y="180" />
              <mxPoint x="750" y="310" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: D2 -> 3.2 -->
        <mxCell id="f_d2_p3_2" value="Retrieve Grade Level &amp;amp; Section Division" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_class" target="p3_2">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: 3.2 -> Student -->
        <mxCell id="f_p3_2_stud" value="Display Student Profile &amp;amp; Class Card" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p3_2" target="ent_student">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="290" y="340" />
              <mxPoint x="290" y="440" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Student -> 3.3 Score Card -->
        <mxCell id="f_stud_p3_3" value="Request Semester Exam Scores" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_student" target="p3_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: D3 -> 3.3 -->
        <mxCell id="f_d3_p3_3" value="Fetch Exam Scores (student_id)" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_score" target="p3_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: D4 -> 3.3 -->
        <mxCell id="f_d4_p3_3" value="Fetch Subject Code &amp;amp; Subject Name" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_subj" target="p3_3">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="710" y="543" />
              <mxPoint x="710" y="495" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 3.3 -> Student -->
        <mxCell id="f_p3_3_stud" value="Display Academic Report Card &amp;amp; Results" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p3_3" target="ent_student">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="280" y="475" />
              <mxPoint x="280" y="465" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Student -> 3.4 Contact Inquiry -->
        <mxCell id="f_stud_p3_4" value="Submit Contact Inquiry (name, email, text)" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_student" target="p3_4">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="260" y="470" />
              <mxPoint x="260" y="630" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 3.4 -> D5 -->
        <mxCell id="f_p3_4_d5" value="Insert Message Record into message Table" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p3_4" target="ds_msg">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="680" y="630" />
              <mxPoint x="680" y="673" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 3.4 -> Student Confirmation -->
        <mxCell id="f_p3_4_stud" value="Inquiry Submitted Confirmation" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p3_4" target="ent_student">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="290" y="650" />
              <mxPoint x="290" y="485" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: D5 -> Admin Entity -->
        <mxCell id="f_d5_admin" value="Forward Contact Inquiries to Admin" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_msg" target="ent_admin">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="1300" y="673" />
              <mxPoint x="1300" y="632" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Student -> 3.5 Password -->
        <mxCell id="f_stud_p3_5" value="Change Password Request (old, new pass)" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_student" target="p3_5">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="240" y="485" />
              <mxPoint x="240" y="780" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 3.5 -> D1 -->
        <mxCell id="f_p3_5_d1" value="Update Encrypted Password in student Table" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p3_5" target="ds_stud">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="750" y="780" />
              <mxPoint x="750" y="160" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 3.5 -> Student Success -->
        <mxCell id="f_p3_5_stud" value="Password Changed Notification" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p3_5" target="ent_student">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="220" y="800" />
              <mxPoint x="220" y="490" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- ================= DFD SHAPE LEGEND ================= -->
        <mxCell id="legend_box" value="" style="rounded=1;arcSize=4;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#CBD5E1;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="50" y="980" width="1550" height="70" as="geometry" />
        </mxCell>
        <mxCell id="leg_title" value="&lt;b&gt;DFD SHAPES USED IN THIS DIAGRAM (Standard Reference)&lt;/b&gt;" style="text;html=1;align=center;verticalAlign=middle;fontSize=12;fontColor=#0F172A;" vertex="1" parent="legend_box">
          <mxGeometry x="10" y="2" width="1530" height="20" as="geometry" />
        </mxCell>
        <mxCell id="leg_ent" value="External Entity" style="''' + STYLE_ENTITY + '''fontSize=10;" vertex="1" parent="legend_box">
          <mxGeometry x="120" y="26" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_ent_desc" value="&lt;b&gt;Rectangle:&lt;/b&gt; Source/Sink of data" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="230" y="26" width="200" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_proc" value="Process" style="''' + STYLE_PROCESS + '''fontSize=10;" vertex="1" parent="legend_box">
          <mxGeometry x="510" y="24" width="80" height="38" as="geometry" />
        </mxCell>
        <mxCell id="leg_proc_desc" value="&lt;b&gt;Oval:&lt;/b&gt; Transforms inputs to outputs" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="600" y="26" width="220" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_ds" value="Data Store" style="''' + STYLE_DATASTORE + '''fontSize=10;" vertex="1" parent="legend_box">
          <mxGeometry x="890" y="28" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="leg_ds_desc" value="&lt;b&gt;Parallel Lines:&lt;/b&gt; DB Table / Storage" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="1000" y="26" width="220" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_flow" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=classic;strokeColor=#1E293B;strokeWidth=2;" edge="1" parent="legend_box">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1290" y="43" as="sourcePoint" />
            <mxPoint x="1360" y="43" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_flow_desc" value="&lt;b&gt;Solid Arrow:&lt;/b&gt; Movement of data" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="1380" y="26" width="180" height="34" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml

def generate_registrar_drawio():
    xml = '''<mxfile host="app.diagrams.net" modified="2026-09-26T00:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="registrar-module-dfd" name="Registrar Office Module DFD">
    <mxGraphModel dx="1600" dy="1100" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1650" pageHeight="1100" background="#FFFFFF" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Banner -->
        <mxCell id="title" value="DATA FLOW DIAGRAM (DFD): REGISTRAR OFFICE MODULE&#xa;School Management System (sms_db) | Standard Shapes: Entity (Rectangle), Process (Oval), Data Store (Parallel Lines)" style="shape=rectangle;fillColor=#1E293B;strokeColor=#0F172A;fontColor=#FFFFFF;fontStyle=1;fontSize=15;align=center;verticalAlign=middle;rounded=1;arcSize=6;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="1550" height="46" as="geometry" />
        </mxCell>

        <!-- ================= EXTERNAL ENTITIES (Rectangles) ================= -->
        <!-- Primary Entity: Registrar Office Staff -->
        <mxCell id="ent_reg" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 15px;&quot;&gt;Registrar Staff&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Admissions &amp;amp; Records)&lt;/i&gt;" style="''' + STYLE_ENTITY + '''" vertex="1" parent="1">
          <mxGeometry x="50" y="380" width="160" height="110" as="geometry" />
        </mxCell>

        <!-- Secondary Entity: Newly Enrolled Student -->
        <mxCell id="ent_student" value="&lt;b&gt;EXTERNAL ENTITY&lt;/b&gt;&lt;br/&gt;&lt;font style=&quot;font-size: 14px;&quot;&gt;New Student&lt;/font&gt;&lt;br/&gt;&lt;i&gt;(Receives Enrollment)&lt;/i&gt;" style="''' + STYLE_ENTITY_SECONDARY + '''" vertex="1" parent="1">
          <mxGeometry x="1440" y="275" width="160" height="90" as="geometry" />
        </mxCell>

        <!-- ================= PROCESSES (Ovals / Ellipses) ================= -->
        <!-- Process 4.1 -->
        <mxCell id="p4_1" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;4.1&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Registrar Login &amp;amp;&lt;br/&gt;Authentication&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="120" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- Process 4.2 -->
        <mxCell id="p4_2" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;4.2&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Student Admission &amp;amp;&lt;br/&gt;Registration&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="270" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- Process 4.3 -->
        <mxCell id="p4_3" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;4.3&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Grade &amp;amp; Section&lt;br/&gt;Class Assignment&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="430" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- Process 4.4 -->
        <mxCell id="p4_4" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;4.4&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Student Search &amp;amp;&lt;br/&gt;Demographic View&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="580" width="160" height="100" as="geometry" />
        </mxCell>

        <!-- Process 4.5 -->
        <mxCell id="p4_5" value="&lt;b style=&quot;font-size: 14px;&quot;&gt;4.5&lt;/b&gt;&lt;br/&gt;&lt;b&gt;Registrar Profile &amp;amp;&lt;br/&gt;Password Update&lt;/b&gt;" style="''' + STYLE_PROCESS + '''" vertex="1" parent="1">
          <mxGeometry x="380" y="730" width="160" height="100" as="geometry" />
        </mxCell>


        <!-- ================= DATA STORES (Two Parallel Horizontal Lines) ================= -->
        <!-- D1: registrar_office -->
        <mxCell id="ds_reg" value="&lt;b&gt;D1&lt;/b&gt; | registrar_office (Staff Credentials &amp;amp; Employee Details)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="145" width="340" height="46" as="geometry" />
        </mxCell>

        <!-- D2: student -->
        <mxCell id="ds_stud" value="&lt;b&gt;D2&lt;/b&gt; | student (Admitted Student Records, Parents &amp;amp; Contacts)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="295" width="340" height="46" as="geometry" />
        </mxCell>

        <!-- D3: grades & section & class -->
        <mxCell id="ds_class" value="&lt;b&gt;D3&lt;/b&gt; | grades &amp;amp; section &amp;amp; class (Available Tiers &amp;amp; Divisions)" style="''' + STYLE_DATASTORE + '''" vertex="1" parent="1">
          <mxGeometry x="840" y="455" width="340" height="46" as="geometry" />
        </mxCell>


        <!-- ================= DATA FLOWS (Directed Solid Arrows) ================= -->
        <!-- Flow: Registrar -> 4.1 Auth -->
        <mxCell id="f_reg_p4_1" value="Staff Credentials (username, password)" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_reg" target="p4_1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="280" y="400" />
              <mxPoint x="280" y="170" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 4.1 <-> D1 -->
        <mxCell id="f_p4_1_d1" value="Verify Credentials &amp;amp; Establish Session" style="''' + STYLE_FLOW_BIDIR + '''" edge="1" parent="1" source="p4_1" target="ds_reg">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: 4.1 -> Registrar Dashboard -->
        <mxCell id="f_p4_1_reg" value="Registrar Dashboard Access" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p4_1" target="ent_reg">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="300" y="190" />
              <mxPoint x="300" y="420" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Registrar -> 4.2 Admission -->
        <mxCell id="f_reg_p4_2" value="New Student Data (fname, lname, DOB, parents, email)" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_reg" target="p4_2">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="260" y="430" />
              <mxPoint x="260" y="320" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 4.2 -> D2 -->
        <mxCell id="f_p4_2_d2" value="Insert New Student Record into student Table" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p4_2" target="ds_stud">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: 4.2 -> Registrar Confirmation -->
        <mxCell id="f_p4_2_reg" value="Admission Success &amp;amp; Student ID Created" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p4_2" target="ent_reg">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="290" y="340" />
              <mxPoint x="290" y="440" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: D2 -> New Student Entity -->
        <mxCell id="f_d2_stud" value="Admission Notice &amp;amp; Login Credentials" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_stud" target="ent_student">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- Flow: Registrar -> 4.3 Class Assign -->
        <mxCell id="f_reg_p4_3" value="Assign Grade &amp;amp; Section to Student" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_reg" target="p4_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: D3 -> 4.3 -->
        <mxCell id="f_d3_p4_3" value="Fetch Active Grades &amp;amp; Section Options" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ds_class" target="p4_3">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <!-- Flow: 4.3 -> D2 -->
        <mxCell id="f_p4_3_d2" value="Update Student Grade &amp;amp; Section FK" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p4_3" target="ds_stud">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="750" y="480" />
              <mxPoint x="750" y="325" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 4.3 -> Registrar -->
        <mxCell id="f_p4_3_reg" value="Class Allocation Confirmed" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p4_3" target="ent_reg">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="280" y="475" />
              <mxPoint x="280" y="465" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Registrar -> 4.4 Search -->
        <mxCell id="f_reg_p4_4" value="Search Student by Name or ID" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_reg" target="p4_4">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="260" y="470" />
              <mxPoint x="260" y="630" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: D2 <-> 4.4 -->
        <mxCell id="f_d2_p4_4" value="Query Demographics &amp;amp; Roster" style="''' + STYLE_FLOW_BIDIR + '''" edge="1" parent="1" source="ds_stud" target="p4_4">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="720" y="340" />
              <mxPoint x="720" y="630" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 4.4 -> Registrar -->
        <mxCell id="f_p4_4_reg" value="Display Student Profile &amp;amp; Search Results" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p4_4" target="ent_reg">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="290" y="650" />
              <mxPoint x="290" y="485" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- Flow: Registrar -> 4.5 Password -->
        <mxCell id="f_reg_p4_5" value="Change Password Request (old, new)" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="ent_reg" target="p4_5">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="240" y="485" />
              <mxPoint x="240" y="780" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 4.5 -> D1 -->
        <mxCell id="f_p4_5_d1" value="Update Password in registrar_office" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p4_5" target="ds_reg">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="750" y="780" />
              <mxPoint x="750" y="160" />
            </Array>
          </mxGeometry>
        </mxCell>
        <!-- Flow: 4.5 -> Registrar Success -->
        <mxCell id="f_p4_5_reg" value="Password Updated Successfully" style="''' + STYLE_FLOW + '''" edge="1" parent="1" source="p4_5" target="ent_reg">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="220" y="800" />
              <mxPoint x="220" y="490" />
            </Array>
          </mxGeometry>
        </mxCell>

        <!-- ================= DFD SHAPE LEGEND ================= -->
        <mxCell id="legend_box" value="" style="rounded=1;arcSize=4;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#CBD5E1;strokeWidth=1.5;" vertex="1" parent="1">
          <mxGeometry x="50" y="980" width="1550" height="70" as="geometry" />
        </mxCell>
        <mxCell id="leg_title" value="&lt;b&gt;DFD SHAPES USED IN THIS DIAGRAM (Standard Reference)&lt;/b&gt;" style="text;html=1;align=center;verticalAlign=middle;fontSize=12;fontColor=#0F172A;" vertex="1" parent="legend_box">
          <mxGeometry x="10" y="2" width="1530" height="20" as="geometry" />
        </mxCell>
        <mxCell id="leg_ent" value="External Entity" style="''' + STYLE_ENTITY + '''fontSize=10;" vertex="1" parent="legend_box">
          <mxGeometry x="120" y="26" width="100" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_ent_desc" value="&lt;b&gt;Rectangle:&lt;/b&gt; Source/Sink of data" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="230" y="26" width="200" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_proc" value="Process" style="''' + STYLE_PROCESS + '''fontSize=10;" vertex="1" parent="legend_box">
          <mxGeometry x="510" y="24" width="80" height="38" as="geometry" />
        </mxCell>
        <mxCell id="leg_proc_desc" value="&lt;b&gt;Oval:&lt;/b&gt; Transforms inputs to outputs" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="600" y="26" width="220" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_ds" value="Data Store" style="''' + STYLE_DATASTORE + '''fontSize=10;" vertex="1" parent="legend_box">
          <mxGeometry x="890" y="28" width="100" height="30" as="geometry" />
        </mxCell>
        <mxCell id="leg_ds_desc" value="&lt;b&gt;Parallel Lines:&lt;/b&gt; DB Table / Storage" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="1000" y="26" width="220" height="34" as="geometry" />
        </mxCell>
        <mxCell id="leg_flow" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=classic;strokeColor=#1E293B;strokeWidth=2;" edge="1" parent="legend_box">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="1290" y="43" as="sourcePoint" />
            <mxPoint x="1360" y="43" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="leg_flow_desc" value="&lt;b&gt;Solid Arrow:&lt;/b&gt; Movement of data" style="text;html=1;fontSize=11;align=left;verticalAlign=middle;" vertex="1" parent="legend_box">
          <mxGeometry x="1380" y="26" width="180" height="34" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml


# SVG Generators for direct viewing in browser & embedding in Markdown
def generate_admin_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1650 1150" width="100%" height="100%" style="background:#ffffff; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.15" />
    </filter>
    <marker id="arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b" />
    </marker>
    <marker id="arr-blue" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563eb" />
    </marker>
  </defs>

  <!-- Title Banner -->
  <rect x="50" y="20" width="1550" height="48" rx="8" fill="#1e293b" />
  <text x="825" y="42" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">DATA FLOW DIAGRAM (DFD): ADMIN MODULE — SCHOOL MANAGEMENT SYSTEM</text>
  <text x="825" y="58" fill="#94a3b8" font-size="11" text-anchor="middle">Notation Standard: External Entity (Rectangle) | Process (Oval) | Data Store (Two Parallel Lines) | Data Flow (Solid Arrow)</text>

  <!-- External Entities (Rectangles) -->
  <!-- Admin -->
  <rect x="50" y="380" width="160" height="110" fill="#ebf3fb" stroke="#2563eb" stroke-width="2" filter="url(#shadow)" />
  <text x="130" y="415" fill="#1e3a8a" font-size="11" font-weight="bold" text-anchor="middle">EXTERNAL ENTITY</text>
  <text x="130" y="445" fill="#0f172a" font-size="18" font-weight="bold" text-anchor="middle">Admin</text>
  <text x="130" y="470" fill="#475569" font-size="11" font-style="italic" text-anchor="middle">(School Administrator)</text>

  <!-- Public Visitor -->
  <rect x="50" y="860" width="160" height="85" fill="#f1f5f9" stroke="#475569" stroke-width="2" filter="url(#shadow)" />
  <text x="130" y="890" fill="#334155" font-size="11" font-weight="bold" text-anchor="middle">EXTERNAL ENTITY</text>
  <text x="130" y="915" fill="#0f172a" font-size="14" font-weight="bold" text-anchor="middle">Public / Visitor</text>
  <text x="130" y="933" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">(Inquiry Sender)</text>

  <!-- Teacher Entity -->
  <rect x="1440" y="310" width="160" height="80" fill="#f1f5f9" stroke="#475569" stroke-width="2" filter="url(#shadow)" />
  <text x="1520" y="338" fill="#334155" font-size="11" font-weight="bold" text-anchor="middle">EXTERNAL ENTITY</text>
  <text x="1520" y="360" fill="#0f172a" font-size="14" font-weight="bold" text-anchor="middle">Teacher Staff</text>
  <text x="1520" y="377" fill="#64748b" font-size="10" font-style="italic" text-anchor="middle">(Receives Credentials)</text>

  <!-- Registrar Entity -->
  <rect x="1440" y="470" width="160" height="80" fill="#f1f5f9" stroke="#475569" stroke-width="2" filter="url(#shadow)" />
  <text x="1520" y="498" fill="#334155" font-size="11" font-weight="bold" text-anchor="middle">EXTERNAL ENTITY</text>
  <text x="1520" y="520" fill="#0f172a" font-size="14" font-weight="bold" text-anchor="middle">Registrar Staff</text>
  <text x="1520" y="537" fill="#64748b" font-size="10" font-style="italic" text-anchor="middle">(Receives Credentials)</text>

  <!-- Processes (Ovals) -->
  <!-- 1.1 -->
  <ellipse cx="435" cy="150" rx="75" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="435" y="140" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">1.1</text>
  <text x="435" y="160" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Admin Login &amp;</text>
  <text x="435" y="176" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Authentication</text>

  <!-- 1.2 -->
  <ellipse cx="435" cy="290" rx="75" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="435" y="280" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">1.2</text>
  <text x="435" y="300" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">School Settings</text>
  <text x="435" y="316" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Configuration</text>

  <!-- 1.3 -->
  <ellipse cx="435" cy="430" rx="75" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="435" y="420" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">1.3</text>
  <text x="435" y="440" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Teacher Account &amp;</text>
  <text x="435" y="456" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Subject Assign</text>

  <!-- 1.4 -->
  <ellipse cx="435" cy="570" rx="75" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="435" y="560" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">1.4</text>
  <text x="435" y="580" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Registrar Staff</text>
  <text x="435" y="596" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Account Setup</text>

  <!-- 1.5 -->
  <ellipse cx="435" cy="710" rx="75" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="435" y="700" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">1.5</text>
  <text x="435" y="720" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Academic Structure</text>
  <text x="435" y="736" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">(Grades &amp; Sections)</text>

  <!-- 1.6 -->
  <ellipse cx="435" cy="840" rx="75" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="435" y="830" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">1.6</text>
  <text x="435" y="850" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Course &amp; Subject</text>
  <text x="435" y="866" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Curriculum Setup</text>

  <!-- 1.7 -->
  <ellipse cx="435" cy="970" rx="75" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="435" y="960" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">1.7</text>
  <text x="435" y="980" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Feedback Inquiries</text>
  <text x="435" y="996" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">&amp; Message Review</text>

  <!-- Data Stores (Two Parallel Horizontal Lines) -->
  <!-- D1 -->
  <g transform="translate(840, 125)">
    <line x1="0" y1="0" x2="310" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="310" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="155" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D1 | admin (Admin Logins &amp; Profiles)</text>
  </g>
  <!-- D2 -->
  <g transform="translate(840, 265)">
    <line x1="0" y1="0" x2="310" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="310" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="155" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D2 | setting (School Name, Term, Year)</text>
  </g>
  <!-- D3 -->
  <g transform="translate(840, 405)">
    <line x1="0" y1="0" x2="310" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="310" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="155" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D3 | teacher (Faculty Roster &amp; Classes)</text>
  </g>
  <!-- D4 -->
  <g transform="translate(840, 545)">
    <line x1="0" y1="0" x2="310" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="310" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="155" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D4 | registrar_office (Registrar Staff)</text>
  </g>
  <!-- D5 -->
  <g transform="translate(840, 685)">
    <line x1="0" y1="0" x2="310" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="310" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="155" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D5 | grades &amp; section &amp; class</text>
  </g>
  <!-- D6 -->
  <g transform="translate(840, 815)">
    <line x1="0" y1="0" x2="310" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="310" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="155" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D6 | subjects &amp; courses (Curriculum)</text>
  </g>
  <!-- D7 -->
  <g transform="translate(840, 945)">
    <line x1="0" y1="0" x2="310" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="310" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="155" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D7 | message (Inquiries &amp; Feedback)</text>
  </g>

  <!-- Connectors / Data Flows -->
  <!-- Admin to 1.1 -->
  <path d="M 210 400 L 270 400 L 270 150 L 360 150" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="235" y="160" width="115" height="18" fill="#ffffff" rx="3" />
  <text x="240" y="173" font-size="10" fill="#0f172a">Admin Credentials</text>

  <!-- 1.1 to D1 -->
  <path d="M 510 148 L 840 148" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="620" y="138" width="130" height="18" fill="#ffffff" rx="3" />
  <text x="625" y="151" font-size="10" fill="#1e3a8a">Validate &amp; Session</text>

  <!-- 1.1 to Admin -->
  <path d="M 370 175 L 290 175 L 290 420 L 210 420" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="390" width="105" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="403" font-size="10" fill="#0f172a">Dashboard Token</text>

  <!-- Admin to 1.2 -->
  <path d="M 210 435 L 260 435 L 260 290 L 360 290" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="225" y="270" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="230" y="283" font-size="10" fill="#0f172a">School Name &amp; Term</text>

  <!-- 1.2 to D2 -->
  <path d="M 510 288 L 840 288" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="630" y="278" width="115" height="18" fill="#ffffff" rx="3" />
  <text x="635" y="291" font-size="10" fill="#1e3a8a">Save System Settings</text>

  <!-- Admin to 1.3 -->
  <path d="M 210 440 L 360 430" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="225" y="415" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="230" y="428" font-size="10" fill="#0f172a">Teacher Data &amp; Class</text>

  <!-- 1.3 to D3 -->
  <path d="M 510 428 L 840 428" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="625" y="418" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="630" y="431" font-size="10" fill="#1e3a8a">Manage Teacher Data</text>

  <!-- D3 to Teacher Entity -->
  <path d="M 1150 428 L 1280 428 L 1280 350 L 1440 350" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="1270" y="375" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="1275" y="388" font-size="10" fill="#0f172a">Credentials Notice</text>

  <!-- Admin to 1.4 -->
  <path d="M 210 460 L 260 460 L 260 570 L 360 570" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="220" y="540" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="225" y="553" font-size="10" fill="#0f172a">Registrar Staff Info</text>

  <!-- 1.4 to D4 -->
  <path d="M 510 568 L 840 568" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="620" y="558" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="625" y="571" font-size="10" fill="#1e3a8a">Create Registrar User</text>

  <!-- D4 to Registrar Entity -->
  <path d="M 1150 568 L 1280 568 L 1280 510 L 1440 510" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="1270" y="530" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="1275" y="543" font-size="10" fill="#0f172a">Account Provisioned</text>

  <!-- Admin to 1.5 -->
  <path d="M 210 475 L 250 475 L 250 710 L 360 710" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="220" y="680" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="225" y="693" font-size="10" fill="#0f172a">Grades &amp; Sections</text>

  <!-- 1.5 to D5 -->
  <path d="M 510 708 L 840 708" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="630" y="698" width="115" height="18" fill="#ffffff" rx="3" />
  <text x="635" y="711" font-size="10" fill="#1e3a8a">Update Classrooms</text>

  <!-- Admin to 1.6 -->
  <path d="M 210 485 L 230 485 L 230 840 L 360 840" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="220" y="810" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="225" y="823" font-size="10" fill="#0f172a">Course Code &amp; Title</text>

  <!-- 1.6 to D6 -->
  <path d="M 510 838 L 840 838" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="625" y="828" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="630" y="841" font-size="10" fill="#1e3a8a">Write Course Catalog</text>

  <!-- Visitor to 1.7 -->
  <path d="M 210 902 L 280 902 L 280 970 L 360 970" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="930" width="115" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="943" font-size="10" fill="#0f172a">Inquiry / Feedback</text>

  <!-- 1.7 to D7 -->
  <path d="M 510 968 L 840 968" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="625" y="958" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="630" y="971" font-size="10" fill="#1e3a8a">Record Message Log</text>

  <!-- D7 to 1.7 to Admin -->
  <path d="M 370 990 L 210 990 L 210 490" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="180" y="750" width="135" height="18" fill="#ffffff" rx="3" />
  <text x="185" y="763" font-size="10" fill="#0f172a">Feedback Logs to Admin</text>

  <!-- Legend Box -->
  <rect x="50" y="1050" width="1550" height="70" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
  <text x="825" y="1068" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">DFD SHAPES USED IN THIS DIAGRAM (Standard Reference Specification)</text>

  <!-- Legend Item 1 -->
  <rect x="120" y="1076" width="90" height="32" fill="#ebf3fb" stroke="#2563eb" stroke-width="2" />
  <text x="165" y="1096" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Entity</text>
  <text x="220" y="1096" font-size="11" fill="#334155"><tspan font-weight="bold">Rectangle:</tspan> External Entity (Source / Sink)</text>

  <!-- Legend Item 2 -->
  <ellipse cx="550" cy="1092" rx="40" ry="18" fill="#fffbeb" stroke="#d97706" stroke-width="2" />
  <text x="550" y="1096" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">Process</text>
  <text x="600" y="1096" font-size="11" fill="#334155"><tspan font-weight="bold">Oval:</tspan> System Process / Function</text>

  <!-- Legend Item 3 -->
  <line x1="890" y1="1080" x2="980" y2="1080" stroke="#334155" stroke-width="2.5" />
  <line x1="890" y1="1104" x2="980" y2="1104" stroke="#334155" stroke-width="2.5" />
  <text x="935" y="1096" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Data Store</text>
  <text x="995" y="1096" font-size="11" fill="#334155"><tspan font-weight="bold">Two Parallel Lines:</tspan> Database Table</text>

  <!-- Legend Item 4 -->
  <line x1="1290" y1="1092" x2="1360" y2="1092" stroke="#1e293b" stroke-width="2" marker-end="url(#arr)" />
  <text x="1375" y="1096" font-size="11" fill="#334155"><tspan font-weight="bold">Solid Arrow:</tspan> Data Flow</text>
</svg>'''

def generate_teacher_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1650 1100" width="100%" height="100%" style="background:#ffffff; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.15" />
    </filter>
    <marker id="arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b" />
    </marker>
    <marker id="arr-blue" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563eb" />
    </marker>
  </defs>

  <!-- Title Banner -->
  <rect x="50" y="20" width="1550" height="48" rx="8" fill="#1e293b" />
  <text x="825" y="42" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">DATA FLOW DIAGRAM (DFD): TEACHER MODULE — SCHOOL MANAGEMENT SYSTEM</text>
  <text x="825" y="58" fill="#94a3b8" font-size="11" text-anchor="middle">Notation Standard: External Entity (Rectangle) | Process (Oval) | Data Store (Two Parallel Lines) | Data Flow (Solid Arrow)</text>

  <!-- External Entities -->
  <rect x="50" y="380" width="160" height="110" fill="#ebf3fb" stroke="#2563eb" stroke-width="2" filter="url(#shadow)" />
  <text x="130" y="415" fill="#1e3a8a" font-size="11" font-weight="bold" text-anchor="middle">EXTERNAL ENTITY</text>
  <text x="130" y="445" fill="#0f172a" font-size="18" font-weight="bold" text-anchor="middle">Teacher</text>
  <text x="130" y="470" fill="#475569" font-size="11" font-style="italic" text-anchor="middle">(Faculty Member)</text>

  <rect x="1440" y="580" width="160" height="90" fill="#f1f5f9" stroke="#475569" stroke-width="2" filter="url(#shadow)" />
  <text x="1520" y="612" fill="#334155" font-size="11" font-weight="bold" text-anchor="middle">EXTERNAL ENTITY</text>
  <text x="1520" y="635" fill="#0f172a" font-size="14" font-weight="bold" text-anchor="middle">Student</text>
  <text x="1520" y="653" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">(Evaluated Learner)</text>

  <!-- Processes (Ovals) -->
  <!-- 2.1 -->
  <ellipse cx="460" cy="170" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="160" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">2.1</text>
  <text x="460" y="180" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Teacher Login &amp;</text>
  <text x="460" y="196" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Authentication</text>

  <!-- 2.2 -->
  <ellipse cx="460" cy="320" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="310" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">2.2</text>
  <text x="460" y="330" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">View Assigned</text>
  <text x="460" y="346" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Classes &amp; Subjects</text>

  <!-- 2.3 -->
  <ellipse cx="460" cy="470" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="460" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">2.3</text>
  <text x="460" y="480" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Student Class Roster</text>
  <text x="460" y="496" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Retrieval</text>

  <!-- 2.4 -->
  <ellipse cx="460" cy="620" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="610" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">2.4</text>
  <text x="460" y="630" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Student Marks &amp;</text>
  <text x="460" y="646" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Score Evaluation</text>

  <!-- 2.5 -->
  <ellipse cx="460" cy="780" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="770" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">2.5</text>
  <text x="460" y="790" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Teacher Profile &amp;</text>
  <text x="460" y="806" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Password Update</text>

  <!-- Data Stores (Two Parallel Lines) -->
  <!-- D1 -->
  <g transform="translate(840, 145)">
    <line x1="0" y1="0" x2="330" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="330" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="165" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D1 | teacher (Faculty Profiles &amp; Logins)</text>
  </g>
  <!-- D2 -->
  <g transform="translate(840, 295)">
    <line x1="0" y1="0" x2="330" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="330" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="165" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D2 | class &amp; subjects (Assigned Cohorts)</text>
  </g>
  <!-- D3 -->
  <g transform="translate(840, 445)">
    <line x1="0" y1="0" x2="330" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="330" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="165" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D3 | student (Enrolled Class Roster)</text>
  </g>
  <!-- D4 -->
  <g transform="translate(840, 595)">
    <line x1="0" y1="0" x2="330" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="330" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="165" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D4 | student_score (Exam Marks &amp; Grades)</text>
  </g>
  <!-- D5 -->
  <g transform="translate(840, 755)">
    <line x1="0" y1="0" x2="330" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="330" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="165" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D5 | setting (Current Year &amp; Term)</text>
  </g>

  <!-- Connectors -->
  <!-- Teacher -> 2.1 -->
  <path d="M 210 400 L 280 400 L 280 170 L 380 170" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="235" y="180" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="240" y="193" font-size="10" fill="#0f172a">Teacher Credentials</text>

  <!-- 2.1 <-> D1 -->
  <path d="M 540 168 L 840 168" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="635" y="158" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="640" y="171" font-size="10" fill="#1e3a8a">Validate Teacher Auth</text>

  <!-- 2.1 -> Teacher Dashboard -->
  <path d="M 390 190 L 300 190 L 300 420 L 210 420" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="240" y="390" width="110" height="18" fill="#ffffff" rx="3" />
  <text x="245" y="403" font-size="10" fill="#0f172a">Dashboard &amp; Profile</text>

  <!-- Teacher -> 2.2 Classes -->
  <path d="M 210 430 L 260 430 L 260 320 L 380 320" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="300" width="130" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="313" font-size="10" fill="#0f172a">Request Assigned Class</text>

  <!-- D2 -> 2.2 -->
  <path d="M 840 318 L 540 318" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="630" y="308" width="135" height="18" fill="#ffffff" rx="3" />
  <text x="635" y="321" font-size="10" fill="#1e3a8a">Retrieve Class &amp; Subjects</text>

  <!-- 2.2 -> Teacher -->
  <path d="M 390 340 L 290 340 L 290 440 L 210 440" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="360" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="373" font-size="10" fill="#0f172a">Display Assigned Class</text>

  <!-- Teacher -> 2.3 Roster -->
  <path d="M 210 450 L 380 470" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="445" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="458" font-size="10" fill="#0f172a">Select Class &amp; Section</text>

  <!-- D3 -> 2.3 -->
  <path d="M 840 468 L 540 468" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="630" y="458" width="135" height="18" fill="#ffffff" rx="3" />
  <text x="635" y="471" font-size="10" fill="#1e3a8a">Fetch Enrolled Roster</text>

  <!-- 2.3 -> Teacher -->
  <path d="M 385 490 L 280 490 L 280 465 L 210 465" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="240" y="500" width="110" height="18" fill="#ffffff" rx="3" />
  <text x="245" y="513" font-size="10" fill="#0f172a">Class Roster List</text>

  <!-- Teacher -> 2.4 Scores -->
  <path d="M 210 475 L 260 475 L 260 620 L 380 620" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="225" y="590" width="130" height="18" fill="#ffffff" rx="3" />
  <text x="230" y="603" font-size="10" fill="#0f172a">Submit Student Marks</text>

  <!-- 2.4 <-> D4 -->
  <path d="M 540 618 L 840 618" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="630" y="608" width="135" height="18" fill="#ffffff" rx="3" />
  <text x="635" y="621" font-size="10" fill="#1e3a8a">Save Marks to student_score</text>

  <!-- D5 -> 2.4 -->
  <path d="M 840 778 L 680 778 L 680 640 L 530 640" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="660" y="700" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="665" y="713" font-size="10" fill="#1e3a8a">Active Term &amp; Year</text>

  <!-- 2.4 -> Teacher Feedback -->
  <path d="M 390 640 L 290 640 L 290 485 L 210 485" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="650" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="663" font-size="10" fill="#0f172a">Score Saved Notice</text>

  <!-- D4 -> Student Entity -->
  <path d="M 1170 618 L 1440 618" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="1230" y="608" width="145" height="18" fill="#ffffff" rx="3" />
  <text x="1235" y="621" font-size="10" fill="#0f172a">Published Term Scores</text>

  <!-- Teacher -> 2.5 Password -->
  <path d="M 210 488 L 240 488 L 240 780 L 380 780" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="220" y="750" width="130" height="18" fill="#ffffff" rx="3" />
  <text x="225" y="763" font-size="10" fill="#0f172a">Change Password Req</text>

  <!-- 2.5 -> D1 -->
  <path d="M 540 780 L 750 780 L 750 170 L 840 170" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="680" y="470" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="685" y="483" font-size="10" fill="#1e3a8a">Update Password Hash</text>

  <!-- Legend -->
  <rect x="50" y="980" width="1550" height="70" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
  <text x="825" y="998" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">DFD SHAPES USED IN THIS DIAGRAM (Standard Reference Specification)</text>

  <rect x="120" y="1006" width="90" height="32" fill="#ebf3fb" stroke="#2563eb" stroke-width="2" />
  <text x="165" y="1026" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Entity</text>
  <text x="220" y="1026" font-size="11" fill="#334155"><tspan font-weight="bold">Rectangle:</tspan> External Entity (Source / Sink)</text>

  <ellipse cx="550" cy="1022" rx="40" ry="18" fill="#fffbeb" stroke="#d97706" stroke-width="2" />
  <text x="550" y="1026" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">Process</text>
  <text x="600" y="1026" font-size="11" fill="#334155"><tspan font-weight="bold">Oval:</tspan> System Process / Function</text>

  <line x1="890" y1="1010" x2="980" y2="1010" stroke="#334155" stroke-width="2.5" />
  <line x1="890" y1="1034" x2="980" y2="1034" stroke="#334155" stroke-width="2.5" />
  <text x="935" y="1026" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Data Store</text>
  <text x="995" y="1026" font-size="11" fill="#334155"><tspan font-weight="bold">Two Parallel Lines:</tspan> Database Table</text>

  <line x1="1290" y1="1022" x2="1360" y2="1022" stroke="#1e293b" stroke-width="2" marker-end="url(#arr)" />
  <text x="1375" y="1026" font-size="11" fill="#334155"><tspan font-weight="bold">Solid Arrow:</tspan> Data Flow</text>
</svg>'''

def generate_student_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1650 1100" width="100%" height="100%" style="background:#ffffff; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.15" />
    </filter>
    <marker id="arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b" />
    </marker>
    <marker id="arr-blue" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563eb" />
    </marker>
  </defs>

  <!-- Title Banner -->
  <rect x="50" y="20" width="1550" height="48" rx="8" fill="#1e293b" />
  <text x="825" y="42" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">DATA FLOW DIAGRAM (DFD): STUDENT MODULE — SCHOOL MANAGEMENT SYSTEM</text>
  <text x="825" y="58" fill="#94a3b8" font-size="11" text-anchor="middle">Notation Standard: External Entity (Rectangle) | Process (Oval) | Data Store (Two Parallel Lines) | Data Flow (Solid Arrow)</text>

  <!-- External Entities -->
  <rect x="50" y="380" width="160" height="110" fill="#ebf3fb" stroke="#2563eb" stroke-width="2" filter="url(#shadow)" />
  <text x="130" y="415" fill="#1e3a8a" font-size="11" font-weight="bold" text-anchor="middle">EXTERNAL ENTITY</text>
  <text x="130" y="445" fill="#0f172a" font-size="18" font-weight="bold" text-anchor="middle">Student</text>
  <text x="130" y="470" fill="#475569" font-size="11" font-style="italic" text-anchor="middle">(Learner / Enrollee)</text>

  <rect x="1440" y="590" width="160" height="85" fill="#f1f5f9" stroke="#475569" stroke-width="2" filter="url(#shadow)" />
  <text x="1520" y="620" fill="#334155" font-size="11" font-weight="bold" text-anchor="middle">EXTERNAL ENTITY</text>
  <text x="1520" y="642" fill="#0f172a" font-size="14" font-weight="bold" text-anchor="middle">Admin / Support</text>
  <text x="1520" y="660" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">(Receives Inquiries)</text>

  <!-- Processes (Ovals) -->
  <!-- 3.1 -->
  <ellipse cx="460" cy="170" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="160" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">3.1</text>
  <text x="460" y="180" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Student Login &amp;</text>
  <text x="460" y="196" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Authentication</text>

  <!-- 3.2 -->
  <ellipse cx="460" cy="320" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="310" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">3.2</text>
  <text x="460" y="330" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Demographic &amp;</text>
  <text x="460" y="346" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Class Enrollment</text>

  <!-- 3.3 -->
  <ellipse cx="460" cy="480" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="470" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">3.3</text>
  <text x="460" y="490" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Academic Scores &amp;</text>
  <text x="460" y="506" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Report Card View</text>

  <!-- 3.4 -->
  <ellipse cx="460" cy="630" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="620" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">3.4</text>
  <text x="460" y="640" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Submit Feedback &amp;</text>
  <text x="460" y="656" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Contact Inquiries</text>

  <!-- 3.5 -->
  <ellipse cx="460" cy="780" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="770" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">3.5</text>
  <text x="460" y="790" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Password Change &amp;</text>
  <text x="460" y="806" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Account Security</text>

  <!-- Data Stores -->
  <!-- D1 -->
  <g transform="translate(840, 145)">
    <line x1="0" y1="0" x2="340" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="340" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="170" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D1 | student (Demographics, Logins &amp; Parents)</text>
  </g>
  <!-- D2 -->
  <g transform="translate(840, 295)">
    <line x1="0" y1="0" x2="340" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="340" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="170" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D2 | class &amp; grades &amp; section</text>
  </g>
  <!-- D3 -->
  <g transform="translate(840, 445)">
    <line x1="0" y1="0" x2="340" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="340" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="170" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D3 | student_score (Term Marks &amp; Evaluations)</text>
  </g>
  <!-- D4 -->
  <g transform="translate(840, 520)">
    <line x1="0" y1="0" x2="340" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="340" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="170" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D4 | subjects (Subject Codes &amp; Titles)</text>
  </g>
  <!-- D5 -->
  <g transform="translate(840, 650)">
    <line x1="0" y1="0" x2="340" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="340" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="170" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D5 | message (Contact Messages &amp; Sender Info)</text>
  </g>

  <!-- Connectors -->
  <!-- Student to 3.1 -->
  <path d="M 210 400 L 280 400 L 280 170 L 380 170" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="235" y="180" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="240" y="193" font-size="10" fill="#0f172a">Student Credentials</text>

  <!-- 3.1 <-> D1 -->
  <path d="M 540 168 L 840 168" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="635" y="158" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="640" y="171" font-size="10" fill="#1e3a8a">Validate Student Auth</text>

  <!-- 3.1 -> Student Portal -->
  <path d="M 390 190 L 300 190 L 300 420 L 210 420" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="240" y="390" width="115" height="18" fill="#ffffff" rx="3" />
  <text x="245" y="403" font-size="10" fill="#0f172a">Student Portal Access</text>

  <!-- Student to 3.2 Profile -->
  <path d="M 210 430 L 260 430 L 260 320 L 380 320" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="300" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="313" font-size="10" fill="#0f172a">Request Student Profile</text>

  <!-- D1 -> 3.2 -->
  <path d="M 840 180 L 750 180 L 750 310 L 540 310" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="635" y="278" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="640" y="291" font-size="10" fill="#1e3a8a">Fetch Demographics</text>

  <!-- D2 -> 3.2 -->
  <path d="M 840 325 L 540 325" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="640" y="330" width="115" height="18" fill="#ffffff" rx="3" />
  <text x="645" y="343" font-size="10" fill="#1e3a8a">Fetch Class &amp; Grade</text>

  <!-- 3.2 -> Student -->
  <path d="M 390 340 L 290 340 L 290 440 L 210 440" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="360" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="373" font-size="10" fill="#0f172a">Display Profile Info</text>

  <!-- Student to 3.3 Score Card -->
  <path d="M 210 450 L 380 480" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="455" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="468" font-size="10" fill="#0f172a">Request Report Card</text>

  <!-- D3 -> 3.3 -->
  <path d="M 840 468 L 540 468" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="635" y="458" width="130" height="18" fill="#ffffff" rx="3" />
  <text x="640" y="471" font-size="10" fill="#1e3a8a">Fetch Exam Marks (ID)</text>

  <!-- D4 -> 3.3 -->
  <path d="M 840 540 L 710 540 L 710 495 L 540 495" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="660" y="525" width="115" height="18" fill="#ffffff" rx="3" />
  <text x="665" y="538" font-size="10" fill="#1e3a8a">Subject Code &amp; Name</text>

  <!-- 3.3 -> Student -->
  <path d="M 385 505 L 280 505 L 280 465 L 210 465" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="235" y="515" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="240" y="528" font-size="10" fill="#0f172a">Display Grade Sheet</text>

  <!-- Student to 3.4 Contact -->
  <path d="M 210 475 L 260 475 L 260 630 L 380 630" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="225" y="600" width="130" height="18" fill="#ffffff" rx="3" />
  <text x="230" y="613" font-size="10" fill="#0f172a">Send Inquiry Message</text>

  <!-- 3.4 -> D5 -->
  <path d="M 540 640 L 680 640 L 680 673 L 840 673" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="635" y="630" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="640" y="643" font-size="10" fill="#1e3a8a">Write to message Table</text>

  <!-- 3.4 -> Student Feedback -->
  <path d="M 390 650 L 290 650 L 290 485 L 210 485" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="660" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="673" font-size="10" fill="#0f172a">Submission Received</text>

  <!-- D5 -> Admin Support -->
  <path d="M 1180 673 L 1300 673 L 1300 632 L 1440 632" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="1270" y="640" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="1275" y="653" font-size="10" fill="#0f172a">Inquiry to Admin</text>

  <!-- Student to 3.5 Password -->
  <path d="M 210 488 L 240 488 L 240 780 L 380 780" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="220" y="750" width="130" height="18" fill="#ffffff" rx="3" />
  <text x="225" y="763" font-size="10" fill="#0f172a">Change Password Req</text>

  <!-- 3.5 -> D1 -->
  <path d="M 540 780 L 750 780 L 750 160 L 840 160" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="680" y="470" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="685" y="483" font-size="10" fill="#1e3a8a">Update Encrypted Hash</text>

  <!-- Legend -->
  <rect x="50" y="980" width="1550" height="70" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
  <text x="825" y="998" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">DFD SHAPES USED IN THIS DIAGRAM (Standard Reference Specification)</text>

  <rect x="120" y="1006" width="90" height="32" fill="#ebf3fb" stroke="#2563eb" stroke-width="2" />
  <text x="165" y="1026" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Entity</text>
  <text x="220" y="1026" font-size="11" fill="#334155"><tspan font-weight="bold">Rectangle:</tspan> External Entity (Source / Sink)</text>

  <ellipse cx="550" cy="1022" rx="40" ry="18" fill="#fffbeb" stroke="#d97706" stroke-width="2" />
  <text x="550" y="1026" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">Process</text>
  <text x="600" y="1026" font-size="11" fill="#334155"><tspan font-weight="bold">Oval:</tspan> System Process / Function</text>

  <line x1="890" y1="1010" x2="980" y2="1010" stroke="#334155" stroke-width="2.5" />
  <line x1="890" y1="1034" x2="980" y2="1034" stroke="#334155" stroke-width="2.5" />
  <text x="935" y="1026" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Data Store</text>
  <text x="995" y="1026" font-size="11" fill="#334155"><tspan font-weight="bold">Two Parallel Lines:</tspan> Database Table</text>

  <line x1="1290" y1="1022" x2="1360" y2="1022" stroke="#1e293b" stroke-width="2" marker-end="url(#arr)" />
  <text x="1375" y="1026" font-size="11" fill="#334155"><tspan font-weight="bold">Solid Arrow:</tspan> Data Flow</text>
</svg>'''

def generate_registrar_svg():
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1650 1100" width="100%" height="100%" style="background:#ffffff; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.15" />
    </filter>
    <marker id="arr" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#1e293b" />
    </marker>
    <marker id="arr-blue" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563eb" />
    </marker>
  </defs>

  <!-- Title Banner -->
  <rect x="50" y="20" width="1550" height="48" rx="8" fill="#1e293b" />
  <text x="825" y="42" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">DATA FLOW DIAGRAM (DFD): REGISTRAR OFFICE MODULE — SCHOOL MANAGEMENT SYSTEM</text>
  <text x="825" y="58" fill="#94a3b8" font-size="11" text-anchor="middle">Notation Standard: External Entity (Rectangle) | Process (Oval) | Data Store (Two Parallel Lines) | Data Flow (Solid Arrow)</text>

  <!-- External Entities -->
  <rect x="50" y="380" width="160" height="110" fill="#ebf3fb" stroke="#2563eb" stroke-width="2" filter="url(#shadow)" />
  <text x="130" y="415" fill="#1e3a8a" font-size="11" font-weight="bold" text-anchor="middle">EXTERNAL ENTITY</text>
  <text x="130" y="445" fill="#0f172a" font-size="18" font-weight="bold" text-anchor="middle">Registrar</text>
  <text x="130" y="470" fill="#475569" font-size="11" font-style="italic" text-anchor="middle">(Admissions &amp; Records)</text>

  <rect x="1440" y="275" width="160" height="90" fill="#f1f5f9" stroke="#475569" stroke-width="2" filter="url(#shadow)" />
  <text x="1520" y="305" fill="#334155" font-size="11" font-weight="bold" text-anchor="middle">EXTERNAL ENTITY</text>
  <text x="1520" y="328" fill="#0f172a" font-size="14" font-weight="bold" text-anchor="middle">New Student</text>
  <text x="1520" y="347" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">(Receives Enrollment)</text>

  <!-- Processes (Ovals) -->
  <!-- 4.1 -->
  <ellipse cx="460" cy="170" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="160" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">4.1</text>
  <text x="460" y="180" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Registrar Login &amp;</text>
  <text x="460" y="196" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Authentication</text>

  <!-- 4.2 -->
  <ellipse cx="460" cy="320" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="310" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">4.2</text>
  <text x="460" y="330" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Student Admission &amp;</text>
  <text x="460" y="346" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Registration</text>

  <!-- 4.3 -->
  <ellipse cx="460" cy="480" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="470" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">4.3</text>
  <text x="460" y="490" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Grade &amp; Section</text>
  <text x="460" y="506" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Class Assignment</text>

  <!-- 4.4 -->
  <ellipse cx="460" cy="630" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="620" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">4.4</text>
  <text x="460" y="640" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Student Search &amp;</text>
  <text x="460" y="656" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Demographic View</text>

  <!-- 4.5 -->
  <ellipse cx="460" cy="780" rx="80" ry="50" fill="#fffbeb" stroke="#d97706" stroke-width="2" filter="url(#shadow)" />
  <text x="460" y="770" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">4.5</text>
  <text x="460" y="790" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Registrar Profile &amp;</text>
  <text x="460" y="806" fill="#78350f" font-size="12" font-weight="bold" text-anchor="middle">Password Update</text>

  <!-- Data Stores -->
  <!-- D1 -->
  <g transform="translate(840, 145)">
    <line x1="0" y1="0" x2="340" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="340" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="170" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D1 | registrar_office (Staff Credentials)</text>
  </g>
  <!-- D2 -->
  <g transform="translate(840, 295)">
    <line x1="0" y1="0" x2="340" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="340" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="170" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D2 | student (Admissions &amp; Demographics)</text>
  </g>
  <!-- D3 -->
  <g transform="translate(840, 455)">
    <line x1="0" y1="0" x2="340" y2="0" stroke="#334155" stroke-width="2.5" />
    <line x1="0" y1="46" x2="340" y2="46" stroke="#334155" stroke-width="2.5" />
    <text x="170" y="28" fill="#0f172a" font-size="13" font-weight="bold" text-anchor="middle">D3 | grades &amp; section &amp; class</text>
  </g>

  <!-- Connectors -->
  <!-- Registrar to 4.1 -->
  <path d="M 210 400 L 280 400 L 280 170 L 380 170" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="235" y="180" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="240" y="193" font-size="10" fill="#0f172a">Registrar Credentials</text>

  <!-- 4.1 <-> D1 -->
  <path d="M 540 168 L 840 168" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="630" y="158" width="130" height="18" fill="#ffffff" rx="3" />
  <text x="635" y="171" font-size="10" fill="#1e3a8a">Validate Registrar Auth</text>

  <!-- 4.1 -> Dashboard -->
  <path d="M 390 190 L 300 190 L 300 420 L 210 420" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="240" y="390" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="245" y="403" font-size="10" fill="#0f172a">Registrar Dashboard</text>

  <!-- Registrar to 4.2 Admission -->
  <path d="M 210 430 L 260 430 L 260 320 L 380 320" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="300" width="130" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="313" font-size="10" fill="#0f172a">New Student Data Entry</text>

  <!-- 4.2 -> D2 -->
  <path d="M 540 318 L 840 318" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="630" y="308" width="135" height="18" fill="#ffffff" rx="3" />
  <text x="635" y="321" font-size="10" fill="#1e3a8a">Insert into student Table</text>

  <!-- 4.2 -> Registrar Confirmation -->
  <path d="M 390 340 L 290 340 L 290 440 L 210 440" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="360" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="373" font-size="10" fill="#0f172a">Admission Confirmed</text>

  <!-- D2 -> New Student Entity -->
  <path d="M 1180 318 L 1440 318" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="1245" y="308" width="140" height="18" fill="#ffffff" rx="3" />
  <text x="1250" y="321" font-size="10" fill="#0f172a">Student Login Created</text>

  <!-- Registrar to 4.3 Class Assign -->
  <path d="M 210 450 L 380 480" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="455" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="468" font-size="10" fill="#0f172a">Assign Class &amp; Section</text>

  <!-- D3 -> 4.3 -->
  <path d="M 840 478 L 540 478" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="630" y="468" width="135" height="18" fill="#ffffff" rx="3" />
  <text x="635" y="481" font-size="10" fill="#1e3a8a">Fetch Grade &amp; Section</text>

  <!-- 4.3 -> D2 -->
  <path d="M 500 440 L 750 440 L 750 330 L 840 330" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="670" y="380" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="675" y="393" font-size="10" fill="#1e3a8a">Update Class in student</text>

  <!-- 4.3 -> Registrar -->
  <path d="M 385 505 L 280 505 L 280 465 L 210 465" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="235" y="515" width="120" height="18" fill="#ffffff" rx="3" />
  <text x="240" y="528" font-size="10" fill="#0f172a">Assignment Complete</text>

  <!-- Registrar to 4.4 Search -->
  <path d="M 210 475 L 260 475 L 260 630 L 380 630" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="225" y="600" width="130" height="18" fill="#ffffff" rx="3" />
  <text x="230" y="613" font-size="10" fill="#0f172a">Search Student by Name</text>

  <!-- D2 <-> 4.4 -->
  <path d="M 840 340 L 720 340 L 720 630 L 540 630" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="645" y="570" width="130" height="18" fill="#ffffff" rx="3" />
  <text x="650" y="583" font-size="10" fill="#1e3a8a">Query Student Demog</text>

  <!-- 4.4 -> Registrar -->
  <path d="M 390 650 L 290 650 L 290 485 L 210 485" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="230" y="660" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="235" y="673" font-size="10" fill="#0f172a">Display Search List</text>

  <!-- Registrar to 4.5 Password -->
  <path d="M 210 488 L 240 488 L 240 780 L 380 780" fill="none" stroke="#1e293b" stroke-width="1.5" marker-end="url(#arr)" />
  <rect x="220" y="750" width="130" height="18" fill="#ffffff" rx="3" />
  <text x="225" y="763" font-size="10" fill="#0f172a">Change Password Req</text>

  <!-- 4.5 -> D1 -->
  <path d="M 540 780 L 750 780 L 750 160 L 840 160" fill="none" stroke="#2563eb" stroke-width="1.5" marker-end="url(#arr-blue)" />
  <rect x="680" y="470" width="125" height="18" fill="#ffffff" rx="3" />
  <text x="685" y="483" font-size="10" fill="#1e3a8a">Update Staff Password</text>

  <!-- Legend -->
  <rect x="50" y="980" width="1550" height="70" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
  <text x="825" y="998" fill="#0f172a" font-size="12" font-weight="bold" text-anchor="middle">DFD SHAPES USED IN THIS DIAGRAM (Standard Reference Specification)</text>

  <rect x="120" y="1006" width="90" height="32" fill="#ebf3fb" stroke="#2563eb" stroke-width="2" />
  <text x="165" y="1026" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Entity</text>
  <text x="220" y="1026" font-size="11" fill="#334155"><tspan font-weight="bold">Rectangle:</tspan> External Entity (Source / Sink)</text>

  <ellipse cx="550" cy="1022" rx="40" ry="18" fill="#fffbeb" stroke="#d97706" stroke-width="2" />
  <text x="550" y="1026" font-size="10" font-weight="bold" fill="#78350f" text-anchor="middle">Process</text>
  <text x="600" y="1026" font-size="11" fill="#334155"><tspan font-weight="bold">Oval:</tspan> System Process / Function</text>

  <line x1="890" y1="1010" x2="980" y2="1010" stroke="#334155" stroke-width="2.5" />
  <line x1="890" y1="1034" x2="980" y2="1034" stroke="#334155" stroke-width="2.5" />
  <text x="935" y="1026" font-size="10" font-weight="bold" fill="#0f172a" text-anchor="middle">Data Store</text>
  <text x="995" y="1026" font-size="11" fill="#334155"><tspan font-weight="bold">Two Parallel Lines:</tspan> Database Table</text>

  <line x1="1290" y1="1022" x2="1360" y2="1022" stroke="#1e293b" stroke-width="2" marker-end="url(#arr)" />
  <text x="1375" y="1026" font-size="11" fill="#334155"><tspan font-weight="bold">Solid Arrow:</tspan> Data Flow</text>
</svg>'''

def generate_interactive_viewer():
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Module-Specific DFD Interactive Viewer | School Management System</title>
  <style>
    :root {
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --bg: #0f172a;
      --card-bg: #1e293b;
      --text: #f8fafc;
      --text-muted: #94a3b8;
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
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }
    header {
      background: var(--card-bg);
      padding: 16px 28px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #334155;
      gap: 16px;
    }
    .title-area h1 {
      font-size: 1.25rem;
      font-weight: 700;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .badge {
      background: rgba(37, 99, 235, 0.2);
      color: #60a5fa;
      border: 1px solid #2563eb;
      padding: 2px 8px;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 600;
    }
    .title-area p {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 4px;
    }
    .tabs {
      display: flex;
      gap: 8px;
      background: #0f172a;
      padding: 4px;
      border-radius: 8px;
      border: 1px solid #334155;
    }
    .tab-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .tab-btn:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.05);
    }
    .tab-btn.active {
      background: var(--primary);
      color: #ffffff;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    .actions {
      display: flex;
      gap: 10px;
    }
    .btn {
      background: #334155;
      color: #ffffff;
      border: none;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      text-decoration: none;
      transition: all 0.2s;
    }
    .btn:hover {
      background: #475569;
    }
    .btn-primary {
      background: var(--primary);
    }
    .btn-primary:hover {
      background: var(--primary-dark);
    }
    main {
      flex: 1;
      padding: 20px;
      display: flex;
      flex-direction: column;
    }
    .diagram-container {
      flex: 1;
      background: #ffffff;
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
      position: relative;
    }
    .diagram-panel {
      width: 100%;
      height: 100%;
      min-height: 820px;
      display: none;
      padding: 20px;
    }
    .diagram-panel.active {
      display: block;
    }
    .diagram-panel img, .diagram-panel object {
      width: 100%;
      height: 100%;
      min-height: 800px;
      display: block;
    }
    footer {
      background: var(--card-bg);
      padding: 12px 28px;
      font-size: 0.8rem;
      color: var(--text-muted);
      border-top: 1px solid #334155;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }
    .legend-chips {
      display: flex;
      gap: 16px;
      align-items: center;
    }
    .chip {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .chip-shape {
      display: inline-block;
      width: 14px;
      height: 14px;
      border-radius: 2px;
    }
    .chip-rect {
      background: #ebf3fb;
      border: 1.5px solid #2563eb;
    }
    .chip-oval {
      background: #fffbeb;
      border: 1.5px solid #d97706;
      border-radius: 50%;
    }
    .chip-lines {
      height: 8px;
      border-top: 2px solid #334155;
      border-bottom: 2px solid #334155;
    }
  </style>
</head>
<body>

  <header>
    <div class="title-area">
      <h1>School Management System — Module DFDs <span class="badge">Standard Compliance</span></h1>
      <p>Interactive Data Flow Diagrams for all 4 System Modules | Shapes: Entity (Rectangle), Process (Oval), Data Store (Parallel Lines)</p>
    </div>

    <div class="tabs">
      <button class="tab-btn active" onclick="switchTab('admin')">1. Admin Module</button>
      <button class="tab-btn" onclick="switchTab('teacher')">2. Teacher Module</button>
      <button class="tab-btn" onclick="switchTab('student')">3. Student Module</button>
      <button class="tab-btn" onclick="switchTab('registrar')">4. Registrar Module</button>
    </div>

    <div class="actions">
      <a id="download-drawio" href="admin.drawio" download class="btn btn-primary">
        <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
        Download .drawio
      </a>
      <a id="download-svg" href="admin_dfd.svg" download class="btn">
        <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
        Download SVG
      </a>
    </div>
  </header>

  <main>
    <div class="diagram-container">
      <div id="panel-admin" class="diagram-panel active">
        <object data="admin_dfd.svg" type="image/svg+xml"></object>
      </div>
      <div id="panel-teacher" class="diagram-panel">
        <object data="teacher_dfd.svg" type="image/svg+xml"></object>
      </div>
      <div id="panel-student" class="diagram-panel">
        <object data="student_dfd.svg" type="image/svg+xml"></object>
      </div>
      <div id="panel-registrar" class="diagram-panel">
        <object data="registrar_dfd.svg" type="image/svg+xml"></object>
      </div>
    </div>
  </main>

  <footer>
    <div class="legend-chips">
      <span class="chip"><span class="chip-shape chip-rect"></span> Rectangle: External Entity</span>
      <span class="chip"><span class="chip-shape chip-oval"></span> Oval: System Process</span>
      <span class="chip"><span class="chip-shape chip-lines"></span> Parallel Lines: Data Store</span>
      <span class="chip">&rarr; Solid Arrow: Data Flow</span>
    </div>
    <div>
      Editable in diagrams.net / Draw.io / VS Code extension
    </div>
  </footer>

  <script>
    function switchTab(mod) {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.diagram-panel').forEach(p => p.classList.remove('active'));

      event.target.classList.add('active');
      document.getElementById('panel-' + mod).classList.add('active');

      document.getElementById('download-drawio').href = mod + '.drawio';
      document.getElementById('download-drawio').setAttribute('download', mod + '.drawio');
      document.getElementById('download-svg').href = mod + '_dfd.svg';
      document.getElementById('download-svg').setAttribute('download', mod + '_dfd.svg');
    }
  </script>
</body>
</html>'''
    return html_content


def main():
    workspace = r"c:\xampp\htdocs\school-management"
    print(f"Generating module-specific DFDs in: {workspace}")

    # 1. Admin Draw.io
    admin_xml = generate_admin_drawio()
    with open(os.path.join(workspace, "admin.drawio"), "w", encoding="utf-8") as f:
        f.write(admin_xml)
    # Also write admin.drowio
    with open(os.path.join(workspace, "admin.drowio"), "w", encoding="utf-8") as f:
        f.write(admin_xml)
    print("[OK] Created admin.drawio and admin.drowio")

    # 2. Teacher Draw.io
    teacher_xml = generate_teacher_drawio()
    with open(os.path.join(workspace, "teacher.drawio"), "w", encoding="utf-8") as f:
        f.write(teacher_xml)
    with open(os.path.join(workspace, "teacher.drowio"), "w", encoding="utf-8") as f:
        f.write(teacher_xml)
    print("[OK] Created teacher.drawio and teacher.drowio")

    # 3. Student Draw.io
    student_xml = generate_student_drawio()
    with open(os.path.join(workspace, "student.drawio"), "w", encoding="utf-8") as f:
        f.write(student_xml)
    with open(os.path.join(workspace, "student.drowio"), "w", encoding="utf-8") as f:
        f.write(student_xml)
    print("[OK] Created student.drawio and student.drowio")

    # 4. Registrar Draw.io
    registrar_xml = generate_registrar_drawio()
    with open(os.path.join(workspace, "registrar.drawio"), "w", encoding="utf-8") as f:
        f.write(registrar_xml)
    with open(os.path.join(workspace, "registrar.drowio"), "w", encoding="utf-8") as f:
        f.write(registrar_xml)
    # Also copy as registarar.drowio (matching user spelling)
    with open(os.path.join(workspace, "registarar.drowio"), "w", encoding="utf-8") as f:
        f.write(registrar_xml)
    print("[OK] Created registrar.drawio, registrar.drowio, and registarar.drowio")

    # 5. SVGs
    with open(os.path.join(workspace, "admin_dfd.svg"), "w", encoding="utf-8") as f:
        f.write(generate_admin_svg())
    with open(os.path.join(workspace, "teacher_dfd.svg"), "w", encoding="utf-8") as f:
        f.write(generate_teacher_svg())
    with open(os.path.join(workspace, "student_dfd.svg"), "w", encoding="utf-8") as f:
        f.write(generate_student_svg())
    with open(os.path.join(workspace, "registrar_dfd.svg"), "w", encoding="utf-8") as f:
        f.write(generate_registrar_svg())
    print("[OK] Created high-res SVGs for all 4 modules")

    # 6. Interactive HTML Viewer
    with open(os.path.join(workspace, "dfd_modules_viewer.html"), "w", encoding="utf-8") as f:
        f.write(generate_interactive_viewer())
    print("[OK] Created dfd_modules_viewer.html")

if __name__ == "__main__":
    main()
