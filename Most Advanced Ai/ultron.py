import speech_recognition as sr
import os
import win32com.client
import openai
from key import APIkey
from time import sleep
import pyautogui

Speaker = win32com.client.Dispatch("SAPI.SpVoice")


def ai(prompt):
    openai.api_key = APIkey

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    print("********************************************************************************************************************************************")
    print("Your Result is Here : \n")
    print("-----------------------------------------------------------------------------------------------")
    print(response["choices"][0]["text"])
    Speaker.speak(response["choices"][0]["text"])
    print("\n ----------------------------------------------------------------------------------------------- \n")
 


def info():
    r = sr.Recognizer()
    print("Listening ...")
    with sr.Microphone() as source:
        audio = r.listen(source)
        try :
            print("Recognizing ...")
            query = r.recognize_google(audio)
            print(f"User Said : {query}")
            return query
        except Exception as e :
            return "Sorry Sometthing Went wrong . Please try again ..."
            

def Img(imgdesc):
    openai.api_key = APIkey
    result = openai.Image.create(
        prompt = imgdesc,
        n=2,
        size="1024x1024"
    )

    result = str(result)
    with open("image.py","w") as f:
        f.write(result)

    print("Here is your image : \n")
   
  
while True :
    x = info()
    print(x)

    if "friday".lower() in x.lower():
        
        if "text input".lower() in x.lower():
            x = input("Enter your command here : \n ")

        if "generate an image".lower() in x.lower():
            print("Please describe about what type of image you want to generate : ")
            x = info()
            Img(imgdesc=x)
    

        try :
            ai(prompt=x)
        except Exception as e:
            print("Something went wrong")
        sleep(2)


    

# ToDO = Make AI able to speak and give the results in audio form also and make Ai to the Advanced level where it must be able to create pictures also 