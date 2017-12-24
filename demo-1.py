import speech_recognition as sr
import time
import serial
import subprocess
import asyncio
from gtts import gTTS
import os
import threading

r = sr.Recognizer()
r.energy_threshold = 4000

# GPIO.setmode(GPIO.BCM)
# GPIO_list=[2,3,4,5]#2,3LED 4,5SERVO
# GPIO.setup(GPIO_list, GPIO.OUT)
# p = GPIO.PWM(5, 50)
# p2 = GPIO.PWM(4, 50)
# p.start(0)
# p2.start(0)
# listPWM=[7.5,5]#[6,8.5,11]

# setGP=[8,9,10,11,12,13,14,15]
# setGP2=[18,19,20,21,22,23,24,25]
# state=[[0,1,1,1,1,1,1,1],#0
#              [0,0,0,1,1,1,0,0],#1
#              [1,0,1,1,1,0,1,1],#2
#              [1,0,1,1,1,1,1,0],#3
#              [1,1,0,1,1,1,0,0],#4
#              [1,1,1,0,1,1,1,0],#5
#              [1,1,1,0,1,1,1,1],#6
#              [0,0,1,1,1,1,0,0],#7
#              [1,1,1,1,1,1,1,1],#8
#              [1,1,1,1,1,1,0,0],#9
#              [0,0,0,0,0,0,0,0]#no
#        ]
# for i in range(0,len(setGP),1):
#     GPIO.setup(setGP[i],GPIO.OUT)
# for i in range(0,len(setGP2),1):
#     GPIO.setup(setGP2[i],GPIO.OUT)

# def process_led(led_list,ten,digit):
#     GPIO.output(2,False)#r
#     GPIO.output(3,False)#y
#     GPIO.output(led_list,True)
#     for i in range(0,len(setGP),1):
#         GPIO.output(setGP[i],state[ten][i])
#     for i in range(0,len(setGP2),1):
#         GPIO.output(setGP2[i],state[digit][i])
#     return

# def process_sound(station,color,price):
#     a=station+'站請搭'+color+'車票'+str(price)+'元'
#     tts=gTTS(text=a,lang='zh-tw')
#     tts.save("testmicro.mp3")
#     os.system("mpg321 testmicro.mp3")
#     return

def speak(s):
	tts=gTTS(text=s,lang='zh-tw')
	tts.save("hello.mp3")
	audio_file = "hello.mp3"
	subprocess.call(["afplay", audio_file])
	return
def move():
	# for i in range(0,2,1):
	# 	for dc in listPWM:
	# 		if dc==5:
	# 			p.ChangeDutyCycle(dc)
	# 			p2.ChangeDutyCycle(dc+5)
	# 		else:
	# 			p.ChangeDutyCycle(dc)
	# 			p2.ChangeDutyCycle(dc)
	# 		time.sleep(1)
	name = input("What's your name? ")
	print(input)
def sing():
	speak("blah blah blah blah")
	audio_file = "sing.mp3"
	subprocess.call(["afplay", audio_file])
	return
def joke():
	audio_file = "joke.mp3"
	subprocess.call(["afplay", audio_file])
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
	audio_file = "dance.mp3"
	subprocess.call(["afplay", audio_file])

def lazy():
	speak("來耍廢嘿嘿嘿")
	sleep(1000)
	return
def bye():
	# audio_file = "bye.mp3"
	# subprocess.call(["afplay", audio_file])
	speak("掰掰謝謝惠顧")
	return
	

sing_word=['聽我唱歌','唱歌','唱','聽你唱歌','聽歌']
joke_word=['聽你說笑話','聽笑話','講笑話','笑話','聽你講笑話','說笑話']
dance_word=['看你跳舞','跳','跳舞']
lazy_word=['耍廢','看你耍廢']
bye_word=['掰掰','拜拜','閉嘴']

while True:
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		isay= r.recognize_google(audio, language="zh-tw")
		print(isay)
		if isay =="你好" :
			speak("你好我是兔子")
			speak("請問你叫什麼名字呢")
			with sr.Microphone() as source_2:
				audio_2 = r.listen(source_2)
			try:
				isay_second= r.recognize_google(audio_2, language="zh-tw")
				speak(isay_second+"你好")
				print(isay_second)
				while True:
					speak("你想要聽我唱歌、說個笑話、看我跳舞、還是一起耍廢")
					with sr.Microphone() as source_3:
						audio_3 = r.listen(source_3)
					try:
						isay_third= r.recognize_google(audio_3, language="zh-tw")
						if isay_third in sing_word:
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
						   speak("我聽不懂你說什麼")
						print(isay_third)
					except sr.UnknownValueError:
						print("could not understand your audio_3")
					except sr.RequestError as e:
						print("could not request results_3")

			except sr.UnknownValueError:
				print("could not understand your audio_2")
			except sr.RequestError as e:
				print("could not request results_2")
	except sr.UnknownValueError:
		print("could not understand your audio")
	except sr.RequestError as e:
		print("could not request results")

# p.stop()
# p2.stop()
# GPIO.cleanup()