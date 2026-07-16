from models.evaluation import Evaluation
from models.policy import PolicyDocument


def run(policy: PolicyDocument) -> Evaluation:
    """
    Evaluates the generated policy.
    Placeholder implementation.
    """

    return Evaluation(
        clarity=8.0,
        fairness=8.0,
        actionability=8.0,
        compliance=8.0,
        justification="Placeholder evaluation.",
        strengths=[
            "Balanced structure.",
            "Readable formatting.",
        ],
        improvements=[
            "Replace placeholder content.",
        ],
    )