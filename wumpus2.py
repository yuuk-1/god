from random import choice
import tkinter as tk

bot_name = 'Wumpus'

cinema_movie_list = {
    "action": ["Transformers: Rise of the Beasts", "Polis Evo 3", "The Roundup: No Way Out", "Fast X", "Red Line",
               "Guardians of Galaxy Volume 3", "The Dark Knight", "Inception"],
    "superhero": ["The Flash", "Spiderman Across the Spider-Verse"],
    "romance": ["Elemental", "My Precious", "No Hard Feelings", "Friend Zone", "Love Destiny the Movie"],
    "comedy": ["Elemental", "No Hard Feelings", "Rise", "The Innocent ", "Sue-On", "The Super Mario Bros. Movie"],
    "horror": ["Jemputan Ke Neraka", "Tasbih Kosong", "The Boogeyman", "Haunted Universities 2nd Semester",
               "The Conjuring 2", "Talk to Me", "Sue-On"],
    "fantasy": ["The Little Mermaid", "Takkar"],
    "historical": ["Father & Soldier"],
    "adventure": ["The Three Musketeers: Dartagnan", "Indiana Jones And The Dial of Destiny",
                  "The Super Mario Bros. Movie"],
    "thriller": ["Faces the Anne", "Talk to Me"]
}

netflix_list = {
    "action": ["Extraction 2", "Interceptor", "The Big 4", "The Mother"],
    "romance": ["No Limit", "20th Century Girl", "Your Place of Mind", "365 Days"],
    "mystery": ["Last Seen Alive", "Unlocked", "The Pale Blue Eye", "Luckiest Girl Alive"],
    "crime": ["The Guilty", "Blackout", "The Good Nurse", "The Takeover"],
}

area = {
    "Kuala Lumpur": ["Aurum Theatre, The Gardens Mall", "GSC 1 Utama", "GSC 3 Damansara", "GSC Berjaya Times Square",
                     "GSC CITTA Mall",
                     "GSC EkoCheras Mall", "GSC Lotus's Kepong", "GSC Melawati Mall", "GSC Mid Valley Megamall",
                     "GSC MyTOWN", "GSC NU Sentral",
                     "GSC Quill City Mall", "GSC Setapak Central, KL", "GSC The Starling Mall"],
    "Melaka": ["GSC Aeon Bandaraya Melaka", "GSC Dataran Pahlawan"],
    "Johor Bahru": ["Aurum Theatre, The Mall, Mid Valley SouthKey", "GSC AEON Mall Bandar Dato' Onn, Kempas",
                    "GSC IOI Mall Kulai",
                    "GSC KSL City Mall, JB", "GSC Mid Valley Southkey", "GSC Paradigm JB", "GSC Sunway Big Box"],
    "Ipoh": ["GSC AEON Mall Ipoh Falim", "GSC Ipoh Parade"],
    "Putrajaya": ["GSC Alamanda", "GSC IOI City Mall", "GSC IOI City Mall 2"],
    "Alor Setar": ["GSC Aman Central"],
    "Sungai Petani": ["GSC Amanjaya Mall", "GSC Central Square"],
    "Kuantan": ["GSC East Coast Mall", "GSC Kuantan City Mall"],
    "Kota Bharu": ["GSC Aeon Mall Kota Bharu"],
    "Kuala Terengganu": ["GSC Mesra Mall"],
    "Kuching": ["GSC CityONE Megamall", "GSC Riverside Majestic"],
    "Miri": ["GSC Bintang Megamall", "GSC Imperial City Mall"],
    "Sibu": ["GSC Sibu Delta Mall"],
    "Kota Kinabalu": ["GSC Imago Mall", "GSC Suria Sabah"],
    "Sandakan": ["GSC Sandakan Sentral", "GSC Harbour Mall"],
    "Tawau": ["GSC Mesra Mall"],
    "Labuan": ["GSC Labuan Parade"],
}

greeting_list = ["Hello!", "Hi there!", "Greetings!", "Hey!"]

def cinema_recommend(user_inputs):
    genres = user_inputs.split()[2:]
    movies = []
    for genre in genres:
        if genre in cinema_movie_list:
            movies.extend(cinema_movie_list[genre])
            break
    if movies:
        return "\n".join(movies)
    else:
        return "No movies found for the given genres."

def netflix_recommend(user_inputs):
    genres = user_inputs.split()[2:]
    movies = []
    for genre in genres:
        if genre in netflix_list:
            movies.extend(netflix_list[genre])
    if movies:
        return "\n".join(movies)
    else:
        return "No movies found for the given genres."

def bot_greetings():
    return choice(greeting_list)

def greetings(user_input):
    return "Wumpus--> " + bot_greetings()

def farewell(user_input):
    return "Wumpus--> Goodbye! Have a great day!"

def location(user_inputs):
    area_found = []
    for a in area:
        for word in user_inputs.split():
            if word.lower() in a.lower():
                area_found.append(a)
    if area_found:
        return area_found
    else:
        return "Location not found!"

def recommend_movies():
    user_inputs = input_entry.get().lower()

    if "cinema" in user_inputs.split():
        result_label.config(text="Wumpus --> What genres of movie are you looking for?")
        recommendations = cinema_recommend(user_inputs)
        result_label.config(text="Wumpus --> Here are some cinema movie recommendations: \n" + recommendations)

    elif "netflix" in user_inputs.split():
        result_label.config(text="Wumpus --> What genres of movie are you looking for?")
        recommendations = netflix_recommend(user_inputs)
        result_label.config(text="Wumpus --> Here are some Netflix movie recommendations: \n" + recommendations)

    elif "location" in user_inputs.split():
        result_label.config(text="Wumpus --> Please enter your area:")
        areas = location(user_inputs)
        result_label.config(text="Wumpus --> The cinema locations available in your area are: \n" + ", ".join(areas))

    else:
        result_label.config(text="Wumpus --> Invalid Input")

# Create the GUI window
window = tk.Tk()
window.title("Movie Recommendation Bot")
window.geometry("400x300")

# Create labels and entry fields
greeting_label = tk.Label(window, text=greetings(""))
greeting_label.pack()

instruction_label = tk.Label(window, text="Wumpus--> Are you looking for cinema movies, Netflix, or cinema locations?")
instruction_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

# Create button
recommend_button = tk.Button(window, text="Recommend Movies", command=recommend_movies)
recommend_button.pack()

# Create result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
