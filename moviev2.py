from random import choice
from time import sleep
from tkinter import *
# GUI
root = Tk()
root.title("Movie Recommander :-)")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

flag = 0
bot_name = "Wumpus"

m_actions = [
  "Transformers: Rise of the Beasts", "Polis Evo 3", "The Roundup: No Way Out",
  "Fast X", "Fast X", "Red Line", "Guardians of Galaxy Volume 3",
  "The Dark Knight", "Inception"
]
m_superheroes = [
    "The Flash", "Spiderman Across the Spider-Verse"
]
m_romance = [
    "Elemental", "My Precious", "No Hard Feelings", "Friend Zone",
    "Love Destiny the Movie"
]
m_comedy = [
    "Elemental", "No Hard Feelings", "Rise", "The Innocent ",
    "Sue-On", "The Super Mario Bros. Movie"
]
m_horror = [
    "Jemputan Ke Neraka", "Tasbih Kosong", "The Boogeyman",
    "Haunted Universities 2nd Semester", "The Conjuring 2",
    "Talk to Me", "Sue-On" 
]
m_fantasy = [
    "The Little Mermaid", "Takkar"
]
m_historical = [
    "Father & Soldier"
]
m_adventure = [
    "The Three Musketeers: Dartagnan", 
    "Indiana Jones And The Dial of Destiny",
    "The Super Mario Bros. Movie"
]
m_thriller = [
    "Faces the Anne", "Talk to Me"
]
###############################################################################################################################

n_action = [
    "Extraction 2", "Interceptor", "The Big 4",
    "The Mother"
]
n_romance = [
    "No Limit", "20th Century Girl", "Your Place of Mind",
    "365 Days"
]
n_mystery = [
    "Last Seen Alive", "Unlocked", "The Pale Blue Eye",
    "Luckiest Girl Alive"
]
n_crime = [
    "The Guilty", "Blackout", "The Good Nurse",
    "The Takeover"
]
genra_s = ["action", "superhero", "romance", "comedy", "horror", "fantasy", "historical", "adventure", "thriller"]

Cinema = {
  "action": choice(m_actions),
  "superhero": choice(m_superheroes),
  "romance": choice(m_romance),
  "comedy":choice(m_comedy),
  "horror":choice(m_horror),
  "fantasy":choice(m_fantasy),
  "historical":choice(m_historical),
  "adventure":choice(m_adventure),
  "thriller":choice(m_thriller),
}

Netflix = {
  "action": choice(n_action),
  "romance": choice(n_romance),
  "mystery": choice(n_mystery),
  "crime":choice(n_crime),
}
error_key = "invalid input noob"
farewell_in = ["bye", "got to go"]
farewell_out = ["adios amigo!", "have a great time!", "see ya next time", "please come again"]


def check_input(user_input, mode = 1):
    if mode == 1:
        flag = 0
        for inputs in user_input:
            if inputs in genra_s:
                txt.insert(END, "\n" + bot_name + "-> " +  Cinema[inputs])
                flag = 1
        if flag == 0:
            txt.insert(END, "\n" + bot_name + "-> " +  error_key)
    elif mode == 2:
        flag = 0
        for inputs in user_input:
            if inputs in genra_s:
                txt.insert(END, "\n" + bot_name + "-> " +  Netflix[inputs])
                flag = 1
        if flag == 0:
            txt.insert(END, "\n" + bot_name + "-> " +  error_key)
    #else: 

def check_bye(user_input):
    for inputs in user_input:
        if inputs in farewell_in:
            print(choice(farewell_out))
            txt.insert(END, "\n" + bot_name + "-> " +  choice(farewell_out))
            #sleep(5)
            #root.quit()
            return False
        else:
            return True
        
def main():
    main = "You -> " + e.get()
    txt.insert(END, "\n" + main)

    while True:
        user_input = str(e.get().lower())
        e.delete(0, END)
        user_input = user_input.split()
        run = check_bye(user_input)
        if run == True:
            check_input(user_input)
            break
        else:
            break


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

main = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=main).grid(row=2, column=1)

root.mainloop()


e.delete(0, END)
