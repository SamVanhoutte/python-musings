from gtts import gTTS
import os

output_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'text.mp3')
print(output_file)
text = 'Ik denk aan mijn kratje bier en dat geeft veel plezier.'
language = 'nl'

speech = gTTS(text = text, lang = language, slow = False)
speech.save(output_file)