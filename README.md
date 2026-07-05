# Customer Call NLP Analysis

A Python project that analyzes customer-support calls using speech recognition and natural language processing.

The project performs four main tasks:

1. Transcribes a customer-support audio file.
2. Reads the audio frame rate and number of channels.
3. Performs sentiment analysis on pre-transcribed customer calls.
4. Extracts named entities and finds calls similar to a search query.

## Project Structure

```text
customer-call-nlp/
├── data/
│   ├── sample_customer_call.wav
│   └── customer_call_transcriptions.csv
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── transcription.py
│   ├── sentiment.py
│   ├── entities.py
│   └── similarity.py
│
├── tests/
├── .gitignore
├── README.md
└── requirements.txt
```

## Technologies

* Python
* pandas
* SpeechRecognition
* PyDub
* NLTK VADER
* spaCy

## Features

### Audio transcription

The program uses Google Speech Recognition through the `SpeechRecognition` Python package to convert a WAV audio file into text.

### Audio information

PyDub is used to obtain:

* the frame rate;
* the number of audio channels.

### Sentiment analysis

VADER analyzes each transcription and produces a compound sentiment score.

The sentiment thresholds are:

```text
compound >= 0.05  → positive
compound <= -0.05 → negative
otherwise         → neutral
```

The program compares VADER's prediction with the true sentiment label from the CSV file and counts true-positive predictions.

### Named entity recognition

spaCy identifies entities such as:

* people;
* dates;
* organizations;
* locations;
* products.

The project counts the entities across all transcriptions and returns the most frequent one.

### Similarity search

The query:

```text
wrong package delivery
```

is compared with all customer-call transcriptions.

The program returns the transcription with the highest spaCy similarity score.

## Installation

Clone the repository and enter the project folder:

```bash
git clone <repository-url>
cd customer-call-nlp
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Download the NLTK VADER lexicon:

```bash
python -c "import nltk; nltk.download('vader_lexicon')"
```

Download the spaCy English model:

```bash
python -m spacy download en_core_web_md
```

Install FFmpeg on macOS:

```bash
brew install ffmpeg
```

## Running the Project

From the project root, run:

```bash
python3 -m src.main
```

## Current Results

The current execution produces:

```text
Frame rate: 44100
Number of channels: 1
True positive sentiment predictions: 2
Most frequent named entity: yesterday
Most similar transcription: wrong package delivered
```

The transcription result depends on the provided audio file.

## Important Notes

The `SpeechRecognition` package is open source, but the `recognize_google()` method uses Google's online speech-recognition service.

VADER analyzes sentiment from written words. It does not analyze the speaker's tone, stress, or emotion directly.

The project is intended for learning speech processing, NLP, modular Python project organization, and Git.
