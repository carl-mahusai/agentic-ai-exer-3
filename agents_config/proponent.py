from models.debate import DebateArguments
from agents import Agent, Runner

from tools.prompt_loader import load_prompt
from tools.prompt_builder import build_proponent_prompt

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

    prompt = build_proponent_prompt(topic)

    result = Runner.run_sync(
        proponent_agent,
        prompt,
    )

    return result.final_output