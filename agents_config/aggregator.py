from agents import Agent, Runner

from models.debate import DebateArguments
from models.policy import PolicyDocument
from tools.prompt_loader import load_prompt


instructions = load_prompt("aggregator.md")

aggregator_agent = Agent(
    name="Aggregator Agent",
    instructions=instructions,
    output_type=PolicyDocument,
)


def run(
    topic: str,
    proponent: DebateArguments,
    opponent: DebateArguments,
) -> PolicyDocument:
    """
    Generates a balanced policy document.
    """

    supporting_arguments = "\n".join(
        f"- {argument}"
        for argument in proponent.arguments
    )

    opposing_arguments = "\n".join(
        f"- {argument}"
        for argument in opponent.arguments
    )

    prompt = f"""
Policy Topic:
{topic}

Supporting Arguments:
{supporting_arguments}

Opposing Arguments:
{opposing_arguments}
"""

    result = Runner.run_sync(
        aggregator_agent,
        prompt,
    )

    return result.final_output