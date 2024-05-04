import customtkinter as ctk
import database.colors as colors
from Pages.build_car import BuildCar


# Build Menu
class Menu:
    # Constructor
    def __init__(self, _root):
        # Root
        self.root = _root

    # The function that creates all the widgets
    def gui(self) -> None:

        # Main Frame Menu
        self.main_frame_menu = ctk.CTkFrame(
            self.root,
            width=600, height=400,
            fg_color=colors.main_background_color
        )
        self.main_frame_menu.place(x=0, y=0)

        # Title
        self.title = ctk.CTkLabel(
            self.main_frame_menu,
            width=570, height=100,
            fg_color=colors.lightest_blue,
            font=('Inter Bold', 24),
            text='Simulation of Car Performance\nUsing Physical Forces',
            corner_radius=30
        )
        self.title.place(x=15, y=15)

        # Create your own car Button
        self.first_button = ctk.CTkButton(
            self.main_frame_menu,
            width=270, height=200,
            fg_color=colors.white,
            font=('Inter Black', 24),
            text_color=colors.main_background_color,
            hover_color=colors.lightest_blue,
            text='CREATE YOUR\nOWN CAR',
            corner_radius=15,
            command=self.first_button_function
        )
        self.first_button.place(anchor='sw', x=15, y=385)

        # Choose a preset car Button
        self.second_button = ctk.CTkButton(
            self.main_frame_menu,
            width=270, height=200,
            fg_color=colors.white,
            font=('Inter Black', 24),
            text_color=colors.main_background_color,
            hover_color=colors.lightest_blue,
            text='CHOOSE A\nPRESET CAR',
            corner_radius=15,
            command=self.second_button_function
        )
        self.second_button.place(anchor='se', x=585, y=385)

    # Create your own car function
    def first_button_function(self):
        BuildCar(self.root).gui()

    # Choose a preset car function
    def second_button_function(self):
        print('Second button was pressed.')


if __name__ == '__main__':

    root = ctk.CTk()
    root.geometry('600x400')
    menu = Menu(root)
    menu.gui()
    root.mainloop()
