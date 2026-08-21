from groq import RateLimitError


class LLMServiceClass():
    @staticmethod
    def Chatservice(client: str, content: str):
        try:
            response = client.chat.completions.create(
                model = "openai/gpt-oss-20b",
                messages = content,
                temperature = 0.5,
                max_completion_tokens = 4096,
            )


        except RateLimitError as r:
            print("API limit overloaded")
            print(r)

        return response