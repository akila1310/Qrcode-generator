QRCODE GENERATOR USING PYTHON

   *  In this Qrcode Generator using python , the User is given the TEXT or URL then convert the QRCODE by saving the image codes.png.


INSTALL REQUIRED LIBRARIES :

   * pip install qrcode[pil] pillow
   * pip install tk
   * pip install qrcode
   * pip install Image
   * pip install ImageTk

TKINTER :
   * Tkinter ("Tee-Kay-Inter")is the Standard GUI(Graphical User Interface) library for python . It allows  Python developers to create desktop applications with graphical intefaces.

BASIC STRUCTURE OF A TKINTER PROGRAM :
   * Importing  Libraries
   * Creating the Main Application Window
   * Defining Functions and callbacks
   * Creating Widgets such as Labels,buttons,text Boxes etc..
   * Placing Widgets
   * Running the application
COMMON WIDGETS :

   LABEL :
       * Displays text or images
             label = tk.Label(root,,text="Hello")
             label.pack()
  BUTTON  :
       * A clickable button
             button = tk.Button(root,text="Click me", command = on_button_click)
             button.pack()
  ENTRY :
         * A Single-line text input
             entry = tk.Entry(root)
             entry.pack()
 TEXT :    
        * A multi-line text input                
             text = tk.Text(root)
             text.pack()
 FRAME : 
       * A Container for Organizing other widgets
              frame = tk.Frame(root)
              frame.pack()

GEOMETRY MANAGERS :

 PACK :
      * Packs widgets into the parent Widgets in order , either vertically or horizontally.
            widgets.pack(side="top",fill="both",expand="true")
 PLACE :
      *  places widgets at an absolute position you specify.
            widget.place(x=50,y=50)
         
