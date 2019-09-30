import speech_recognition as sr
from playsound import playsound
import webbrowser
import random
import os
import pyttsx3



speech = sr.Recognizer()

greeting_dict = {'hello': 'hello', 'hi': 'hi'}
open_launch_dict = {'open': 'open', 'launch': 'launch'}
social_media_site = {'facebook': 'https://www.facebook.com', 'twitter': 'https://www.twitter.com'}

mp3_greeting_list = ['male voice/hello.mp3', 'male voice/hi.mp3']
mp3_launch_lists = ['male voice/launching sir...mp3', 'male voice/opening sir.mp3']

try:
    engine = pyttsx3.init()
except ImportError:
    print("Requested driver not found")
except RuntimeError:
    print("Driver fails to initialize")


engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()


def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)

def read_voice_cmd():
    voice_text= ''
    print('listning...')
    with sr.Microphone() as source:
        audio = speech.listen(source)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network error.')
        speak_text_cmd('network error. please try again later')
    except sr.WaitTimeoutError:
        pass

    return voice_text

def is_valid_note(greet_dict, voice_notes):
    for key, value in greet_dict.iteritems():
        #'Hello Denim'
        try:
            if value == voice_notes.split(' ')[0]:
                return True
                break
            elif key == voice_notes.split(' ')[1]:
                return True
                break
        except IndexError:
            pass

    return False


if __name__ == '__main__':
   playsound('male voice/hello mr tuhin.mp3')

   while True:
        voice_notes = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_notes))

        if is_valid_note(greeting_dict, voice_notes):
            print('in Greeting')
            play_sound(mp3_greeting_list)
            continue
        elif is_valid_note(open_launch_dict, voice_notes):
            print('opening in process')
            play_sound(mp3_launch_lists)
            if(is_valid_note(social_media_site,voice_notes)):
                #launch facebook
                key = voice_notes.split(' ')[1]
                webbrowser.open(social_media_site.get(key))
            else:
                os.system('explorer D:\\"{}"'.format(voice_notes.replace('Open ', '').replace('launch ', '')))
            continue
        elif 'bye' in voice_notes:
            playsound('male voice/bye.mp3')
            exit()
