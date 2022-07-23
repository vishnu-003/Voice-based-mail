import smtplib
import speech_recognition as sr
import pyttsx3
import easyimap as e
from email.message import EmailMessage
una="svishnuvardhan1209@gmail.com"
pwd="wufnsitmvfwhraqs"
r=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

def speak(str):
	print(str)
	engine.say(str)
	engine.runAndWait()
	
def listen():
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		str="Speak Now:"
		speak(str)
		audio=r.listen(source)
		try:
			text = r.recognize_google(audio)
			return text
		except:
			str="Sorry could not recognize what you said"
			speak(str)
	
def sendmail():
	rec="bannus369@gmail.com"
	str="Please speak the body of your email"
	speak(str)
	msg=listen()
	
	str="You have spoken the message"
	speak(str)
	speak(msg)
	
	server=smtplib.SMTP_SSL("smtp.gmail.com",465)
	server.login(una,pwd)
	server.sendmail(una,rec,msg)
	server.quit()

	
	str="The email has been sent"
	speak(str)
	
def readmail():
	server=e.connect("imap.gmail.com",una,pwd)
	server.listids()
	
	str="Please say the Serial Number of the email you wanna read starting  from latest"
	speak(str)
	
	a =listen()
	if(a == "Tu"):
		a="2"
	b=int(a)-1
	
	email=server.mail(server.listids()[b])
	
	str="The email is from:"
	speak(str)
	speak(email.from_addr)
	str="the subject of the email is:"
	speak(str)
	speak(email.title)
	str = "The body of the email  is:"
	speak(str)
	speak(email.body)
	
str="Welcome to voice controlled email serivce"
speak(str)

while(1):
	str="what do you want to do?"
	speak(str)
	
	str="Speak SEND to send email Speak Read to Read Inbox  Speak EXIT to Exit"
	
	speak(str)
	
	ch=listen()
	
	if(ch == 'send'):
		str="you have chosen to send an email"
		speak(str)
		sendmail()
	elif(ch =='read'):
		str="You have chosen to read email"
		speak(str)
		readmail()
	elif(ch=='exit'):
		str ="You have chosen to exit ,bye bye"
		speak(str)
		exit(1)
	else:
		str="Invalid choice, you said:"
		speak(str)
		speak(ch)
	

	