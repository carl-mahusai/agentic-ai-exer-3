from agents import Agent, Runner

from models.evaluation import Evaluation
from models.policy import PolicyDocument
from models.publication import PublicationReport
from tools.prompt_loader import load_prompt


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
    Publishes the policy.
    """

    prompt = f"""
Policy Title:
{policy.title}

Evaluation

Clarity: {evaluation.clarity}
Fairness: {evaluation.fairness}
Actionability: {evaluation.actionability}
Compliance: {evaluation.compliance}

Justification:
{evaluation.justification}

Strengths:
{"\n".join(f"- {item}" for item in evaluation.strengths)}

Improvements:
{"\n".join(f"- {item}" for item in evaluation.improvements)}
"""

    result = Runner.run_sync(
        publisher_agent,
        prompt,
    )

    return result.final_output