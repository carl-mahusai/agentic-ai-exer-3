from agents import (
    run_aggregator,
    run_evaluator,
    run_opponent,
    run_proponent,
    run_publisher,
)

from models.workflow import PolicyGenerationResult


def generate_policy_workflow(topic: str) -> PolicyGenerationResult:

    proponent = run_proponent(topic)

    opponent = run_opponent(topic)

    policy = run_aggregator(
        topic,
        proponent,
        opponent,
    )

    evaluation = run_evaluator(policy)

    publication = run_publisher(
        policy,
        evaluation,
    )

    return PolicyGenerationResult(
        policy=policy,
        evaluation=evaluation,
        publication=publication,
    )