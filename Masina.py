class Masina:
    deceleratie_tipica_uscat = -7.5  # m/s^2
    deceleratie_tipica_umed = -3  # m/s^2
    deceleratie_tipica_zapada = -1.5  # m/s^2

    def __init__(self, marca, model, acceleratia_km_h_0_100, viteza_maxima_km_h, masa=0):

        def convert_km_h_to_m_s2(valoare):
            """
            :param valoare: valoarea care trebuie convertita
            :return: m/s^2
            """
            return valoare * 1000 / 3600

        # Variabile unice pentru fiecare masina
        self.marca = marca
        self.model = model
        self.nume_complet_masina = f"{self.marca} {self.model}"
        self.viteza_maxima_km_h = viteza_maxima_km_h
        self.masa = masa
        self.acceleratia_km_h_0_100 = acceleratia_km_h_0_100

        # Variabile convertite
        self.viteza_maxima_m_s2 = convert_km_h_to_m_s2(viteza_maxima_km_h)
        self.viteza_100 = convert_km_h_to_m_s2(100)

    def acceleratia_masinii(self) -> float:
        """
        :return: (viteza_finala_m_s - viteza_initiala) / timpul
        """
        return (self.viteza_100 - 0) / self.acceleratia_km_h_0_100

    def timp_pana_la_viteza_maxima(self):
        """
        :return: viteza_maxima_m_s / a
        """
        return self.viteza_maxima_m_s2 / self.acceleratia_masinii()

    def timp_franare_viteza_maxima(self, tipul_deceleratiei):

        match tipul_deceleratiei:

            case "Uscat":
                return self.viteza_maxima_m_s2 / abs(Masina.deceleratie_tipica_uscat)

            case "Umed":
                return self.viteza_maxima_m_s2 / abs(Masina.deceleratie_tipica_umed)

            case "Zapada":
                return self.viteza_maxima_m_s2 / abs(Masina.deceleratie_tipica_zapada)

            case _:
                print(Exception("tipul_deceleratiei nu este cunoscut. Incearca 'Uscat'/'Umed'/'Zapada'"))

    def forta_de_tractiune(self):
        return self.masa * self.acceleratia_masinii()

    def distanta_franare(self, tipul_deceleratiei):

        deceleratie = 0
        match tipul_deceleratiei:

            case "Uscat":
                deceleratie = Masina.deceleratie_tipica_uscat

            case "Umed":
                deceleratie = Masina.deceleratie_tipica_umed

            case "Zapada":
                deceleratie = Masina.deceleratie_tipica_zapada

            case _:
                print(Exception("tipul_deceleratiei nu este cunoscut. Incearca 'Uscat'/'Umed'/'Zapada'"))

        return (self.viteza_maxima_m_s2 * self.timp_franare_viteza_maxima(tipul_deceleratiei)
                + 0.5 * deceleratie * (self.timp_franare_viteza_maxima(tipul_deceleratiei)
                                       * self.timp_franare_viteza_maxima(tipul_deceleratiei)))

    # Functii get_string
    def get_string_acceleratia_masinii(self) -> str:
        return f"Acceleratia:\n {self.acceleratia_masinii():.2f} m/s^2"

    def get_string_timp_pana_la_viteza_maxima(self) -> str:
        return f"Timpul pana la {self.viteza_maxima_km_h} Km/h:\n {self.timp_pana_la_viteza_maxima():.2f} secunde."

    def get_string_timp_franare_viteza_maxima(self, tipul_deceleratiei) -> str:
        return (f"Timpul de franare de la {self.viteza_maxima_km_h}km/h:\n"
                f" {self.timp_franare_viteza_maxima(tipul_deceleratiei):.2f} secunde. ")

    def get_string_forta_de_tractiune(self) -> str:
        return f"Forta de tractiune:\n {self.forta_de_tractiune():.2f} N"

    def get_string_distanta_franare(self, tipul_decelerarii) -> str:
        return (f"Distanta parcursa in frana de la {self.viteza_maxima_km_h} km/h:\n"
                f" {self.distanta_franare(tipul_decelerarii):.2f} m")
