import random
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.secret_number = random.randint(1, 100)
        self.max_attempts = 10
        self.attempts = 0

        # Fetch the background image from the internet
        response = requests.get("https://img.freepik.com/premium-photo/blue-question-mark-random-pattern-background-illustration_103740-566.jpg?size=626&ext=jpg&ga=GA1.1.1826414947.1699056000&semt=ais")
        image_data = response.content

        # Create an image object
        img = Image.open(BytesIO(image_data))
        self.background_image = ImageTk.PhotoImage(img)

        # Create a label for the background image
        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.label = tk.Label(root, text="Guess the number between 1 and 100:", font=("Helvetica", 16))
        self.label.pack()

        # Create an entry widget
        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack()

        # Create a submit button
        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess, font=("Helvetica", 14))
        self.submit_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        self.attempts += 1

        if guess < self.secret_number:
            messagebox.showinfo("Result", "Too low! Try again.")
        elif guess > self.secret_number:
            messagebox.showinfo("Result", "Too high! Try again.")
        else:
            messagebox.showinfo("Congratulations", f"You guessed the secret number {self.secret_number} in {self.attempts} attempts.")
            self.root.quit()

        if self.attempts == self.max_attempts:
            messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The secret number was {self.secret_number}.")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.geometry("600x400")  # Set the window size
    root.mainloop()
