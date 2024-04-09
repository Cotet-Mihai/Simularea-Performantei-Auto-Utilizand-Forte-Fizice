import customtkinter as ctk
from GUI.MenuGui import MenuGui

if __name__ == '__main__':

    root: ctk.CTk = ctk.CTk()  # Root
    root.geometry("600x500")  # Dimensiune fereastra
    root.resizable(False, False)  # Nu permitem modificarea dimensiunii ferestrei
    root.title("Proiect MCSN")

    # Crearea meniului și afișarea acestuia
    MenuGui(root)

    root.mainloop()  # Rularea buclei de evenimente
