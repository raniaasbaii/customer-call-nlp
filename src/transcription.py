from pathlib import Path
import speech_recognition as sr

def transcribe_audio(filename : str | Path) -> str :
    """Convert a wav audio into text using google speech recognition.
    audio_path as the argument : path to the audio
    return a string of the transcribed audio
    
    raises  :
        FileNotFoundError: If the audio file does not exist.
        ValueError: If the speech cannot be understood.
        RuntimeError: If the recognition service is unavailable.
    """
    
    filename = Path(filename)

    if not filename.exists():
        raise FileNotFoundError(f"Audio file not found {filename}")
    
    # setup a recognizer instance
    recognizer = sr.Recognizer()

    # import the audio
    audio_file = sr.AudioFile(str(filename))

    #convert the audio file to audio data
    with audio_file as source :
        audio_data = recognizer.record(source)

    try:
        #return transcribed audio
        return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError as error :
        raise ValueError('The speech could not be understood') from error
    
    except sr.RequestError as error :
        raise RuntimeError(f"Speech-recognition service failed: {error}") from error
