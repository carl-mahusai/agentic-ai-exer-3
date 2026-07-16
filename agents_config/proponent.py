from models.debate import DebateArguments
from agents import Agent, Runner

from tools.prompt_loader import load_prompt

instructions = load_prompt("proponent.md")

proponent_agent = Agent(
    name="Proponent Agent",
    instructions=instructions,
    output_type=DebateArguments,
)

def run(topic: str) -> DebateArguments:
    """
    Generates arguments supporting the policy topic.
    """

    result = Runner.run_sync(
        proponent_agent,
        f"Policy topic:\n{topic}",
    )

    return result.final_output