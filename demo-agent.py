import os
from huggingface_hub import InferenceClient, login
from dotenv import load_dotenv 

# login(token="hf_**")

HF_TOKEN = os.environ.get("HF_TOKEN")

client = InferenceClient(model="moonshotai/Kimi-K2.5")

output = client.chat.completions.create(
    messages=[{"role": "user",
               "content": "The capital of France is"},],
               stream=False,
               max_tokens=1024,
               extra_body={'thinking':{'type':'disabled'}}
)
print(output.choices[0].message.content)