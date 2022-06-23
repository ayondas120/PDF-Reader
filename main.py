import pyttsx3
import PyPDF2
book = open('python.pdf' , 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(50,pages):
    page = pdfreader.getPage(50)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()