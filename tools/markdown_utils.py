def format_arguments(arguments: list[str]) -> str:
    """
    Converts a list of arguments into Markdown bullet points.
    """

    return "\n".join(
        f"- {argument}"
        for argument in arguments
    )