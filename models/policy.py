from pydantic import BaseModel


class PolicyDocument(BaseModel):
    title: str
    markdown: str