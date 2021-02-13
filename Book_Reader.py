import pyttsx3 # pip install pyttsx3
import PyPDF2 # pip install PyPDF2
book = open('oop.pdf', 'rb') # Specify Name & Path
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()