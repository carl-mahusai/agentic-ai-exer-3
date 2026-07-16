from agents import Agent, Runner

from models.evaluation import Evaluation
from models.policy import PolicyDocument
from tools.prompt_loader import load_prompt


instructions = load_prompt("evaluator.md")

evaluator_agent = Agent(
    name="Evaluator Agent",
    instructions=instructions,
    output_type=Evaluation,
)


def run(policy: PolicyDocument) -> Evaluation:
    """
    Evaluates the generated policy.
    """

    prompt = f"""
Evaluate the following policy document.

Title:
{policy.title}

Markdown:

{policy.markdown}
"""

    result = Runner.run_sync(
        evaluator_agent,
        prompt,
    )

    return result.final_output