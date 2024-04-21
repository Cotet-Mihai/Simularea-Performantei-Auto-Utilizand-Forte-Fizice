import customtkinter as ctk
from GUI.Make_car import CreazatiMasina


class MenuGui:
    """
    Clasa pentru crearea unei interfețe grafice de meniu.
    """
    def __init__(self, root: ctk.CTk):
        """
        Inițializează interfața grafică pentru meniu.

        :param root: Fereastra de bază CustomTkinter.
        """

        self.root: ctk.CTk = root
        self.widgets()

    def widgets(self) -> None:
        """
        :return: Returnează toate widget-urile necesare pentru fereastra menu
        """

        self.title = ctk.CTkLabel(
            self.root,
            text="Simularea Performanței Auto\nUtilizând Forțe Fizice",
            font=("Inter BOLD", 25)
        )
        self.title.place(anchor='center', x=300, y=50)

        self.info_text = ctk.CTkLabel(
            self.root,
            text="Cu această aplicație, poți analiza performanța mașinii tale în diverse condiții de drum. Folosind\n"
                 "datele introduse pentru marcă, brand, viteză maximă și alte caracteristici, aplicația calculează\n"
                 "aspecte precum accelerarea, timpul necesar pentru a atinge viteza maximă, timpul și distanța de\n"
                 "frânare în funcție de tipul de suprafață (uscat, umed sau zăpadă). Prin intermediul clasei integrate"
                 "\n'Mașină', obții o imagine clară și detaliată a performanței vehiculului tău.\n\n",
            font=("Inter SemiBold", 12)
        )
        self.info_text.place(anchor="center", x=300, y=200)

        self.creazati_propria_masina = ctk.CTkButton(
            self.root,
            width=200, height=50,
            text="Creaza-ti masina",
            font=("Inter Bold", 15),
            command=self.go_to_creazati_masina
        )
        self.creazati_propria_masina.place(anchor='center', x=300, y=350)

    def go_to_creazati_masina(self) -> None:
        """
        :return: Funcție pentru a naviga către interfața de creare a mașinii.
        """
        CreazatiMasina(self.root)
