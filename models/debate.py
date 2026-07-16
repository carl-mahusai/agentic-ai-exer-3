from pydantic import BaseModel
from enum import Enum

class Stance(str, Enum):
    PROPONENT = "proponent"
    OPPONENT = "opponent"

class DebateArguments(BaseModel):
    stance: Stance
    arguments: list[str]