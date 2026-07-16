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

    supporting_arguments = "\n".join(
        f"- {argument}"
        for argument in proponent.arguments
    )

    opposing_arguments = "\n".join(
        f"- {argument}"
        for argument in opponent.arguments
    )

    markdown = f"""# {topic}    

## Policy

This is a placeholder compromise policy.

## Supporting Arguments

{supporting_arguments}

## Opposing Arguments

{opposing_arguments}

## Justification

This policy attempts to balance both viewpoints.
"""

    print(markdown)

    return PolicyDocument(
        title=topic,
        markdown=markdown,
    )