from models.debate import DebateArguments
from models.evaluation import Evaluation
from models.policy import PolicyDocument

def format_bullets(items: list[str]) -> str:
    """
    Formats a list of strings as a Markdown bullet list.
    """

    if not items:
        return "None"

    return "\n".join(
        f"- {item}"
        for item in items
    )

def build_aggregator_prompt(
    topic: str,
    proponent: DebateArguments,
    opponent: DebateArguments,
) -> str:
    """
    Builds the prompt for the Aggregator Agent.
    """

    # supporting_arguments = "\n".join(
    #     f"- {argument}"
    #     for argument in proponent.arguments
    # )

    # opposing_arguments = "\n".join(
    #     f"- {argument}"
    #     for argument in opponent.arguments
    # )

    supporting_arguments = format_bullets(proponent.arguments)

    opposing_arguments = format_bullets(opponent.arguments)

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



def build_publisher_prompt(
    policy: PolicyDocument,
    evaluation: Evaluation,
    overall_score: float,
    passed: bool,
    pdf_path: str | None,
) -> str:

    status = "PASS" if passed else "FAIL"

    pdf_location = pdf_path if pdf_path else "No PDF generated."

    return f"""
Policy Title:
{policy.title}

Policy Document:

{policy.markdown}

Evaluation Scores

Clarity: {evaluation.clarity}
Fairness: {evaluation.fairness}
Actionability: {evaluation.actionability}
Compliance: {evaluation.compliance}

Overall Score:
{overall_score:.2f}

Status:
{status}

PDF Location:
{pdf_location}

Evaluator Feedback

Justification:
{evaluation.justification}

Strengths:
{format_bullets(evaluation.strengths)}

Improvements:
{format_bullets(evaluation.improvements)}
"""


def build_proponent_prompt(topic: str) -> str:
    return f"Policy topic:\n{topic}"

def build_opponent_prompt(topic: str) -> str:
    return f"Policy topic:\n{topic}"