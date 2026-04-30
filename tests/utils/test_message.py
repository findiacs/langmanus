from src.utils.message import extract_message_chunks
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class MockChunk:
    content: str = ""
    additional_kwargs: Dict[str, Any] = field(default_factory=dict)
    id: str = "test_id"

def test_extract_message_chunks_content():
    chunk = MockChunk(content="hello")
    content, reasoning = extract_message_chunks(chunk)
    assert content == "hello"
    assert reasoning is None

def test_extract_message_chunks_reasoning():
    chunk = MockChunk(content="", additional_kwargs={"reasoning_content": "thinking"})
    content, reasoning = extract_message_chunks(chunk)
    assert content == ""
    assert reasoning == "thinking"

def test_extract_message_chunks_both():
    chunk = MockChunk(content="hello", additional_kwargs={"reasoning_content": "thinking"})
    content, reasoning = extract_message_chunks(chunk)
    assert content == "hello"
    assert reasoning == "thinking"

def test_extract_message_chunks_empty():
    chunk = MockChunk(content="")
    content, reasoning = extract_message_chunks(chunk)
    assert content == ""
    assert reasoning is None
