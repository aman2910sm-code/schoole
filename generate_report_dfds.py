#!/usr/bin/env python3
"""
Generate Black-and-White Functional Decomposition Level 1 DFDs
Exactly matching the user's reference image:
- Single tall Entity rectangle on the left with vertical text
- Vertical stack of Process ovals in the middle
- Open-right Data Store boxes on the right
- Paired straight arrows with input above and response/reply below
- Clean black and white / grayscale (no colors)
- Standard report page border, header, caption, and page number
"""

import os

def build_drawio_xml(module_key, config):
    entity_name = config["entity"]
    title_sub = config["title_sub"]
    fig_caption = config["fig_caption"]
    rows = config["rows"]
    
    num_rows = len(rows)
    page_w = 900
    page_h = 1180
    
    # Calculate row vertical positions
    start_y = 190 if num_rows >= 7 else 240
    row_gap = 105 if num_rows >= 7 else 125
    total_h = (num_rows - 1) * row_gap + 65
    
    entity_x = 100
    entity_w = 100
    entity_y = start_y
    entity_h = total_h
    
    proc_x = 360
    proc_w = 145
    proc_h = 60
    
    ds_x = 610
    ds_w = 150
    ds_h = 50
    
    xml = f'''<mxfile host="app.diagrams.net" modified="2026-09-26T00:00:00.000Z" agent="Mozilla/5.0" version="21.0.0" type="device">
  <diagram id="{module_key}-dfd" name="{entity_name} Level 1 DFD">
    <mxGraphModel dx="1200" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{page_w}" pageHeight="{page_h}" background="#FFFFFF" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Double Page Border (Report Style) -->
        <mxCell id="border_outer" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#000000;strokeWidth=2;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="820" height="1100" as="geometry" />
        </mxCell>
        <mxCell id="border_inner" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#000000;strokeWidth=0.8;" vertex="1" parent="1">
          <mxGeometry x="45" y="45" width="810" height="1090" as="geometry" />
        </mxCell>

        <!-- Top Left Section Header -->
        <mxCell id="hdr_left" value="&lt;b&gt;Level 1 DFD (Functional Decomposition)&lt;/b&gt;" style="text;html=1;align=left;verticalAlign=middle;fontSize=13;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="65" y="80" width="350" height="30" as="geometry" />
        </mxCell>

        <!-- Centered Subheader -->
        <mxCell id="hdr_center1" value="&lt;b&gt;1st Level DFD&lt;/b&gt;" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="350" y="115" width="200" height="18" as="geometry" />
        </mxCell>
        <mxCell id="hdr_center2" value="&lt;i&gt;{title_sub}&lt;/i&gt;" style="text;html=1;align=center;verticalAlign=middle;fontSize=9;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="350" y="130" width="200" height="18" as="geometry" />
        </mxCell>

        <!-- Left Tall Entity Box with Vertical Text -->
        <mxCell id="ent_{module_key}" value="&lt;b&gt;{entity_name}&lt;/b&gt;" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontColor=#000000;fontSize=14;fontStyle=1;horizontal=0;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="{entity_x}" y="{entity_y}" width="{entity_w}" height="{entity_h}" as="geometry" />
        </mxCell>
'''
    
    # Add Rows
    for i, r in enumerate(rows):
        ry = start_y + i * row_gap
        pid = f"p_{i+1}"
        dsid = f"ds_{i+1}"
        
        proc_label = f"&lt;b&gt;{r['proc_id']}&lt;/b&gt;&lt;br/&gt;{r['proc_name']}"
        ds_label = f"&lt;b&gt;{r['ds_name']}&lt;/b&gt;"
        
        # Process Oval
        xml += f'''
        <!-- Row {i+1}: Process {r['proc_id']} -->
        <mxCell id="{pid}" value="{proc_label}" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;fontColor=#000000;fontSize=10;align=center;verticalAlign=middle;" vertex="1" parent="1">
          <mxGeometry x="{proc_x}" y="{ry}" width="{proc_w}" height="{proc_h}" as="geometry" />
        </mxCell>

        <!-- Row {i+1}: Data Store (Open Right Box) -->
        <mxCell id="{dsid}" value="{ds_label}" style="shape=partialRectangle;top=1;bottom=1;left=1;right=0;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.2;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;fontColor=#000000;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="{ds_x}" y="{ry + 5}" width="{ds_w}" height="{ds_h}" as="geometry" />
        </mxCell>

        <!-- Flow: Entity -> Process (Upper Arrow) -->
        <mxCell id="f_in_{i+1}" value="{r['in_label']}" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;strokeColor=#000000;strokeWidth=1;fontSize=8;fontColor=#000000;labelBackgroundColor=#FFFFFF;verticalAlign=bottom;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="{entity_x + entity_w}" y="{ry + 15}" as="sourcePoint" />
            <mxPoint x="{proc_x}" y="{ry + 15}" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- Flow: Process -> Entity (Lower Arrow) -->
        <mxCell id="f_out_{i+1}" value="{r['out_label']}" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;strokeColor=#000000;strokeWidth=1;fontSize=8;fontColor=#000000;labelBackgroundColor=#FFFFFF;verticalAlign=top;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="{proc_x}" y="{ry + 45}" as="sourcePoint" />
            <mxPoint x="{entity_x + entity_w}" y="{ry + 45}" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- Flow: Process -> Data Store (Upper Arrow) -->
        <mxCell id="f_ds_in_{i+1}" value="{r['ds_in_label']}" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;strokeColor=#000000;strokeWidth=1;fontSize=8;fontColor=#000000;labelBackgroundColor=#FFFFFF;verticalAlign=bottom;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="{proc_x + proc_w}" y="{ry + 15}" as="sourcePoint" />
            <mxPoint x="{ds_x}" y="{ry + 15}" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- Flow: Data Store -> Process (Lower Arrow) -->
        <mxCell id="f_ds_out_{i+1}" value="{r['ds_out_label']}" style="edgeStyle=none;rounded=0;html=1;endArrow=classic;endFill=1;strokeColor=#000000;strokeWidth=1;fontSize=8;fontColor=#000000;labelBackgroundColor=#FFFFFF;verticalAlign=top;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="{ds_x}" y="{ry + 45}" as="sourcePoint" />
            <mxPoint x="{proc_x + proc_w}" y="{ry + 45}" as="targetPoint" />
          </mxGeometry>
        </mxCell>
'''

    # Bottom Caption, Divider, Page Number
    xml += f'''
        <!-- Bottom Figure Caption -->
        <mxCell id="fig_caption" value="&lt;i&gt;{fig_caption}&lt;/i&gt;" style="text;html=1;align=center;verticalAlign=middle;fontSize=11;fontColor=#000000;fontStyle=2;" vertex="1" parent="1">
          <mxGeometry x="250" y="990" width="400" height="25" as="geometry" />
        </mxCell>

        <!-- Bottom Divider Line -->
        <mxCell id="div_line" value="" style="edgeStyle=none;rounded=0;html=1;endArrow=none;strokeColor=#000000;strokeWidth=1.5;" edge="1" parent="1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="65" y="1030" as="sourcePoint" />
            <mxPoint x="835" y="1030" as="targetPoint" />
          </mxGeometry>
        </mxCell>

        <!-- Bottom Page Number -->
        <mxCell id="page_num" value="08" style="text;html=1;align=center;verticalAlign=middle;fontSize=11;fontColor=#000000;" vertex="1" parent="1">
          <mxGeometry x="425" y="1055" width="50" height="20" as="geometry" />
        </mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''
    return xml


def build_svg(module_key, config):
    entity_name = config["entity"]
    title_sub = config["title_sub"]
    fig_caption = config["fig_caption"]
    rows = config["rows"]
    
    num_rows = len(rows)
    page_w = 900
    page_h = 1180
    
    start_y = 190 if num_rows >= 7 else 240
    row_gap = 105 if num_rows >= 7 else 125
    total_h = (num_rows - 1) * row_gap + 65
    
    entity_x = 100
    entity_w = 100
    entity_y = start_y
    entity_h = total_h
    
    proc_x = 360
    proc_w = 145
    proc_h = 60
    
    ds_x = 610
    ds_w = 150
    ds_h = 50
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {page_w} {page_h}" width="100%" height="100%" style="background:#ffffff; font-family: 'Times New Roman', Times, serif;">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 2 L 8 5 L 0 8 z" fill="#000000" />
    </marker>
  </defs>

  <!-- Double Page Border (Exact replica of Reference Page) -->
  <rect x="40" y="40" width="820" height="1100" fill="none" stroke="#000000" stroke-width="2" />
  <rect x="45" y="45" width="810" height="1090" fill="none" stroke="#000000" stroke-width="0.8" />

  <!-- Top Left Header -->
  <text x="65" y="100" font-size="14" font-weight="bold" fill="#000000">Level 1 DFD (Functional Decomposition)</text>

  <!-- Centered Subtitles -->
  <text x="450" y="125" font-size="10" font-weight="bold" text-anchor="middle" fill="#000000">1st Level DFD</text>
  <text x="450" y="140" font-size="9" font-style="italic" text-anchor="middle" fill="#000000">{title_sub}</text>

  <!-- Left Entity Box (Sharp Rectangle with Vertical Text) -->
  <rect x="{entity_x}" y="{entity_y}" width="{entity_w}" height="{entity_h}" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <g transform="translate({entity_x + entity_w/2}, {entity_y + entity_h/2}) rotate(-90)">
    <text x="0" y="5" font-size="15" font-weight="bold" text-anchor="middle" letter-spacing="4" fill="#000000">{entity_name}</text>
  </g>
'''

    for i, r in enumerate(rows):
        ry = start_y + i * row_gap
        
        # Process Oval
        svg += f'''
  <!-- Row {i+1}: Process {r['proc_id']} -->
  <ellipse cx="{proc_x + proc_w/2}" cy="{ry + proc_h/2}" rx="{proc_w/2}" ry="{proc_h/2}" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="{proc_x + proc_w/2}" y="{ry + 24}" font-size="10" font-weight="bold" text-anchor="middle" fill="#000000">{r['proc_id']}</text>
  <text x="{proc_x + proc_w/2}" y="{ry + 38}" font-size="10" text-anchor="middle" fill="#000000">{r['proc_name']}</text>

  <!-- Row {i+1}: Data Store (Open Right Box: top line, bottom line, left line) -->
  <path d="M {ds_x + ds_w} {ry + 5} L {ds_x} {ry + 5} L {ds_x} {ry + 5 + ds_h} L {ds_x + ds_w} {ry + 5 + ds_h}" fill="none" stroke="#000000" stroke-width="1.2" />
  <text x="{ds_x + ds_w/2}" y="{ry + 5 + ds_h/2 + 4}" font-size="10" font-weight="bold" text-anchor="middle" fill="#000000">{r['ds_name']}</text>

  <!-- Entity -> Process (Upper Flow) -->
  <line x1="{entity_x + entity_w}" y1="{ry + 15}" x2="{proc_x}" y2="{ry + 15}" stroke="#000000" stroke-width="1" marker-end="url(#arr)" />
  <rect x="{(entity_x + entity_w + proc_x)/2 - 50}" y="{ry + 3}" width="100" height="11" fill="#ffffff" />
  <text x="{(entity_x + entity_w + proc_x)/2}" y="{ry + 12}" font-size="8" text-anchor="middle" fill="#000000">{r['in_label']}</text>

  <!-- Process -> Entity (Lower Flow) -->
  <line x1="{proc_x}" y1="{ry + 45}" x2="{entity_x + entity_w}" y2="{ry + 45}" stroke="#000000" stroke-width="1" marker-end="url(#arr)" />
  <rect x="{(entity_x + entity_w + proc_x)/2 - 35}" y="{ry + 47}" width="70" height="11" fill="#ffffff" />
  <text x="{(entity_x + entity_w + proc_x)/2}" y="{ry + 56}" font-size="8" text-anchor="middle" fill="#000000">{r['out_label']}</text>

  <!-- Process -> Data Store (Upper Flow) -->
  <line x1="{proc_x + proc_w}" y1="{ry + 15}" x2="{ds_x}" y2="{ry + 15}" stroke="#000000" stroke-width="1" marker-end="url(#arr)" />
  <rect x="{(proc_x + proc_w + ds_x)/2 - 40}" y="{ry + 3}" width="80" height="11" fill="#ffffff" />
  <text x="{(proc_x + proc_w + ds_x)/2}" y="{ry + 12}" font-size="8" text-anchor="middle" fill="#000000">{r['ds_in_label']}</text>

  <!-- Data Store -> Process (Lower Flow) -->
  <line x1="{ds_x}" y1="{ry + 45}" x2="{proc_x + proc_w}" y2="{ry + 45}" stroke="#000000" stroke-width="1" marker-end="url(#arr)" />
  <rect x="{(proc_x + proc_w + ds_x)/2 - 25}" y="{ry + 47}" width="50" height="11" fill="#ffffff" />
  <text x="{(proc_x + proc_w + ds_x)/2}" y="{ry + 56}" font-size="8" text-anchor="middle" fill="#000000">{r['ds_out_label']}</text>
'''

    svg += f'''
  <!-- Bottom Caption -->
  <text x="450" y="1005" font-size="11" font-weight="bold" font-style="italic" text-anchor="middle" fill="#000000">{fig_caption}</text>

  <!-- Bottom Divider Line -->
  <line x1="65" y1="1030" x2="835" y2="1030" stroke="#000000" stroke-width="1.5" />

  <!-- Bottom Page Number -->
  <text x="450" y="1065" font-size="11" text-anchor="middle" fill="#000000">08</text>
</svg>'''
    return svg


