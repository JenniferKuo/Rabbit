import speech_recognition as sr
import time
import serial
import subprocess
import asyncio
from gtts import gTTS
import os
import threading
from pyfirmata import Arduino, util

r = sr.Recognizer()
r.energy_threshold = 4000
# s = serial.Serial("/dev/cu.wchusbserialfa130",9600)

def speak(s):
	tts=gTTS(text=s,lang='zh-tw')
	tts.save("hello.mp3")
	# s.write('H',encode())
	time.sleep(1)
	# s.write('L',encode())
	audio_file = "hello.mp3"
	subprocess.call(["afplay", audio_file])
	return
def move():
	# s.write('H',encode())
	print("moving")
def sing():
	audio_file = "sing.mp3"
	subprocess.call(["afplay", audio_file])
	return
def joke():
	speak("有一個人叫做小菜、然後他就被端走了、ㄏㄏ")
	# audio_file = "joke.mp3"
	# subprocess.call(["afplay", audio_file])
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
	return
def chat():
	while True:
		word = input("要聊什麼？>>")
		if word == "結束":
			break
		else:
			speak(word)
	return
def bye():
	speak("掰掰謝謝惠顧")
	return
	

sing_word=['聽我唱歌','唱歌','唱','聽你唱歌','聽歌']
joke_word=['聽你說笑話','聽笑話','講笑話','笑話','聽你講笑話','說笑話']
dance_word=['看你跳舞','跳','跳舞']
chat_word=['一起聊天','聊天','來聊天']
bye_word=['掰掰','拜拜','閉嘴']

if True:
	speak("你好我是兔子、是一個療癒機器人、我是小美的好朋友、可以陪她聊天跟玩、請問你叫什麼名字呢")
	name = input("What's your name?\n")
	speak(name+"你好")
	speak("你想要聽我唱歌、說個笑話、看我跳舞、還是一起聊天")
	while True:
		option = input("你想要聽我唱歌、說個笑話、看我跳舞、還是一起聊天\n")
		if option in sing_word:
			sing()
		elif option in joke_word:
			joke()
		elif option in dance_word:
			dance()
		elif option in chat_word:
			chat()
		elif option in bye_word:
			bye()
			break
		else:
			speak("我聽不懂你說什麼")