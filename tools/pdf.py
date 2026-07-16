from pathlib import Path
import re

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


POLICIES_DIR = Path("data") / "policies"


def sanitize_filename(title: str) -> str:
    """
    Converts a policy title into a valid filename.
    """

    filename = re.sub(
        r"[^\w\s-]",
        "",
        title,
    )

    return filename.strip().replace(" ", "_")


def generate_pdf(
    title: str,
    markdown: str,
) -> str:
    """
    Generates a PDF from the policy markdown.

    Returns the saved PDF path.
    """

    POLICIES_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    filename = sanitize_filename(title)

    pdf_path = POLICIES_DIR / f"{filename}.pdf"

    styles = getSampleStyleSheet()

    document = SimpleDocTemplate(str(pdf_path))

    story = []

    for line in markdown.splitlines():

        line = line.strip()

        if not line:
            continue

        if line.startswith("# "):

            story.append(
                Paragraph(
                    f"<b><font size=18>{line[2:]}</font></b>",
                    styles["Heading1"],
                )
            )

        elif line.startswith("## "):

            story.append(
                Paragraph(
                    f"<b><font size=14>{line[3:]}</font></b>",
                    styles["Heading2"],
                )
            )

        else:

            story.append(
                Paragraph(
                    line,
                    styles["BodyText"],
                )
            )

    document.build(story)

    return str(pdf_path)