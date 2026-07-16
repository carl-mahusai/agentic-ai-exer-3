from agents import Agent, Runner

from models.debate import DebateArguments
from models.policy import PolicyDocument
from models.aggregator import AggregatorOutput

from tools.prompt_loader import load_prompt
from tools.prompt_builder import build_aggregator_prompt


instructions = load_prompt("aggregator.md")

aggregator_agent = Agent(
    name="Aggregator Agent",
    instructions=instructions,
    output_type=AggregatorOutput,
)


def run(
    topic: str,
    proponent: DebateArguments,
    opponent: DebateArguments,
) -> PolicyDocument:
    """
    Generates a balanced policy document.
    """

    prompt = build_aggregator_prompt(
        topic,
        proponent,
        opponent,
    )

    result = Runner.run_sync(
        aggregator_agent,
        prompt,
    )

    return PolicyDocument(
        title=result.final_output.title,
        topic=topic,
        markdown=result.final_output.markdown,
        proponent_arguments=proponent,
        opponent_arguments=opponent,
    )