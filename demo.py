import json

import openai
from pydantic import BaseModel, Field
client = openai.Client(base_url=f"http://127.0.0.1:30000/v1", api_key="None")

model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"

# Define the schema using Pydantic
class Answer(BaseModel):
    name: str = Field(..., pattern=r"^\w+$", description="Name of the answer")
    ans: int = Field(..., description="integer anwser")

response_non_stream = client.chat.completions.create(
    model=model_name,
    messages=[
        {
            "role": "user",
            "content": "What is 1+4?",
        }
    ],
    temperature=0,
    top_p=0.95,
    stream=False,  # Non-streaming
    max_tokens=2048,
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "foo",
            # convert the pydantic model to json schema
            "schema": Answer.model_json_schema(),
        },
    },
    extra_body={"separate_reasoning": True},
)
print("==== Reasoning ====")
print(response_non_stream.choices[0].message.reasoning_content)
print("==== Text ====")
print(response_non_stream.choices[0].message.content)