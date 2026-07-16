from models.evaluation import Evaluation


def calculate_overall_score(evaluation: Evaluation) -> float:
    """
    Calculates the average evaluation score.
    """

    return (
        evaluation.clarity
        + evaluation.fairness
        + evaluation.actionability
        + evaluation.compliance
    ) / 4


def determine_pass_fail(
    evaluation: Evaluation,
    overall_score: float,
) -> bool:
    """
    Determines whether a policy passes evaluation.

    A policy fails if:
    - Any metric is below 6.0
    - Overall score is below 6.5
    """

    metrics = [
        evaluation.clarity,
        evaluation.fairness,
        evaluation.actionability,
        evaluation.compliance,
    ]

    return (
        min(metrics) >= 6
        and overall_score >= 6.5
    )