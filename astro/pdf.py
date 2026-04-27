from reportlab.pdfgen import canvas

def generate_pdf(filename="kundli.pdf"):
    c = canvas.Canvas(filename)
    c.drawString(100, 800, "Vedic Astrology Report")
    c.drawString(100, 780, "Generated Kundli Analysis")
    c.save()
