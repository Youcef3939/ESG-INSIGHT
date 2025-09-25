import re

UNITS = ["%", "tons", "kwh", "employees", "million", "billion"]

ESG_KEYWORDS = [
    "carbon emissions",
    "renewable energy",
    "water usage",
    "biodiversity",
    "diversity",
    "inclusion",
    "energy consumption",
    "waste reduction",
    "co2",
    "ghg"
]

def extract_entities(sentence):
    """
    extract measurable ESG entities from a sentence
    returns a list of dicts: [{'entity': ..., 'value': ..., 'unit': ...}, ...]
    """
    entities = []

    pattern = r"(\d+(?:\.\d+)?)(\s*(?:%|tons|kwh|employees|million|billion))?"
    matches = re.findall(pattern, sentence, flags=re.IGNORECASE)

    for match in matches:
        value = match[0]
        unit = match[1].strip() if match[1] else None

        entity = None
        for keyword in ESG_KEYWORDS:
            if keyword in sentence.lower():
                entity = keyword
                break
        if not entity:
            entity = "Unknown"

        entities.append({"entity": entity, "value": value, "unit": unit})

    return entities