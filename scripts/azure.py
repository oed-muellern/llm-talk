import os
import sys

from .chat import AzureChat

def main():
    chat = AzureChat(
        api_key=os.environ['AZURE_OPENAI_KEY'],
        azure_endpoint=os.environ['AZURE_OPENAI_ENDPOINT'],
        deployment_name=os.environ['AZURE_OPENAI_DEPLOYMENT'],
    )
    chat.start(context="Act as a computer science educator, assume your audience is a group of junior software engineers. The focus should be on use cases and examples of prompt engineering  best practices.")

    response = chat.send_message("""Create a list of introductory topics you should learn about large language models before using them in production. For each topic, give a reasoning why it is important for the given audience.""")
    print(response)

    response = chat.send_message("""Write the outline of a workshop that introduces large language models and prompt engineering to the given audience, based on your introductory topics.""")
    print(response)

    response = chat.send_message("""From now on, when I use the following syntax

    write ```topic```

    You will write the text for a slide based on that topic for the given audience. Wait for my first input before you start writing the first slide.""")
    print(response)

    response = chat.send_message("""write `What are large language models?`""")
    print(response)

    response = chat.send_message("""write `How do large language models work?`""")
    print(response)

    response = chat.send_message("""write `What are the benefits and limitations of large language models?`""")
    print(response)

    response = chat.send_message("""write `What is prompt engineering?`""")
    print(response)

    response = chat.send_message("""write `How can prompt engineering improve the performance of large language models?`""")
    print(response)

    response = chat.send_message("""Give me a list of important prompt pattern used for prompt engineering of large language models.""")
    print(response)

    response = chat.send_message("""For each pattern, give me a concrete example.""")
    print(response)

    response = chat.send_message("""write `What are some best practices for prompt engineering?`""")
    print(response)

    response = chat.send_message("""write `What are the ethical considerations of using large language models?`""")
    print(response)

    response = chat.send_message("""Summarise the key points of our conversation""")
    print(response)

    response = chat.send_message("""Create a list of questions and answers based on the original outline. List them in the form

    ---

    Q: QUESTION
    A: ANSWER

    ---""")
    print(response)

if __name__ == '__main__':
    sys.exit(main())