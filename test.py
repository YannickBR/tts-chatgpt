# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
import PyPDF2

# creating a pdf reader object
reader = PyPDF2.PdfReader('study_guide.pdf')
import requests

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-cased-distilled-squad"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

 



context = reader.pages[4].extract_text()
# context = "In Future Technology you learn, in various phases to investigate the possibilities of new  technologies and work on new applications using technology. Students work in  multidisciplinary teams of three to five students with each member bringing in their own area  of expertise. In this way, you learn from the professional environment, as well as other  disciplines in the project. The feedback, evaluation and supervision focus on preparing  students as much as possible for the final and last project phase of their study program: graduation."



# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	
	
# Loop infinitely for user to
# speak

while(1):
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			output = query({'question': MyText, 'context': context})
			SpeakText(output.get('answer'))
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")
