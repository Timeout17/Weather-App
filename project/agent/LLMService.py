from groq import RateLimitError


class LLMServiceClass():
    @staticmethod
    def Chatservice(client: str, content: str):
        try:
            response = client.chat.completions.create(
                model = "llama-3.3-70b-versatile",
                messages = content,
                temperature = 0.5,
                max_completion_tokens = 1024,
            )


        except RateLimitError as r:
            print("API limit overloaded")
            print(r)

        return response