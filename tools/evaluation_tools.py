from agents import function_tool

from models.evaluation import Evaluation

from tools.evaluation import (
    calculate_overall_score,
    determine_pass_fail,
)


@function_tool
def calculate_overall_score_tool(
    evaluation: Evaluation,
) -> float:
    """
    Calculates the overall evaluation score.
    """

    return calculate_overall_score(evaluation)


@function_tool
def determine_pass_fail_tool(
    evaluation: Evaluation,
    overall_score: float,
) -> bool:
    """
    Determines whether the policy passes evaluation.
    """

    return determine_pass_fail(
        evaluation,
        overall_score,
    )