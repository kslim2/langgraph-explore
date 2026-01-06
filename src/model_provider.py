from transformers import pipeline
from dotenv import load_dotenv

import os

class ModelProvider:

    def __init__(self):
        load_dotenv()

    def pipeline(self):
        pipe = pipeline(os.getenv("PURPOSE"), model=os.getenv("MODEL"))
        message = [
            {
                "role": "user",
                "content": "Who are you?",
            }
        ]
        pipe(message)

    def __str__(self):
        return f"{os.getenv("PURPOSE")}: {os.getenv("MODEL")}"


model = ModelProvider()
print(model)
print(model.pipeline())