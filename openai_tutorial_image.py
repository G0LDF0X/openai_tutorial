from dotenv import load_dotenv
from openai import OpenAI
import os
from PIL import Image
import requests

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)
MODEL = "dall-e-3"

response = client.images.generate(
    model=MODEL,
    prompt="black cat with purple eyes and border collie with black eyes",
    size="1024x1024",
    quality="standard",
    n=1,
    )

image_url = response.data[0].url
print(image_url)

# 이미지 파일 저장 경로
filename = "image.jpg"

# 이미지 데이터 요청
response = requests.get(image_url)

# 이미지 파일 저장
with open(filename, "wb") as f:
    f.write(response.content)

Image.open(filename)


pass