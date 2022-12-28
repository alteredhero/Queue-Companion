import cv2 as cv
# from time import sleep
# from time import time
from windowcapture import WindowCapture
from vision import Vision, CharSelect
from tkinter import *
from tkinter.ttk import *
from pathlib import *
# from charselect import CharSelect
import glob
import pyautogui




# Initialize the WindowCapture class
wincap = WindowCapture()

# Initialize the Vision class
vision_accept = Vision('./Resources/accept.jpg')

Char_Select = CharSelect('./Resources/character_search.jpg')




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



# Create Portrait List pulling in image files to use as radio buttons
image_files = glob.glob('./CharacterSelect/*.png')
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
                "Random",
                "Rio", 
                "Rozzi", 
                "Shoichi", 
                "Silvia", 
                "Sissela", 
                "Sua", 
                "Tazia", 
                # "Theodore", 
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
                # bg=selected_bg,
                command = start_off
                )
    start()
    is_on = True

def start_off():
    # stops autoaccept
    global is_on
    button.config(image = unselected,
                # bg=unselected_bg,
                command = start_on
                )
    is_on = False



# Start Object Detection for Queue Pop
def start():
    if is_on:
        # get an updated image of the game
        screenshot = wincap.get_screenshot()

        points = vision_accept.find(screenshot, .35, 'rectangles')
        
        
        # debug the loop rate
        # print('FPS {}'.format(1 / (time() - loop_time)))
        # loop_time = time()

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        # if cv.waitKey(1) == ord('q'):
        #     cv.destroyAllWindows()


    window.after(500, start)


# This function searches for the character and types out the name of the character in the search field based on characters list
def Char_Search(): 
    if is_on:
        screenshot = wincap.get_screenshot()

        points = Char_Select.find(screenshot, .75, 'rectangles')

    # Iterates through characters list to capture character name
    for (i, item) in enumerate(characters, start=v):
        print (item)
        
    window.after(500, Char_Search)



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

# def selection():
#    selected = "You selected the option " + str(v.get())


# Radio button loops for character select
for index in range(len(characters)):
    Radiobutton(bottomframe,
        compound = TOP,
        image = portraits[index],
        text = characters[index],
        variable = v,
        value = index,
        command = Char_Search
    ).grid(
        row = index//5,
        column = index%5,
    )




window.mainloop()