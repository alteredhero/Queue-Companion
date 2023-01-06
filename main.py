import cv2 as cv
from windowcapture import WindowCapture
from vision import Vision, CharSelect, charSearch
from tkinter import *
from tkinter.ttk import *
from pathlib import *
import glob
import pyautogui as pyag
import keyboard
import win32gui
import os
from time import sleep




# Initialize the WindowCapture class
wincap = WindowCapture()

# Initialize the Vision class
vision_accept = Vision('./Resources/accept.jpg')
Char_Select = CharSelect('./Resources/character_search.jpg')
matchFound = Vision('./Resources/matchfound.jpg')



# Window parameters
window = Tk()
window.iconbitmap("./Resources/SSC.ico")
window.geometry("450x640")
window.resizable(False, False)
window.title('Eternal Return - Queue Companion')

# Match Search and Accept button variables
unselected = PhotoImage(file='./Resources/Button_unselected.png')
selected = PhotoImage(file='./Resources/matching.png')
unselected_bg='white'
selected_bg='black'
is_on = True
search = True
select = True



# Create Portrait List pulling in image files to use as radio buttons
image_files = glob.glob('./CharacterIcons/*.png')
portraits = []

for file in image_files:

    image = PhotoImage(file=file)
    portraits.append(image)



# Master Character List
characters = [
                "Adela", 
                "Adina", 
                "Adriana", 
                "Aiden", 
                "Alex", 
                # "Arda",
                "Aya", 
                "Barbara", 
                "Bernice", 
                "Bianca", 
                "Camilo", 
                "Cathy", 
                "Celine", 
                "Chiara", 
                "Chloe", 
                "Daniel",
                # "Debbie/Marlene", 
                "Echion", 
                "Elena", 
                "Eleven", 
                "Emma", 
                "Estelle", 
                "Eva", 
                "Felix", 
                "Fiora", 
                "Hart", 
                "Haze", 
                "Hyejin", 
                "Hyunwoo", 
                "Irem", 
                "Isaac", 
                "Isol", 
                "Jackie", 
                "Jan", 
                "Jenny", 
                "Johann", 
                "Karla", 
                "Laura", 
                "Lenox", 
                "Leon", 
                "Li Dailin", 
                "Luke", 
                # "Ly Anh", 
                "Magnus", 
                "Mai", 
                "Markus", 
                "Martina", 
                "Nadine", 
                "Nathapon", 
                "Nicky", 
                "Piolo", 
                "Priya",  
                "Rio", 
                "Rozzi", 
                "Shoichi", 
                "Silvia", 
                "Sissela", 
                "Sua", 
                "Tazia", 
                "Theodore", 
                "Tia",
                # "Vanya" 
                "William", 
                "Xiukai", 
                "Yuki", 
                "Zahir", 
                ]


# Start game/Matching button functions
def start_on():
    global is_on
   
   # starts autoaccept
    button.config(image = selected,
                command = start_off
                )
    start()
    is_on = True

def start_off():
    # stops autoaccept
    global is_on
    button.config(image = unselected,
                command = start_on
                )
    is_on = False

def search_on():
    # Looks for search field
    global search
    Char_Search()
    search = True

def search_off():
    # Stops looking for search field
    global search
    search = False

def charSelect_on():
    global select
    selection()
    select = True

def charSelect_off():
    global select
    select = False
    global search
    search = False


# Start Object Detection for Queue Pop
def start():
    
    if is_on:
        # get an updated image of the game
        screenshot = wincap.get_screenshot()

        points = vision_accept.find(screenshot, .35, 'rectangles')
        
        if len(points):
            handle = win32gui.FindWindow(0, "Eternal Return")
            win32gui.SetForegroundWindow(handle)

            #passing enter keystroke
            keyboard.press_and_release('enter')

            # Buffer for charachter select to come up.
            sleep(11)

            # Search for onscreen confirmation that character select is up.
            screenshot = wincap.get_screenshot()
            matchfound = matchFound.find(screenshot, .5, 'rectangles')

            # If confirmed, move on.
            if len(matchfound):

                start_off()
                search_on()
            
            # If unconfirmed, start over.
            elif():
                start()

    window.after(500, start)



# This function searches for the character and types out the name of the character in the search field based on characters list
def Char_Search(): 

    # charVariable=0
    # charVariable=v.get()

    if search:
        screenshot = wincap.get_screenshot()

        search_field = Char_Select.find(screenshot, .75, 'rectangles')

        if len(search_field):
            #Debug character selection using as label to verify character selection matches what is selected.
            # game_selection_label.configure(text = "You have chosen: " + str(characters[charVariable]),)
            search_off()
            charSelect_on()



    window.after(1000, Char_Search)



def selection():
    
    if select:
        # Set character name as variable in list
        charVariable=0
        charVariable=v.get()
        # Type character name in search bar
        pyag.typewrite(str(characters[charVariable]))

        screenshot = wincap.get_screenshot()

        # Import selection to Vision Class
        pathtoCharacters = os.path.join(os.getcwd(), "CharacterSearch", str(characters[charVariable]+".jpg"))
        characterSearch = charSearch(pathtoCharacters)
        characterMatch = characterSearch.find(screenshot, .50, 'rectangles')

        if len(characterMatch):
            charSelect_off()
    
    window.after(1000, selection)


####Window and Button/Radiobutton details####

# Match Making Frame
topframe = Frame(window)
topframe.pack(padx = 50, side = TOP, anchor = W)

# Frame to hold Canvas
inceptionframe = Frame(window)
inceptionframe.pack(fill=BOTH, expand=1)

# Canvas to hold frame with buttons/scrollbar
canvy = Canvas(inceptionframe)
canvy.pack(side=LEFT, fill=BOTH, expand=1)

# Scrollbar
my_scrollbar = Scrollbar(inceptionframe, orient = VERTICAL, command=canvy.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)


# Canvas config
canvy.configure(yscrollcommand = my_scrollbar.set)
canvy.bind('<Configure>', lambda e: canvy.configure(scrollregion = canvy.bbox("all")))

# Character List Frame
bottomframe = Frame(canvy)

# Window that holds bounding frame
canvy.create_window((0,0), window=bottomframe, anchor=NW)

# Queue Match Button!
button = Button(topframe,
                image=unselected,
                command=start_on
                )
button.pack(anchor = N, side = TOP)

#Stores interger values
v = IntVar()
v.set = ()

# Radio button loops for character select
for index in range(len(characters)):
    Radiobutton(bottomframe,
        compound = TOP,
        image = portraits[index],
        text = characters[index],
        variable = v,
        value = index,
    ).grid(
        row = index//5,
        column = index%5,
    )




window.mainloop()