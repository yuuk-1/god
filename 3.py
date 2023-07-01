from random import choice
import pygame
from pygame.locals import *

pygame.init()
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wumpus")

font = pygame.font.Font(None, 24)

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up chatbot variables
bot_name = 'Wumpus'
user_input = ''
bot_response = ''
bot_name = 'Wumpus'
invalid = False
cinema_movie_list={
        "action":["Transformers: Rise of the Beasts", "Polis Evo 3", "The Roundup: No Way Out","Fast X", "Red Line",
                "Guardians of Galaxy Volume 3","The Dark Knight", "Inception"],
        "superhero":["The Flash", "Spiderman Across the Spider-Verse"],
        "romance":["Elemental", "My Precious", "No Hard Feelings", "Friend Zone","Love Destiny the Movie"],
        "comedy":["Elemental", "No Hard Feelings", "Rise", "The Innocent ","Sue-On", "The Super Mario Bros. Movie"],
        "horror":["Jemputan Ke Neraka", "Tasbih Kosong", "The Boogeyman","Haunted Universities 2nd Semester", "The Conjuring 2",
                "Talk to Me", "Sue-On" ],
        "fantasy":["The Little Mermaid", "Takkar"],
        "historical":["Father & Soldier"],
        "adventure":["The Three Musketeers: Dartagnan", "Indiana Jones And The Dial of Destiny","The Super Mario Bros. Movie"],
        "thriller":["Faces the Anne", "Talk to Me"]
    }

netflix_list={
        "action": ["Extraction 2", "Interceptor", "The Big 4","The Mother"],
        "romance": ["No Limit", "20th Century Girl", "Your Place of Mind","365 Days"],
        "mystery": ["Last Seen Alive", "Unlocked", "The Pale Blue Eye","Luckiest Girl Alive"],
        "crime":["The Guilty", "Blackout", "The Good Nurse", "The Takeover"],
    }

area = {
    "Kuala_Lumpur" : ["Aurum Theatre, The Gardens Mall","GSC 1 Utama","GSC 3 Damansara","GSC Berjaya Times Square","GSC CITTA Mall",
                    "GSC EkoCheras Mall","GSC Lotus's Kepong","GSC Melawati Mall","GSC Mid Valley Megamall","GSC MyTOWN","GSC NU Sentral",
                    "GSC Quill City Mall","GSC Setapak Central, KL","GSC The Starling Mall"],
    "Melaka":["GSC Aeon Bandaraya Melaka","GSC Dataran Pahlawan"],
    "Johor_Bahru":["Aurum Theatre, The Mall, Mid Valley SouthKey","GSC AEON Mall Bandar Dato' Onn, Kempas","GSC IOI Mall Kulai",
                "GSC KSL City Mall, JB","GSC Mid Valley Southkey","GSC Paradigm JB","GSC Sunway Big Box"],
    "Ipoh":["GSC AEON Mall Ipoh Falim","GSC Ipoh Parade"],
    "Putrajaya":["GSC Alamanda","GSC IOI City Mall","GSC IOI City Mall 2"],
    "Alor_Setar":["GSC Aman Central"],
    "Sungai_Petani":["GSC Amanjaya Mall","GSC Central Square"],
    "Kuantan":["GSC East Coast Mall","GSC Kuantan City Mall, Kuantan"],
    "Penang":["GSC Gurney Plaza","GSC Queensbay Mall","GSC Sunway Carnival"],
    "Puchong":["GSC IOI Mall"],
    "Klang":["GSC Klang Parade"],
    "Seremban":["GSC Palm Mall"],
    "Petaling_Jaya":["GSC Paradigm Mall","GSC Tropicana Gardens Mall"],
    "Shah_Alam":["GSC Setia City Mall"],
    "Subang":["GSC Subang Parade","GSC Summit USJ"]
} 
###############################################################################################################################
def cinema_recommend(user_inputs):
    if user_inputs in cinema_movie_list.keys(): #check user input in our data ?
        for key in cinema_movie_list: # loop all the key to check user input one by one
            if user_inputs==key: #check if user input is equal to our data location
                for keys, values in cinema_movie_list.items(): # get items from data
                    if keys==user_inputs: # if same key print the value
                        recommendation = choice(values)
                        return recommendation
            else:
                pass
    else:
        return "Invalid Input.Please try again!"
    
def netflix_recommend(user_inputs):
    if user_inputs in netflix_list.keys(): #check user input in our data ?
        for key in netflix_list: # loop all the key to check user input one by one
            if user_inputs==key: #check if user input is equal to our data location
                for keys, values in netflix_list.items(): # get items from data
                    if keys==user_inputs: # if same key print the value
                        recommendation = choice(values)
                        return recommendation
            else:
                pass
    else:
        return "Invalid Input.Please try again!"
####################################################################################################################################
greeting_check = ['hallo', 'halo', 'konichiwa']
greeting_list = ['halo, how I can help you sir?', 'hello, how may I help you?']
farewell_check = ["bye", "got to go"]
farewell_list = ["adios amigo!", "have a great time!", "see ya next time", "please come again"]
watch_request = ["what you feel like having?", "what movie u want to watch?"]

def bot_greetings():
    wumpus_greeting= [
    "Hi",
    "Hello",
    "How are you?",
    "What's up?",
    "Yo",
    "How you doin?",
    "Good Morning",
    "Good Evening",
    "Good Afternoon",
    "Good Night",
    "What can I do with you?",
    "My name is Wumpus :D",
    "How can I help you?",
    ]
    return choice(wumpus_greeting)
def greetings(user_input):
    for inputs in user_input:
        if inputs in greeting_check:
            return bot_name,": ", choice(greeting_list)

def farewell(user_input):
    for inputs in user_input:
        if inputs in farewell_check:
            return bot_name,": ", choice(farewell_list)

def location(user_input):
    if user_input in area.keys(): #check user input in our data ?
        for key in area: # loop all the key to check user input one by one
            if user_input==key: #check if user input is equal to our data location
                for keys, values in area.items(): # get items from data
                    if keys==user_input: # if same key print the value
                        return'\n'.join(values)
            else:
                pass
    else:
        return'The location have no Theatre/Cinema around.'

def time(user_input):
    return

def display_text(text, font, position, color):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)

running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:
                # Process user input and generate bot response
                bot_greetings()
                bot_response = greetings(user_input)
                if not bot_response:
                    bot_response = cinema_recommend(user_input)
                if not bot_response:
                    bot_response = netflix_recommend(user_input)
                if not bot_response:
                    bot_response = location(user_input)
                if not bot_response:
                    bot_response = time(user_input)
                if not bot_response:
                    bot_response = farewell(user_input)

            elif event.key == K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    # Render text
    user_input_text = font.render('User: ' + str(user_input), True, BLACK)
    bot_response_text = font.render('Bot: ' + str(bot_response), True, BLACK)

    # Blit text to the screen
    screen.blit(user_input_text, (10, 10))
    screen.blit(bot_response_text, (10, 40))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
