from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    frenchText=MyMemoryTranslator(source='auto', target='french').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    englishText=MyMemoryTranslator(source='auto', target='french').translate(frenchText)
    return englishText

