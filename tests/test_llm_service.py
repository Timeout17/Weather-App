from unittest.mock import Mock

from project.agent.LLMService import LLMServiceClass


def test_chatservice():

    mock_client = Mock()

    mock_response = Mock()
    mock_response.choices = ["test response"]

    mock_client.chat.completions.create.return_value = mock_response

    messages = [
        {
            "role": "system",
            "content": "Válaszolj magyarul."
        },
        {
            "role": "user",
            "content": "Milyen idő van?"
        }
    ]

    result = LLMServiceClass.Chatservice(
        mock_client,
        messages
    )

    mock_client.chat.completions.create.assert_called_once_with(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=0.5,
        max_completion_tokens=4096,
    )

    assert result == mock_response