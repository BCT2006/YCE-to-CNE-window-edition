from tkinter import *
from tkinter import filedialog as fd
#from tkinter.filedialog import asksaveasfile
import json
import requests
import yceProcessor

root = Tk()
root.geometry("300x120")
root.title(" CodenameUtils ")
root.iconbitmap("icon.ico")

def open_text_file():
    # file type
    filetypes = (
        ('Character Json', '*.json'),
        ('All', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfilename(filetypes=filetypes)
    # read the text file and show its content on the Text
    #dajson = response.content.decode("utf-8")
    #jsonStr = f.content.decode("utf-8")
    with open(f, 'r') as f:
      dajson = json.load(f)
    print(dajson)
    print(yceProcessor.processcharxml(dajson))
    save = fd.asksaveasfile(initialfile = 'Character.xml',
defaultextension=".xml",filetypes=[("XML","*.xml")])
    save.write(yceProcessor.processcharxml(dajson))
    save.close
    #print(dajson)

openFileButton = Button(root, height = 2,
                 width = 20,
                 text ="Open Character Json",
                 command = lambda:open_text_file())

openFileButton.pack()
Label(root, text = "Theres not much goin on\njust open the json, and save the xml\n\nthis was literally made to just make things easier").pack()

mainloop()