import vertexai
from google.api_core import retry
from openai import AzureOpenAI
from vertexai.language_models import ChatModel

class AzureChat:
    def __init__(self, api_key, azure_endpoint, deployment_name):
        self.client = AzureOpenAI(
            api_key=api_key,
            api_version="2023-05-15",
            azure_endpoint=azure_endpoint,
        )
        self.conversation = []
        self.deployment_name = deployment_name


    def send_message(self, msg):
        self.conversation.append({'role': 'user', 'content': msg})

        response = self.client.chat.completions.create(
            model=self.deployment_name, messages=self.conversation
        )
        answer = response.choices[0].message.content
        self.conversation.append({'role': 'assistant', 'content': answer})

        return answer

    def start(self, context):
        self.conversation = [{'role': 'system', 'content': context}]


class GoogleChat:
    def __init__(self, project, location, parameters, model='chat-bison'):
        vertexai.init(project=project, location=location)
        self.model = ChatModel.from_pretrained(model)
        self.parameters = parameters

    @retry.Retry()
    def send_message(self, msg):
        response = self.chat.send_message(msg, **self.parameters)
        return response
    
    def start(self, context):
        self.chat = self.model.start_chat(context=context)
