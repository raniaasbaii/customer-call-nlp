from pathlib import Path

import pandas as pd

from src.transcription import transcribe_audio, get_audio_information
from src.sentiment import analyze_sentiment
from src.entities import find_most_frequent_entity
from src.similarity import find_most_similar_text

PROJECT_ROOT = Path(__file__).resolve().parent.parent
AUDIO_PATH = PROJECT_ROOT / "data" / "sample_customer_call.wav"
CSV_PATH = PROJECT_ROOT / "data" / "customer_call_transcriptions.csv"

def main() -> None:

    # PART1 : AUDIO TRANSCCRIPTION

    #transcribe the audio
    transcript = transcribe_audio(AUDIO_PATH)
    print("Transcript:")
    print(transcript)

    #read audio technical info
    frame_rate, number_channels = get_audio_information(AUDIO_PATH)

    print("\nFrame rate: ")
    print(frame_rate)

    print('\nNumber of channels: ')
    print(number_channels)

    # PART2 : SENTIMENT ANALYSIS
   
    # Read the CSV file and convert it into a pandas DataFrame.
    calls = pd.read_csv(CSV_PATH)

    #true-positive counter
    true_positive = 0

    #go through the csv file at a time.
    for _,row in calls.iterrows():

        # get the call transcription 
        text = row["text"]

        # get the real sentiment label
        true_label = row["sentiment_label"]

        #analyze the transcription using VADER

        sentiment_result = analyze_sentiment(text)

        # Get only the predicted label from the dictionary.
        predicted_label = sentiment_result["label"]

        if true_label == "positive" and predicted_label == "positive":
            true_positive += 1


    print("\nTrue positive sentiment predictions:")
    print(true_positive)   

    # PART 3 : MOST FREQUENTS ENTITY
    most_freq_ent = find_most_frequent_entity(calls["text"])

    print("\n Most frequent named entity :")
    print(most_freq_ent)

    # PART : FIND MOST SIMILAR TEXT

    query = "wrong package delivery"
    most_similar = find_most_similar_text(query, calls["text"])

    print(f'\nMost similar transcription to "{query}" :')
    print(most_similar)

# Command to run:
# python3 -m src.main
if __name__ == "__main__":
    main()


