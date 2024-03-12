from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)
MODEL = "gpt-3.5-turbo"

data = ["편하게 입기 좋아요. 비친다고 해서 검은색 구매했는데 흰색이 더 예쁜 것 같아요. 56kg 배부분 고무줄이 쫄려요. 날씬한 사람이 입어야 예쁠듯. 치마가 두겹정도로 속치마가 있었으면 좋겠어요", "저렴한가격에 득템! 만삭임산부임다,, 키는 153인데 발목까지 오고 배쪼임없고 아주 맘에 들어용! 봄에 딱 입기조아요! 가디건색상이이쁜데 카메라에 안담기네영 ㅠ 저렴한가격에 둘다득템! 배송도 짱빨라요", "옷에서 냄새가 좀 나네요 배송은 빠릅니다 ~", "이뻐 보였는데.. 너무 임부복 같네요. 저 몸매가 날씬하지는 않지만 그래도 좀 심해요ㅠ 옷도 너무 바스락 거리네요^^", "크림 색상이 너무 예뻐요 속치마는 꼭 입어야 할 것 같아요"]
data_list = []
for review in data:
    data_list.append({"type": "text", "text": review})

response = client.chat.completions.create(
      model=MODEL,
      top_p=0.1,
      temperature=0.1,
      messages=[{"role": "system", "content": "고객이 남긴 후기를 보고 각각 개인의 만족도를 요약해서 파악해줘. list 원소 하나당 고객 개인이 남긴 후기야."},
                {"role": "user", "content": data_list}]
  )


print(response.choices[0].message.content)