# Configurations for the 4 modules based on sms_db
CONFIGS = {
    "admin": {
        "entity": "ADMIN",
        "title_sub": "1 Level DFD (Admin DFD)",
        "fig_caption": "Figure 6.1: Level 1 DFD of Admin Module",
        "rows": [
            {
                "proc_id": "1.1",
                "proc_name": "Login",
                "ds_name": "Admins Table",
                "in_label": "login credentials",
                "out_label": "response",
                "ds_in_label": "check admin",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "1.2",
                "proc_name": "Manage Settings",
                "ds_name": "Settings Table",
                "in_label": "school details",
                "out_label": "response",
                "ds_in_label": "update settings",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "1.3",
                "proc_name": "Manage Teachers",
                "ds_name": "Teachers Table",
                "in_label": "teacher details",
                "out_label": "response",
                "ds_in_label": "add/update/delete",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "1.4",
                "proc_name": "Manage Registrar",
                "ds_name": "Registrar Table",
                "in_label": "registrar details",
                "out_label": "response",
                "ds_in_label": "add/update/delete",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "1.5",
                "proc_name": "Manage Classes",
                "ds_name": "Class Table",
                "in_label": "class &amp; grade details",
                "out_label": "response",
                "ds_in_label": "add/update/delete",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "1.6",
                "proc_name": "Manage Courses",
                "ds_name": "Courses Table",
                "in_label": "course &amp; subject data",
                "out_label": "response",
                "ds_in_label": "add/update/delete",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "1.7",
                "proc_name": "View Inquiries",
                "ds_name": "Inquiries Table",
                "in_label": "inquiry request",
                "out_label": "response",
                "ds_in_label": "view/status",
                "ds_out_label": "reply"
            }
        ]
    },
    "teacher": {
        "entity": "TEACHER",
        "title_sub": "1 Level DFD (Teacher DFD)",
        "fig_caption": "Figure 6.2: Level 1 DFD of Teacher Module",
        "rows": [
            {
                "proc_id": "2.1",
                "proc_name": "Login",
                "ds_name": "Teachers Table",
                "in_label": "login credentials",
                "out_label": "response",
                "ds_in_label": "check teacher",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "2.2",
                "proc_name": "View Classes",
                "ds_name": "Class Table",
                "in_label": "class request",
                "out_label": "response",
                "ds_in_label": "fetch classes",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "2.3",
                "proc_name": "View Students",
                "ds_name": "Students Table",
                "in_label": "roster request",
                "out_label": "response",
                "ds_in_label": "fetch students",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "2.4",
                "proc_name": "Manage Scores",
                "ds_name": "Scores Table",
                "in_label": "student marks data",
                "out_label": "response",
                "ds_in_label": "add/update marks",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "2.5",
                "proc_name": "Manage Profile",
                "ds_name": "Teachers Table",
                "in_label": "profile update data",
                "out_label": "response",
                "ds_in_label": "update profile",
                "ds_out_label": "reply"
            }
        ]
    },
    "student": {
        "entity": "STUDENT",
        "title_sub": "1 Level DFD (Student DFD)",
        "fig_caption": "Figure 6.3: Level 1 DFD of Student Module",
        "rows": [
            {
                "proc_id": "3.1",
                "proc_name": "Login",
                "ds_name": "Students Table",
                "in_label": "login credentials",
                "out_label": "response",
                "ds_in_label": "check student",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "3.2",
                "proc_name": "View Profile",
                "ds_name": "Students Table",
                "in_label": "profile request",
                "out_label": "response",
                "ds_in_label": "fetch details",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "3.3",
                "proc_name": "View Results",
                "ds_name": "Scores Table",
                "in_label": "results request",
                "out_label": "response",
                "ds_in_label": "fetch scores",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "3.4",
                "proc_name": "Send Inquiry",
                "ds_name": "Inquiries Table",
                "in_label": "inquiry details",
                "out_label": "response",
                "ds_in_label": "store inquiry",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "3.5",
                "proc_name": "Manage Password",
                "ds_name": "Students Table",
                "in_label": "password update data",
                "out_label": "response",
                "ds_in_label": "update password",
                "ds_out_label": "reply"
            }
        ]
    },
    "registrar": {
        "entity": "REGISTRAR",
        "title_sub": "1 Level DFD (Registrar DFD)",
        "fig_caption": "Figure 6.4: Level 1 DFD of Registrar Module",
        "rows": [
            {
                "proc_id": "4.1",
                "proc_name": "Login",
                "ds_name": "Registrar Table",
                "in_label": "login credentials",
                "out_label": "response",
                "ds_in_label": "check registrar",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "4.2",
                "proc_name": "Student Admission",
                "ds_name": "Students Table",
                "in_label": "admission details",
                "out_label": "response",
                "ds_in_label": "insert student",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "4.3",
                "proc_name": "Assign Class",
                "ds_name": "Class Table",
                "in_label": "class assign details",
                "out_label": "response",
                "ds_in_label": "update class",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "4.4",
                "proc_name": "Search Students",
                "ds_name": "Students Table",
                "in_label": "search query",
                "out_label": "response",
                "ds_in_label": "fetch records",
                "ds_out_label": "reply"
            },
            {
                "proc_id": "4.5",
                "proc_name": "Manage Profile",
                "ds_name": "Registrar Table",
                "in_label": "profile update data",
                "out_label": "response",
                "ds_in_label": "update profile",
                "ds_out_label": "reply"
            }
        ]
    }
}


