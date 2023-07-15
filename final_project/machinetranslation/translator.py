from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    frenchText=MyMemoryTranslator(source='EN', target='FR').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    englishText=MyMemoryTranslator(source='FR', target='EN').translate(frenchText)
    return englishText

