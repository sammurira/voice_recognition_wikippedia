#virtual assistant prog
#pip install pyaudio
#pip install SpeechRecognition
#pip install gTTs
# pip install wikipedia

#import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia


#ignore any warning messages
warnings.filterwarnings("ignore")

# record audio

def recordAudio():

    #Record Audio
    r = sr.Recognizer()

    #open the mic
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)

    #use google sppech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print("You said " + data)
        return data
    except sr.UnknownValueError:
        print('Google speech recognition could not recognize the audio, unknowm error')

    except sr.RequestError as e:
        print('Results from google speech error '+ e)

        return data



#Get viatual assistant responce
def assistantResponse(text):
    print(text)

    #convert the text to speech
    myObj = gTTS(text = text , lang= "en", slow=False)

    myObj.save('assistant_response.mp3')

    #play the converted file
    #pygame.mixer.init()
    #pygame.mixer_music.load('assistant_response.mp3')
    #pygame.mixer_music.play()
    os.system('open assistant_response.mp3')



def wakeWord(txt):
    WAKE_WORDS = ['Hi lap','Hi Mac']

    text = txt.lower() # convert the the text to all lower text

    #check if user the contains wake words
    for phrase in WAKE_WORDS:
        if phrase in text:

            return True

        return False
    #Get cuurent date
def getDate():

    now = datetime.datetime.now()

    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    #a list of months
    monthNames = ['January', 'February', 'March','April','May','June','July','August', 'September','October','November','December']
    ordinalNumbers =['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th',
                     '11th','12th','13th','14th','15th','16th','17th', '18th', '19th', '20th',
                     '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '29th', '30th', '31st']

    return 'Today is ' + weekday + ' ' + monthNames[monthNum - 1] + ' the ' + ordinalNumbers[dayNum -1] + '.'

def greeting(text):
    #Random rgreetings
    GREETING_INPUT = ['hi','hey','hola','greetings','wassup','hello']

    #Response
    GREETING_RESPONSE = ['howdy','whats good','hello','hey there']

    for word in text.split():
        if word.lower() in GREETING_INPUT:
            return  random.choice(GREETING_RESPONSE) + '.'

def getPerson(text):

    wordlist = text.split()

    for i in range(0, len(wordlist)):
        if i + 3 <= len(wordlist) - 1  and  wordlist[i].lower() == 'who'  and wordlist[i+1].lower() == 'is':
            return wordlist[i+2] + ' ' + wordlist[i+3]

while True:

    text = recordAudio()
    response = ''

    #if wakeWord(text):

    #response = response + greeting(text)

    #if ('date' in text):
    #   response = response + getDate()

    if('who is' in text):
        person = getPerson(text)
        wiki =  wikipedia.summary(person, sentences=3)

        response = response + ' ' + wiki
    if ('what is' in text):
        search_input = getPerson(text)
        wiki = wikipedia.summary( text)

        response = response + ' ' + wiki
    assistantResponse(response)
