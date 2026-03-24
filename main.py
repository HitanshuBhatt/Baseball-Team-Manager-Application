import tkinter as tk 
from ui import GUI

def main ():
    # initializing the main application window
    root = tk.TK ()
    app= GUI(root)

    # sart loop to keep application open 
    root.mainloop()

if __name__ =="__main__":
    main()


