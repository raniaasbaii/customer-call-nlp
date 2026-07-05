from collections import Counter

import spacy

def find_most_frequent_entity(texts) -> str:
    """
    Find and return the most frequently occurring named entity
    across all customer call transcriptions.
    """

    #load the english spaCy model
    nlp = spacy.load("en_core_web_md")

     # Counter will store how many times each entity appears.
    entity_counts = Counter()

    #go through each transcription
    for text in texts:
        #process the text with spaCy
        document = nlp(str(text))

        #document.ents contains the named entities found
        for entity in document.ents:
            #convert to lower case first
            normalized_entity = entity.text.strip().lower()

            if normalized_entity :
                entity_counts[normalized_entity] += 1

    #if spaCy find no entities raise an error.
    if not entity_counts:
            raise ValueError('No named entities were found.') 
    

    most_freq_ent = entity_counts.most_common(1)[0][0]

    return most_freq_ent

        


