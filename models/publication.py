from pydantic import BaseModel

class PublicationReport(BaseModel):
    """
    Result of the publication stage.
    """
    overall_score: float
    passed: bool
    pdf_path: str | None
    message: str

