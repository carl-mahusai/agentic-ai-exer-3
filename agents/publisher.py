from models.evaluation import Evaluation
from models.policy import PolicyDocument
from models.publication import PublicationReport


def run(
    policy: PolicyDocument,
    evaluation: Evaluation,
) -> PublicationReport:
    """
    Publishes the policy.
    Placeholder implementation.
    """

    return PublicationReport(
        overall_score=8.0,
        passed=True,
        pdf_path=None,
        message="Publisher placeholder executed successfully.",
    )