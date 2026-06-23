from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
        filename,
        risk_score,
        quality_score,
        review,
        suggestions
):

    pdf_path = "AI_Code_Review_Report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Code Review Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"<b>File:</b> {filename}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Risk Score:</b> {risk_score}/100",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Quality Score:</b> {quality_score}/100",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>AI Review</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            review.replace("\n", "<br/>"),
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>Optimization Suggestions</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            suggestions.replace("\n", "<br/>"),
            styles["Normal"]
        )
    )

    doc.build(content)

    return pdf_path