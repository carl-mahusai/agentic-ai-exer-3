from models.debate import DebateArguments


def run(topic: str) -> DebateArguments:
    """
    Generates arguments opposing the policy topic.
    Placeholder implementation.
    """

    return DebateArguments(
        stance="opponent",
        arguments=[
            f"Opposing argument 1 for '{topic}'.",
            f"Opposing argument 2 for '{topic}'.",
            f"Opposing argument 3 for '{topic}'.",
        ],
    )