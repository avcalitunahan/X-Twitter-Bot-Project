import os 
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("ai_api_key")
messages = [ {"role": "system", 
              "content": "Intelligent assistant."}]


def ai_Configuration(horocope_number):
    horocopes = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    tweet_configuration = "Create daily horoscope tweet for this horoscope sign with Hashtags and emojis following Twitter community guidelines and use 140 characters"
    message = horocopes[horocope_number] + tweet_configuration
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        
    reply = chat.choices[0].message.content
    print(f"Byte Buddy: {reply}")
    messages.append({"role": "assistant", "content": reply})
    return reply


 
