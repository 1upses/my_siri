from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def text_to_speech(text: str) -> None:
    tts = gTTS(text=text, lang="fr", slow=False)
    tts.save("output.mp3")
    audio = AudioSegment.from_mp3("output.mp3")
    audio.speedup(playback_speed=1.3).export("output.mp3", format="mp3")
    audio = AudioSegment.from_mp3("output.mp3")
    play(audio)
