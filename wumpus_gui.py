from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from random import choice

class Chatbot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Wumpus - The knowledge-based agent')
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout()

        self.chat_label = QLabel('Chat:')
        self.layout.addWidget(self.chat_label)

        self.conversation = QLabel()
        self.layout.addWidget(self.conversation)

        self.input_label = QLabel('User:')
        self.layout.addWidget(self.input_label)

        self.input_line = QLineEdit()
        self.layout.addWidget(self.input_line)

        self.send_button = QPushButton('Send')
        self.send_button.clicked.connect(self.handle_send)
        self.layout.addWidget(self.send_button)

        self.setLayout(self.layout)

        self.greeting_list = ['Hello, how may I help you?', 'Hi there! What can I assist you with?']
        self.farewell_list = ['Goodbye!', 'See you next time!', 'Take care!']

        self.greet()

    def handle_send(self):
        user_input = self.input_line.text()
        self.input_line.clear()

        self.add_message('User:', user_input)

        if "cinema" in user_input.lower().split():
            self.cinema_recommendation()
        elif "netflix"  in user_input.lower().split():
            self.netflix_recommendation()
        elif "goodbye" in user_input.lower().split():
            self.farewell()
        else:
            self.add_message('Wumpus:', 'Invalid input. Please try again!')

    def greet(self):
        greeting = choice(self.greeting_list)
        self.add_message('Wumpus:', greeting)

    def farewell(self):
        farewell = choice(self.farewell_list)
        self.add_message('Wumpus:', farewell)

    def cinema_recommendation(self):
        genres = ['action', 'superhero', 'romance', 'comedy', 'horror', 'fantasy', 'historical', 'adventure', 'thriller']
        genre = choice(genres)

        cinema_movie_list = {
            'action': ['Transformers: Rise of the Beasts', 'Polis Evo 3', 'The Roundup: No Way Out', 'Fast X', 'Red Line', 'Guardians of Galaxy Volume 3', 'The Dark Knight', 'Inception'],
            'superhero': ['The Flash', 'Spiderman Across the Spider-Verse'],
            'romance': ['Elemental', 'My Precious', 'No Hard Feelings', 'Friend Zone', 'Love Destiny the Movie'],
            'comedy': ['Elemental', 'No Hard Feelings', 'Rise', 'The Innocent', 'Sue-On', 'The Super Mario Bros. Movie'],
            'horror': ['Jemputan Ke Neraka', 'Tasbih Kosong', 'The Boogeyman', 'Haunted Universities 2nd Semester', 'The Conjuring 2', 'Talk to Me', 'Sue-On'],
            'fantasy': ['The Little Mermaid', 'Takkar'],
            'historical': ['Father & Soldier'],
            'adventure': ['The Three Musketeers: Dartagnan', 'Indiana Jones And The Dial of Destiny', 'The Super Mario Bros. Movie'],
            'thriller': ['Faces the Anne', 'Talk to Me']
        }

        recommendation = choice(cinema_movie_list[genre])
        self.add_message('Wumpus:', f"I recommend you to watch '{recommendation}' ({genre} genre).")

    def netflix_recommendation(self):
        genres = ['action', 'drama', 'comedy', 'sci-fi', 'horror', 'romance', 'documentary']
        genre = choice(genres)

        netflix_movie_list = {
            'action': ['Extraction', 'The Old Guard', 'Army of the Dead', 'Triple Frontier', '6 Underground'],
            'drama': ['Marriage Story', 'The Irishman', 'Roma', 'The Trial of the Chicago 7', 'Manchester by the Sea'],
            'comedy': ['The Half of It', 'To All the Boys I\'ve Loved Before', 'Always Be My Maybe', 'Eurovision Song Contest: The Story of Fire Saga', 'Dolemite Is My Name'],
            'sci-fi': ['Stranger Things', 'Black Mirror', 'Altered Carbon', 'The Expanse', 'Sense8'],
            'horror': ['The Haunting of Hill House', 'Bird Box', 'The Witcher', 'Locke & Key', 'The Ritual'],
            'romance': ['Bridgerton', 'Emily in Paris', 'Love, Death & Robots', 'Sex Education', 'Virgin River'],
            'documentary': ['Tiger King', 'Making a Murderer', 'The Social Dilemma', 'The Last Dance', 'Fyre']
        }

        recommendation = choice(netflix_movie_list[genre])
        self.add_message('Wumpus:', f"I recommend you to watch '{recommendation}' on Netflix ({genre} genre).")

    def add_message(self, sender, message):
        conversation = self.conversation.text()
        if conversation == '':
            conversation += f'{sender} {message}'
        else:
            conversation += f'\n{sender} {message}'

        self.conversation.setText(conversation)
        self.conversation.repaint()


if __name__ == '__main__':
    app = QApplication([])
    chatbot = Chatbot()
    chatbot.show()
    app.exec()
