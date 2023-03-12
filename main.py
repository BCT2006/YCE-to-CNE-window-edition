from tkinter import *
from tkinter import filedialog as fd
#from tkinter.filedialog import asksaveasfile
import json
#import requests
import yceProcessor

root = Tk()
root.geometry("300x240")
root.title(" YCE to CNE ")
root.iconbitmap("icon.ico")
print('hi')
def open_character_file():
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
    print(yceProcessor.convertChar(dajson))
    save = fd.asksaveasfile(initialfile = 'Character.xml',
defaultextension=".xml",filetypes=[("XML","*.xml")])
    save.write(yceProcessor.convertChar(dajson))
    save.close
    #print(dajson)

def open_stage_file():
    # file type
    filetypes = (
        ('Stage Json', '*.json'),
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
    print(yceProcessor.convertStage(dajson,'name','src'))
    save = fd.asksaveasfile(initialfile = f'''stage.xml''',
defaultextension=".xml",filetypes=[("XML","*.xml")])
    save.write(yceProcessor.convertStage(dajson,'name','src'))
    save.close
    #print(dajson)

openFileButton = Button(root, height = 2,
                 width = 20,
                 text ="Open Character Json",
                 command = lambda:open_character_file())

openStageButton = Button(root, height = 2,
                 width = 20,
                 text ="Open Stage Json",
                 command = lambda:open_stage_file())

openFileButton.pack()

openStageButton.pack()
Label(root, text = "When making a stage XML,\n its your job to put the name\n and the source folder\nIt's also not completely fisnished yet\n").pack()
Label(root, text = "I made this for myself,\nbut I decided to releace it\ncause why not\n\nv0.9").pack()

print('is this working')
mainloop()