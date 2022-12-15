import cv2 as cv
# from time import sleep
# from time import time
from windowcapture import WindowCapture
from vision import Vision
from tkinter import *
from tkinter.ttk import *
from pathlib import *
from charselect import CharSelect




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

# # Character Portraits
Adela = PhotoImage(file="./CharacterSelect/adela.png")
Adina = PhotoImage(file="./CharacterSelect/adina.png")
Adriana = PhotoImage(file="./CharacterSelect/adriana.png")
Aiden = PhotoImage(file="./CharacterSelect/aiden.png")
Alex = PhotoImage(file="./CharacterSelect/alex.png")
# Arda = PhotoImage(file="./CharacterSelect/arda.png")
Aya = PhotoImage(file="./CharacterSelect/aya.png")
Barbara = PhotoImage(file="./CharacterSelect/barbara.png")
Bernice = PhotoImage(file="./CharacterSelect/bernice.png")
Bianca = PhotoImage(file="./CharacterSelect/bianca.png")
Camilo = PhotoImage(file="./CharacterSelect/camilo.png")
Cathy = PhotoImage(file="./CharacterSelect/cathy.png")
Celine = PhotoImage(file="./CharacterSelect/celine.png")
Chiara = PhotoImage(file="./CharacterSelect/chiara.png")
Chloe = PhotoImage(file="./CharacterSelect/chloe.png")
Daniel = PhotoImage(file="./CharacterSelect/daniel.png")
# Debbie_Marlene = PhotoImage(file="./CharacterSelect/debbi_marlene.png")
Echion = PhotoImage(file="./CharacterSelect/echion.png")
Elena = PhotoImage(file="./CharacterSelect/elena.png")
Eleven = PhotoImage(file="./CharacterSelect/eleven.png")
Emma = PhotoImage(file="./CharacterSelect/emma.png")
Estelle = PhotoImage(file="./CharacterSelect/estelle.png")
Eva = PhotoImage(file="./CharacterSelect/eva.png")
Felix = PhotoImage(file="./CharacterSelect/felix.png")
Fiora = PhotoImage(file="./CharacterSelect/fiora.png")
Hart = PhotoImage(file="./CharacterSelect/hart.png")
Haze = PhotoImage(file="./CharacterSelect/haze.png")
Hyejin = PhotoImage(file="./CharacterSelect/hyejin.png")
Hyunwoo = PhotoImage(file="./CharacterSelect/hyunwoo.png")
Irem = PhotoImage(file="./CharacterSelect/irem.png")
Isaac = PhotoImage(file="./CharacterSelect/isaac.png")
Isol = PhotoImage(file="./CharacterSelect/isol.png")
Jackie = PhotoImage(file="./CharacterSelect/jackie.png")
Jan = PhotoImage(file="./CharacterSelect/jan.png")
Jenny = PhotoImage(file="./CharacterSelect/jenny.png")
Johann = PhotoImage(file="./CharacterSelect/johann.png")
Karla = PhotoImage(file="./CharacterSelect/karla.png")
Laura = PhotoImage(file="./CharacterSelect/laura.png")
Lenox = PhotoImage(file="./CharacterSelect/lenox.png")
Leon = PhotoImage(file="./CharacterSelect/leon.png")
Li_Dailin = PhotoImage(file="./CharacterSelect/li dailin.png")
Luke = PhotoImage(file="./CharacterSelect/luke.png")
# Ly_Anh = PhotoImage(file="./CharacterSelect/ly anh.png")
Magnus = PhotoImage(file="./CharacterSelect/magnus.png")
Mai = PhotoImage(file="./CharacterSelect/mai.png")
Markus = PhotoImage(file="./CharacterSelect/markus.png")
Martina = PhotoImage(file="./CharacterSelect/martina.png")
Nadine = PhotoImage(file="./CharacterSelect/nadine.png")
Nathapon = PhotoImage(file="./CharacterSelect/nathapon.png")
Nicky = PhotoImage(file="./CharacterSelect/nicky.png")
Piolo = PhotoImage(file="./CharacterSelect/piolo.png")
Priya = PhotoImage(file="./CharacterSelect/priya.png")
Random = PhotoImage(file="./CharacterSelect/random.png")
Rio = PhotoImage(file="./CharacterSelect/rio.png")
Rozzi = PhotoImage(file="./CharacterSelect/rozzi.png")
Shoichi = PhotoImage(file="./CharacterSelect/shoichi.png")
Silvia = PhotoImage(file="./CharacterSelect/silvia.png")
Sissela = PhotoImage(file="./CharacterSelect/sissela.png")
Sua = PhotoImage(file="./CharacterSelect/sua.png")
Tazia = PhotoImage(file="./CharacterSelect/tazia.png")
# Theodore = PhotoImage(file="./CharacterSelect/theodore.png")
Tia = PhotoImage(file="./CharacterSelect/tia.png")
# Vanya = PhotoImage(file="./CharacterSelect/vanya.png")
William = PhotoImage(file="./CharacterSelect/william.png")
Xiukai = PhotoImage(file="./CharacterSelect/xiukai.png")
Yuki = PhotoImage(file="./CharacterSelect/yuki.png")
Zahir = PhotoImage(file="./CharacterSelect/zahir.png")

# Master Character Image List
characterPortraits = [
                Random,                
                Adela, 
                Adina, 
                Adriana, 
                Aiden, 
                Alex,
                # Arda, 
                Aya, 
                Barbara, 
                Bernice, 
                Bianca, 
                Camilo, 
                Cathy, 
                Celine, 
                Chiara, 
                Chloe, 
                Daniel, 
                # Debbie_Marlene,
                Echion, 
                Elena, 
                Eleven, 
                Emma, 
                Estelle, 
                Eva, 
                Felix, 
                Fiora, 
                Hart, 
                Haze, 
                Hyejin, 
                Hyunwoo, 
                Irem, 
                Isaac, 
                Isol, 
                Jackie, 
                Jan, 
                Jenny, 
                Johann, 
                Karla, 
                Laura, 
                Lenox, 
                Leon, 
                Li_Dailin, 
                Luke,
                # Ly_Anh, 
                Magnus, 
                Mai, 
                Markus, 
                Martina, 
                Nadine, 
                Nathapon, 
                Nicky, 
                Piolo, 
                Priya,  
                Rio, 
                Rozzi, 
                Shoichi, 
                Silvia, 
                Sissela, 
                Sua, 
                Tazia, 
                # Theodore, 
                Tia, 
                # Vanya
                William, 
                Xiukai, 
                Yuki, 
                Zahir, 
                ]

# Master Character List
characters = [
                "Random",
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
                # "Theodore", 
                "Tia",
                # "Vanya" 
                "William", 
                "Xiukai", 
                "Yuki", 
                "Zahir", 
                ]



# Intitialize Character Select
# char_select = CharSelect(characterPortraits[])

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
        image = characterPortraits[index],
        text = characters[index],
        variable = v,
        value = index,
    ).grid(
        row = index//5,
        column = index%5,
    )


window.mainloop()