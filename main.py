import tkinter as tk

# Constants for colors
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}


def text_to_morse():
    user_input = text_input.get()
    morse_code_list = []

    # Convert user input to uppercase for consistency
    user_text = user_input.upper()

    for char in user_text:
        if char == " ":
            morse_code_list.append("   ")
        elif char in morse_code_dict:
            morse_code_list.append(morse_code_dict[char])

    morse_code.config(text=f'Morse Code: {"".join(morse_code_list)}', padx=10, pady=10)


# Create the main application window
window = tk.Tk()
window.title("Text To Morse-Code Converter")
window.config(padx=100, pady=50, bg='white')

# Create GUI elements
header = tk.Label(
    text="Text To Morse-Code Converter",
    font=('Arial', 20, "bold"),
    foreground=GREEN,
    background=YELLOW
)
header.grid(column=1, row=0)

text = tk.Label(
    text="Text:",
    font=('Arial', 12, "normal")
)
text.grid(column=0, row=1)

text_input = tk.Entry(window)
text_input.insert(0, "")
text_input.grid(column=1, row=1, padx=10, pady=10)

morse_code = tk.Label(
    text="",
    font=('Arial', 48, "normal")
)
morse_code.grid(column=1, row=2)

start_button = tk.Button(
    text="Convert",
    font=('Arial', 12, "bold"),
    padx=20,
    pady=5,
    command=text_to_morse
)
start_button.grid(column=1, row=3)

window.mainloop()