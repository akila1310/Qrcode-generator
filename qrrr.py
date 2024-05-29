import tkinter as tk
from tkinter import messagebox
import pyqrcode
from tkinter import ttk
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Input field cannot be empty")
        return
    
    
    # Generate QR code
    qr = pyqrcode.create(data)
    
    # Save QR code as PNG
    file_name = 'codes.png'
    qr.png(file_name, scale=8)
    
    # Display QR code
    display_qr(file_name)

def display_qr(file_name):
    img = Image.open(file_name)
    resized_img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    
    panel.config(image=img)
    panel.image = img

# Create main window
root = tk.Tk()
root.title("QR Code Generator")

# Create input frame
frame = tk.Frame(root)
frame.pack(pady=20)


# Create input label and entry
label = tk.Label(frame, text="Enter TEXT or URL:",font="Geogre,25")
label.grid(row=0, column=0, padx=10)

entry = tk.Entry(frame, width=40,border= 6,background='lightblue',font="Geogre,15,Bold ")
entry.grid(row=0, column=1, padx=50,pady=100)




# Create generate button
button = tk.Button(root, text="Generate QR Code", command=generate_qr,bg='pink',font="Times,20")
button.pack(padx=5)

# Create panel to display QR code
panel = tk.Label(root)
panel.pack(pady=20)

# Start the GUI loop
root.mainloop()