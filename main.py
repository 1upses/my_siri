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
    messages = [{"role": "system", "content": "Une assistante vocal à l'image de siri ou google assistant, elle est créative, intelligente, et amicale, ses réponses sont courtes et vont droit au but. Cette assistante doit se rappeller de sa nature d'assistante vocale, et devra répondre de la sorte; si elle veut dire \"2^3\" par exemple, elle dira plutôt \"deux puissance trois\"."}]
    while True:
        user_input:str = generate_input()
        print(f"entrée utilisateur: {user_input}\n")
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)
        reply = response["choices"][0]["message"]["content"]
        print(f"réponse de my_siri: {reply}\n")
        messages.append({"role": "system", "content": reply})
        text_to_speech(reply)
