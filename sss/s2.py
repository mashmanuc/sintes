import pyttsx3

# Створення об'єкту голосу
engine = pyttsx3.init()

# Встановлення мови на українську
engine.setProperty('voice', 'uk')

# Встановлення швидкості голосу (за бажанням)
engine.setProperty('rate', 150)

# Встановлення гучності голосу (за бажанням)
engine.setProperty('volume', 0.7)

# Відтворення тексту
engine.say('Привіт, як справи?')
engine.runAndWait()
