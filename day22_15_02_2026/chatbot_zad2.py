import os
from dotenv import load_dotenv
from openai import OpenAI

# pip install openai
load_dotenv()


# api_key = os.getenv("OPENAI_API_KEY")
#
# print("OPENAI_API_KEY=", api_key)

class ChatBot:
    def __init__(self, model="gpt-3.5-turbo"):
        """
        ChatBot w pythonie
        :param model:
        """
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)
        self.message = []
        self.model = model

    def add_message(self, role, content):
        if role in ['user', 'assistant']:
            self.message.append(
                {"role": role, "content": content}
            )
        else:
            raise ValueError("Role must be 'user' or 'assistant'!")

    def get_models(self):
        print([m.id for m in self.client.models.list().data])

    def get_response(self, user_message):
        self.add_message("user", user_message)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.message
        )
        print(response)
