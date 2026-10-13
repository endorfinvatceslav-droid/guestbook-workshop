import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import Message


def test_message():
    message = Message(author="Slava", text="Hello")
    assert message.author == "Slava"
    assert message.text == "Hello"