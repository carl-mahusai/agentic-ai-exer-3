from models.debate import DebateArguments
from models.policy import PolicyDocument


def run(
    topic: str,
    proponent: DebateArguments,
    opponent: DebateArguments,
) -> PolicyDocument:
    """
    Produces a balanced policy document.
    Placeholder implementation.
    """

    markdown = f"""# {topic}

## Policy

This is a placeholder compromise policy.

## Supporting Arguments

{chr(10).join(f"- {arg}" for arg in proponent.arguments)}

## Opposing Arguments

{chr(10).join(f"- {arg}" for arg in opponent.arguments)}

## Justification

This policy attempts to balance both viewpoints.
"""

    return PolicyDocument(
        title=topic,
        markdown=markdown,
    )