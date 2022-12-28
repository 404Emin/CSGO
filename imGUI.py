import dearpygui.dearpygui as dpg
from subprocess import *
import allin1 as a
from threading import Thread

#main
dpg.create_context()
dpg.create_viewport(title='Skill issue', width=300, height=200, resizable=False)

#Defs
def Glow(box):
    
    if dpg.get_value(box) == True:
        Popen (["python", "Glow.py"])
        print("Glow ESP enabled")
    else:
        print("Glow ESP disabled")

def Trigger(box):
      
    if dpg.get_value(box) == True:
        Popen (["python", "Trigger.py"])
        print("Trigger BOT enabled")
    else:
        print("Trigger BOT disabled")

def Chams(box):
    
    if dpg.get_value(box) == True:
        Popen (["python", "Chams.py"])
        print("Chams enabled")
    else:
        print("Chams disabled")

def Map(box):
    
    if dpg.get_value(box) == True:
        Popen (["python", "Map.py"])
        print("Map radar enabled")
    else:
        print("Map radar disabled")


#Visual
with dpg.window(label="CS:GO Gaming Chair", width=300, height=300, no_move=True, no_collapse=True):
    dpg.add_text("""404 Gaming chair
    Press H to deactivate everything""")
    
    #Trigger button
    dpg.add_checkbox(label="Trigger bot", callback= Trigger, default_value= False)
    #map location button
    dpg.add_checkbox(label="Map radar", callback= Map, default_value= False)
    #Glow ESP button
    dpg.add_checkbox(label="Glow ESP", callback= Glow, default_value= False)
    #chams button
    dpg.add_checkbox(label="Chams", callback= Chams, default_value= False)
    


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

#def Glow_th():
#    Thread(target=a.glow).start()
#
#def Trigger_th():
#    Thread(target=a.trigger).start()
#
#def Chams_th():
#    Thread(target=a.chams).start()
#
#def Map_th():
#    Thread(target=a.map).start()