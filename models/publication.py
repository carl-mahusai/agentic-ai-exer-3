from pydantic import BaseModel


class PublicationReport(BaseModel):
    overall_score: float
    passed: bool
    pdf_path: str | None
    message: str