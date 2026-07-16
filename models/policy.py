from pydantic import BaseModel
from models.debate import DebateArguments


class PolicyDocument(BaseModel):
    title: str
    topic: str

    markdown: str

    proponent_arguments: DebateArguments
    opponent_arguments: DebateArguments