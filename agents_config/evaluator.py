from agents import Agent, Runner

from models.evaluation import Evaluation
from models.policy import PolicyDocument

from tools.prompt_loader import load_prompt
from tools.prompt_builder import build_evaluator_prompt


instructions = load_prompt("evaluator.md")

evaluator_agent = Agent(
    name="Evaluator Agent",
    instructions=instructions,
    output_type=Evaluation,
)


def run(
    policy: PolicyDocument,
) -> Evaluation:
    """
    Evaluates a generated policy.
    """

    prompt = build_evaluator_prompt(
        policy,
    )

    result = Runner.run_sync(
        evaluator_agent,
        prompt,
    )

    return result.final_output