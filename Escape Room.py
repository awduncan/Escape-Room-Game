import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter

# Initialize the speech recognition object
r = sr.Recognizer()

# Set the microphone energy threshold
r.energy_threshold = 4000

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to listen to the user's speech and convert it to text
def listen_speech():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source, timeout=5)  # Set a timeout of 5 seconds for listening
        try:
            text = r.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None

# Function to handle user commands and perform actions accordingly as well as show background photos
def handle_command(command):
    if check_keyword(command, ["look", "examine room", "look around", "look around room", "search room"]):
        output_text("You look around the room. It's dimly lit room with a door, a blood stained rug, a flashlight, a crooked mountain painting, and a dresser.")
        speak_text("You look around the room. It's dimly lit room with a door, a blood stained rug, a flashlight, a crooked mountain painting, and a dresser.")
        change_background_image("Final\\background.jpg")
    elif check_keyword(command, ["open door", "pull door", "turn knob", "hit door"]):
        output_text("The door is locked. You need to find a key.")
        speak_text("The door is locked. You need to find a key.")
        change_background_image("Final\\door1.jpg", )
    elif check_keyword(command, ["use flashlight", "grab flashlight", "examine flashlight", "turn on flashlight"]):
       output_text("You turn on the flashlight, illuminating the room.")
       speak_text("You turn on the flashlight, illuminating the room.")
       change_background_image("Final\\flashlight.jpg")
    elif check_keyword(command, ["look in dresser drawers", "look in drawers", "search dresser", "search drawers", "exmaine drawers", "look in dresser"]):
        output_text("You look in the dresser drawers and find a carving that says red rum but it might be backwards.")
        speak_text("You look in the dresser drawers and find a carving that says red rum but it might be backwards.")
        change_background_image("Final\\dresser.jpg")
    elif check_keyword(command, ["look at rug", "examine rug", "search rug", "look at blood stain"]):
        output_text("You look at the blood stained rug and you notice theres a cold draft under it.")
        speak_text("You look at the blood stained rug and you notice theres a cold draft under it.")
        change_background_image("Final\\rug.jpg")
    elif check_keyword(command, ["move rug", "lift rug", "touch rug"]):
        output_text("You move the rug aside, revealing a hidden compartment.")
        speak_text("You move the rug aside, revealing a hidden compartment.")
        change_background_image("Final\\secret.jpg")
    elif check_keyword(command, ["search compartment", "examine compartment", "look in compartment", "feel in compartment"]):
        output_text("You search the hidden compartment and find a note with a clue.")
        speak_text("You search the hidden compartment and find a note with a clue.")
        change_background_image("Final\\secret.jpg")
    elif check_keyword(command, ["read note", "look at note"]):
        output_text("The note reads: 'I stand tall, yet I never grow, A majestic presence, covered in snow. Hikers seek me, climbers aspire, Nature's challenge, reaching higher. What am I?'")
        speak_text("The note reads: 'I stand tall, yet I never grow, A majestic presence, covered in snow. Hikers seek me, climbers aspire, Nature's challenge, reaching higher. What am I?'")
        change_background_image("Final\\note.jpg")
    elif check_keyword(command, ["a mountain", "mountain"]):
        output_text("You remembered the painting on the wall and you take a look at it. It appears to be crooked.")
        speak_text("You remembered the painting on the wall and you take a look at it. It appears to be crooked.")
        change_background_image("Final\\painting.jpg")
    elif check_keyword(command, ["fix painting", "move painting", "touch painting", "move picture", "fix picture", "touch picture"]):
        output_text("As you straighten the painting, you notice a safe hidden behind it with a letter key pad lock.")
        speak_text("As you straighten the painting, you notice a safe hidden behind it with a letter key pad lock.")
        change_background_image("Final\\safe.jpg")
    elif check_keyword(command, ["murder", "enter murder", "type in murder", "type murder into safe", "type murder", "enter murder into key pad"]):
        output_text("You enter murder into the safe and it opens up and you find a door key.")
        speak_text("You enter murder into the safe and it opens up and you find a door key.")
        change_background_image("Final\\murder.jpg")
    elif check_keyword(command, ["use key", "open door", "unlock door"]):
        output_text("You use the key to unlock the door. Congratulations! You've escaped!")
        speak_text("You use the key to unlock the door. Congratulations! You've escaped!")
        change_background_image("Final\\You won!.jpg")
        messagebox.showinfo("Escape Room", "You use the key to unlock the door.\nCongratulations! You've escaped!")
        window.destroy() # Close game window once user has won 
    elif check_keyword(command, ["exit", "quit", "leave"]): # If player wants to exit game prematurely
        output_text("Thank you for playing! Goodbye!")
        speak_text("Thank you for playing! Goodbye!")
        change_background_image("Final\\exit.jpg")
        messagebox.showinfo("Thank you for playing! Goodbye!")
        window.destroy()
        return
    else:
        output_text("I'm sorry, I don't understand that command.")

# Function to check if a keyword is present in the users input
def check_keyword(text, keywords):
    for keyword in keywords:
        if keyword in text:
            return True
    return False

# Function to convert text to speech
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to display text in the GUI
def output_text(text):
    textbox.config(state=tk.NORMAL)
    textbox.insert(tk.END, text + "\n")
    textbox.config(state=tk.DISABLED)
    textbox.see(tk.END)

# Function to handle the "Speak" button click event
def speak_button_click():
    command = listen_speech()
    if command is not None:
        output_text("You said: " + command)
        handle_command(command)
    else:
        output_text("Sorry, I didn't understand.")

# Function to change the background image
def change_background_image(image_path):
    width = 600
    height = 400

    background_image = Image.open(image_path)
    background_image = background_image.resize((width, height), Image.LANCZOS)
    background_image = background_image.filter(ImageFilter.SHARPEN)
    background_photo = ImageTk.PhotoImage(background_image)
    background_label.configure(image=background_photo)
    background_label.image = background_photo

# Create the main window
window = tk.Tk()
window.title("Mystery Escape Room")

# Load and display the background photo
background_image = Image.open("D:\\Updated APC and AI\\Final\\Final\\background.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.pack(fill="both", expand=True)

# Create the text box for displaying the game output
textbox = tk.Text(window, width=60, height=15, state=tk.DISABLED, bg="black", fg="white")
textbox.pack(padx=10, pady=10)

# Create the "Speak" button
speak_button = tk.Button(window, text="Speak", width=10, command=speak_button_click)
speak_button.pack(pady=5)

# Start the game
output_text("Welcome to Mystery Escape Room!")
output_text("You are trapped in a room. Your goal is to find a key and escape. Try saying look around while pressing the speak button.")
speak_text("Welcome to Mystery Escape Room!")
speak_text("You are trapped in a room. Your goal is to find a key and escape. Try saying look around while pressing the speak button.")

window.mainloop()
