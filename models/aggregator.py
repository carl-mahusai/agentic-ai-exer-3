from pydantic import BaseModel

class AggregatorOutput(BaseModel):
    title: str
    markdown: str