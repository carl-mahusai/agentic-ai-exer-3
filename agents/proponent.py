from models.debate import DebateArguments


def run(topic: str) -> DebateArguments:
    """
    Generates arguments supporting the policy topic.
    Placeholder implementation.
    """

    return DebateArguments(
        stance="proponent",
        arguments=[
            f"Supporting argument 1 for '{topic}'.",
            f"Supporting argument 2 for '{topic}'.",
            f"Supporting argument 3 for '{topic}'.",
        ],
    )