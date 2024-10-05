import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        # Initialize game variables
        self.random_number = random.randint(1, 100)
        self.attempts = 0
        
        # Label to guide user
        self.instruction_label = tk.Label(root, text="Guess a number between 1 and 100")
        self.instruction_label.pack(pady=10)
        
        # Entry widget for user input
        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack(pady=10)
        
        # Button to submit guess
        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=10)
        
        # Label to show feedback
        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack(pady=10)

    def check_guess(self):
        try:
            # Get user input and increment attempts
            user_guess = int(self.guess_entry.get())
            self.attempts += 1
            
            # Check if the guess is correct, too high, or too low
            if user_guess < self.random_number:
                self.feedback_label.config(text="Too low! Try again.")
            elif user_guess > self.random_number:
                self.feedback_label.config(text="Too high! Try again.")
            else:
                self.feedback_label.config(text=f"Correct! It took you {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
        
    def reset_game(self):
        # Ask if user wants to play again
        play_again = messagebox.askyesno("Game Over", "You guessed it! Do you want to play again?")
        if play_again:
            self.random_number = random.randint(1, 100)
            self.attempts = 0
            self.guess_entry.delete(0, tk.END)
            self.feedback_label.config(text="")
        else:
            self.root.quit()

# Main setup
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
