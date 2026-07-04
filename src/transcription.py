from pathlib import Path

from pydub import AudioSegment

import speech_recognition as sr

def get_audio_information(filename : str | Path) -> tuple[int,int]:
    """
   return the rate and the number of channels of an audio file
    
    :param filename: path to the audio file
    :type filename: str | Path
    :return: a tuple containing : frame rate and number of channels
    """

    filename = Path(filename)

    #check if th efile exists 
    if not filename.exists():
        raise FileNotFoundError(f"Audio file not found: {filename}")
    
    #load the audio file with pydub
    audio = AudioSegment.from_file(filename)

    #get number of audio samples
    frame_rate = audio.frame_rate

    #get number of channels 
    number_channels = audio.channels

    return frame_rate, number_channels


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

    #open and convert the audio file to audio data
    with audio_file as source :
        audio_data = recognizer.record(source)

    try:
        #return transcribed audio
        return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError as error :
        raise ValueError('The speech could not be understood') from error
    
    except sr.RequestError as error :
        raise RuntimeError(f"Speech-recognition service failed: {error}") from error
