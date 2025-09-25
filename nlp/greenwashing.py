# common vague / weasel phrases
WEASEL_PHRASES = [
    "committed to",
    "aims to",
    "strives for",
    "plans to",
    "focused on",
    "dedicated to",
    "working towards",
    "seeks to",
    "endeavor to"
]

def detect_greenwashing(tagged_sentence):
    """
    input: dict with 'sentence' and 'entities' fields
    output: dict with added 'greenwashing' field
    """
    sentence = tagged_sentence.get('sentence', '').lower()
    entities = tagged_sentence.get('entities', [])

    greenwash_flag = False
    if not entities:
        for phrase in WEASEL_PHRASES:
            if phrase in sentence:
                greenwash_flag = True
                break

    tagged_sentence['greenwashing'] = greenwash_flag
    return tagged_sentence