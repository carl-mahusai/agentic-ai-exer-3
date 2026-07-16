from agents import function_tool

from tools.pdf import generate_pdf


@function_tool
def generate_pdf_tool(
    title: str,
    markdown: str,
) -> str:
    """
    Generates a PDF from the supplied markdown.

    Returns the saved PDF path.
    """

    return generate_pdf(
        title,
        markdown,
    )