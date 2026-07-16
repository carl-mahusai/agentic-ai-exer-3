from pydantic import BaseModel

from .policy import PolicyDocument
from .evaluation import Evaluation
from .publication import PublicationReport


class PolicyGenerationResult(BaseModel):
    policy: PolicyDocument
    evaluation: Evaluation
    publication: PublicationReport