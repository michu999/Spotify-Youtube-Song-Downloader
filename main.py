from gui import GUI
import tkinter as tk

def main():
    """Initialize and run the GUI application."""
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
