"""import translator"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """function to translate from english to french"""
    french_text=MyMemoryTranslator(source='en-CA', target='fr-CA').translate(english_text)
    return french_text

def french_to_english(french_text):
    """function to translate from french to english"""
    english_text=MyMemoryTranslator(source='fr-CA', target='en-CA').translate(french_text)
    return english_text
