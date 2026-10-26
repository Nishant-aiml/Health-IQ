import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import fitz  # PyMuPDF

def generate_samples():
    dirs = ["sample_data", os.path.join("frontend", "public", "sample_data")]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

    # ---------------------------------------------------------
    # 1. Generate sample_lab_report.pdf
    # ---------------------------------------------------------
    pdf_path = os.path.join("sample_data", "sample_lab_report.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "LabTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#0f766e"),
        alignment=1,
    )
    subtitle_style = ParagraphStyle(
        "LabSub",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#64748b"),
        alignment=1,
    )
    h2_style = ParagraphStyle(
        "H2",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=15,
        textColor=colors.HexColor("#0f172a"),
        spaceAfter=6,
    )
    cell_style = ParagraphStyle(
        "Cell",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=11,
    )
    cell_bold = ParagraphStyle(
        "CellBold",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=11,
    )
    cell_flag_high = ParagraphStyle(
        "CellHigh",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=11,
        textColor=colors.HexColor("#dc2626"),
    )
    cell_flag_low = ParagraphStyle(
        "CellLow",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=11,
        textColor=colors.HexColor("#d97706"),
    )

    story = []
    story.append(Paragraph("METROPOLIS CLINICAL HEALTHCARE LABORATORIES", title_style))
    story.append(Paragraph("Accredited Medical Testing Laboratory | ISO 15189 Certified | Report ID: LAB-2026-9812", subtitle_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0f766e"), spaceAfter=12))

    # Patient info table
    pat_data = [
        [
            Paragraph("<b>Patient Name:</b> John Doe", cell_style),
            Paragraph("<b>Age / Gender:</b> 38 Yrs / Male", cell_style),
            Paragraph("<b>Sample Collected:</b> 25-Oct-2026 08:30 AM", cell_style),
        ],
        [
            Paragraph("<b>Patient ID:</b> PT-44821", cell_style),
            Paragraph("<b>Referred By:</b> Dr. R. Sharma, MD", cell_style),
            Paragraph("<b>Report Finalized:</b> 25-Oct-2026 12:45 PM", cell_style),
        ]
    ]
    t_pat = Table(pat_data, colWidths=[180, 180, 180])
    t_pat.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f8fafc")),
        ("PADDING", (0, 0), (-1, -1), 6),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(t_pat)
    story.append(Spacer(1, 14))

    # Test Results Table
    story.append(Paragraph("BIOCHEMICAL & HEMATOLOGICAL INVESTIGATION", h2_style))
    table_data = [
        [
            Paragraph("Investigation / Parameter", cell_bold),
            Paragraph("Observed Value", cell_bold),
            Paragraph("Unit", cell_bold),
            Paragraph("Biological Reference", cell_bold),
            Paragraph("Status / Flag", cell_bold),
        ],
        [
            Paragraph("Hemoglobin (Hb)", cell_style),
            Paragraph("11.2", cell_bold),
            Paragraph("g/dL", cell_style),
            Paragraph("13.8 - 17.2", cell_style),
            Paragraph("LOW", cell_flag_low),
        ],
        [
            Paragraph("Fasting Blood Sugar (Glucose)", cell_style),
            Paragraph("128.0", cell_bold),
            Paragraph("mg/dL", cell_style),
            Paragraph("70.0 - 99.0", cell_style),
            Paragraph("HIGH", cell_flag_high),
        ],
        [
            Paragraph("HbA1c (Glycated Hemoglobin)", cell_style),
            Paragraph("6.8", cell_bold),
            Paragraph("%", cell_style),
            Paragraph("4.0 - 5.6", cell_style),
            Paragraph("HIGH", cell_flag_high),
        ],
        [
            Paragraph("Total Cholesterol", cell_style),
            Paragraph("245.0", cell_bold),
            Paragraph("mg/dL", cell_style),
            Paragraph("125.0 - 200.0", cell_style),
            Paragraph("HIGH", cell_flag_high),
        ],
        [
            Paragraph("Triglycerides", cell_style),
            Paragraph("195.0", cell_bold),
            Paragraph("mg/dL", cell_style),
            Paragraph("50.0 - 150.0", cell_style),
            Paragraph("HIGH", cell_flag_high),
        ],
        [
            Paragraph("HDL Cholesterol (Good)", cell_style),
            Paragraph("38.0", cell_bold),
            Paragraph("mg/dL", cell_style),
            Paragraph("> 40.0", cell_style),
            Paragraph("LOW", cell_flag_low),
        ],
        [
            Paragraph("LDL Cholesterol (Bad)", cell_style),
            Paragraph("168.0", cell_bold),
            Paragraph("mg/dL", cell_style),
            Paragraph("< 100.0", cell_style),
            Paragraph("HIGH", cell_flag_high),
        ],
        [
            Paragraph("Serum Creatinine", cell_style),
            Paragraph("0.95", cell_bold),
            Paragraph("mg/dL", cell_style),
            Paragraph("0.70 - 1.30", cell_style),
            Paragraph("NORMAL", cell_style),
        ],
        [
            Paragraph("Serum Calcium", cell_style),
            Paragraph("7.8", cell_bold),
            Paragraph("mg/dL", cell_style),
            Paragraph("8.5 - 10.2", cell_style),
            Paragraph("LOW", cell_flag_low),
        ],
        [
            Paragraph("Vitamin D (25-OH Cholecalciferol)", cell_style),
            Paragraph("14.2", cell_bold),
            Paragraph("ng/mL", cell_style),
            Paragraph("30.0 - 100.0", cell_style),
            Paragraph("LOW", cell_flag_low),
        ],
        [
            Paragraph("Total Platelet Count", cell_style),
            Paragraph("240000", cell_bold),
            Paragraph("/mcL", cell_style),
            Paragraph("150,000 - 450,000", cell_style),
            Paragraph("NORMAL", cell_style),
        ],
        [
            Paragraph("Total WBC Count", cell_style),
            Paragraph("7400", cell_bold),
            Paragraph("/mcL", cell_style),
            Paragraph("4,000 - 11,000", cell_style),
            Paragraph("NORMAL", cell_style),
        ],
    ]

    t_results = Table(table_data, colWidths=[170, 95, 75, 110, 90])
    t_results.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f766e")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
        ("TOPPADDING", (0, 0), (-1, 0), 6),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (1, 1), (1, -1), "CENTER"),
        ("ALIGN", (2, 1), (2, -1), "CENTER"),
        ("ALIGN", (3, 1), (3, -1), "CENTER"),
        ("ALIGN", (4, 1), (4, -1), "CENTER"),
    ]))
    story.append(t_results)
    story.append(Spacer(1, 14))

    # Notes & Signature
    story.append(Paragraph("<b>Clinical Observations & Notes:</b> Patient demonstrates mild microcytic anemia, borderline fasting hyperglycemia (prediabetes trajectory), and atherogenic lipid profile. Clinical correlation advised.", cell_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Verified by: <b>Dr. A. K. Verma, MD (Pathologist)</b> &nbsp;&nbsp;|&nbsp;&nbsp; Metropolis Diagnostic Health", cell_style))

    doc.build(story)
    print(f"Generated: {pdf_path}")

    # Copy to frontend/public/sample_data/
    frontend_pdf = os.path.join("frontend", "public", "sample_data", "sample_lab_report.pdf")
    with open(pdf_path, "rb") as f_in, open(frontend_pdf, "wb") as f_out:
        f_out.write(f_in.read())

    # Convert page 1 of PDF to PNG image
    pdf_doc = fitz.open(pdf_path)
    page = pdf_doc.load_page(0)
    pix = page.get_pixmap(dpi=150)
    png_path = os.path.join("sample_data", "sample_lab_report.png")
    pix.save(png_path)
    frontend_png = os.path.join("frontend", "public", "sample_data", "sample_lab_report.png")
    pix.save(frontend_png)
    print(f"Generated: {png_path} and {frontend_png}")

    # ---------------------------------------------------------
    # 2. Generate sample_prescription.pdf
    # ---------------------------------------------------------
    rx_pdf_path = os.path.join("sample_data", "sample_prescription.pdf")
    rx_doc = SimpleDocTemplate(rx_pdf_path, pagesize=letter, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=36)
    rx_story = []

    rx_title = ParagraphStyle(
        "RxTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        textColor=colors.HexColor("#1e3a8a"),
        alignment=1,
    )
    rx_sub = ParagraphStyle(
        "RxSub",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#475569"),
        alignment=1,
    )

    rx_story.append(Paragraph("APOLLO CLINICAL HEALTHCARE & CARDIOMETABOLIC CLINIC", rx_title))
    rx_story.append(Paragraph("Dr. R. Sharma, MD, FACC (Internal Medicine & Cardiometabolic Specialist)<br/>Reg No: MCI-2014-99214 | Contact: clinic@apollohealth.org", rx_sub))
    rx_story.append(Spacer(1, 10))
    rx_story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=12))

    # Patient info
    rx_pat_data = [
        [
            Paragraph("<b>Patient Name:</b> John Doe", cell_style),
            Paragraph("<b>Age / Sex:</b> 38 Yrs / M", cell_style),
            Paragraph("<b>Date:</b> 25-Oct-2026", cell_style),
        ],
        [
            Paragraph("<b>Weight / BP:</b> 78 kg / 134/86 mmHg", cell_style),
            Paragraph("<b>Diagnosis:</b> Dyslipidemia, Impaired Fasting Glucose, Joint Pain", cell_style),
            Paragraph("<b>Follow-up:</b> 12 Weeks", cell_style),
        ]
    ]
    t_rx_pat = Table(rx_pat_data, colWidths=[180, 220, 140])
    t_rx_pat.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f1f5f9")),
        ("PADDING", (0, 0), (-1, -1), 6),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
    ]))
    rx_story.append(t_rx_pat)
    rx_story.append(Spacer(1, 14))

    # Rx header
    rx_story.append(Paragraph("<font size='18' color='#1e3a8a'><b>&#8478; (Prescription)</b></font>", h2_style))
    rx_story.append(Spacer(1, 6))

    rx_meds_table = [
        [
            Paragraph("#", cell_bold),
            Paragraph("Medicine Name & Strength", cell_bold),
            Paragraph("Dosage & Frequency", cell_bold),
            Paragraph("Administration / Food Timing", cell_bold),
            Paragraph("Duration", cell_bold),
        ],
        [
            Paragraph("1", cell_bold),
            Paragraph("<b>Tab. Glycomet 500mg</b><br/>(Metformin Hydrochloride)", cell_style),
            Paragraph("1 Tab &bull; Twice Daily (BD)", cell_style),
            Paragraph("With or immediately after meals (Breakfast & Dinner)", cell_style),
            Paragraph("30 Days", cell_style),
        ],
        [
            Paragraph("2", cell_bold),
            Paragraph("<b>Tab. Lipitor 20mg</b><br/>(Atorvastatin Calcium)", cell_style),
            Paragraph("1 Tab &bull; Once Daily (OD)", cell_style),
            Paragraph("At bedtime with a glass of water", cell_style),
            Paragraph("30 Days", cell_style),
        ],
        [
            Paragraph("3", cell_bold),
            Paragraph("<b>Tab. Ecosprin 75mg</b><br/>(Aspirin / Acetylsalicylic Acid)", cell_style),
            Paragraph("1 Tab &bull; Once Daily (OD)", cell_style),
            Paragraph("After breakfast (do NOT take on empty stomach)", cell_style),
            Paragraph("30 Days", cell_style),
        ],
        [
            Paragraph("4", cell_bold),
            Paragraph("<b>Tab. Brufen 400mg</b><br/>(Ibuprofen)", cell_style),
            Paragraph("1 Tab &bull; As needed (SOS)", cell_style),
            Paragraph("After food for severe joint discomfort only", cell_style),
            Paragraph("5 Days (SOS)", cell_style),
        ],
        [
            Paragraph("5", cell_bold),
            Paragraph("<b>Cap. Pan-D</b><br/>(Pantoprazole 40mg + Domperidone 30mg)", cell_style),
            Paragraph("1 Cap &bull; Once Daily (OD)", cell_style),
            Paragraph("In the morning 30 minutes before breakfast", cell_style),
            Paragraph("15 Days", cell_style),
        ],
    ]

    t_rx_meds = Table(rx_meds_table, colWidths=[25, 175, 120, 160, 60])
    t_rx_meds.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1e3a8a")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
        ("TOPPADDING", (0, 0), (-1, 0), 6),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 1), (0, -1), "CENTER"),
        ("ALIGN", (4, 1), (4, -1), "CENTER"),
    ]))
    rx_story.append(t_rx_meds)
    rx_story.append(Spacer(1, 14))

    rx_story.append(Paragraph("<b>Clinical Warning / Advice:</b><br/>&bull; Avoid concurrent use of Ibuprofen with daily Aspirin (increased gastric bleeding risk and antiplatelet inhibition).<br/>&bull; Avoid high amounts of grapefruit while taking Atorvastatin.<br/>&bull; Maintain 30 minutes of daily physical aerobic activity.", cell_style))
    rx_story.append(Spacer(1, 16))
    rx_story.append(Paragraph("Doctor's Signature & Seal: _________________________<br/><b>Dr. R. Sharma, MD</b>", cell_style))

    rx_doc.build(rx_story)
    print(f"Generated: {rx_pdf_path}")

    # Copy to frontend/public/sample_data/
    frontend_rx_pdf = os.path.join("frontend", "public", "sample_data", "sample_prescription.pdf")
    with open(rx_pdf_path, "rb") as f_in, open(frontend_rx_pdf, "wb") as f_out:
        f_out.write(f_in.read())

    # Convert rx PDF to PNG
    rx_pdf_doc = fitz.open(rx_pdf_path)
    rx_page = rx_pdf_doc.load_page(0)
    rx_pix = rx_page.get_pixmap(dpi=150)
    rx_png_path = os.path.join("sample_data", "sample_prescription.png")
    rx_pix.save(rx_png_path)
    frontend_rx_png = os.path.join("frontend", "public", "sample_data", "sample_prescription.png")
    rx_pix.save(frontend_rx_png)
    print(f"Generated: {rx_png_path} and {frontend_rx_png}")

    # ---------------------------------------------------------
    # 3. Generate sample text files
    # ---------------------------------------------------------
    lab_txt = """METROPOLIS CLINICAL HEALTHCARE LABORATORIES
Patient Name: John Doe | Age: 38 Years | Gender: Male
Referred By: Dr. R. Sharma, MD | Date: 25-Oct-2026

COMPLETE BLOOD COUNT (CBC) & METABOLIC INVESTIGATION:
------------------------------------------------------------
Hemoglobin                   11.2 g/dL       (Ref: 13.8 - 17.2)   [LOW]
Fasting Blood Sugar (FBS)    128.0 mg/dL     (Ref: 70.0 - 99.0)   [HIGH]
HbA1c Glycated Hemoglobin    6.8 %           (Ref: 4.0 - 5.6)     [HIGH]
Total Cholesterol            245.0 mg/dL     (Ref: 125.0 - 200.0) [HIGH]
Triglycerides                195.0 mg/dL     (Ref: 50.0 - 150.0)  [HIGH]
HDL (Good) Cholesterol       38.0 mg/dL      (Ref: > 40.0)        [LOW]
LDL (Bad) Cholesterol        168.0 mg/dL     (Ref: < 100.0)       [HIGH]
Serum Creatinine             0.95 mg/dL      (Ref: 0.70 - 1.30)   [NORMAL]
Serum Calcium                7.8 mg/dL       (Ref: 8.5 - 10.2)    [LOW]
Vitamin D (25-OH)            14.2 ng/mL      (Ref: 30.0 - 100.0)  [LOW]
Total Platelet Count         240000 /mcL     (Ref: 150k - 450k)   [NORMAL]
Total WBC Count              7400 /mcL       (Ref: 4,000 - 11,000)[NORMAL]
------------------------------------------------------------
Impression: Mild microcytic anemia, impaired fasting glucose (prediabetes), and atherogenic dyslipidemia.
"""
    for p in ["sample_data/sample_lab_report.txt", "frontend/public/sample_data/sample_lab_report.txt"]:
        with open(p, "w", encoding="utf-8") as f:
            f.write(lab_txt)

    rx_txt = """PRESCRIPTION / Rx
Patient: John Doe | Age: 38 | Date: 25-Oct-2026
Diagnosis: Impaired Fasting Glucose, Dyslipidemia, Mild Knee Joint Pain

Rx:
1. Tab. Glycomet 500mg - 1 tablet twice daily with meals (Breakfast & Dinner)
2. Tab. Lipitor 20mg - 1 tablet once daily at bedtime
3. Tab. Ecosprin 75mg - 1 tablet once daily after breakfast
4. Tab. Brufen 400mg - 1 tablet as needed for severe joint pain
5. Cap. Pan-D - 1 capsule once daily 30 minutes before breakfast
"""
    for p in ["sample_data/sample_prescription.txt", "frontend/public/sample_data/sample_prescription.txt"]:
        with open(p, "w", encoding="utf-8") as f:
            f.write(rx_txt)

    print("All sample files generated successfully!")

if __name__ == "__main__":
    generate_samples()
