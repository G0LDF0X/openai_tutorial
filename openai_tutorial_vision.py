from dotenv import load_dotenv
from openai import OpenAI
import os
from PIL import Image
import requests

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)
MODEL = "gpt-4-vision-preview"

response = client.chat.completions.create(
  model=MODEL,
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "이 이미지는 무슨 내용이니?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2019/01/07/11/bunny-rabbit.jpg?width=1200&height=1200&fit=crop",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
pass