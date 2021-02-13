import pyttsx3 # pip install pyttsx3
import PyPDF2 # pip install PyPDF2
book = open('oop.pdf', 'rb') # Specify Name & Path
pdfReader = PyPDF2.PdfFileReader(book) # Importing My PDF
pages = pdfReader.numPages # Counting Number Of Pages

speaker = pyttsx3.init() # Initializing Speaking Out
for num in range(7, pages): # Loop After Index Page To Last Page
    page = pdfReader.getPage(num) # Getting Page Number
    text = page.extractText() # Extracting The Text From The Page
    speaker.say(text) # Speaking Out
    speaker.runAndWait() # For Time Pause