def build_viewer_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Level 1 DFD (Functional Decomposition) | School Management System</title>
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
      padding: 7px 16px;
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
      max-width: 960px;
      display: flex;
      justify-content: center;
    }
    .sheet-card {
      background: #ffffff;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
      width: 100%;
      max-width: 900px;
      border-radius: 4px;
      overflow: hidden;
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
      <h1>Level 1 DFD (Functional Decomposition) — Black &amp; White Report Format</h1>
      <p>School Management System | Entity (Rectangle), Process (Oval), Data Store (Open Box)</p>
    </div>

    <div class="nav-tabs">
      <button class="nav-btn active" onclick="showTab('admin')">Admin DFD</button>
      <button class="nav-btn" onclick="showTab('teacher')">Teacher DFD</button>
      <button class="nav-btn" onclick="showTab('student')">Student DFD</button>
      <button class="nav-btn" onclick="showTab('registrar')">Registrar DFD</button>
    </div>

    <div class="actions">
      <a id="download-drawio" href="admin.drawio" download>Download .drawio</a>
    </div>
  </header>

  <main>
    <div class="sheet-card">
      <div id="tab-admin" class="panel active">
        <object data="admin_dfd.svg" type="image/svg+xml"></object>
      </div>
      <div id="tab-teacher" class="panel">
        <object data="teacher_dfd.svg" type="image/svg+xml"></object>
      </div>
      <div id="tab-student" class="panel">
        <object data="student_dfd.svg" type="image/svg+xml"></object>
      </div>
      <div id="tab-registrar" class="panel">
        <object data="registrar_dfd.svg" type="image/svg+xml"></object>
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
    print("Generating exact Black & White reference DFDs in:", workspace)
    
    for key, config in CONFIGS.items():
        # 1. Generate Draw.io XML
        xml_content = build_drawio_xml(key, config)
        
        # Write .drawio
        drawio_path = os.path.join(workspace, f"{key}.drawio")
        with open(drawio_path, "w", encoding="utf-8") as f:
            f.write(xml_content)
            
        # Write .drowio
        drowio_path = os.path.join(workspace, f"{key}.drowio")
        with open(drowio_path, "w", encoding="utf-8") as f:
            f.write(xml_content)
            
        # Write extra spelling for registrar if needed
        if key == "registrar":
            with open(os.path.join(workspace, "registarar.drowio"), "w", encoding="utf-8") as f:
                f.write(xml_content)
                
        print(f"[OK] Generated {key}.drawio and {key}.drowio")
        
        # 2. Generate Standalone SVG
        svg_content = build_svg(key, config)
        svg_path = os.path.join(workspace, f"{key}_dfd.svg")
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"[OK] Generated {key}_dfd.svg")

    # 3. Viewer HTML
    viewer_path = os.path.join(workspace, "dfd_modules_viewer.html")
    with open(viewer_path, "w", encoding="utf-8") as f:
        f.write(build_viewer_html())
    print("[OK] Generated dfd_modules_viewer.html")

if __name__ == "__main__":
    main()
