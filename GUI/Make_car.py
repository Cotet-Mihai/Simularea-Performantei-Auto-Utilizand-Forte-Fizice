import customtkinter as ctk
from Masina import Masina


class CreazatiMasina:

    marca = "Adauga"
    model = "Masina"
    acceleratia = None
    viteza = None
    masa = None
    deceleratia = None

    masina_creata = None

    def __init__(self, root):

        self.root = root
        self.widgets()

    def widgets(self):

        self.frame = ctk.CTkFrame(
            self.root,
            width=600, height=500
        )
        self.frame.place(x=0, y=0)

        self.title = ctk.CTkLabel(
            self.frame,
            text="Creaza Masina",
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
            values=["Uscat", "Umed", "Inghetat"]
        )
        self.deceleratia.place(anchor='n', x=150, y=125)

        self.i = 0
        self.y = 200
        self.pointer = 0

        self.parametrii_list = ["Marca", "Model", "Acceleratie(de la 0 la 100Km/H)", "Viteza maxima(Km/H)", "masa(Kg)"]
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
            text="Executa",
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

        self.info_text_list = ["Acceleratia:", "Forta de tractiune:", "Timpul pana la viteza maxima:",
                               "Timpul de franare de la viteza maxima:",
                               "Distanta parcurs in frana de la viteza maxima"]
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

    def execute_button_function(self):

        CreazatiMasina.masina_creata = Masina(self.lista_entry[0].get(), self.lista_entry[1].get(),
                                              float(self.lista_entry[2].get()),
                                              float(self.lista_entry[3].get()), float(self.lista_entry[4].get()))

        self.full_name_car.configure(text=f'{CreazatiMasina.masina_creata.nume_complet_masina}')

        if self.deceleratia.get() != "":
            self.error_label.configure(text='')

            match self.deceleratia.get():
                case "Uscat":
                    CreazatiMasina.deceleratia = "Uscat"
                case "Umed":
                    CreazatiMasina.deceleratia = "Umed"
                case "Inghetat":
                    CreazatiMasina.deceleratia = "Zapada"

            self.info_list[0].configure(text=CreazatiMasina.masina_creata.get_string_acceleratia_masinii())
            self.info_list[1].configure(text=CreazatiMasina.masina_creata.get_string_forta_de_tractiune())
            self.info_list[2].configure(text=CreazatiMasina.masina_creata.get_string_timp_pana_la_viteza_maxima())
            self.info_list[3].configure(
                text=CreazatiMasina.masina_creata.get_string_timp_franare_viteza_maxima(CreazatiMasina.deceleratia))
            self.info_list[4].configure(
                text=CreazatiMasina.masina_creata.get_string_distanta_franare(CreazatiMasina.deceleratia))
        else:
            self.error_label.configure(text='Nu ati starea asfaltului')
