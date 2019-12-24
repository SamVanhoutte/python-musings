import speech_recognition as sr
from os import path

audio_file = path.join(path.dirname(path.realpath(__file__)), 'speech.wav')

recognizer = sr.Recognizer()
with sr.AudioFile(audio_file) as audio_source:
    audio = recognizer.record(audio_source)
    try:
        print(recognizer.recognize_google(audio, None, 'nl-NL'))
    except sr.UnknownValueError:
        print('Could not understand')
    except sr.RequestError as e:
        print(f'Google requestion error: {e}')