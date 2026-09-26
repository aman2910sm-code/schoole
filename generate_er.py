#!/usr/bin/env python3
"""
ER Diagram Generator for School Management System and Reference E-Commerce Diagram.
Strictly conforms to the attached ER diagram symbol guide (Peter Chen ER Notation):
- Entity: Rectangle
- Relationship: Diamond
- Attribute: Oval / Ellipse
- Primary Key Attribute: Underlined text in Oval / Ellipse
- Connecting Line: Solid line
- Directed Line: Directed arrow
"""

import os
import xml.etree.ElementTree as ET

def build_er_drawio_xml():
    xml = '''<mxfile host="app.diagrams.net" modified="2026-09-26T00:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <!-- ========================================================================= -->
  <!-- TAB 1: SCHOOL MANAGEMENT SYSTEM ER DIAGRAM (sms_db)                       -->
  <!-- ========================================================================= -->
  <diagram id="sms-er-diagram" name="School Management System ERD">
    <mxGraphModel dx="2000" dy="1400" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2400" pageHeight="1800" background="#FFFFFF" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Title Banner -->
        <mxCell id="title_sms" value="ENTITY-RELATIONSHIP (ER) DIAGRAM: SCHOOL MANAGEMENT SYSTEM (sms_db)&#xa;Notation: Chen's ER Notation | Entities (Rectangles), Relationships (Diamonds), Attributes (Ovals), PKs (Underlined)" style="shape=rectangle;fillColor=#1E293B;strokeColor=#0F172A;fontColor=#FFFFFF;fontStyle=1;fontSize=18;align=center;verticalAlign=middle;rounded=1;arcSize=6;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="20" width="2280" height="50" as="geometry" />
        </mxCell>

        <!-- ================= ENTITY: ADMIN ================= -->
        <mxCell id="ent_admin" value="ADMIN" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=15;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="300" y="260" width="160" height="65" as="geometry" />
        </mxCell>
        <!-- Admin Attributes -->
        <mxCell id="att_admin_id" value="&lt;u&gt;admin_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#1E3A8A;align=center;" vertex="1" parent="1">
          <mxGeometry x="130" y="190" width="95" height="38" as="geometry" />
        </mxCell>
        <mxCell id="att_admin_user" value="username" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="240" y="150" width="85" height="35" as="geometry" />
        </mxCell>
        <mxCell id="att_admin_pass" value="password" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="340" y="150" width="85" height="35" as="geometry" />
        </mxCell>
        <mxCell id="att_admin_fname" value="fname" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="130" y="260" width="80" height="35" as="geometry" />
        </mxCell>
        <mxCell id="att_admin_lname" value="lname" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="130" y="315" width="80" height="35" as="geometry" />
        </mxCell>
        <!-- Lines: Admin Attributes -->
        <mxCell id="line_adm_1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_admin" target="att_admin_id"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_adm_2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_admin" target="att_admin_user"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_adm_3" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_admin" target="att_admin_pass"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_adm_4" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_admin" target="att_admin_fname"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_adm_5" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_admin" target="att_admin_lname"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ================= ENTITY: SETTING ================= -->
        <mxCell id="ent_setting" value="SETTING" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=14;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="580" y="100" width="150" height="55" as="geometry" />
        </mxCell>
        <!-- Setting Attributes -->
        <mxCell id="att_set_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="1">
          <mxGeometry x="490" y="30" width="75" height="35" as="geometry" />
        </mxCell>
        <mxCell id="att_set_name" value="school_name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="580" y="25" width="95" height="35" as="geometry" />
        </mxCell>
        <mxCell id="att_set_slogan" value="slogan" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="690" y="25" width="80" height="35" as="geometry" />
        </mxCell>
        <mxCell id="att_set_year" value="current_year" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="760" y="70" width="95" height="35" as="geometry" />
        </mxCell>
        <mxCell id="att_set_sem" value="current_semester" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="760" y="120" width="115" height="35" as="geometry" />
        </mxCell>
        <!-- Lines: Setting Attributes -->
        <mxCell id="line_set_1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_setting" target="att_set_id"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_set_2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_setting" target="att_set_name"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_set_3" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_setting" target="att_set_slogan"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_set_4" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_setting" target="att_set_year"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_set_5" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_setting" target="att_set_sem"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Admin Configures Setting (1:1) -->
        <mxCell id="rel_configures" value="Configures" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="325" y="100" width="110" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_cfg_1" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_admin" target="rel_configures"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_rel_cfg_2" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_configures" target="ent_setting"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ================= ENTITY: MESSAGE ================= -->
        <mxCell id="ent_message" value="MESSAGE" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=14;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="70" y="500" width="150" height="55" as="geometry" />
        </mxCell>
        <!-- Message Attributes -->
        <mxCell id="att_msg_id" value="&lt;u&gt;message_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="1">
          <mxGeometry x="20" y="420" width="95" height="36" as="geometry" />
        </mxCell>
        <mxCell id="att_msg_sender" value="sender_full_name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=10;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="10" y="585" width="110" height="35" as="geometry" />
        </mxCell>
        <mxCell id="att_msg_email" value="sender_email" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=10;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="130" y="590" width="95" height="35" as="geometry" />
        </mxCell>
        <mxCell id="att_msg_txt" value="message" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="10" y="475" width="75" height="35" as="geometry" />
        </mxCell>
        <mxCell id="att_msg_time" value="date_time" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="230" y="525" width="80" height="35" as="geometry" />
        </mxCell>
        <!-- Lines: Message Attributes -->
        <mxCell id="line_msg_1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_message" target="att_msg_id"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_msg_2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_message" target="att_msg_sender"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_msg_3" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_message" target="att_msg_email"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_msg_4" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_message" target="att_msg_txt"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_msg_5" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_message" target="att_msg_time"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Admin Reviews Message (1:N) -->
        <mxCell id="rel_reviews" value="Reviews" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="200" y="390" width="100" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_rev_1" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_admin" target="rel_reviews"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_rel_rev_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_reviews" target="ent_message"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ================= ENTITY: TEACHER ================= -->
        <mxCell id="ent_teacher" value="TEACHER" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=15;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="580" y="510" width="160" height="65" as="geometry" />
        </mxCell>
        <!-- Teacher Attributes -->
        <mxCell id="att_tch_id" value="&lt;u&gt;teacher_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="1">
          <mxGeometry x="430" y="490" width="95" height="36" as="geometry" />
        </mxCell>
        <mxCell id="att_tch_user" value="username" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="430" y="535" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_tch_pass" value="password" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="430" y="580" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_tch_fname" value="fname" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="470" y="630" width="75" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_tch_lname" value="lname" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="555" y="630" width="75" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_tch_emp" value="employee_no" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="640" y="630" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_tch_qual" value="qualification" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="745" y="630" width="90" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_tch_phone" value="phone_number" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="760" y="580" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_tch_email" value="email_address" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="760" y="535" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_tch_gender" value="gender" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="760" y="490" width="75" height="34" as="geometry" />
        </mxCell>
        <!-- Lines: Teacher Attributes -->
        <mxCell id="line_tch_1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_teacher" target="att_tch_id"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_tch_2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_teacher" target="att_tch_user"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_tch_3" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_teacher" target="att_tch_pass"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_tch_4" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_teacher" target="att_tch_fname"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_tch_5" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_teacher" target="att_tch_lname"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_tch_6" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_teacher" target="att_tch_emp"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_tch_7" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_teacher" target="att_tch_qual"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_tch_8" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_teacher" target="att_tch_phone"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_tch_9" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_teacher" target="att_tch_email"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_tch_10" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_teacher" target="att_tch_gender"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Admin Manages Teacher (1:N) -->
        <mxCell id="rel_manages_tch" value="Manages" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="460" y="380" width="100" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_mt_1" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_admin" target="rel_manages_tch"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_rel_mt_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_manages_tch" target="ent_teacher"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ================= ENTITY: REGISTRAR_OFFICE ================= -->
        <mxCell id="ent_registrar" value="REGISTRAR_OFFICE" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=14;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1600" y="260" width="180" height="65" as="geometry" />
        </mxCell>
        <!-- Registrar Attributes -->
        <mxCell id="att_reg_id" value="&lt;u&gt;r_user_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="1">
          <mxGeometry x="1815" y="190" width="95" height="36" as="geometry" />
        </mxCell>
        <mxCell id="att_reg_user" value="username" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1815" y="240" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_reg_pass" value="password" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1815" y="285" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_reg_fname" value="fname" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1815" y="330" width="75" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_reg_lname" value="lname" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1815" y="375" width="75" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_reg_emp" value="employee_no" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1710" y="160" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_reg_qual" value="qualification" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1600" y="160" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_reg_phone" value="phone_number" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1490" y="160" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_reg_email" value="email_address" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1490" y="210" width="95" height="34" as="geometry" />
        </mxCell>
        <!-- Lines: Registrar Attributes -->
        <mxCell id="line_reg_1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_registrar" target="att_reg_id"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_reg_2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_registrar" target="att_reg_user"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_reg_3" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_registrar" target="att_reg_pass"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_reg_4" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_registrar" target="att_reg_fname"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_reg_5" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_registrar" target="att_reg_lname"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_reg_6" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_registrar" target="att_reg_emp"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_reg_7" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_registrar" target="att_reg_qual"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_reg_8" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_registrar" target="att_reg_phone"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_reg_9" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_registrar" target="att_reg_email"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Admin Supervises Registrar (1:N) -->
        <mxCell id="rel_supervises" value="Supervises" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1000" y="265" width="110" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_sup_1" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_admin" target="rel_supervises"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_rel_sup_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_supervises" target="ent_registrar"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ================= ENTITY: STUDENT ================= -->
        <mxCell id="ent_student" value="STUDENT" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=15;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1300" y="510" width="160" height="65" as="geometry" />
        </mxCell>
        <!-- Student Attributes -->
        <mxCell id="att_stu_id" value="&lt;u&gt;student_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="1">
          <mxGeometry x="1335" y="425" width="95" height="36" as="geometry" />
        </mxCell>
        <mxCell id="att_stu_user" value="username" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1225" y="425" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_stu_pass" value="password" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1125" y="435" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_stu_fname" value="fname" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1485" y="485" width="75" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_stu_lname" value="lname" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1485" y="535" width="75" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_stu_gender" value="gender" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1485" y="585" width="75" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_stu_email" value="email_address" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1485" y="635" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_stu_addr" value="address" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1380" y="665" width="75" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_stu_dob" value="date_of_birth" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1275" y="665" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_stu_parent_fname" value="parent_fname" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1165" y="665" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_stu_parent_phone" value="parent_phone" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1115" y="615" width="95" height="34" as="geometry" />
        </mxCell>
        <!-- Lines: Student Attributes -->
        <mxCell id="line_stu_1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_student" target="att_stu_id"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_stu_2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_student" target="att_stu_user"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_stu_3" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_student" target="att_stu_pass"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_stu_4" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_student" target="att_stu_fname"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_stu_5" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_student" target="att_stu_lname"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_stu_6" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_student" target="att_stu_gender"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_stu_7" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_student" target="att_stu_email"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_stu_8" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_student" target="att_stu_addr"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_stu_9" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_student" target="att_stu_dob"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_stu_10" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_student" target="att_stu_parent_fname"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_stu_11" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_student" target="att_stu_parent_phone"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Registrar Admits Student (1:N) -->
        <mxCell id="rel_admits" value="Admits" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1470" y="380" width="100" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_adm_1" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_registrar" target="rel_admits"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_rel_adm_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_admits" target="ent_student"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ================= ENTITY: CLASS ================= -->
        <mxCell id="ent_class" value="CLASS" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=15;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="950" y="850" width="150" height="60" as="geometry" />
        </mxCell>
        <mxCell id="att_cls_id" value="&lt;u&gt;class_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="1">
          <mxGeometry x="980" y="770" width="90" height="36" as="geometry" />
        </mxCell>
        <mxCell id="line_cls_1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_class" target="att_cls_id"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Student Enrolled_In Class (N:1) -->
        <mxCell id="rel_enrolled_cls" value="Enrolled_In" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1140" y="690" width="100" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_ec_1" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_student" target="rel_enrolled_cls"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_rel_ec_2" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_enrolled_cls" target="ent_class"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Teacher Teaches Class (N:M or 1:N) -->
        <mxCell id="rel_teaches" value="Teaches" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="780" y="690" width="100" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_tc_1" value="M" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_teacher" target="rel_teaches"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_rel_tc_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_teaches" target="ent_class"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ================= ENTITY: GRADE ================= -->
        <mxCell id="ent_grade" value="GRADE" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=15;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="580" y="1150" width="150" height="60" as="geometry" />
        </mxCell>
        <!-- Grade Attributes -->
        <mxCell id="att_grd_id" value="&lt;u&gt;grade_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="1">
          <mxGeometry x="440" y="1150" width="90" height="36" as="geometry" />
        </mxCell>
        <mxCell id="att_grd_name" value="grade" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="450" y="1210" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_grd_code" value="grade_code" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="550" y="1250" width="90" height="34" as="geometry" />
        </mxCell>
        <mxCell id="line_grd_1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_grade" target="att_grd_id"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_grd_2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_grade" target="att_grd_name"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_grd_3" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_grade" target="att_grd_code"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Class Comprises Grade (N:1) -->
        <mxCell id="rel_class_grade" value="Comprises" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="760" y="1000" width="110" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_cg_1" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_class" target="rel_class_grade"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_rel_cg_2" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_class_grade" target="ent_grade"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ================= ENTITY: SECTION ================= -->
        <mxCell id="ent_section" value="SECTION" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=15;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1320" y="1150" width="150" height="60" as="geometry" />
        </mxCell>
        <!-- Section Attributes -->
        <mxCell id="att_sec_id" value="&lt;u&gt;section_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="1">
          <mxGeometry x="1510" y="1150" width="90" height="36" as="geometry" />
        </mxCell>
        <mxCell id="att_sec_name" value="section" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1480" y="1210" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="line_sec_1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_section" target="att_sec_id"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_sec_2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_section" target="att_sec_name"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Class Divides Section (N:1) -->
        <mxCell id="rel_class_sec" value="Divides" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1150" y="1000" width="100" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_cs_1" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_class" target="rel_class_sec"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_rel_cs_2" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_class_sec" target="ent_section"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- ================= ENTITY: SUBJECTS ================= -->
        <mxCell id="ent_subjects" value="SUBJECTS" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=15;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="580" y="1450" width="150" height="60" as="geometry" />
        </mxCell>
        <!-- Subject Attributes -->
        <mxCell id="att_sbj_id" value="&lt;u&gt;subject_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="1">
          <mxGeometry x="430" y="1450" width="95" height="36" as="geometry" />
        </mxCell>
        <mxCell id="att_sbj_name" value="subject" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="440" y="1505" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_sbj_code" value="subject_code" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="550" y="1550" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="line_sbj_1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_subjects" target="att_sbj_id"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_sbj_2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_subjects" target="att_sbj_name"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_sbj_3" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_subjects" target="att_sbj_code"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Grade Curriculum_Of Subjects (1:N) -->
        <mxCell id="rel_grade_sbj" value="Curriculum_Of" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="595" y="1300" width="120" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_gs_1" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_grade" target="rel_grade_sbj"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_rel_gs_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_grade_sbj" target="ent_subjects"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Teacher Instructs Subjects (1:N) -->
        <mxCell id="rel_tch_sbj" value="Instructs" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="360" y="980" width="100" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_ts_1" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_teacher" target="rel_tch_sbj">
          <mxGeometry relative="1" as="geometry">
            <Array as="points"><mxPoint x="410" y="542" /></Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="line_rel_ts_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_tch_sbj" target="ent_subjects">
          <mxGeometry relative="1" as="geometry">
            <Array as="points"><mxPoint x="410" y="1480" /></Array>
          </mxGeometry>
        </mxCell>


        <!-- ================= ENTITY: STUDENT_SCORE ================= -->
        <mxCell id="ent_score" value="STUDENT_SCORE" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=15;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1300" y="1450" width="170" height="65" as="geometry" />
        </mxCell>
        <!-- Score Attributes -->
        <mxCell id="att_scr_id" value="&lt;u&gt;id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="1">
          <mxGeometry x="1510" y="1450" width="70" height="36" as="geometry" />
        </mxCell>
        <mxCell id="att_scr_sem" value="semester" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1500" y="1505" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_scr_year" value="year" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1410" y="1550" width="75" height="34" as="geometry" />
        </mxCell>
        <mxCell id="att_scr_res" value="results" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="1">
          <mxGeometry x="1290" y="1550" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="line_scr_1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_score" target="att_scr_id"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_scr_2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_score" target="att_scr_sem"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_scr_3" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_score" target="att_scr_year"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_scr_4" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="1" source="ent_score" target="att_scr_res"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Subjects Assessed_In Score (1:N) -->
        <mxCell id="rel_sbj_score" value="Assessed_In" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="965" y="1455" width="110" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_ss_1" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_subjects" target="rel_sbj_score"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="line_rel_ss_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_sbj_score" target="ent_score"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Student Receives Score (1:N) -->
        <mxCell id="rel_stu_score" value="Receives" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="1650" y="980" width="100" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_sts_1" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_student" target="rel_stu_score">
          <mxGeometry relative="1" as="geometry">
            <Array as="points"><mxPoint x="1700" y="542" /></Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="line_rel_sts_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_stu_score" target="ent_score">
          <mxGeometry relative="1" as="geometry">
            <Array as="points"><mxPoint x="1700" y="1482" /></Array>
          </mxGeometry>
        </mxCell>

        <!-- Relationship: Teacher Evaluates Score (1:N) -->
        <mxCell id="rel_tch_score" value="Evaluates" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="1">
          <mxGeometry x="975" y="1155" width="100" height="55" as="geometry" />
        </mxCell>
        <mxCell id="line_rel_tsr_1" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="ent_teacher" target="rel_tch_score">
          <mxGeometry relative="1" as="geometry">
            <Array as="points"><mxPoint x="880" y="542" /><mxPoint x="880" y="1182" /></Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="line_rel_tsr_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="1" source="rel_tch_score" target="ent_score">
          <mxGeometry relative="1" as="geometry">
            <Array as="points"><mxPoint x="1025" y="1410" /><mxPoint x="1385" y="1410" /></Array>
          </mxGeometry>
        </mxCell>


        <!-- ================= LEGEND BOX (Chen ER Notation) ================= -->
        <mxCell id="legend_box" value="" style="group;" vertex="1" connectable="0" parent="1">
          <mxGeometry x="60" y="1650" width="2280" height="110" as="geometry" />
        </mxCell>
        <mxCell id="leg_bg" value="" style="rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#CBD5E1;strokeWidth=1.5;" vertex="1" parent="legend_box">
          <mxGeometry x="0" y="0" width="2280" height="110" as="geometry" />
        </mxCell>
        <mxCell id="leg_hdr" value="&lt;b&gt;ER DIAGRAM SYMBOLS LEGEND (COMPLIANT WITH SPECIFICATION)&lt;/b&gt;" style="text;html=1;fontSize=13;fontColor=#1E293B;" vertex="1" parent="legend_box">
          <mxGeometry x="20" y="10" width="600" height="20" as="geometry" />
        </mxCell>
        <!-- Leg 1: Entity -->
        <mxCell id="leg_ent" value="Entity" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2;fontStyle=1;fontSize=11;align=center;" vertex="1" parent="legend_box">
          <mxGeometry x="30" y="45" width="110" height="45" as="geometry" />
        </mxCell>
        <mxCell id="leg_ent_t" value="&lt;b&gt;Entity (Rectangle):&lt;/b&gt;&lt;br/&gt;Real-world object or table (e.g. STUDENT, TEACHER)" style="text;html=1;fontSize=10;fontColor=#475569;" vertex="1" parent="legend_box">
          <mxGeometry x="150" y="45" width="240" height="45" as="geometry" />
        </mxCell>
        <!-- Leg 2: Relationship -->
        <mxCell id="leg_rel" value="Relationship" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=11;align=center;" vertex="1" parent="legend_box">
          <mxGeometry x="420" y="40" width="110" height="55" as="geometry" />
        </mxCell>
        <mxCell id="leg_rel_t" value="&lt;b&gt;Relationship (Diamond):&lt;/b&gt;&lt;br/&gt;Association between entities (e.g. Admits, Teaches)" style="text;html=1;fontSize=10;fontColor=#475569;" vertex="1" parent="legend_box">
          <mxGeometry x="540" y="45" width="240" height="45" as="geometry" />
        </mxCell>
        <!-- Leg 3: Attribute -->
        <mxCell id="leg_att" value="Attribute" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;align=center;" vertex="1" parent="legend_box">
          <mxGeometry x="810" y="47" width="90" height="40" as="geometry" />
        </mxCell>
        <mxCell id="leg_att_t" value="&lt;b&gt;Attribute (Oval):&lt;/b&gt;&lt;br/&gt;Property or characteristic (e.g. username, email)" style="text;html=1;fontSize=10;fontColor=#475569;" vertex="1" parent="legend_box">
          <mxGeometry x="910" y="45" width="230" height="45" as="geometry" />
        </mxCell>
        <!-- Leg 4: PK Attribute -->
        <mxCell id="leg_pk" value="&lt;u&gt;user_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;align=center;" vertex="1" parent="legend_box">
          <mxGeometry x="1170" y="47" width="90" height="40" as="geometry" />
        </mxCell>
        <mxCell id="leg_pk_t" value="&lt;b&gt;Primary Key (Underlined Oval):&lt;/b&gt;&lt;br/&gt;Unique entity identifier (e.g. &lt;u&gt;student_id&lt;/u&gt;, &lt;u&gt;admin_id&lt;/u&gt;)" style="text;html=1;fontSize=10;fontColor=#475569;" vertex="1" parent="legend_box">
          <mxGeometry x="1270" y="45" width="250" height="45" as="geometry" />
        </mxCell>
        <!-- Leg 5: Connecting Line -->
        <mxCell id="leg_line" style="endArrow=none;strokeColor=#475569;strokeWidth=2;" edge="1" parent="legend_box">
          <mxGeometry relative="1" as="geometry"><mxPoint x="1560" y="67" as="sourcePoint" /><mxPoint x="1650" y="67" as="targetPoint" /></mxGeometry>
        </mxCell>
        <mxCell id="leg_line_t" value="&lt;b&gt;Connecting Line:&lt;/b&gt;&lt;br/&gt;Connects entity to attribute or relationship" style="text;html=1;fontSize=10;fontColor=#475569;" vertex="1" parent="legend_box">
          <mxGeometry x="1660" y="45" width="230" height="45" as="geometry" />
        </mxCell>
        <!-- Leg 6: Cardinality -->
        <mxCell id="leg_card" value="1 : N" style="rounded=1;arcSize=20;fillColor=#E2E8F0;strokeColor=#94A3B8;strokeWidth=1;fontStyle=1;fontSize=11;align=center;" vertex="1" parent="legend_box">
          <mxGeometry x="1920" y="50" width="60" height="35" as="geometry" />
        </mxCell>
        <mxCell id="leg_card_t" value="&lt;b&gt;Cardinality Ratio:&lt;/b&gt;&lt;br/&gt;1:1, 1:N, M:N relationship participation" style="text;html=1;fontSize=10;fontColor=#475569;" vertex="1" parent="legend_box">
          <mxGeometry x="1990" y="45" width="220" height="45" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>


  <!-- ========================================================================= -->
  <!-- TAB 2: REFERENCE E-COMMERCE ER DIAGRAM (From Image Examples)               -->
  <!-- ========================================================================= -->
  <diagram id="ecommerce-er-diagram" name="Reference E-Commerce ERD">
    <mxGraphModel dx="1600" dy="1100" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1800" pageHeight="1200" background="#FFFFFF" math="0" shadow="0">
      <root>
        <mxCell id="ec_0" />
        <mxCell id="ec_1" parent="ec_0" />

        <!-- Title Banner -->
        <mxCell id="ec_title" value="REFERENCE E-COMMERCE ER DIAGRAM (BASED ON IMAGE EXAMPLES)&#xa;Entities: User, Products, Orders, Cart | Relationships: Manages_Cart, Contains_Item, Places_Order" style="shape=rectangle;fillColor=#1E293B;strokeColor=#0F172A;fontColor=#FFFFFF;fontStyle=1;fontSize=16;align=center;verticalAlign=middle;rounded=1;arcSize=6;shadow=1;" vertex="1" parent="ec_1">
          <mxGeometry x="60" y="20" width="1680" height="50" as="geometry" />
        </mxCell>

        <!-- Entity: User -->
        <mxCell id="ec_ent_user" value="USER" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=15;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="ec_1">
          <mxGeometry x="250" y="260" width="160" height="65" as="geometry" />
        </mxCell>
        <!-- User Attributes -->
        <mxCell id="ec_att_uid" value="&lt;u&gt;user_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#1E3A8A;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="90" y="200" width="95" height="38" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_uname" value="name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="100" y="260" width="80" height="35" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_uemail" value="email" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="100" y="315" width="80" height="35" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_upass" value="password" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="200" y="160" width="85" height="35" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_uaddr" value="address" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="310" y="160" width="85" height="35" as="geometry" />
        </mxCell>
        <mxCell id="ec_line_u1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_user" target="ec_att_uid"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_u2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_user" target="ec_att_uname"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_u3" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_user" target="ec_att_uemail"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_u4" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_user" target="ec_att_upass"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_u5" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_user" target="ec_att_uaddr"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- Entity: Cart -->
        <mxCell id="ec_ent_cart" value="CART" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=15;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="ec_1">
          <mxGeometry x="800" y="260" width="160" height="65" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_cid" value="&lt;u&gt;cart_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="780" y="170" width="85" height="35" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_cdate" value="created_at" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="890" y="170" width="85" height="35" as="geometry" />
        </mxCell>
        <mxCell id="ec_line_c1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_cart" target="ec_att_cid"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_c2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_cart" target="ec_att_cdate"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: User Manages_Cart Cart (1:1) -->
        <mxCell id="ec_rel_mc" value="Manages_Cart" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="ec_1">
          <mxGeometry x="520" y="265" width="130" height="55" as="geometry" />
        </mxCell>
        <mxCell id="ec_line_mc_1" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="ec_1" source="ec_ent_user" target="ec_rel_mc"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_mc_2" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="ec_1" source="ec_rel_mc" target="ec_ent_cart"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- Entity: Products -->
        <mxCell id="ec_ent_prod" value="PRODUCTS" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=15;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="ec_1">
          <mxGeometry x="1350" y="260" width="160" height="65" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_pid" value="&lt;u&gt;product_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="1560" y="200" width="95" height="36" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_pname" value="name" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="1560" y="250" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_pprice" value="price" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="1560" y="295" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_pdesc" value="description" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="1560" y="340" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_pstock" value="stock" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="1450" y="160" width="75" height="34" as="geometry" />
        </mxCell>
        <mxCell id="ec_line_p1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_prod" target="ec_att_pid"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_p2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_prod" target="ec_att_pname"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_p3" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_prod" target="ec_att_pprice"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_p4" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_prod" target="ec_att_pdesc"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_p5" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_prod" target="ec_att_pstock"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: Cart Contains_Item Products (M:N) -->
        <mxCell id="ec_rel_ci" value="Contains_Item" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="ec_1">
          <mxGeometry x="1080" y="265" width="130" height="55" as="geometry" />
        </mxCell>
        <!-- Attribute of Contains_Item relationship: quantity -->
        <mxCell id="ec_att_ci_qty" value="quantity" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FEF3C7;strokeColor=#D97706;strokeWidth=1.5;fontSize=11;fontColor=#92400E;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="1105" y="190" width="80" height="34" as="geometry" />
        </mxCell>
        <mxCell id="ec_line_ci_q" style="endArrow=none;strokeColor=#B45309;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_rel_ci" target="ec_att_ci_qty"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_ci_1" value="M" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="ec_1" source="ec_ent_cart" target="ec_rel_ci"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_ci_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="ec_1" source="ec_rel_ci" target="ec_ent_prod"><mxGeometry relative="1" as="geometry" /></mxCell>


        <!-- Entity: Orders -->
        <mxCell id="ec_ent_order" value="ORDERS" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#4A7BB0;strokeWidth=2.5;fontStyle=1;fontSize=15;fontColor=#0F172A;align=center;shadow=1;" vertex="1" parent="ec_1">
          <mxGeometry x="800" y="650" width="160" height="65" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_oid" value="&lt;u&gt;order_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#EFF6FF;strokeColor=#1E40AF;strokeWidth=2;fontStyle=1;fontSize=11;fontColor=#1E3A8A;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="670" y="665" width="95" height="36" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_odate" value="order_date" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="720" y="750" width="85" height="34" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_oamt" value="total_amount" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="825" y="750" width="95" height="34" as="geometry" />
        </mxCell>
        <mxCell id="ec_att_ostat" value="status" style="ellipse;whiteSpace=wrap;html=1;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=1.5;fontSize=11;fontColor=#334155;align=center;" vertex="1" parent="ec_1">
          <mxGeometry x="940" y="750" width="75" height="34" as="geometry" />
        </mxCell>
        <mxCell id="ec_line_o1" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_order" target="ec_att_oid"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_o2" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_order" target="ec_att_odate"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_o3" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_order" target="ec_att_oamt"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ec_line_o4" style="endArrow=none;strokeColor=#475569;strokeWidth=1.2;" edge="1" parent="ec_1" source="ec_ent_order" target="ec_att_ostat"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- Relationship: User Places_Order Orders (1:N) -->
        <mxCell id="ec_rel_po" value="Places_Order" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="ec_1">
          <mxGeometry x="450" y="500" width="130" height="55" as="geometry" />
        </mxCell>
        <mxCell id="ec_line_po_1" value="1" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="ec_1" source="ec_ent_user" target="ec_rel_po">
          <mxGeometry relative="1" as="geometry">
            <Array as="points"><mxPoint x="330" y="527" /></Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="ec_line_po_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="ec_1" source="ec_rel_po" target="ec_ent_order">
          <mxGeometry relative="1" as="geometry">
            <Array as="points"><mxPoint x="880" y="527" /></Array>
          </mxGeometry>
        </mxCell>

        <!-- Relationship: Orders Includes_Item Products (M:N) -->
        <mxCell id="ec_rel_ii" value="Includes_Item" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=2;fontStyle=1;fontSize=12;fontColor=#7C2D12;align=center;shadow=1;" vertex="1" parent="ec_1">
          <mxGeometry x="1190" y="500" width="130" height="55" as="geometry" />
        </mxCell>
        <mxCell id="ec_line_ii_1" value="M" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="ec_1" source="ec_ent_order" target="ec_rel_ii">
          <mxGeometry relative="1" as="geometry">
            <Array as="points"><mxPoint x="880" y="527" /></Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="ec_line_ii_2" value="N" style="endArrow=none;strokeColor=#B45309;strokeWidth=2;fontSize=13;fontStyle=1;labelBackgroundColor=#FFFFFF;" edge="1" parent="ec_1" source="ec_rel_ii" target="ec_ent_prod">
          <mxGeometry relative="1" as="geometry">
            <Array as="points"><mxPoint x="1430" y="527" /></Array>
          </mxGeometry>
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>


  <!-- ========================================================================= -->
  <!-- TAB 3: EXACT SYMBOLS TABLE RECREATED (From Attached Reference Image)     -->
  <!-- ========================================================================= -->
  <diagram id="symbols-table-diagram" name="ER Diagram Symbols Reference">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1200" pageHeight="900" background="#FFFFFF" math="0" shadow="0">
      <root>
        <mxCell id="st_0" />
        <mxCell id="st_1" parent="st_0" />

        <!-- Header -->
        <mxCell id="st_header" value="Symbols Used in the Above ER Diagram" style="shape=rectangle;fillColor=#1976D2;strokeColor=#1565C0;fontColor=#FFFFFF;fontStyle=1;fontSize=18;align=center;verticalAlign=middle;rounded=1;arcSize=6;" vertex="1" parent="st_1">
          <mxGeometry x="80" y="40" width="1040" height="50" as="geometry" />
        </mxCell>

        <!-- Table Columns Header -->
        <mxCell id="th_sym" value="Symbol" style="shape=rectangle;fillColor=#D6E4F0;strokeColor=#B0BEC5;strokeWidth=1;fontStyle=1;fontSize=14;fontColor=#0F172A;align=center;verticalAlign=middle;" vertex="1" parent="st_1">
          <mxGeometry x="80" y="90" width="220" height="40" as="geometry" />
        </mxCell>
        <mxCell id="th_name" value="Name" style="shape=rectangle;fillColor=#D6E4F0;strokeColor=#B0BEC5;strokeWidth=1;fontStyle=1;fontSize=14;fontColor=#0F172A;align=center;verticalAlign=middle;" vertex="1" parent="st_1">
          <mxGeometry x="300" y="90" width="220" height="40" as="geometry" />
        </mxCell>
        <mxCell id="th_desc" value="Description" style="shape=rectangle;fillColor=#D6E4F0;strokeColor=#B0BEC5;strokeWidth=1;fontStyle=1;fontSize=14;fontColor=#0F172A;align=center;verticalAlign=middle;" vertex="1" parent="st_1">
          <mxGeometry x="520" y="90" width="600" height="40" as="geometry" />
        </mxCell>

        <!-- Row 1: Entity -->
        <mxCell id="r1_cell1" value="" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;" vertex="1" parent="st_1"><mxGeometry x="80" y="130" width="220" height="80" as="geometry" /></mxCell>
        <mxCell id="r1_sym" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1E293B;strokeWidth=2;" vertex="1" parent="st_1"><mxGeometry x="125" y="148" width="130" height="45" as="geometry" /></mxCell>
        <mxCell id="r1_name" value="Entity" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;fontStyle=1;fontSize=14;fontColor=#0F172A;align=center;verticalAlign=middle;" vertex="1" parent="st_1"><mxGeometry x="300" y="130" width="220" height="80" as="geometry" /></mxCell>
        <mxCell id="r1_desc" value="Represents a real-world object or thing.&#xa;(e.g., User, Products, Orders)" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;fontSize=13;fontColor=#334155;align=left;spacingLeft=20;verticalAlign=middle;" vertex="1" parent="st_1"><mxGeometry x="520" y="130" width="600" height="80" as="geometry" /></mxCell>

        <!-- Row 2: Relationship -->
        <mxCell id="r2_cell1" value="" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;" vertex="1" parent="st_1"><mxGeometry x="80" y="210" width="220" height="80" as="geometry" /></mxCell>
        <mxCell id="r2_sym" value="" style="shape=rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1E293B;strokeWidth=2;" vertex="1" parent="st_1"><mxGeometry x="125" y="222" width="130" height="55" as="geometry" /></mxCell>
        <mxCell id="r2_name" value="Relationship" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;fontStyle=1;fontSize=14;fontColor=#0F172A;align=center;verticalAlign=middle;" vertex="1" parent="st_1"><mxGeometry x="300" y="210" width="220" height="80" as="geometry" /></mxCell>
        <mxCell id="r2_desc" value="Represents a relationship between two entities.&#xa;(e.g., Contains_Item, Manages_Cart)" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;fontSize=13;fontColor=#334155;align=left;spacingLeft=20;verticalAlign=middle;" vertex="1" parent="st_1"><mxGeometry x="520" y="210" width="600" height="80" as="geometry" /></mxCell>

        <!-- Row 3: Attribute -->
        <mxCell id="r3_cell1" value="" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;" vertex="1" parent="st_1"><mxGeometry x="80" y="290" width="220" height="80" as="geometry" /></mxCell>
        <mxCell id="r3_sym" value="" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1E293B;strokeWidth=2;" vertex="1" parent="st_1"><mxGeometry x="125" y="307" width="130" height="45" as="geometry" /></mxCell>
        <mxCell id="r3_name" value="Attribute" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;fontStyle=1;fontSize=14;fontColor=#0F172A;align=center;verticalAlign=middle;" vertex="1" parent="st_1"><mxGeometry x="300" y="290" width="220" height="80" as="geometry" /></mxCell>
        <mxCell id="r3_desc" value="Represents a property or characteristic of an entity.&#xa;(e.g., product_id, name, email)" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;fontSize=13;fontColor=#334155;align=left;spacingLeft=20;verticalAlign=middle;" vertex="1" parent="st_1"><mxGeometry x="520" y="290" width="600" height="80" as="geometry" /></mxCell>

        <!-- Row 4: Primary Key Attribute -->
        <mxCell id="r4_cell1" value="" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;" vertex="1" parent="st_1"><mxGeometry x="80" y="370" width="220" height="80" as="geometry" /></mxCell>
        <mxCell id="r4_sym" value="&lt;u&gt;user_id&lt;/u&gt;" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1E293B;strokeWidth=2;fontStyle=1;fontSize=13;fontColor=#0F172A;align=center;" vertex="1" parent="st_1"><mxGeometry x="125" y="387" width="130" height="45" as="geometry" /></mxCell>
        <mxCell id="r4_name" value="Primary Key Attribute" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;fontStyle=1;fontSize=14;fontColor=#0F172A;align=center;verticalAlign=middle;" vertex="1" parent="st_1"><mxGeometry x="300" y="370" width="220" height="80" as="geometry" /></mxCell>
        <mxCell id="r4_desc" value="Represents a unique identifier for an entity.&#xa;(Underlined attribute) (e.g., user_id, order_id)" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;fontSize=13;fontColor=#334155;align=left;spacingLeft=20;verticalAlign=middle;" vertex="1" parent="st_1"><mxGeometry x="520" y="370" width="600" height="80" as="geometry" /></mxCell>

        <!-- Row 5: Connecting Line -->
        <mxCell id="r5_cell1" value="" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;" vertex="1" parent="st_1"><mxGeometry x="80" y="450" width="220" height="80" as="geometry" /></mxCell>
        <mxCell id="r5_sym" style="endArrow=none;strokeColor=#1E293B;strokeWidth=2;" edge="1" parent="st_1"><mxGeometry relative="1" as="geometry"><mxPoint x="110" y="490" as="sourcePoint" /><mxPoint x="270" y="490" as="targetPoint" /></mxGeometry></mxCell>
        <mxCell id="r5_name" value="Connecting Line" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;fontStyle=1;fontSize=14;fontColor=#0F172A;align=center;verticalAlign=middle;" vertex="1" parent="st_1"><mxGeometry x="300" y="450" width="220" height="80" as="geometry" /></mxCell>
        <mxCell id="r5_desc" value="Shows the connection between an entity and its attribute&#xa;or between an entity and a relationship." style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;fontSize=13;fontColor=#334155;align=left;spacingLeft=20;verticalAlign=middle;" vertex="1" parent="st_1"><mxGeometry x="520" y="450" width="600" height="80" as="geometry" /></mxCell>

        <!-- Row 6: Directed Line -->
        <mxCell id="r6_cell1" value="" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;" vertex="1" parent="st_1"><mxGeometry x="80" y="530" width="220" height="80" as="geometry" /></mxCell>
        <mxCell id="r6_sym" style="endArrow=classic;strokeColor=#1E293B;strokeWidth=2;" edge="1" parent="st_1"><mxGeometry relative="1" as="geometry"><mxPoint x="110" y="570" as="sourcePoint" /><mxPoint x="270" y="570" as="targetPoint" /></mxGeometry></mxCell>
        <mxCell id="r6_name" value="Directed Line" style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;fontStyle=1;fontSize=14;fontColor=#0F172A;align=center;verticalAlign=middle;" vertex="1" parent="st_1"><mxGeometry x="300" y="530" width="220" height="80" as="geometry" /></mxCell>
        <mxCell id="r6_desc" value="Shows the direction of the relationship (optional,&#xa;used in some ER diagrams)." style="shape=rectangle;fillColor=#FFFFFF;strokeColor=#CFD8DC;strokeWidth=1;fontSize=13;fontColor=#334155;align=left;spacingLeft=20;verticalAlign=middle;" vertex="1" parent="st_1"><mxGeometry x="520" y="530" width="600" height="80" as="geometry" /></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml


def generate_sms_er_svg():
    """Generates an SVG for the School Management System ER Diagram."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 2400 1800" width="100%" height="100%" style="background-color: #ffffff; font-family: 'Segoe UI', Arial, Helvetica, sans-serif;">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" flood-color="#000000" />
    </filter>
  </defs>

  <!-- Title Banner -->
  <rect x="60" y="20" width="2280" height="50" rx="8" fill="#1E293B" filter="url(#shadow)"/>
  <text x="1200" y="44" fill="#FFFFFF" font-size="18" font-weight="bold" text-anchor="middle" dominant-baseline="middle">ENTITY-RELATIONSHIP (ER) DIAGRAM: SCHOOL MANAGEMENT SYSTEM (sms_db)</text>
  <text x="1200" y="60" fill="#94A3B8" font-size="12" text-anchor="middle" dominant-baseline="middle">Chen ER Notation Standard | Entities (Rectangles), Relationships (Diamonds), Attributes (Ovals), Primary Keys (Underlined)</text>

  <!-- ================= RELATIONSHIP LINES ================= -->
  <!-- Admin -> Configures -> Setting -->
  <line x1="380" y1="260" x2="380" y2="155" stroke="#B45309" stroke-width="2"/>
  <line x1="380" y1="100" x2="580" y2="127" stroke="#B45309" stroke-width="2"/>
  <rect x="365" y="235" width="20" height="18" fill="#FFFFFF"/>
  <text x="375" y="248" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>
  <rect x="540" y="105" width="20" height="18" fill="#FFFFFF"/>
  <text x="550" y="118" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>

  <!-- Admin -> Reviews -> Message -->
  <line x1="300" y1="310" x2="250" y2="390" stroke="#B45309" stroke-width="2"/>
  <line x1="250" y1="445" x2="145" y2="500" stroke="#B45309" stroke-width="2"/>
  <rect x="280" y="325" width="20" height="18" fill="#FFFFFF"/>
  <text x="290" y="338" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>
  <rect x="160" y="475" width="20" height="18" fill="#FFFFFF"/>
  <text x="170" y="488" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>

  <!-- Admin -> Manages -> Teacher -->
  <line x1="420" y1="325" x2="510" y2="380" stroke="#B45309" stroke-width="2"/>
  <line x1="510" y1="435" x2="620" y2="510" stroke="#B45309" stroke-width="2"/>
  <rect x="430" y="340" width="20" height="18" fill="#FFFFFF"/>
  <text x="440" y="353" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>
  <rect x="590" y="475" width="20" height="18" fill="#FFFFFF"/>
  <text x="600" y="488" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>

  <!-- Admin -> Supervises -> Registrar -->
  <line x1="460" y1="292" x2="1000" y2="292" stroke="#B45309" stroke-width="2"/>
  <line x1="1110" y1="292" x2="1600" y2="292" stroke="#B45309" stroke-width="2"/>
  <rect x="480" y="280" width="20" height="18" fill="#FFFFFF"/>
  <text x="490" y="293" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>
  <rect x="1560" y="280" width="20" height="18" fill="#FFFFFF"/>
  <text x="1570" y="293" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>

  <!-- Registrar -> Admits -> Student -->
  <line x1="1650" y1="325" x2="1520" y2="380" stroke="#B45309" stroke-width="2"/>
  <line x1="1520" y1="435" x2="1420" y2="510" stroke="#B45309" stroke-width="2"/>
  <rect x="1620" y="340" width="20" height="18" fill="#FFFFFF"/>
  <text x="1630" y="353" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>
  <rect x="1435" y="475" width="20" height="18" fill="#FFFFFF"/>
  <text x="1445" y="488" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>

  <!-- Teacher -> Teaches -> Class -->
  <line x1="680" y1="575" x2="830" y2="690" stroke="#B45309" stroke-width="2"/>
  <line x1="830" y1="745" x2="980" y2="850" stroke="#B45309" stroke-width="2"/>
  <rect x="700" y="605" width="20" height="18" fill="#FFFFFF"/>
  <text x="710" y="618" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">M</text>
  <rect x="945" y="815" width="20" height="18" fill="#FFFFFF"/>
  <text x="955" y="828" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>

  <!-- Student -> Enrolled_In -> Class -->
  <line x1="1340" y1="575" x2="1190" y2="690" stroke="#B45309" stroke-width="2"/>
  <line x1="1190" y1="745" x2="1060" y2="850" stroke="#B45309" stroke-width="2"/>
  <rect x="1300" y="605" width="20" height="18" fill="#FFFFFF"/>
  <text x="1310" y="618" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>
  <rect x="1080" y="815" width="20" height="18" fill="#FFFFFF"/>
  <text x="1090" y="828" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>

  <!-- Class -> Comprises -> Grade -->
  <line x1="980" y1="910" x2="815" y2="1000" stroke="#B45309" stroke-width="2"/>
  <line x1="815" y1="1055" x2="680" y2="1150" stroke="#B45309" stroke-width="2"/>
  <rect x="950" y="930" width="20" height="18" fill="#FFFFFF"/>
  <text x="960" y="943" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>
  <rect x="705" y="1120" width="20" height="18" fill="#FFFFFF"/>
  <text x="715" y="1133" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>

  <!-- Class -> Divides -> Section -->
  <line x1="1060" y1="910" x2="1200" y2="1000" stroke="#B45309" stroke-width="2"/>
  <line x1="1200" y1="1055" x2="1350" y2="1150" stroke="#B45309" stroke-width="2"/>
  <rect x="1080" y="930" width="20" height="18" fill="#FFFFFF"/>
  <text x="1090" y="943" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>
  <rect x="1310" y="1120" width="20" height="18" fill="#FFFFFF"/>
  <text x="1320" y="1133" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>

  <!-- Grade -> Curriculum_Of -> Subjects -->
  <line x1="655" y1="1210" x2="655" y2="1300" stroke="#B45309" stroke-width="2"/>
  <line x1="655" y1="1355" x2="655" y2="1450" stroke="#B45309" stroke-width="2"/>
  <rect x="660" y="1230" width="20" height="18" fill="#FFFFFF"/>
  <text x="670" y="1243" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>
  <rect x="660" y="1420" width="20" height="18" fill="#FFFFFF"/>
  <text x="670" y="1433" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>

  <!-- Teacher -> Instructs -> Subjects -->
  <path d="M 580 542 L 410 542 L 410 980" stroke="#B45309" stroke-width="2" fill="none"/>
  <path d="M 410 1035 L 410 1480 L 580 1480" stroke="#B45309" stroke-width="2" fill="none"/>
  <rect x="470" y="530" width="20" height="18" fill="#FFFFFF"/>
  <text x="480" y="543" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>
  <rect x="520" y="1470" width="20" height="18" fill="#FFFFFF"/>
  <text x="530" y="1483" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>

  <!-- Subjects -> Assessed_In -> Student_Score -->
  <line x1="730" y1="1480" x2="965" y2="1482" stroke="#B45309" stroke-width="2"/>
  <line x1="1075" y1="1482" x2="1300" y2="1480" stroke="#B45309" stroke-width="2"/>
  <rect x="750" y="1470" width="20" height="18" fill="#FFFFFF"/>
  <text x="760" y="1483" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>
  <rect x="1260" y="1470" width="20" height="18" fill="#FFFFFF"/>
  <text x="1270" y="1483" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>

  <!-- Student -> Receives -> Student_Score -->
  <path d="M 1460 542 L 1700 542 L 1700 980" stroke="#B45309" stroke-width="2" fill="none"/>
  <path d="M 1700 1035 L 1700 1482 L 1470 1482" stroke="#B45309" stroke-width="2" fill="none"/>
  <rect x="1560" y="530" width="20" height="18" fill="#FFFFFF"/>
  <text x="1570" y="543" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>
  <rect x="1530" y="1470" width="20" height="18" fill="#FFFFFF"/>
  <text x="1540" y="1483" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>

  <!-- Teacher -> Evaluates -> Student_Score -->
  <path d="M 740 542 L 880 542 L 880 1182 L 975 1182" stroke="#B45309" stroke-width="2" fill="none"/>
  <path d="M 1075 1182 L 1150 1182 L 1150 1482 L 1300 1482" stroke="#B45309" stroke-width="2" fill="none"/>
  <rect x="800" y="530" width="20" height="18" fill="#FFFFFF"/>
  <text x="810" y="543" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>
  <rect x="1210" y="1470" width="20" height="18" fill="#FFFFFF"/>
  <text x="1220" y="1483" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>


  <!-- ================= ATTRIBUTE CONNECTING LINES ================= -->
  <!-- Admin Lines -->
  <line x1="300" y1="270" x2="225" y2="209" stroke="#64748B" stroke-width="1.2"/>
  <line x1="340" y1="260" x2="282" y2="185" stroke="#64748B" stroke-width="1.2"/>
  <line x1="400" y1="260" x2="382" y2="185" stroke="#64748B" stroke-width="1.2"/>
  <line x1="300" y1="290" x2="210" y2="277" stroke="#64748B" stroke-width="1.2"/>
  <line x1="300" y1="310" x2="210" y2="332" stroke="#64748B" stroke-width="1.2"/>

  <!-- Setting Lines -->
  <line x1="580" y1="110" x2="565" y2="47" stroke="#64748B" stroke-width="1.2"/>
  <line x1="630" y1="100" x2="627" y2="60" stroke="#64748B" stroke-width="1.2"/>
  <line x1="680" y1="100" x2="730" y2="60" stroke="#64748B" stroke-width="1.2"/>
  <line x1="730" y1="115" x2="760" y2="87" stroke="#64748B" stroke-width="1.2"/>
  <line x1="730" y1="135" x2="760" y2="137" stroke="#64748B" stroke-width="1.2"/>

  <!-- Message Lines -->
  <line x1="100" y1="500" x2="67" y2="456" stroke="#64748B" stroke-width="1.2"/>
  <line x1="70" y1="510" x2="47" y2="492" stroke="#64748B" stroke-width="1.2"/>
  <line x1="90" y1="555" x2="65" y2="585" stroke="#64748B" stroke-width="1.2"/>
  <line x1="160" y1="555" x2="177" y2="590" stroke="#64748B" stroke-width="1.2"/>
  <line x1="220" y1="535" x2="230" y2="542" stroke="#64748B" stroke-width="1.2"/>

  <!-- Teacher Lines -->
  <line x1="580" y1="520" x2="525" y2="508" stroke="#64748B" stroke-width="1.2"/>
  <line x1="580" y1="540" x2="515" y2="552" stroke="#64748B" stroke-width="1.2"/>
  <line x1="580" y1="560" x2="515" y2="597" stroke="#64748B" stroke-width="1.2"/>
  <line x1="600" y1="575" x2="507" y2="630" stroke="#64748B" stroke-width="1.2"/>
  <line x1="630" y1="575" x2="592" y2="630" stroke="#64748B" stroke-width="1.2"/>
  <line x1="670" y1="575" x2="687" y2="630" stroke="#64748B" stroke-width="1.2"/>
  <line x1="710" y1="575" x2="790" y2="630" stroke="#64748B" stroke-width="1.2"/>
  <line x1="740" y1="560" x2="760" y2="597" stroke="#64748B" stroke-width="1.2"/>
  <line x1="740" y1="540" x2="760" y2="552" stroke="#64748B" stroke-width="1.2"/>
  <line x1="740" y1="520" x2="760" y2="507" stroke="#64748B" stroke-width="1.2"/>

  <!-- Registrar Lines -->
  <line x1="1780" y1="270" x2="1815" y2="208" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1780" y1="285" x2="1815" y2="257" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1780" y1="305" x2="1815" y2="302" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1780" y1="320" x2="1815" y2="347" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1750" y1="325" x2="1815" y2="392" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1730" y1="260" x2="1757" y2="194" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1670" y1="260" x2="1647" y2="194" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1620" y1="260" x2="1537" y2="194" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1600" y1="280" x2="1585" y2="227" stroke="#64748B" stroke-width="1.2"/>

  <!-- Student Lines -->
  <line x1="1380" y1="510" x2="1382" y2="461" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1330" y1="510" x2="1267" y2="459" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1300" y1="520" x2="1210" y2="452" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1460" y1="520" x2="1485" y2="502" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1460" y1="542" x2="1485" y2="552" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1460" y1="565" x2="1485" y2="602" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1440" y1="575" x2="1485" y2="652" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1400" y1="575" x2="1417" y2="665" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1340" y1="575" x2="1322" y2="665" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1300" y1="575" x2="1212" y2="665" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1300" y1="560" x2="1210" y2="632" stroke="#64748B" stroke-width="1.2"/>

  <!-- Class Lines -->
  <line x1="1025" y1="850" x2="1025" y2="806" stroke="#64748B" stroke-width="1.2"/>

  <!-- Grade Lines -->
  <line x1="580" y1="1170" x2="530" y2="1168" stroke="#64748B" stroke-width="1.2"/>
  <line x1="580" y1="1195" x2="530" y2="1227" stroke="#64748B" stroke-width="1.2"/>
  <line x1="620" y1="1210" x2="595" y2="1250" stroke="#64748B" stroke-width="1.2"/>

  <!-- Section Lines -->
  <line x1="1470" y1="1170" x2="1510" y2="1168" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1470" y1="1195" x2="1480" y2="1210" stroke="#64748B" stroke-width="1.2"/>

  <!-- Subject Lines -->
  <line x1="580" y1="1470" x2="525" y2="1468" stroke="#64748B" stroke-width="1.2"/>
  <line x1="580" y1="1495" x2="525" y2="1522" stroke="#64748B" stroke-width="1.2"/>
  <line x1="620" y1="1510" x2="597" y2="1550" stroke="#64748B" stroke-width="1.2"/>

  <!-- Score Lines -->
  <line x1="1470" y1="1470" x2="1510" y2="1468" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1470" y1="1495" x2="1500" y2="1522" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1420" y1="1515" x2="1447" y2="1550" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1350" y1="1515" x2="1330" y2="1550" stroke="#64748B" stroke-width="1.2"/>


  <!-- ================= ENTITY RECTANGLES ================= -->
  <!-- Admin -->
  <g filter="url(#shadow)">
    <rect x="300" y="260" width="160" height="65" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="380" y="298" font-size="15" font-weight="bold" fill="#0F172A" text-anchor="middle">ADMIN</text>
  </g>

  <!-- Setting -->
  <g filter="url(#shadow)">
    <rect x="580" y="100" width="150" height="55" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="655" y="133" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">SETTING</text>
  </g>

  <!-- Message -->
  <g filter="url(#shadow)">
    <rect x="70" y="500" width="150" height="55" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="145" y="533" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">MESSAGE</text>
  </g>

  <!-- Teacher -->
  <g filter="url(#shadow)">
    <rect x="580" y="510" width="160" height="65" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="660" y="548" font-size="15" font-weight="bold" fill="#0F172A" text-anchor="middle">TEACHER</text>
  </g>

  <!-- Registrar -->
  <g filter="url(#shadow)">
    <rect x="1600" y="260" width="180" height="65" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="1690" y="298" font-size="14" font-weight="bold" fill="#0F172A" text-anchor="middle">REGISTRAR_OFFICE</text>
  </g>

  <!-- Student -->
  <g filter="url(#shadow)">
    <rect x="1300" y="510" width="160" height="65" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="1380" y="548" font-size="15" font-weight="bold" fill="#0F172A" text-anchor="middle">STUDENT</text>
  </g>

  <!-- Class -->
  <g filter="url(#shadow)">
    <rect x="950" y="850" width="150" height="60" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="1025" y="886" font-size="15" font-weight="bold" fill="#0F172A" text-anchor="middle">CLASS</text>
  </g>

  <!-- Grade -->
  <g filter="url(#shadow)">
    <rect x="580" y="1150" width="150" height="60" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="655" y="1186" font-size="15" font-weight="bold" fill="#0F172A" text-anchor="middle">GRADE</text>
  </g>

  <!-- Section -->
  <g filter="url(#shadow)">
    <rect x="1320" y="1150" width="150" height="60" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="1395" y="1186" font-size="15" font-weight="bold" fill="#0F172A" text-anchor="middle">SECTION</text>
  </g>

  <!-- Subjects -->
  <g filter="url(#shadow)">
    <rect x="580" y="1450" width="150" height="60" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="655" y="1486" font-size="15" font-weight="bold" fill="#0F172A" text-anchor="middle">SUBJECTS</text>
  </g>

  <!-- Student_Score -->
  <g filter="url(#shadow)">
    <rect x="1300" y="1450" width="170" height="65" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="1385" y="1488" font-size="15" font-weight="bold" fill="#0F172A" text-anchor="middle">STUDENT_SCORE</text>
  </g>


  <!-- ================= RELATIONSHIP DIAMONDS ================= -->
  <!-- Configures -->
  <g filter="url(#shadow)">
    <polygon points="380,100 435,127 380,155 325,127" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="380" y="132" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Configures</text>
  </g>

  <!-- Reviews -->
  <g filter="url(#shadow)">
    <polygon points="250,390 300,417 250,445 200,417" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="250" y="422" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Reviews</text>
  </g>

  <!-- Manages (Teacher) -->
  <g filter="url(#shadow)">
    <polygon points="510,380 560,407 510,435 460,407" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="510" y="412" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Manages</text>
  </g>

  <!-- Supervises (Registrar) -->
  <g filter="url(#shadow)">
    <polygon points="1055,265 1110,292 1055,320 1000,292" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="1055" y="297" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Supervises</text>
  </g>

  <!-- Admits (Student) -->
  <g filter="url(#shadow)">
    <polygon points="1520,380 1570,407 1520,435 1470,407" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="1520" y="412" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Admits</text>
  </g>

  <!-- Teaches -->
  <g filter="url(#shadow)">
    <polygon points="830,690 880,717 830,745 780,717" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="830" y="722" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Teaches</text>
  </g>

  <!-- Enrolled_In -->
  <g filter="url(#shadow)">
    <polygon points="1190,690 1240,717 1190,745 1140,717" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="1190" y="722" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Enrolled_In</text>
  </g>

  <!-- Comprises -->
  <g filter="url(#shadow)">
    <polygon points="815,1000 870,1027 815,1055 760,1027" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="815" y="1032" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Comprises</text>
  </g>

  <!-- Divides -->
  <g filter="url(#shadow)">
    <polygon points="1200,1000 1250,1027 1200,1055 1150,1027" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="1200" y="1032" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Divides</text>
  </g>

  <!-- Curriculum_Of -->
  <g filter="url(#shadow)">
    <polygon points="655,1300 715,1327 655,1355 595,1327" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="655" y="1332" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Curriculum_Of</text>
  </g>

  <!-- Instructs -->
  <g filter="url(#shadow)">
    <polygon points="410,980 460,1007 410,1035 360,1007" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="410" y="1012" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Instructs</text>
  </g>

  <!-- Assessed_In -->
  <g filter="url(#shadow)">
    <polygon points="1020,1455 1075,1482 1020,1510 965,1482" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="1020" y="1487" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Assessed_In</text>
  </g>

  <!-- Receives -->
  <g filter="url(#shadow)">
    <polygon points="1700,980 1750,1007 1700,1035 1650,1007" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="1700" y="1012" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Receives</text>
  </g>

  <!-- Evaluates -->
  <g filter="url(#shadow)">
    <polygon points="1025,1155 1075,1182 1025,1210 975,1182" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="1025" y="1187" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Evaluates</text>
  </g>


  <!-- ================= ATTRIBUTE OVALS ================= -->
  <!-- Admin Attributes -->
  <g>
    <!-- admin_id (PK) -->
    <ellipse cx="177" cy="209" rx="47" ry="19" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="177" y="214" font-size="12" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">admin_id</text>
    <!-- other -->
    <ellipse cx="282" cy="167" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="282" y="171" font-size="11" fill="#334155" text-anchor="middle">username</text>
    <ellipse cx="382" cy="167" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="382" y="171" font-size="11" fill="#334155" text-anchor="middle">password</text>
    <ellipse cx="170" cy="277" rx="40" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="170" y="281" font-size="11" fill="#334155" text-anchor="middle">fname</text>
    <ellipse cx="170" cy="332" rx="40" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="170" y="336" font-size="11" fill="#334155" text-anchor="middle">lname</text>
  </g>

  <!-- Setting Attributes -->
  <g>
    <!-- id (PK) -->
    <ellipse cx="527" cy="47" rx="37" ry="17" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="527" y="52" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">id</text>
    <ellipse cx="627" cy="42" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="627" y="46" font-size="11" fill="#334155" text-anchor="middle">school_name</text>
    <ellipse cx="730" cy="42" rx="40" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="730" y="46" font-size="11" fill="#334155" text-anchor="middle">slogan</text>
    <ellipse cx="807" cy="87" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="807" y="91" font-size="10" fill="#334155" text-anchor="middle">current_year</text>
    <ellipse cx="817" cy="137" rx="57" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="817" y="141" font-size="10" fill="#334155" text-anchor="middle">current_semester</text>
  </g>

  <!-- Message Attributes -->
  <g>
    <!-- message_id (PK) -->
    <ellipse cx="67" cy="438" rx="47" ry="18" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="67" y="443" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">message_id</text>
    <ellipse cx="65" cy="602" rx="55" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="65" y="606" font-size="10" fill="#334155" text-anchor="middle">sender_full_name</text>
    <ellipse cx="177" cy="607" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="177" y="611" font-size="10" fill="#334155" text-anchor="middle">sender_email</text>
    <ellipse cx="47" cy="492" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="47" y="496" font-size="11" fill="#334155" text-anchor="middle">message</text>
    <ellipse cx="270" cy="542" rx="40" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="270" y="546" font-size="11" fill="#334155" text-anchor="middle">date_time</text>
  </g>

  <!-- Teacher Attributes -->
  <g>
    <!-- teacher_id (PK) -->
    <ellipse cx="477" cy="508" rx="47" ry="18" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="477" y="513" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">teacher_id</text>
    <ellipse cx="472" cy="552" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="472" y="556" font-size="11" fill="#334155" text-anchor="middle">username</text>
    <ellipse cx="472" cy="597" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="472" y="601" font-size="11" fill="#334155" text-anchor="middle">password</text>
    <ellipse cx="507" cy="647" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="507" y="651" font-size="11" fill="#334155" text-anchor="middle">fname</text>
    <ellipse cx="592" cy="647" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="592" y="651" font-size="11" fill="#334155" text-anchor="middle">lname</text>
    <ellipse cx="687" cy="647" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="687" y="651" font-size="10" fill="#334155" text-anchor="middle">employee_no</text>
    <ellipse cx="790" cy="647" rx="45" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="790" y="651" font-size="10" fill="#334155" text-anchor="middle">qualification</text>
    <ellipse cx="807" cy="597" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="807" y="601" font-size="10" fill="#334155" text-anchor="middle">phone_number</text>
    <ellipse cx="807" cy="552" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="807" y="556" font-size="10" fill="#334155" text-anchor="middle">email_address</text>
    <ellipse cx="797" cy="507" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="797" y="511" font-size="11" fill="#334155" text-anchor="middle">gender</text>
  </g>

  <!-- Registrar Attributes -->
  <g>
    <!-- r_user_id (PK) -->
    <ellipse cx="1862" cy="208" rx="47" ry="18" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="1862" y="213" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">r_user_id</text>
    <ellipse cx="1857" cy="257" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1857" y="261" font-size="11" fill="#334155" text-anchor="middle">username</text>
    <ellipse cx="1857" cy="302" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1857" y="306" font-size="11" fill="#334155" text-anchor="middle">password</text>
    <ellipse cx="1852" cy="347" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1852" y="351" font-size="11" fill="#334155" text-anchor="middle">fname</text>
    <ellipse cx="1852" cy="392" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1852" y="396" font-size="11" fill="#334155" text-anchor="middle">lname</text>
    <ellipse cx="1757" cy="177" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1757" y="181" font-size="10" fill="#334155" text-anchor="middle">employee_no</text>
    <ellipse cx="1647" cy="177" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1647" y="181" font-size="10" fill="#334155" text-anchor="middle">qualification</text>
    <ellipse cx="1537" cy="177" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1537" y="181" font-size="10" fill="#334155" text-anchor="middle">phone_number</text>
    <ellipse cx="1537" cy="227" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1537" y="231" font-size="10" fill="#334155" text-anchor="middle">email_address</text>
  </g>

  <!-- Student Attributes -->
  <g>
    <!-- student_id (PK) -->
    <ellipse cx="1382" cy="443" rx="47" ry="18" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="1382" y="448" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">student_id</text>
    <ellipse cx="1267" cy="442" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1267" y="446" font-size="11" fill="#334155" text-anchor="middle">username</text>
    <ellipse cx="1167" cy="452" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1167" y="456" font-size="11" fill="#334155" text-anchor="middle">password</text>
    <ellipse cx="1522" cy="502" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1522" y="506" font-size="11" fill="#334155" text-anchor="middle">fname</text>
    <ellipse cx="1522" cy="552" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1522" y="556" font-size="11" fill="#334155" text-anchor="middle">lname</text>
    <ellipse cx="1522" cy="602" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1522" y="606" font-size="11" fill="#334155" text-anchor="middle">gender</text>
    <ellipse cx="1532" cy="652" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1532" y="656" font-size="10" fill="#334155" text-anchor="middle">email_address</text>
    <ellipse cx="1417" cy="682" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1417" y="686" font-size="11" fill="#334155" text-anchor="middle">address</text>
    <ellipse cx="1322" cy="682" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1322" y="686" font-size="10" fill="#334155" text-anchor="middle">date_of_birth</text>
    <ellipse cx="1212" cy="682" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1212" y="686" font-size="10" fill="#334155" text-anchor="middle">parent_fname</text>
    <ellipse cx="1162" cy="632" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1162" y="636" font-size="10" fill="#334155" text-anchor="middle">parent_phone</text>
  </g>

  <!-- Class Attributes -->
  <g>
    <!-- class_id (PK) -->
    <ellipse cx="1025" cy="788" rx="45" ry="18" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="1025" y="793" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">class_id</text>
  </g>

  <!-- Grade Attributes -->
  <g>
    <!-- grade_id (PK) -->
    <ellipse cx="485" cy="1168" rx="45" ry="18" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="485" y="1173" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">grade_id</text>
    <ellipse cx="490" cy="1227" rx="40" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="490" y="1231" font-size="11" fill="#334155" text-anchor="middle">grade</text>
    <ellipse cx="595" cy="1267" rx="45" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="595" y="1271" font-size="11" fill="#334155" text-anchor="middle">grade_code</text>
  </g>

  <!-- Section Attributes -->
  <g>
    <!-- section_id (PK) -->
    <ellipse cx="1555" cy="1168" rx="45" ry="18" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="1555" y="1173" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">section_id</text>
    <ellipse cx="1520" cy="1227" rx="40" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1520" y="1231" font-size="11" fill="#334155" text-anchor="middle">section</text>
  </g>

  <!-- Subject Attributes -->
  <g>
    <!-- subject_id (PK) -->
    <ellipse cx="477" cy="1468" rx="47" ry="18" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="477" y="1473" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">subject_id</text>
    <ellipse cx="482" cy="1522" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="482" y="1526" font-size="11" fill="#334155" text-anchor="middle">subject</text>
    <ellipse cx="597" cy="1567" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="597" y="1571" font-size="10" fill="#334155" text-anchor="middle">subject_code</text>
  </g>

  <!-- Score Attributes -->
  <g>
    <!-- id (PK) -->
    <ellipse cx="1545" cy="1468" rx="35" ry="18" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="1545" y="1473" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">id</text>
    <ellipse cx="1542" cy="1522" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1542" y="1526" font-size="11" fill="#334155" text-anchor="middle">semester</text>
    <ellipse cx="1447" cy="1567" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1447" y="1571" font-size="11" fill="#334155" text-anchor="middle">year</text>
    <ellipse cx="1330" cy="1567" rx="40" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1330" y="1571" font-size="11" fill="#334155" text-anchor="middle">results</text>
  </g>


  <!-- ================= LEGEND BAR ================= -->
  <g>
    <rect x="60" y="1650" width="2280" height="110" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
    <text x="80" y="1675" font-size="13" font-weight="bold" fill="#1E293B">ER DIAGRAM SYMBOLS LEGEND (COMPLIANT WITH SPECIFICATION)</text>

    <!-- Entity -->
    <rect x="90" y="1695" width="110" height="45" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2"/>
    <text x="145" y="1723" font-size="12" font-weight="bold" fill="#0F172A" text-anchor="middle">Entity</text>
    <text x="215" y="1712" font-size="11" font-weight="bold" fill="#0F172A">Entity (Rectangle)</text>
    <text x="215" y="1728" font-size="10" fill="#475569">Real-world object or table</text>

    <!-- Relationship -->
    <polygon points="460,1695 510,1717 460,1740 410,1717" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="460" y="1721" font-size="10" font-weight="bold" fill="#7C2D12" text-anchor="middle">Rel</text>
    <text x="525" y="1712" font-size="11" font-weight="bold" fill="#0F172A">Relationship (Diamond)</text>
    <text x="525" y="1728" font-size="10" fill="#475569">Association between entities</text>

    <!-- Attribute -->
    <ellipse cx="850" cy="1717" rx="45" ry="20" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="850" y="1721" font-size="11" fill="#334155" text-anchor="middle">Attribute</text>
    <text x="910" y="1712" font-size="11" font-weight="bold" fill="#0F172A">Attribute (Oval)</text>
    <text x="910" y="1728" font-size="10" fill="#475569">Property or characteristic</text>

    <!-- Primary Key -->
    <ellipse cx="1200" cy="1717" rx="45" ry="20" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="1200" y="1722" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">user_id</text>
    <text x="1260" y="1712" font-size="11" font-weight="bold" fill="#0F172A">Primary Key (Underlined)</text>
    <text x="1260" y="1728" font-size="10" fill="#475569">Unique entity identifier</text>

    <!-- Connecting Line -->
    <line x1="1570" y1="1717" x2="1660" y2="1717" stroke="#475569" stroke-width="2"/>
    <text x="1680" y="1712" font-size="11" font-weight="bold" fill="#0F172A">Connecting Line</text>
    <text x="1680" y="1728" font-size="10" fill="#475569">Connects entity to attributes</text>

    <!-- Cardinality -->
    <rect x="1950" y="1700" width="60" height="34" rx="6" fill="#E2E8F0" stroke="#94A3B8" stroke-width="1"/>
    <text x="1980" y="1722" font-size="12" font-weight="bold" fill="#0F172A" text-anchor="middle">1 : N</text>
    <text x="2025" y="1712" font-size="11" font-weight="bold" fill="#0F172A">Cardinality Ratio</text>
    <text x="2025" y="1728" font-size="10" fill="#475569">1:1, 1:N, M:N participation</text>
  </g>
</svg>'''
    return svg


