import openai
from pydantic import BaseModel, Field
client = openai.Client(base_url=f"http://127.0.0.1:30000/v1", api_key="None")

class CapitalInfo(BaseModel):
    name: str = Field(..., description="Name of the country")
    population: int = Field(..., description="Population of the capital city")

model_name = "/home/tianhaoyu/.cache/modelscope/hub/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"

response = client.chat.completions.create(
    model=model_name,
    messages=[
        {
            "role": "user",
            "content": "Please generate the information of the capital of France in the JSON format"
        }
    ],
    temperature=0,
    max_tokens=2048,
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "foo",
            "schema": CapitalInfo.model_json_schema(),
        },
    },
)

print(response.choices[0].message.content)
print(response.choices[0].message.reasoning_content)
