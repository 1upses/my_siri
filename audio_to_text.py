import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def audio_to_text(filename: str) -> None:
    audio_file = open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]

if __name__ == "__main__":
    text = audio_to_text("audio.wav")
    print(text)