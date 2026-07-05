import spacy

def find_most_similar_text(query:str, texts) -> str:
    """
    Find the transcription that is most similar to a given query.

    Args:
        query:
            The sentence we want to compare with the customer calls.

        texts:
            A collection of customer call transcriptions,
            usually the "text" column from the CSV.

    Returns:
        The full transcription with the highest similarity score.
    """

    # Load the medium English spaCy model. (medium model include word vectors-> help comparing word vectors)
    nlp = spacy.load("en_core_web_md")
    
     # Convert the query into a spaCy Document object.
    query_doc = nlp(str(query))

    # This variable will store the most similar transcription found.
    most_similar_text = ""
    #similarity score
    highest_similarity = -1.0

    for text in texts:
        #convert the current value to string (in case text containing non strong value)
        text = str(text)

        #convert text to spacy doc
        text_doc = nlp(text)
        
        # Compare the query with the current transcription.
        # A higher score means the texts are more similar.
        similarity_score = query_doc.similarity(text_doc)

        # If this transcription is more similar than every previous transcription
        if similarity_score > highest_similarity:
            #save the new high score
            highest_similarity = similarity_score

            #save the corresponding transcription
            most_similar_text = text
    
    # Return the full transcription with the highest score.
    return most_similar_text        




