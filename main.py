import tkinter as tk
from tkinter import font
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' ',  # Space character
}

def text_to_morse(text):
    morse_code = ""
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            morse_code += char  # Keep non-alphanumeric characters as is
    return morse_code.strip()

def convert_text():
    input_text = text_entry.get()
    result = text_to_morse(input_text)
    morse_label.config(text="Morse Code: " + result)





# Create the main window
root = tk.Tk()
root.title("Text to Morse Code Converter")
root.geometry("400x200")
root.configure(bg="#f0f0f0")  # Set background color

# Create custom font
custom_font = font.Font(family="Helvetica", size=12)

# Create widgets
text_entry = tk.Entry(root, font=custom_font, width=40)
convert_button = tk.Button(root, text="Convert", font=custom_font, command=convert_text, bg="#4CAF50", fg="white")
morse_label = tk.Label(root, font=custom_font, text="Morse Code: ", bg="#f0f0f0")

# Layout widgets using grid
text_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
convert_button.grid(row=1, column=0, padx=10, pady=5)
morse_label.grid(row=1, column=1, padx=10, pady=5)

# Start the main event loop
root.mainloop()