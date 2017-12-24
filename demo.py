import speech_recognition as sr
import time
import RPi.GPIO as GPIO
from gtts import gTTS
import os
import threading

r = sr.Recognizer()
r.energy_threshold = 4000

GPIO.setmode(GPIO.BCM)
GPIO_list=[2,3,4,5]#2,3LED 4,5SERVO
GPIO.setup(GPIO_list, GPIO.OUT)
p = GPIO.PWM(5, 50)
p2 = GPIO.PWM(4, 50)
p.start(0)
p2.start(0)
listPWM=[7.5,5]#[6,8.5,11]

setGP=[8,9,10,11,12,13,14,15]
setGP2=[18,19,20,21,22,23,24,25]
state=[[0,1,1,1,1,1,1,1],#0
             [0,0,0,1,1,1,0,0],#1
             [1,0,1,1,1,0,1,1],#2
             [1,0,1,1,1,1,1,0],#3
             [1,1,0,1,1,1,0,0],#4
             [1,1,1,0,1,1,1,0],#5
             [1,1,1,0,1,1,1,1],#6
             [0,0,1,1,1,1,0,0],#7
             [1,1,1,1,1,1,1,1],#8
             [1,1,1,1,1,1,0,0],#9
             [0,0,0,0,0,0,0,0]#no
       ]
for i in range(0,len(setGP),1):
    GPIO.setup(setGP[i],GPIO.OUT)
for i in range(0,len(setGP2),1):
    GPIO.setup(setGP2[i],GPIO.OUT)

def process_led(led_list,ten,digit):
    GPIO.output(2,False)#r
    GPIO.output(3,False)#y
    GPIO.output(led_list,True)
    for i in range(0,len(setGP),1):
        GPIO.output(setGP[i],state[ten][i])
    for i in range(0,len(setGP2),1):
        GPIO.output(setGP2[i],state[digit][i])
    return

def process_sound(station,color,price):
    a=station+'站請搭'+color+'車票'+str(price)+'元'
    tts=gTTS(text=a,lang='zh-tw')
    tts.save("testmicro.mp3")
    os.system("mpg321 testmicro.mp3")
    return

def speak(s):
    tts=gTTS(text=s,lang='zh-tw')
    tts.save("hello.mp3")
    os.system("mpg321 hello.mp3")
    return
def move():
    for i in range(0,2,1):
        for dc in listPWM:
            if dc==5:
                p.ChangeDutyCycle(dc)
                p2.ChangeDutyCycle(dc+5)
            else:
                p.ChangeDutyCycle(dc)
                p2.ChangeDutyCycle(dc)
            time.sleep(1)
def sing():
    speak("blah blah blah blah")
    #os.system("mpg321 sing.mp3")
    return
def joke():
    speak("tell me a joke")
    #os.system("mpg321 joke.mp3")
    return
def dance():
    t1=threading.Thread(target=dance_music())
    t2=threading.Thread(target=move())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return
def dance_music():
    os.system("mpg321 nfc.mp3")
    #speak("lalalalalalalala")
def lazy():
    #os.system("mpg321 lazy.mp3")
    speak("嘿嘿耍廢")
    return
def bye():
    #os.system("mpg321 bye.mp3")
    speak("掰掰謝謝惠顧")
    return
    

sing_word=['聽我唱歌','唱歌','唱','聽你唱歌','聽歌']
joke_word=['聽你說笑話','聽笑話','講笑話','笑話','聽你講笑話']
dance_word=['看你跳舞','跳','跳舞']
lazy_word=['耍廢','看你耍廢']
bye_word=['掰掰','拜拜','閉嘴']

'''while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        isay= r.recognize_google(audio, language="zh-tw")####
        #isay="小港"
        print(isay)
        if isay =="你好" :
            speak("你好我是兔子")
            speak("請問你叫什麼名字呢")
            while True:
                with sr.Microphone() as source_2:
                    audio_2 = r.listen(source_2)
                try:
                    isay_second= r.recognize_google(audio_2, language="zh-tw")####
                    speak(isay_second+"你好")'''
                   Sord:
                                sing()
                            elif isay_third in joke_word:
                                joke()
                            elif isay_third in dance_word:
                                dance()
                            elif isay_third in lazy_word:
                                lazy()
                            elif isay_third in bye_word:
                                break
                            else:
                                speak("wo ting bu dong")
                            print(isay_third)
                        except sr.UnknownValueError:
                            print("could not understand your audio_3")
                        except sr.RequestError as e:
                            print("could not request results_3")
                    # process_sound(isay_second,red_price[red_station.index(isay_second)])
                    # if isay_second in orange_station:
                    #     led_list=[3]
                    #     ten=int(orange_price[orange_station.index(isay_second)]/10)
                    #     digit=int(orange_price[orange_station.index(isay_second)]%10)
                    #     process_led(led_list,ten,digit)
                    #     process_sound(isay_second,'橘線',orange_price[orange_station.index(isay_second)])
                    # elif isay_second in red_station:
                    #     led_list=[2,3]
                    #     ten=int(red_price[red_station.index(isay_second)]/10)
                    #     digit=int(red_price[red_station.index(isay_second)]%10)
                    #     process_led(led_list,ten,digit)
                    #     process_sound(isay_second,'橘線並轉搭紅線',red_price[red_station.index(isay_second)])
                    # elif isay_second=="謝謝":
                    #     print("謝謝")
                    #     break
                    '''print(isay_second)
                except sr.UnknownValueError:
                    print("could not understand your audio_2")
                except sr.RequestError as e:
                    print("could not request results_2")
    except sr.UnknownValueError:
        print("could not understand your audio")
    except sr.RequestError as e:
        print("could not request results")'''

p.stop()
p2.stop()
GPIO.cleanup()
