import os
from dotenv import load_dotenv
from openai import OpenAI

# pip install openai
load_dotenv()


# api_key = os.getenv("OPENAI_API_KEY")
#
# print("OPENAI_API_KEY=", api_key)

class ChatBot:
    # def __init__(self, model="gpt-3.5-turbo"):
    def __init__(self, model="gpt-4.1"):
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
        # print(response)

        model_message = response.choices[0].message.content
        self.add_message("assistant", model_message)  # dodanie do pamieci konwersacji tej odpowiedzi
        return model_message


bot = ChatBot()

if __name__ == '__main__':
    print("Starting")
    # print(bot.get_response("Opisz Comarch"))
# ChatCompletion(id='chatcmpl-D9T3pKg2VSJgdwQxVtLnUV7U74n6N',
# choices=[Choice(finish_reason='stop', index=0, logprobs=None,
# message=ChatCompletionMessage(content='Comarch to globalna firma specjalizująca się
# w dostarczaniu innowacyjnych rozwiązań IT dla firm z różnych branż.
# Firma została założona w 1993 roku w Polsce i od tego czasu dynamicznie się rozwija.
# Obecnie Comarch zatrudnia ponad 6000 pracowników i ma swoje oddziały w kilkudziesięciu krajach na całym świecie.
# \n\nComarch oferuje szeroki zakres produktów i usług, w tym systemy ERP, CRM,
# Business Intelligence, systemy zarządzania relacjami z klientami, systemy informatyczne dla sektora finansowego,
# telekomunikacyjnego, zdrowotnego oraz energetycznego.
# Firma specjalizuje się również w dostarczaniu rozwiązań z zakresu e-commerce,
# rozwoju oprogramowania dedykowanego oraz usług chmury obliczeniowej.
# \n\nComarch ceniony jest za wysoką jakość swoich produktów, innowacyjność,
# elastyczne podejście do klienta oraz zaangażowanie w rozwój technologii.
# Firma regularnie zdobywa nagrody i wyróżnienia za swoje produkty i usługi,
# co potwierdza jej pozycję jako wiodącego dostawcy rozwiązań IT na rynku światowym.',
# refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))],
# created=1771149033, model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default',
# system_fingerprint=None, usage=CompletionUsage(completion_tokens=325, prompt_tokens=11, total_tokens=336,
# completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0,
# audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0),
# prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))

# bot.get_models()

print(bot.get_response("Opisz Comarch"))
print(bot.get_response("Kto jest właścicielem?"))