def generate_interactive_viewer_html():
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Entity-Relationship (ER) Diagram Viewer</title>
  <style>
    :root {
      --bg: #0F172A;
      --card-bg: #1E293B;
      --text: #F8FAFC;
      --text-muted: #94A3B8;
      --primary: #38BDF8;
      --border: #334155;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
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
    .btn:hover { background: #334155; border-color: #64748B; }
    .btn-primary { background: #2563EB; border-color: #3B82F6; color: #FFFFFF; }
    .btn-primary:hover { background: #1D4ED8; }
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
    iframe {
      border: none;
      border-radius: 8px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.25);
      background: #FFFFFF;
    }
  </style>
</head>
<body>
  <header>
    <div class="header-left">
      <h1>Entity-Relationship (ER) Diagram Viewer</h1>
      <p>Chen ER Notation Standard &bull; Editable in draw.io &bull; College Project Ready</p>
    </div>
    <div class="tabs-group">
      <button class="tab-btn active" onclick="switchTab('sms')">1. School Management System ERD</button>
      <button class="tab-btn" onclick="switchTab('ecommerce')">2. Reference E-Commerce ERD</button>
    </div>
    <div class="header-actions">
      <a href="school_management_er_diagram.drawio" download class="btn btn-primary" title="Download editable draw.io diagram file">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
        Download .drawio
      </a>
      <a href="https://app.diagrams.net/" target="_blank" class="btn" title="Open diagrams.net online editor">
        Open in draw.io
      </a>
    </div>
  </header>

  <div class="viewport">
    <div class="diagram-container" id="container-sms">
      <iframe src="sms_er_diagram.svg" style="width: 2400px; height: 1800px;"></iframe>
    </div>
    <div class="diagram-container" id="container-ec" style="display: none;">
      <iframe src="ecommerce_er_diagram.svg" style="width: 1800px; height: 1200px;"></iframe>
    </div>
  </div>

  <script>
    function switchTab(tab) {
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      if (tab === 'sms') {
        document.querySelectorAll('.tab-btn')[0].classList.add('active');
        document.getElementById('container-sms').style.display = 'flex';
        document.getElementById('container-ec').style.display = 'none';
      } else {
        document.querySelectorAll('.tab-btn')[1].classList.add('active');
        document.getElementById('container-sms').style.display = 'none';
        document.getElementById('container-ec').style.display = 'flex';
      }
    }
  </script>
</body>
</html>'''
    return html_content


def generate_ecommerce_svg():
    """Generates an SVG for the Reference E-Commerce ER Diagram."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1800 1200" width="100%" height="100%" style="background-color: #ffffff; font-family: 'Segoe UI', Arial, Helvetica, sans-serif;">
  <defs>
    <filter id="ec-shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.12" flood-color="#000000" />
    </filter>
  </defs>

  <!-- Title -->
  <rect x="60" y="20" width="1680" height="50" rx="8" fill="#1E293B" filter="url(#ec-shadow)"/>
  <text x="900" y="44" fill="#FFFFFF" font-size="17" font-weight="bold" text-anchor="middle" dominant-baseline="middle">REFERENCE E-COMMERCE ER DIAGRAM (BASED ON IMAGE EXAMPLES)</text>
  <text x="900" y="60" fill="#FCD34D" font-size="12" text-anchor="middle" dominant-baseline="middle">Entities: User, Products, Orders, Cart | Relationships: Manages_Cart, Contains_Item, Places_Order, Includes_Item</text>

  <!-- Lines: User -> Manages_Cart -> Cart -->
  <line x1="410" y1="292" x2="520" y2="292" stroke="#B45309" stroke-width="2"/>
  <line x1="650" y1="292" x2="800" y2="292" stroke="#B45309" stroke-width="2"/>
  <rect x="430" y="280" width="20" height="18" fill="#FFFFFF"/>
  <text x="440" y="293" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>
  <rect x="760" y="280" width="20" height="18" fill="#FFFFFF"/>
  <text x="770" y="293" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>

  <!-- Lines: Cart -> Contains_Item -> Products -->
  <line x1="960" y1="292" x2="1080" y2="292" stroke="#B45309" stroke-width="2"/>
  <line x1="1210" y1="292" x2="1350" y2="292" stroke="#B45309" stroke-width="2"/>
  <rect x="980" y="280" width="20" height="18" fill="#FFFFFF"/>
  <text x="990" y="293" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">M</text>
  <rect x="1310" y="280" width="20" height="18" fill="#FFFFFF"/>
  <text x="1320" y="293" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>

  <!-- Contains_Item attribute line: quantity -->
  <line x1="1145" y1="265" x2="1145" y2="224" stroke="#B45309" stroke-width="1.5"/>

  <!-- Lines: User -> Places_Order -> Orders -->
  <path d="M 330 325 L 330 527 L 450 527" stroke="#B45309" stroke-width="2" fill="none"/>
  <path d="M 580 527 L 880 527 L 880 650" stroke="#B45309" stroke-width="2" fill="none"/>
  <rect x="340" y="420" width="20" height="18" fill="#FFFFFF"/>
  <text x="350" y="433" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">1</text>
  <rect x="860" y="615" width="20" height="18" fill="#FFFFFF"/>
  <text x="870" y="628" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>

  <!-- Lines: Orders -> Includes_Item -> Products -->
  <path d="M 880 650 L 880 527 L 1190 527" stroke="#B45309" stroke-width="2" fill="none"/>
  <path d="M 1320 527 L 1430 527 L 1430 325" stroke="#B45309" stroke-width="2" fill="none"/>
  <rect x="1020" y="517" width="20" height="18" fill="#FFFFFF"/>
  <text x="1030" y="530" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">M</text>
  <rect x="1440" y="420" width="20" height="18" fill="#FFFFFF"/>
  <text x="1450" y="433" font-size="13" font-weight="bold" fill="#B45309" text-anchor="middle">N</text>

  <!-- User Attribute Lines -->
  <line x1="250" y1="270" x2="185" y2="219" stroke="#64748B" stroke-width="1.2"/>
  <line x1="250" y1="285" x2="180" y2="277" stroke="#64748B" stroke-width="1.2"/>
  <line x1="250" y1="305" x2="180" y2="332" stroke="#64748B" stroke-width="1.2"/>
  <line x1="300" y1="260" x2="242" y2="195" stroke="#64748B" stroke-width="1.2"/>
  <line x1="360" y1="260" x2="352" y2="195" stroke="#64748B" stroke-width="1.2"/>

  <!-- Cart Attribute Lines -->
  <line x1="830" y1="260" x2="822" y2="205" stroke="#64748B" stroke-width="1.2"/>
  <line x1="910" y1="260" x2="932" y2="205" stroke="#64748B" stroke-width="1.2"/>

  <!-- Products Attribute Lines -->
  <line x1="1510" y1="270" x2="1560" y2="218" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1510" y1="285" x2="1560" y2="267" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1510" y1="300" x2="1560" y2="312" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1510" y1="315" x2="1560" y2="357" stroke="#64748B" stroke-width="1.2"/>
  <line x1="1470" y1="260" x2="1487" y2="194" stroke="#64748B" stroke-width="1.2"/>

  <!-- Orders Attribute Lines -->
  <line x1="800" y1="682" x2="765" y2="683" stroke="#64748B" stroke-width="1.2"/>
  <line x1="830" y1="715" x2="762" y2="750" stroke="#64748B" stroke-width="1.2"/>
  <line x1="880" y1="715" x2="872" y2="750" stroke="#64748B" stroke-width="1.2"/>
  <line x1="930" y1="715" x2="977" y2="750" stroke="#64748B" stroke-width="1.2"/>


  <!-- Entities -->
  <g filter="url(#ec-shadow)">
    <rect x="250" y="260" width="160" height="65" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="330" y="298" font-size="15" font-weight="bold" fill="#0F172A" text-anchor="middle">USER</text>

    <rect x="800" y="260" width="160" height="65" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="880" y="298" font-size="15" font-weight="bold" fill="#0F172A" text-anchor="middle">CART</text>

    <rect x="1350" y="260" width="160" height="65" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="1430" y="298" font-size="15" font-weight="bold" fill="#0F172A" text-anchor="middle">PRODUCTS</text>

    <rect x="800" y="650" width="160" height="65" fill="#DAE8FC" stroke="#4A7BB0" stroke-width="2.5"/>
    <text x="880" y="688" font-size="15" font-weight="bold" fill="#0F172A" text-anchor="middle">ORDERS</text>
  </g>

  <!-- Relationships -->
  <g filter="url(#ec-shadow)">
    <polygon points="585,265 650,292 585,320 520,292" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="585" y="297" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Manages_Cart</text>

    <polygon points="1145,265 1210,292 1145,320 1080,292" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="1145" y="297" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Contains_Item</text>

    <polygon points="515,500 580,527 515,555 450,527" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="515" y="532" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Places_Order</text>

    <polygon points="1255,500 1320,527 1255,555 1190,527" fill="#FFE6CC" stroke="#D79B00" stroke-width="2"/>
    <text x="1255" y="532" font-size="12" font-weight="bold" fill="#7C2D12" text-anchor="middle">Includes_Item</text>
  </g>

  <!-- Attributes -->
  <g>
    <!-- User Attributes -->
    <ellipse cx="137" cy="219" rx="47" ry="19" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="137" y="224" font-size="12" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">user_id</text>
    <ellipse cx="140" cy="277" rx="40" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="140" y="281" font-size="11" fill="#334155" text-anchor="middle">name</text>
    <ellipse cx="140" cy="332" rx="40" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="140" y="336" font-size="11" fill="#334155" text-anchor="middle">email</text>
    <ellipse cx="242" cy="177" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="242" y="181" font-size="11" fill="#334155" text-anchor="middle">password</text>
    <ellipse cx="352" cy="177" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="352" y="181" font-size="11" fill="#334155" text-anchor="middle">address</text>

    <!-- Cart Attributes -->
    <ellipse cx="822" cy="187" rx="42" ry="17" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="822" y="192" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">cart_id</text>
    <ellipse cx="932" cy="187" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="932" y="191" font-size="11" fill="#334155" text-anchor="middle">created_at</text>

    <!-- Contains_Item Attribute: quantity -->
    <ellipse cx="1145" cy="207" rx="40" ry="17" fill="#FEF3C7" stroke="#D97706" stroke-width="1.5"/>
    <text x="1145" y="211" font-size="11" fill="#92400E" text-anchor="middle">quantity</text>

    <!-- Products Attributes -->
    <ellipse cx="1607" cy="218" rx="47" ry="18" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="1607" y="223" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">product_id</text>
    <ellipse cx="1600" cy="267" rx="40" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1600" y="271" font-size="11" fill="#334155" text-anchor="middle">name</text>
    <ellipse cx="1600" cy="312" rx="40" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1600" y="316" font-size="11" fill="#334155" text-anchor="middle">price</text>
    <ellipse cx="1602" cy="357" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1602" y="361" font-size="11" fill="#334155" text-anchor="middle">description</text>
    <ellipse cx="1487" cy="177" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="1487" y="181" font-size="11" fill="#334155" text-anchor="middle">stock</text>

    <!-- Orders Attributes -->
    <ellipse cx="717" cy="683" rx="47" ry="18" fill="#EFF6FF" stroke="#1E40AF" stroke-width="2"/>
    <text x="717" y="688" font-size="11" font-weight="bold" fill="#1E3A8A" text-anchor="middle" text-decoration="underline">order_id</text>
    <ellipse cx="762" cy="767" rx="42" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="762" y="771" font-size="11" fill="#334155" text-anchor="middle">order_date</text>
    <ellipse cx="872" cy="767" rx="47" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="872" y="771" font-size="10" fill="#334155" text-anchor="middle">total_amount</text>
    <ellipse cx="977" cy="767" rx="37" ry="17" fill="#F8FAFC" stroke="#64748B" stroke-width="1.5"/>
    <text x="977" y="771" font-size="11" fill="#334155" text-anchor="middle">status</text>
  </g>
</svg>'''
    return svg


def main():
    workspace = r"c:\xampp\htdocs\school-management"

    # 1. Write Draw.io Multi-Page XML
    drawio_file = os.path.join(workspace, "school_management_er_diagram.drawio")
    print(f"Generating {drawio_file}...")
    with open(drawio_file, "w", encoding="utf-8") as f:
        f.write(build_er_drawio_xml())

    # 2. Write SVG: School Management System ERD
    svg_sms_file = os.path.join(workspace, "sms_er_diagram.svg")
    print(f"Generating {svg_sms_file}...")
    with open(svg_sms_file, "w", encoding="utf-8") as f:
        f.write(generate_sms_er_svg())

    # 3. Write SVG: E-Commerce ERD
    svg_ec_file = os.path.join(workspace, "ecommerce_er_diagram.svg")
    print(f"Generating {svg_ec_file}...")
    with open(svg_ec_file, "w", encoding="utf-8") as f:
        f.write(generate_ecommerce_svg())

    # 4. Write HTML Viewer
    viewer_file = os.path.join(workspace, "er_diagram_viewer.html")
    print(f"Generating {viewer_file}...")
    with open(viewer_file, "w", encoding="utf-8") as f:
        f.write(generate_interactive_viewer_html())

    print("All ER Diagram files successfully created!")

if __name__ == "__main__":
    main()
