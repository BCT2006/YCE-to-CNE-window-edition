import json
import sys
import os.path

#character stuff

def loadJson(filename):
  file_exists = os.path.exists(f"{filename}.json")
  if file_exists:
    with open(f"{filename}.json", "r") as read_file:
          daJson = json.load(read_file)

  return(daJson)

#
def processcharxml(dajson):

  xml = f'''<!DOCTYPE codename-engine-character>
<character isPlayer="false" flipX="{str(dajson["flipX"]).lower()}" x="{str(dajson["globalOffset"]['x'])}" y="{str(dajson["globalOffset"]['y'])}" holdTime="6.1">'''
  for i in dajson["anims"]:
    tempAnim = f'\n  <anim name="{i["name"]}"       anim="{i["anim"]}"       fps="{i["framerate"]}"    loop="{str(i["loop"]).lower()}" x="{str(i["x"]).lower()}" y="{str(i["y"]).lower()}"'
    #if i["indices"] != None:
      #tempAnim += f' indices="{str(i["indices"]).replace("["," ").replace("]","").replace(" ","")}"'
    tempAnim += " />"
    xml += tempAnim
  xml += "\n</character>"
  return(xml)

#stage stuff

def processstagexml(dajson,name,dasrc):
  xml = f'''<!DOCTYPE codename-engine-stage>
<stage zoom="{str(dajson['defaultCamZoom'])}" name="{name}" folder="{dasrc}">'''
  
  for i in dajson["sprites"]:
    sprite = i["src"]
    if i["type"] == "Bitmap":
      if dasrc in sprite:
        sprite.replace(dasrc, "")
        print(sprite + " " + dasrc)
      xml += f'\n   <sprite name="{i["name"]}" x="{str(i["pos"][0])}" y="{str(i["pos"][1])}" sprite="{sprite}" scrollx="{i["scrollFactor"][0]}" scrolly="{i["scrollFactor"][1]}" />'

    if i["type"] == "SparrowAtlas":
      print("Sparrow spotted")
      xml += f'\n   <sprite name="{i["name"]}" x="{str(i["pos"][0])}" y="{str(i["pos"][1])}" sprite="{sprite}" scrollx="{i["scrollFactor"][0]}" scrolly="{i["scrollFactor"][1]}" anim="{i["animation"]["name"]}"/>'
      
    if i["type"] == "BF":
      xml += "\n  <boyfriend />"
    if i["type"] == "Dad":
      xml += "\n  <dad />"
    if i["type"] == "GF":
      xml += "\n  <girlfriend />"
  xml += "\n</stage>"
  return(xml) 
  
def convertChar(json):
  return processcharxml(json)

def convertStage(json,name,src):
  return processstagexml(json,name,src)