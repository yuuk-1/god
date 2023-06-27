from random import choice

bot_name = 'Wumpus'
invalid = False

cinema_check = ["cinema"]
netflix_check = ["netflix", "home", "house"]
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

cinema = {
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
####################################################################################################################################
greeting_check = ['hallo', 'halo', 'konichiwa']
greeting_list = ['halo, how I can help you sir?', 'hello, how may I help you?']

farewell_check = ["bye", "got to go"]
farewell_list = ["adios amigo!", "have a great time!", "see ya next time", "please come again"]

watch_request = ["what you feel like having?", "what movie u want to watch?"]

def greetings(user_input):
    for inputs in user_input:
        if inputs in greeting_check:
            print(bot_name,"-->", choice(greeting_list))

def farewell(user_input):
    for inputs in user_input:
        if inputs in farewell_check:
            print(bot_name,"-->", choice(farewell_list))

def cinema_movie(user_input):
    
    for inputs in user_input:
        if inputs in cinema_check:
            print(bot_name, "-->", choice(watch_request))
            user_input = str(input("Me --> "))
            user_input = user_input.lower().split()
    for inputs in user_input:
        if inputs in genra_s:
            print(bot_name,"-->", cinema[inputs])

def netflex_movie(user_input):
    for inputs in user_input:
        if inputs in netflix_check:
            print(bot_name, "-->", choice(watch_request))
            user_input = str(input("Me --> "))
            user_input = user_input.lower().split()
    for inputs in user_input:
        if inputs in genra_s:
            print(bot_name,"-->", Netflix[inputs])

def not_in(user_input):
        for inputs in user_input:
            if inputs in (netflix_check or cinema_check or greeting_check or farewell_check):
                print(bot_name, "--> GG invalid input noob", )


def main():
    while True:
        
        user_inputs = str(input("Me --> "))
        user_inputs = user_inputs.lower().split()
        greetings(user_inputs)
        farewell(user_inputs)
        cinema_movie(user_inputs)
        netflex_movie(user_inputs)
        not_in(user_inputs)
        
main()
