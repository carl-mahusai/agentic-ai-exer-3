from models.debate import DebateArguments
from models.evaluation import Evaluation
from models.policy import PolicyDocument


def build_aggregator_prompt(
    topic: str,
    proponent: DebateArguments,
    opponent: DebateArguments,
) -> str:
    """
    Builds the prompt for the Aggregator Agent.
    """

    supporting_arguments = "\n".join(
        f"- {argument}"
        for argument in proponent.arguments
    )

    opposing_arguments = "\n".join(
        f"- {argument}"
        for argument in opponent.arguments
    )

    return f"""
Policy Topic:
{topic}

Supporting Arguments:
{supporting_arguments}

Opposing Arguments:
{opposing_arguments}
""".strip()


def build_evaluator_prompt(
    policy: PolicyDocument,
) -> str:
    """
    Builds the prompt for the Evaluator Agent.
    """

    return f"""
Evaluate the following policy document.

Title:
{policy.title}

Policy:

{policy.markdown}
""".strip()


from models.evaluation import Evaluation
from models.policy import PolicyDocument


def build_publisher_prompt(
    policy: PolicyDocument,
    evaluation: Evaluation,
) -> str:
    """
    Builds the prompt for the Publisher Agent.
    """

    return f"""
Policy Title:
{policy.title}

Policy Topic:
{policy.topic}

Policy Document:

{policy.markdown}

Evaluation Scores

Clarity: {evaluation.clarity}

Fairness: {evaluation.fairness}

Actionability: {evaluation.actionability}

Compliance: {evaluation.compliance}

Evaluator Feedback

Justification:
{evaluation.justification}

Strengths:
{"\n".join(f"- {strength}" for strength in evaluation.strengths)}

Improvements:
{"\n".join(f"- {improvement}" for improvement in evaluation.improvements)}
"""


def build_proponent_prompt(topic: str) -> str:
    return f"Policy topic:\n{topic}"

def build_opponent_prompt(topic: str) -> str:
    return f"Policy topic:\n{topic}"