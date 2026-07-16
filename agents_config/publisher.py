from agents import Agent, Runner

from models.evaluation import Evaluation
from models.policy import PolicyDocument
from models.publication import PublicationReport

from tools.evaluation import (
    calculate_overall_score,
    determine_pass_fail,
)

from tools.pdf import generate_pdf

from tools.evaluation_tools import (
    calculate_overall_score_tool,
    determine_pass_fail_tool,
)

from tools.pdf_tools import (
    generate_pdf_tool,
)

from tools.prompt_builder import build_publisher_prompt
from tools.prompt_loader import load_prompt


instructions = load_prompt("publisher.md")


publisher_agent = Agent(
    name="Publisher Agent",
    instructions=instructions,
    output_type=PublicationReport,
    tools=[
        calculate_overall_score_tool,
        determine_pass_fail_tool,
        generate_pdf_tool,
    ],
)


def run(
    policy: PolicyDocument,
    evaluation: Evaluation,
) -> PublicationReport:
    """
    Publishes a policy document.
    """

    overall_score = calculate_overall_score(
        evaluation,
    )

    passed = determine_pass_fail(
        evaluation,
        overall_score,
    )

    pdf_path = None

    if passed:
        pdf_path = generate_pdf(
            policy.title,
            policy.markdown,
        )

    prompt = build_publisher_prompt(
        policy,
        evaluation,
    )

    result = Runner.run_sync(
        publisher_agent,
        prompt,
    )

    return PublicationReport(
        overall_score=overall_score,
        passed=passed,
        pdf_path=pdf_path,
        message=result.final_output.message,
    )