from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    frenchText=MyMemoryTranslator(source='en-CA', target='fr-CA').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    englishText=MyMemoryTranslator(source='fr-CA', target='en-CA').translate(frenchText)
    return englishText

