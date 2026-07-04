from pathlib import Path

from transcription import transcribe_audio

PROJECT_ROOT = Path(__file__).resolve().parent.parent
AUDIO_PATH = PROJECT_ROOT / "data" / "sample_customer_call.wav"

def main() -> None:
    transcript = transcribe_audio(AUDIO_PATH)
    print("Transcript:")
    print(transcript)

if __name__ == "__main__":
    main()


