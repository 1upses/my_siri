from audio_to_file import audio_to_file
from audio_to_text import audio_to_text
from text_to_speech import text_to_speech
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_input() -> str:
    audio_to_file("input.wav", 'e')
    return audio_to_text("input.wav")

if __name__ == "__main__":
    messages = [{"role": "system", "content": "Un assistant vocal à l'image de siri ou google assistant, il est créatif, intelligent, et amical, ses réponses sont courtes et vont droit au but"}]
    while True:
        messages.append({"role": "user", "content": generate_input()})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "system", "content": reply})
        text_to_speech(reply)
