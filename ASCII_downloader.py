import tkinter as tk
import  requests
import pyfiglet

window = tk.Tk()
window.geometry("900x600")
window.title("ASCII Downloader")
window.grid_columnconfigure(0 , weight=1)

# Download ASCII
def download_ascii():
    if text_input.get():
        user_input = text_input.get()
        payload = {"text": user_input}
        response = pyfiglet.figlet_format(user_input)
        text_response = response
    else:
        text_response = "Aggiungi una parola o una frase nel campo di testo"
        
    textwidget= tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=3, column=0, sticky="we", padx=10 , pady=10)

# Top Frame
welcome_label = tk.Label(window, text="Welcome! Aggiungi una parola o una frase:", font=("helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="n", padx=20, pady=20)

# Bottom Frame
bottom_frame = tk.Label(window , text="Creato da @FabioDG",font=("helvetica", 10))
bottom_frame.grid(row=10, column=0, sticky="we", padx=10, pady=10)
# Text Input
text_input = tk.Entry(window, font=("helvetica", 15), width=30)
text_input.grid(row=1, column=0, sticky="we",padx=10, pady=10)
text_input.bind("<Return>", lambda event: download_ascii())
text_input.focus()

# Download Button
donwload_button = tk.Button(window, text="Download", command=download_ascii)
donwload_button.grid(row=2, column=0 ,sticky="we", padx=10, pady=10)
# Run the window
if __name__ == "__main__":
    window.mainloop()