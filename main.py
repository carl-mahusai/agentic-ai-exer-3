import gradio as gr


def generate_policy(topic: str) -> str:
    """
    Placeholder function.
    Later, this will call your multi-agent workflow.
    """
    if not topic.strip():
        return "Please enter a policy topic."

    # TODO: Call the policy generation workflow here.
    return "Policy generation successful"


with gr.Blocks(title="Policy Brief Generator") as demo:
    gr.Markdown("# Policy Brief Generator")
    gr.Markdown(
        "Enter a policy topic below to generate a balanced policy brief."
    )

    with gr.Row():
        topic_input = gr.Textbox(
            label="Policy Topic",
            placeholder="e.g. Should remote work be mandatory?",
            lines=2,
        )

    generate_button = gr.Button("Generate Policy")

    output = gr.Textbox(
        label="Status",
        interactive=False,
    )

    generate_button.click(
        fn=generate_policy,
        inputs=topic_input,
        outputs=output,
    )

if __name__ == "__main__":
    demo.launch()