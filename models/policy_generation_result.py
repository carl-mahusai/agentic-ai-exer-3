from pydantic import BaseModel


class PolicyDocument(BaseModel):
    title: str
    markdown: str


class Evaluation(BaseModel):
    clarity: float
    fairness: float
    actionability: float
    compliance: float

    justification: str
    strengths: list[str]
    improvements: list[str]


class PublicationReport(BaseModel):
    overall_score: float
    passed: bool
    pdf_path: str | None
    message: str


class PolicyGenerationResult(BaseModel):
    policy: PolicyDocument
    evaluation: Evaluation
    publication: PublicationReport