import speech_recognition as sr
import webbrowser
import datetime

def open_google() -> None:
  webbrowser.open("https://www.google.com")
 
def google_search(search_query: str) -> None:
  webbrowser.open(f"https://www.google.com/search?q={search_query.strip()}")

def get_time() -> None:
  print(datetime.datetime.now().strftime("%H:%M:%S"))

functions = {
  "open Google": lambda: open_google(),
  "search for": lambda: text: google_search(text),
  "what is the time": lambda: get_time()
}

r = sr.Recognizer()

with sr.Microphone() as source:
  # r.adjust_for_ambient_noise(source)
  print("Speak now...")
  # while True: (every option below should be included)
  audio = r.listen(source)

try:
  text = r.recognize_google(audio)
  print("You said ", text)
  # if "hey python" in text.lower():
  #   print activated
  # exceptions go here
  functions.get(text, lambda: print("Sorry, I couldn't understand what you said."))

except sr.UnknownValueError:
  print("Sorry, can you repeat that")

except sr.RequestError as e:
  print("Sorry, could not request results from Google Speech Recognition; {0}".format(e))
  
