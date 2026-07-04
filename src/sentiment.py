from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

POSITIVE_THRESHOLD = 0.05
NEGATIVE_THRESHOLD = -0.05

def classify_sentiment(compound_score: float) -> str:
    """
    convert a VADER compound score into a sentimal label
    
    :param compound_score: decimal between -1 and 1
    :type compound_score: float
    :return: sentiment label: positive, negative, neutral

    """
    if compound_score >= POSITIVE_THRESHOLD :
        return "positive"
    elif compound_score <= NEGATIVE_THRESHOLD :
        return "negative"
    else :
        return "neutral"


def analyze_sentiment(text: str) -> dict[str, float| str] :
    """
        analyse the sentiment of the text using vader 
        Args : text to be ananyzed.
        returns : a dict with the sentiment scores and sentiment label.
    """
    #create and analyzer object
    analyzer = SentimentIntensityAnalyzer()

    #analyse the text -> return a dict
    scores = analyzer.polarity_scores(text)

    #get the compound score only
    compound_score = scores["compound"]

    #convert the compund score into label
    label = classify_sentiment(compound_score)

    #return all the usefull results
    return {
        "negative": scores["neg"],
        "neutral" : scores["neu"],
        "positive": scores["pos"],
        "compound": compound_score,
        "label":label,
    }








