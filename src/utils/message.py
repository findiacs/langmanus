from typing import Dict, Any, Tuple, Optional


def extract_message_chunks(chunk: Any) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract content and reasoning content from a message chunk.

    Args:
        chunk: The message chunk object, typically from a LangChain stream event.

    Returns:
        A tuple of (content, reasoning_content).
    """
    content = getattr(chunk, "content", "")
    reasoning_content = None

    if hasattr(chunk, "additional_kwargs"):
        reasoning_content = chunk.additional_kwargs.get("reasoning_content")

    return content, reasoning_content
