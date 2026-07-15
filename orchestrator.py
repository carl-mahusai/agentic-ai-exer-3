from models.policy_generation_result import (
    PolicyGenerationResult,
    PolicyDocument,
    Evaluation,
    PublicationReport,
)


def generate_policy_workflow(topic: str) -> PolicyGenerationResult:
    """
    Coordinates the policy generation workflow.

    Eventually this will:
        1. Call Proponent Agent
        2. Call Opponent Agent
        3. Call Aggregator Agent
        4. Call Evaluator Agent
        5. Call Publisher Agent
    """

    policy = PolicyDocument(
        title="Placeholder Policy",
        markdown=f"# {topic}\n\nPolicy generation successful.",
    )

    evaluation = Evaluation(
        clarity=0.0,
        fairness=0.0,
        actionability=0.0,
        compliance=0.0,
        justification="Placeholder evaluation.",
        strengths=[],
        improvements=[],
    )

    publication = PublicationReport(
        overall_score=0.0,
        passed=False,
        pdf_path=None,
        message="Publisher has not yet been implemented.",
    )

    return PolicyGenerationResult(
        policy=policy,
        evaluation=evaluation,
        publication=publication,
    )