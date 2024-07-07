import tkinter as tk
import random

class CityGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("City Guessing Game")
        master.configure(bg='#000000')

        self.cities = [
            "KARACHI", "PESHAWAR", "LAHORE", "ISLAMABAD", "PINDI", 
            "QUETTA", "HYDRABAD", "MULTAN", "MURREE", "SUKKUR",
            "ROHRI"
        ]

        self.city_to_guess = random.choice(self.cities).lower()
        self.number_of_guesses = 0
        self.guess_history = []

        self.create_widgets()

    def create_widgets(self):
        self.instructions = tk.Label(
            self.master, 
            text="Guess the city! It's a major city in the PAKISTAN.", 
            font=('Verdana', 15), 
            bg='#f0f0f0', 
            fg='#333'
        )
        self.instructions.pack(pady=10)
    

        self.guess_entry = tk.Entry(self.master, font=('Verdana', 15))
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(
            self.master, 
            text="Guess", 
            command=self.check_guess, 
            font=('Verdana', 15), 
            bg='#4CAF50', 
            fg='white'
        )
        self.guess_button.pack(pady=10)

        self.hint_button = tk.Button(
            self.master, 
            text="Hint", 
            command=self.provide_hint, 
            font=('Helvetica', 12), 
            bg='#2196F3', 
            fg='white'
        )
        self.hint_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="", font=('Helvetica', 15), bg='#f0f0f0', fg='#333')
        self.result_label.pack(pady=10)

        self.guess_history_label = tk.Label(self.master, text="Guess History:", font=('Helvetica', 15), bg='#f0f0f0', fg='#333')
        self.guess_history_label.pack(pady=10)

        self.history_text = tk.Text(self.master, height=10, width=50, state=tk.DISABLED, font=('Helvetica', 15), bg='#fff')
        self.history_text.pack(pady=10)

        self.reset_button = tk.Button(
            self.master, 
            text="Reset", 
            command=self.reset_game, 
            font=('Helvetica', 15), 
            bg='#f44336', 
            fg='white'
        )
        self.reset_button.pack(pady=10)

    def check_guess(self):
        guess = self.guess_entry.get().strip().lower()
        self.number_of_guesses += 1
        self.guess_history.append(guess)
        self.update_history()

        if guess == self.city_to_guess:
            self.result_label.config(text=f"Congratulations! You guessed the city in {self.number_of_guesses} attempts.")
        else:
            self.result_label.config(text="Wrong guess. Try again!")

    def provide_hint(self):
        hint = self.city_to_guess[:self.number_of_guesses + 1]
        self.result_label.config(text=f"Hint: {hint}")

    def update_history(self):
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        for guess in self.guess_history:
            self.history_text.insert(tk.END, guess + "\n")
        self.history_text.config(state=tk.DISABLED)

    def reset_game(self):
        self.city_to_guess = random.choice(self.cities).lower()
        self.number_of_guesses = 0
        self.guess_history = []
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.update_history()

if __name__ == "__main__":
    root = tk.Tk()
    game = CityGuessingGame(root)
    root.mainloop()


   


