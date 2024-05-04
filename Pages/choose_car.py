import customtkinter as ctk
import database.colors as colors

class ChooseCar:
    def __init__(self,  _root: ctk.CTk):
        self.root = root

        self.gui()

    def gui(self) -> None:
        # Choose car Frame
        self.choose_car_frame = ctk.CTkFrame(
            self.root,
            width=300, height=400,
            fg_color=colors.main_background_color,
            corner_radius=0
        )
        self.choose_car_frame.place(x=0, y=0)

        # Build car Title
        self.choose_car_title = ctk.CTkLabel(
            self.choose_car_frame,
            width=270, height=50,
            fg_color=colors.white,
            font=('Inter Black', 20),
            text='CHOOSE A CAR',
            text_color=colors.main_background_color,
            corner_radius=30
        )
        self.choose_car_title.place(x=15, y=15)

        self.choose_car_scrollable_frame = ctk.CTkScrollableFrame(
            self.choose_car_frame,
            width=240,
            fg_color=colors.second_background_color,
            corner_radius=15
        )
        self.choose_car_scrollable_frame.place(anchor='n', x=150, y=80)

        # -------------------------------------------------------------------------------------------------------------

        # Show result Frame
        self.show_result_frame = ctk.CTkFrame(
            self.root,
            width=300, height=400,
            fg_color=colors.second_background_color,
            corner_radius=0
        )
        self.show_result_frame.place(x=300, y=0)



if __name__ == '__main__':

    root = ctk.CTk()
    root.geometry('600x400')
    menu = ChooseCar(root)
    menu.gui()
    root.mainloop()
