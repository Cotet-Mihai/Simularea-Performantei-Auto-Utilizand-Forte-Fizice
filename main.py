import customtkinter as ctk
from Pages.menu import Menu

if __name__ == '__main__':

    root: ctk.CTk = ctk.CTk()  # Root
    root.geometry("600x400")  # Dimensiune fereastra
    root.resizable(False, False)  # Nu permitem modificarea dimensiunii ferestrei
    root.title("Simulation of Car Performance Using Physical Forces")

    # Crearea meniului și afișarea acestuia
    menu = Menu(root)
    menu.gui()

    root.mainloop()  # Rularea buclei de evenimente
