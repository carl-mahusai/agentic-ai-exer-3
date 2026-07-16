from pydantic import BaseModel


class DebateArguments(BaseModel):
    stance: str
    arguments: list[str]