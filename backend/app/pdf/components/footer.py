# --------------------------------------------------
# File: footer.py
# Purpose: PDF Footer canvas callback rendering page numbers, legal disclaimers, and SHA-256 hash.
# Module: PDF Engine / Components
# Used By: PDF Layout & Renderer
# Future Phase: Phase 2E PDF Export
# --------------------------------------------------

from reportlab.pdfgen import canvas
from backend.app.pdf.styles import medical_pdf_styles


class NumberedCanvas(canvas.Canvas):
    """
    Two-Pass Numbered Canvas.

    Why it exists:
        Calculates total page count dynamically ("Page X of Y"), embeds SHA-256 report hash,
        and prints mandatory legal disclaimers at the bottom of every PDF page.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []
        self.sha256_hash = kwargs.get("sha256_hash", "UNVERIFIED")

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(medical_pdf_styles.MUTED_SLATE)

        # Footer line
        self.setStrokeColor(medical_pdf_styles.BORDER_COLOR)
        self.setLineWidth(0.5)
        self.line(36, 40, 576, 40)

        # Footer text
        self.drawString(36, 28, "HealthLens AI — Educational Laboratory Intelligence Report • Non-Diagnostic")
        self.drawRightString(576, 28, f"Page {self._pageNumber} of {page_count}")
        self.drawString(36, 16, f"SHA-256 Integrity Hash: {self.sha256_hash[:32]}...")
        self.restoreState()
