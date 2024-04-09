import customtkinter as ctk
from Masina import Masina
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CreazatiMasina:
    """
    Clasa pentru crearea unei interfețe grafice pentru introducerea parametrilor unei mașini și afișarea graficelor.
    """

    marca = "Adauga"
    model = "Masina"
    acceleratia = None
    viteza = None
    masa = None
    deceleratia = None

    masina_creata = None

    def __init__(self, root: ctk.CTk):
        """
        Inițializează interfața grafică.

        :param root: Fereastra de bază CustomTkinter.
        """

        self.root = root
        self.widgets()

    def widgets(self) -> None:
        """
        :return: Returnează toate widget-urile necesare pentru fereastra de meniu
        """

        self.frame = ctk.CTkFrame(
            self.root,
            width=600, height=500
        )
        self.frame.place(x=0, y=0)

        self.title = ctk.CTkLabel(
            self.frame,
            text="Creați mașina",
            font=("Inter Bold", 25)
        )
        self.title.place(anchor='n', x=150, y=25)

        self.deceleratia_label = ctk.CTkLabel(
            self.frame,
            text="Starea asfaltului",
            font=("Inter SemiBold", 12)
        )
        self.deceleratia_label.place(anchor='n', x=150, y=100)

        self.deceleratia = ctk.CTkSegmentedButton(
            self.frame,
            values=["Uscat", "Umed", "Îngheţat"]
        )
        self.deceleratia.place(anchor='n', x=150, y=125)

        self.i = 0
        self.y = 200
        self.pointer = 0

        self.parametrii_list = ["Marcă", "Model", "Accelerație(de la 0 la 100Km/H)", "Viteza maximă(Km/H)", "Masa(Kg)"]
        self.lista_entry = []

        while self.i < 5:
            print(self.i)

            self.entry = ctk.CTkEntry(
                self.frame,
                width=200,
                placeholder_text=self.parametrii_list[self.pointer],
                justify='center'
            )
            self.entry.place(anchor='center', x=150, y=self.y)

            self.lista_entry.append(self.entry)

            self.i += 1
            self.y += 40
            self.pointer += 1

        self.error_label = ctk.CTkLabel(
            self.frame,
            text='',
            font=('Inter BOLD', 15),
            text_color='red'
        )
        self.error_label.place(anchor='center', x=150, y=400)

        self.execute_button = ctk.CTkButton(
            self.frame,
            text="Execută",
            font=("Inter Bold", 20),
            command=self.execute_button_function
        )
        self.execute_button.place(anchor='s', x=150, y=475)

        self.black_line = ctk.CTkFrame(
            self.frame,
            corner_radius=20,
            width=2, height=450,
            fg_color="#029cff"
        )
        self.black_line.place(anchor='center', x=300, y=250)

        self.full_name_car = ctk.CTkLabel(
            self.frame,
            text=f"{CreazatiMasina.marca} {CreazatiMasina.model}",
            font=("Inter Bold", 25)
        )
        self.full_name_car.place(anchor='n', x=450, y=25)

        self.i_2 = 0
        self.y_2 = 200
        self.pointer_2 = 0

        self.info_text_list = ["Accelerație:", "Forța de tracțiune:", "Timp până la viteza maximă:",
                               "Timp de frânare de la viteza maximă:",
                               "Distanța parcursă la frânare de la viteza maximă"]
        self.info_list = []

        while self.i_2 < 5:

            self.info = ctk.CTkLabel(
                self.frame,
                text=self.info_text_list[self.pointer_2],
                font=("Inter SemiBold", 12)
            )
            self.info.place(anchor='center', x=450, y=self.y_2)

            self.i_2 += 1
            self.y_2 += 40
            self.pointer_2 += 1

            self.info_list.append(self.info)

        self.plot_label = ctk.CTkLabel(
            self.frame,
            text="Afișează graficile pentru toate condițiile de drum",
            font=('Inter SemiBold', 10),
            text_color='green'
        )

        self.button_plot = ctk.CTkButton(
            self.root,
            text="Grafice",
            font=('Inter Bold', 20),
            command=self.show_plot
        )

    def execute_button_function(self) -> None:
        """
        Funcția care se execută atunci când este apăsat butonul 'Execută'.
        Creează un obiect Mașina pe baza introducerii utilizatorului și afișează informațiile relevante.
        """

        CreazatiMasina.masina_creata = Masina(self.lista_entry[0].get(), self.lista_entry[1].get(),
                                              float(self.lista_entry[2].get()),
                                              float(self.lista_entry[3].get()), float(self.lista_entry[4].get()))

        self.full_name_car.configure(text=f'{CreazatiMasina.masina_creata.nume_complet_masina}')

        if self.deceleratia.get() != "":

            self.plot_label.place(anchor='s', x=450, y=440)
            self.button_plot.place(anchor='s', x=450, y=475)

            self.error_label.configure(text='')

            match self.deceleratia.get():
                case "Uscat":
                    CreazatiMasina.deceleratia = "Uscat"
                case "Umed":
                    CreazatiMasina.deceleratia = "Umed"
                case "Îngheţat":
                    CreazatiMasina.deceleratia = "Zapada"

            self.info_list[0].configure(text=CreazatiMasina.masina_creata.get_string_acceleratia_masinii())
            self.info_list[1].configure(text=CreazatiMasina.masina_creata.get_string_forta_de_tractiune())
            self.info_list[2].configure(text=CreazatiMasina.masina_creata.get_string_timp_pana_la_viteza_maxima())
            self.info_list[3].configure(
                text=CreazatiMasina.masina_creata.get_string_timp_franare_viteza_maxima(CreazatiMasina.deceleratia))
            self.info_list[4].configure(
                text=CreazatiMasina.masina_creata.get_string_distanta_franare(CreazatiMasina.deceleratia))
        else:
            self.error_label.configure(text='Nu ai starea asfaltului')

    def show_plot(self) -> None:
        """
        Funcția pentru afișarea graficelor pe baza introducerii utilizatorului.
        """

        self.plot_root = ctk.CTk()
        self.plot_root.title('Grafice')
        self.plot_root.geometry('640x960')
        self.plot_root.resizable(False, False)

        self.frame1 = ctk.CTkFrame(
            self.plot_root,
            width=200, height=200
        )
        self.frame1.place(x=0, y=0)

        self.frame2 = ctk.CTkFrame(
            self.plot_root,
            width=200, height=200
        )
        self.frame2.place(x=0, y=480)

        # Obțineți timpurile de frânare pentru diferite condiții de drum
        timp_franare_uscat = CreazatiMasina.masina_creata.timp_franare_viteza_maxima('Uscat')
        timp_franare_umeda = CreazatiMasina.masina_creata.timp_franare_viteza_maxima('Umed')
        timp_franare_zapada = CreazatiMasina.masina_creata.timp_franare_viteza_maxima('Zapada')

        # Crearea unui nou obiect de figură și unui grafic pe această figură
        fig, ax = plt.subplots()

        # Datele pentru grafic
        ax.plot([0, timp_franare_uscat], [CreazatiMasina.masina_creata.viteza_maxima_km_h, 0],  marker='o', label='Uscat')  # Plotează pentru drum uscat
        ax.plot([0, timp_franare_umeda],[CreazatiMasina.masina_creata.viteza_maxima_km_h, 0],  marker='o', label='Umed')  # Plotează pentru drum umed
        ax.plot([0, timp_franare_zapada],[CreazatiMasina.masina_creata.viteza_maxima_km_h, 0],  marker='o', label='Zapada')  # Plotează pentru drum cu zăpadă
        ax.set_xlabel('Timp de frânare (secunde)')
        ax.set_ylabel('Viteza (km/h)')
        ax.set_title('Timp de frânare de la viteză maximă la 0')
        ax.legend()  # Adaugă o legendă pentru a indica condițiile de drum

        # Integrarea graficului în fereastra Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Obțineți timpurile de frânare pentru diferite condiții de drum
        timp_franare_uscat2 = CreazatiMasina.masina_creata.distanta_franare('Uscat')
        timp_franare_umeda2 = CreazatiMasina.masina_creata.distanta_franare('Umed')
        timp_franare_zapada2 = CreazatiMasina.masina_creata.distanta_franare('Zapada')

        # Crearea unui nou obiect de figură și unui grafic pe această figură
        fig2, ax2 = plt.subplots()

        # Datele pentru grafic
        ax2.plot([0, timp_franare_uscat2], [CreazatiMasina.masina_creata.viteza_maxima_km_h, 0], marker='o',
                 label='Uscat')  # Plotează pentru drum uscat
        ax2.plot([0, timp_franare_umeda2], [CreazatiMasina.masina_creata.viteza_maxima_km_h, 0], marker='o',
                 label='Umed')  # Plotează pentru drum umed
        ax2.plot([0, timp_franare_zapada2], [CreazatiMasina.masina_creata.viteza_maxima_km_h, 0], marker='o',
                 label='Zapada')  # Plotează pentru drum cu zăpadă
        ax2.set_xlabel('Distanta parcursa in frânare (metri)')
        ax2.set_ylabel('Viteza (km/h)')
        ax2.set_title('Distanta parcursa in frânare de la viteză maximă la 0')
        ax2.legend()  # Adaugă o legendă pentru a indica condițiile de drum

        # Integrarea graficului în fereastra Tkinter
        canvas2 = FigureCanvasTkAgg(fig2, master=self.frame2)
        canvas2.draw()
        canvas2.get_tk_widget().pack()

        self.plot_root.mainloop()