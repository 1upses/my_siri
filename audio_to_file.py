from pvrecorder import PvRecorder
import struct
import wave
import keyboard

def audio_to_file(filename: str, key: str) -> None:
    recorder = PvRecorder(device_index=2, frame_length=512)
    audio = []
    
    while not keyboard.is_pressed(key):
        pass

    recorder.start()
    while keyboard.is_pressed(key):
        frame = recorder.read()
        audio.extend(frame)

    recorder.stop()
    with wave.open(filename, 'wb') as f:
        f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
        f.writeframes(struct.pack("h" * len(audio), *audio))
    
    recorder.delete()

if __name__ == "__main__":
    audio_to_file("audio.wav", 'e')
