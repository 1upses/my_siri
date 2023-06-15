from pvrecorder import PvRecorder

for index, device in enumerate(PvRecorder.get_audio_devices()):
    print(f"[{index}] {device}")
