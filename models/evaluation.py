from pydantic import BaseModel


class Evaluation(BaseModel):
    clarity: float
    fairness: float
    actionability: float
    compliance: float

    justification: str
    strengths: list[str]
    improvements: list[str]