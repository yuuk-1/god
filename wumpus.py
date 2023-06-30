from random import choice

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
    "Kuala Lumpur" : ["Aurum Theatre, The Gardens Mall","GSC 1 Utama","GSC 3 Damansara","GSC Berjaya Times Square","GSC CITTA Mall",
                    "GSC EkoCheras Mall","GSC Lotus's Kepong","GSC Melawati Mall","GSC Mid Valley Megamall","GSC MyTOWN","GSC NU Sentral",
                    "GSC Quill City Mall","GSC Setapak Central, KL","GSC The Starling Mall"],
    "Melaka":["GSC Aeon Bandaraya Melaka","GSC Dataran Pahlawan"],
    "Johor Bahru":["Aurum Theatre, The Mall, Mid Valley SouthKey","GSC AEON Mall Bandar Dato' Onn, Kempas","GSC IOI Mall Kulai",
                "GSC KSL City Mall, JB","GSC Mid Valley Southkey","GSC Paradigm JB","GSC Sunway Big Box"],
    "Ipoh":["GSC AEON Mall Ipoh Falim","GSC Ipoh Parade"],
    "Putrajaya":["GSC Alamanda","GSC IOI City Mall","GSC IOI City Mall 2"],
    "Alor Setar":["GSC Aman Central"],
    "Sungai Petani":["GSC Amanjaya Mall","GSC Central Square"],
    "Kuantan":["GSC East Coast Mall","GSC Kuantan City Mall, Kuantan"],
    "Penang":["GSC Gurney Plaza","GSC Queensbay Mall","GSC Sunway Carnival"],
    "Puchong":["GSC IOI Mall"],
    "Klang":["GSC Klang Parade"],
    "Seremban":["GSC Palm Mall"],
    "Petaling Jaya":["GSC Paradigm Mall","GSC Tropicana Gardens Mall"],
    "Shah Alam":["GSC Setia City Mall"],
    "Subang":["GSC Subang Parade","GSC Summit USJ"]
} 
###############################################################################################################################
def cinema_recommend(user_inputs):
    if user_inputs in cinema_movie_list.keys(): #check user input in our data ?
        for key in cinema_movie_list: # loop all the key to check user input one by one
            if user_inputs==key: #check if user input is equal to our data location
                for keys, values in cinema_movie_list.items(): # get items from data
                    if keys==user_inputs: # if same key print the value
                        print(choice(values), end="\n")
            else:
                pass
    else:
        print("Invalid Input.Please try again!")
    
def netflix_recommend(user_inputs):
    if user_inputs in netflix_list.keys(): #check user input in our data ?
        for key in netflix_list: # loop all the key to check user input one by one
            if user_inputs==key: #check if user input is equal to our data location
                for keys, values in netflix_list.items(): # get items from data
                    if keys==user_inputs: # if same key print the value
                        print(choice(values), end="\n")
            else:
                pass
    else:
        print("Invalid Input.Please try again!")
####################################################################################################################################
greeting_check = ['hallo', 'halo', 'konichiwa']
greeting_list = ['halo, how I can help you sir?', 'hello, how may I help you?']
farewell_check = ["bye", "got to go"]
farewell_list = ["adios amigo!", "have a great time!", "see ya next time", "please come again"]
watch_request = ["what you feel like having?", "what movie u want to watch?"]

def bot_greetings():
    wumpus_greeting=statements = [
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
    print(choice(wumpus_greeting))
def greetings(user_input):
    for inputs in user_input:
        if inputs in greeting_check:
            print(bot_name,"-->", choice(greeting_list))

def farewell(user_input):
    for inputs in user_input:
        if inputs in farewell_check:
            print(bot_name,"-->", choice(farewell_list))



def location(user_inputs): 
    if user_inputs in area.keys(): #check user input in our data ?
        for key in area: # loop all the key to check user input one by one
            if user_inputs==key: #check if user input is equal to our data location
                for keys, values in area.items(): # get items from data
                    if keys==user_inputs: # if same key print the value
                        print("Here are cinema theatre near you")
                        print("--------------------------------")
                        print('\n'.join(values), end="\n")
            else:
                pass
    else:
        print('The location have no Theatre/Cinema around.')
        

print("Wumpus--> ",end="")
bot_greetings()
print("Wumpus--> Are you looking For cinema Movie or Netflix? ")
user_inputs = str(input("User --> ")).lower()
if user_inputs == "cinema":
    print("Wumpus--> What genres of movie are you looking for?" )
    while True:
        user_inputs = str(input("User--> "))
        #user_inputs = user_inputs.lower().split()
        if user_inputs == "bye":
            break
        else:
            for key in cinema_movie_list:#loop our key in dict
                if key in user_inputs.split():# check key if same with user input with the key word
                    print("Wumpus --> I recommend you to watch ",end="")
                    user_inputs= key
                    cinema_recommend(user_inputs)
        
elif user_inputs == "netflix":
    print("Wumpus--> What genres of movie are you looking for?" )
    while True:
        user_inputs = str(input("User--> "))
        #user_inputs = user_inputs.lower().split()
        if user_inputs == "Bye":
            break
        else:
            for key in netflix_list: #loop our key in dict
                if key in user_inputs.split(): # check key if same with user input with the key word
                    print("Wumpus --> I recommend you to watch ",end="")
                    user_inputs= key
                    netflix_recommend(user_inputs)

print("Wumpus--> Where Do you Live?")
while True:
        user_inputs = str(input("User--> "))
        #user_inputs = user_inputs.lower().split()
        if user_inputs == "Bye":
            break
        else:
            for key in area: #loop our key in dict
                if key in user_inputs.split(): # check key if same with user input with the key word
                    user_inputs= key
                    location(user_inputs)
    


