from pathlib import Path


PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


def load_prompt(filename: str) -> str:
    """
    Load a prompt file from the prompts directory.

    Args:
        filename: Name of the prompt file (e.g. "proponent.md")

    Returns:
        The prompt contents as a string.
    """
    return (PROMPTS_DIR / filename).read_text(encoding="utf-8")