import cv2 as cv
# from time import sleep
# from time import time
from windowcapture import WindowCapture
from vision import Vision
from tkinter import *
from tkinter.ttk import *
from pathlib import *
from charselect import CharSelect
import glob
from PIL import Image




# Initialize the WindowCapture class
wincap = WindowCapture()

# Initialize the Vision class
vision_accept = Vision('./Resources/accept.jpg')

# Window parameters
window = Tk()
window.iconbitmap("./Resources/SSC.ico")
window.geometry("450x640")
window.resizable(False, False)
window.title('Eternal Return - Queue Companion')

# Match Search and Accept button
unselected = PhotoImage(file='./Resources/Button_unselected.png')
selected = PhotoImage(file='./Resources/matching.png')
unselected_bg='white'
selected_bg='black'
is_on = True


# Create Portrait List
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


# Intitialize Character Select

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



# start object detection
def start():
    if is_on:
        # get an updated image of the game
        screenshot = wincap.get_screenshot()
        # screenshot = cv.resize(screenshot, (800, 600))


        points = vision_accept.find(screenshot, .32, 'rectangles')

        # debug the loop rate
        # print('FPS {}'.format(1 / (time() - loop_time)))
        # loop_time = time()

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        # if cv.waitKey(1) == ord('q'):
        #     cv.destroyAllWindows()
        #     break
    window.after(500, start)

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

# Button!
button = Button(topframe,
                image=unselected,
                command=start_on
                )
button.pack(anchor = N, side = TOP)

#Stores interger values
v = IntVar()

# Radio button loops
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