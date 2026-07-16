from dotenv import load_dotenv
load_dotenv()

import gradio as gr

from orchestrator import generate_policy_workflow


def generate_policy(topic: str):
    """
    Invoked by the Gradio interface.
    """

    if not topic.strip():
        return (
            "Please enter a policy topic.",
            {},
            "",
        )

    result = generate_policy_workflow(topic)

    return (
        result.policy.markdown,
        result.evaluation.model_dump(),
        result.publication.message,
    )


with gr.Blocks(title="Policy Brief Generator") as demo:

    gr.Markdown("# Policy Brief Generator")

    gr.Markdown(
        "Enter a policy topic below to generate a balanced policy brief."
    )

    topic_input = gr.Textbox(
        label="Policy Topic",
        placeholder="e.g. Should remote work be mandatory?",
        lines=2,
    )

    generate_button = gr.Button("Generate Policy")

    policy_output = gr.Markdown(
        label="Generated Policy"
    )

    evaluation_output = gr.JSON(
        label="Evaluation"
    )

    publisher_output = gr.Textbox(
        label="Publisher Report",
        interactive=False,
    )

    generate_button.click(
        fn=generate_policy,
        inputs=topic_input,
        outputs=[
            policy_output,
            evaluation_output,
            publisher_output,
        ],
    )


if __name__ == "__main__":
    demo.launch()