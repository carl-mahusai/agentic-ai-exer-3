from agents import Agent, Runner

from models.debate import DebateArguments
from tools.prompt_loader import load_prompt
from tools.prompt_builder import build_opponent_prompt

instructions = load_prompt("opponent.md")

opponent_agent = Agent(
    name="Opponent Agent",
    instructions=instructions,
    output_type=DebateArguments,
)


def run(topic: str) -> DebateArguments:
    """
    Generates arguments opposing the policy topic.
    """

    prompt = build_opponent_prompt(topic)

    result = Runner.run_sync(
        opponent_agent,
        prompt,
    )

    return result.final_output