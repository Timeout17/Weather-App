from unittest.mock import patch

from project.agent.CreateAgent import CreateClient


@patch("project.agent.CreateAgent.Groq")
def test_make_client(mock_groq):

    CreateClient.make_client()

    mock_groq.assert_called_once()