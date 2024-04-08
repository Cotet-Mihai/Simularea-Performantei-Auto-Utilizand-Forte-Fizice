import customtkinter as ctk
from GUI.MenuGui import MenuGui

if __name__ == '__main__':

    root = ctk.CTk()  # Root
    root.geometry("600x500")  # Dimensiune fereastra
    root.resizable(False, False)
    root.title("Proiect MCSN")

    MenuGui(root)  # Apelam interfata grafica

    root.mainloop()  # Loop
