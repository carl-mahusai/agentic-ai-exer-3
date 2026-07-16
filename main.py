from dotenv import load_dotenv
load_dotenv()

import gradio as gr

from orchestrator import generate_policy_workflow
from tools.markdown_utils import format_arguments

def generate_policy(topic: str):
    """
    Invoked by the Gradio interface.
    """

    if not topic.strip():
        return (
            "",
            "",
            "Please enter a policy topic.",
            {},
            "",
        )

    result = generate_policy_workflow(topic)

    return (
        format_arguments(
            result.policy.proponent_arguments.arguments
        ),

        format_arguments(
            result.policy.opponent_arguments.arguments
        ),

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

    with gr.Row():

        with gr.Group():
            gr.Markdown("## 👍 Proponent Arguments")
            proponent_output = gr.Markdown()

        with gr.Group():
            gr.Markdown("## 👎 Opponent Arguments")
            opponent_output = gr.Markdown()

    gr.Markdown("## 📄 Generated Policy")
    policy_output = gr.Markdown()

    gr.Markdown("## 📊 Evaluation")
    evaluation_output = gr.JSON()

    gr.Markdown("## 📢 Publisher Report")
    publisher_output = gr.Textbox(show_label=False, interactive=False)

    generate_button.click(
        fn=generate_policy,
        inputs=topic_input,
        outputs=[
            proponent_output,
            opponent_output,
            policy_output,
            evaluation_output,
            publisher_output,
        ],
    )


if __name__ == "__main__":
    demo.launch()