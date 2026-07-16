from agents import Agent, Runner

from models.evaluation import Evaluation
from models.policy import PolicyDocument
from models.publication import PublicationReport

from tools.prompt_loader import load_prompt
from tools.prompt_builder import build_publisher_prompt


instructions = load_prompt("publisher.md")

publisher_agent = Agent(
    name="Publisher Agent",
    instructions=instructions,
    output_type=PublicationReport,
)


def run(
    policy: PolicyDocument,
    evaluation: Evaluation,
) -> PublicationReport:
    """
    Publishes a policy document.
    """

    prompt = build_publisher_prompt(
        policy,
        evaluation,
    )

    result = Runner.run_sync(
        publisher_agent,
        prompt,
    )

    return result.final_output