import customtkinter as ctk
import database.colors as colors
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from car import Car


class BuildCar:
    """
    Class for creating a GUI for entering car parameters and displaying graphs.
    """

    brand: str = "Build your"
    model: str = "car"
    acceleration: float = None
    speed: float = None
    mass: float = None
    deceleration: float = None

    built_car = None

    def __init__(self, _root: ctk.CTk):
        self.root = _root

    # The function that creates all the widgets
    def gui(self) -> None:

        # Build car Frame
        self.build_car_frame = ctk.CTkFrame(
            self.root,
            width=300, height=400,
            fg_color=colors.main_background_color,
            corner_radius=0
        )
        self.build_car_frame.place(x=0, y=0)

        # Build car Title
        self.build_car_title = ctk.CTkLabel(
            self.build_car_frame,
            width=270, height=50,
            fg_color=colors.white,
            font=('Inter Black', 20),
            text='BUILD YOUR CAR',
            text_color=colors.main_background_color,
            corner_radius=30
        )
        self.build_car_title.place(x=15, y=15)

        # Entries

        # Control loop vars
        self.i = 0
        self.y = 80
        self.pointer = 0

        # List containing all placeholders for entries
        self.placeholder_list = ['Brand', 'Model', 'Acceleration (from 0 to 100Km/h)', 'Full speed (Km/h)', 'Mass(Kg)']
        # The list that will contain all the entries
        self.all_entries_list = []

        # The loop that will repeat 5 times
        while self.i < 5:
            # Template for entries
            self.entry = ctk.CTkEntry(
                self.build_car_frame,
                width=250, height=25,
                font=('Inter SemiBold', 13),
                placeholder_text=self.placeholder_list[self.pointer],
                justify='center',
                border_width=0,
                fg_color=colors.lightest_blue,
                corner_radius=5,
                placeholder_text_color=colors.white

            )
            self.entry.place(x=25, y=self.y)

            # After creation, add to list_all_entries_list
            self.all_entries_list.append(self.entry)

            # Increase the variables
            self.i += 1
            self.pointer += 1
            self.y += 40

        # Error Label

        self.error_label = ctk.CTkLabel(
            self.build_car_frame,
            text='',
            font=('Inter Bold', 10),
            text_color='red'
        )
        self.error_label.place(anchor='n', x=150, y=270)

        # Label Asphalit Condition
        self.asphalt_condition_label = ctk.CTkLabel(
            self.build_car_frame,
            font=('Inter Medium', 10),
            text='Asphalt condition'
        )
        self.asphalt_condition_label.place(anchor='n', x=150, y=290)

        # Segmented button for selecting the type of asphalt
        self.asphalt_condition_buttons = ctk.CTkSegmentedButton(
            self.build_car_frame,
            values=['Dry', 'Wet', 'Frozen'],
            width=150, height=25,
            text_color=colors.white,
            font=('Inter SemiBold', 13),
            corner_radius=5,
            border_width=0,
            fg_color=colors.lightest_blue,
            unselected_color=colors.lightest_blue,
            unselected_hover_color=colors.mid_dark_blue,
            selected_color=colors.second_background_color,
            selected_hover_color=colors.second_background_color

        )
        self.asphalt_condition_buttons.place(anchor='n', x=150, y=315)

        # Execute button
        self.execute_button = ctk.CTkButton(
            self.build_car_frame,
            width=270, height=25,
            fg_color=colors.white,
            font=('Inter Black', 15),
            text='EXECUTE',
            corner_radius=30,
            text_color=colors.main_background_color,
            hover_color=colors.lightest_blue,
            command=self.execute_button_function
        )
        self.execute_button.place(anchor='sw', x=15, y=385)

        # -------------------------------------------------------------------------------------------------------------

        # Show result Frame
        self.show_result_frame = ctk.CTkFrame(
            self.root,
            width=300, height=400,
            fg_color=colors.second_background_color,
            corner_radius=0
        )
        self.show_result_frame.place(x=300, y=0)

        # Result Title
        self.result_title = ctk.CTkLabel(
            self.show_result_frame,
            width=270, height=50,
            fg_color=colors.white,
            font=('Inter Black', 20),
            text='RESULT',
            text_color=colors.main_background_color,
            corner_radius=30
        )
        self.result_title.place(x=15, y=15)

        # Full name car
        self.full_name_car = ctk.CTkLabel(
            self.show_result_frame,
            text_color=colors.lightest_blue,
            text=f'{BuildCar.brand} {BuildCar.model}',
            font=('Inter Black', 16)
        )
        self.full_name_car.place(anchor='n', x=150, y=85)

        # Labels

        # Control loop vars / We overwrite the existing vars
        self.i = 0
        self.y = 120
        self.pointer = 0

        # List containing all text for labels
        self.text_label_list = ["Acceleration:", "Traction force:", "Time to top speed:",
                                "Braking time from maximum speed:", "Braking distance from maximum speed"]

        # The list that will contain all the result labels
        self.all_result_labels_list = []

        # The loop that will repeat 5 times
        while self.i < 5:
            # Template for labels
            self.label = ctk.CTkLabel(
                self.show_result_frame,
                text=self.text_label_list[self.pointer],
                font=('Inter SemiBold', 10)
            )
            self.label.place(anchor='n', x=150, y=self.y)

            # Raise y for the result label
            self.y += 23

            # Template for result labels
            self.result_label = ctk.CTkLabel(
                self.show_result_frame,
                text="...",
                font=('Inter SemiBold', 10),
                height=10
            )
            self.result_label.place(anchor='n', x=150, y=self.y)

            self.all_result_labels_list.append(self.result_label)

            # Increase the variables
            self.i += 1
            self.y += 15
            self.pointer += 1

        self.info_label = ctk.CTkLabel(
            self.show_result_frame,
            text_color=colors.lightest_blue,
            font=('Inter SemiBold', 10),
            text='Displays graphs for all standard road conditions'
        )
        self.info_label.place(anchor='n', x=150, y=335)

        # Execute button
        self.show_graph_button = ctk.CTkButton(
            self.show_result_frame,
            width=270, height=25,
            fg_color=colors.white,
            font=('Inter Black', 15),
            text='Graphics for all types of asphalt',
            corner_radius=30,
            text_color=colors.main_background_color,
            hover_color=colors.lightest_blue,
            command=self.show_graph_button_function
        )
        self.show_graph_button.place(anchor='sw', x=15, y=385)

    #
    def execute_button_function(self) -> None:
        """
        The Execute button function will perform the necessary calculations and display the results in the Show
        Result frame
        """
        print('Execute button was pressed.')

        print(self.asphalt_condition_buttons.get())

        # Build car
        BuildCar.built_car = Car(self.all_entries_list[0].get(), self.all_entries_list[1].get(),
                                 float(self.all_entries_list[2].get()), float(self.all_entries_list[3].get()),
                                 float(self.all_entries_list[4].get()))

        # Change the full_name_car text to the full name of the built car
        self.full_name_car.configure(text=f'{BuildCar.built_car.full_name}')

        # Verify if asphalt_condition_buttons is not empty
        if self.asphalt_condition_buttons.get() != '':
            # Keep error label empty
            self.error_label.configure(text='')

            # Sets the deceleration according to the value selected in asphalt_condition
            match self.asphalt_condition_buttons.get():
                case "Dry":
                    BuildCar.deceleration = "Dry"
                case "Wet":
                    BuildCar.deceleration = "Wet"
                case "Frozen":
                    BuildCar.deceleration = "Frozen"

            # Change the results displayed in show_result_frame
            self.all_result_labels_list[0].configure(text=BuildCar.built_car.get_string_car_acceleration())
            self.all_result_labels_list[1].configure(text=BuildCar.built_car.get_string_traction_force())
            self.all_result_labels_list[2].configure(text=BuildCar.built_car.get_string_time_to_max_speed())
            self.all_result_labels_list[3].configure(
                text=BuildCar.built_car.get_string_braking_time_max_speed(BuildCar.deceleration))
            self.all_result_labels_list[4].configure(
                text=BuildCar.built_car.get_string_braking_distance(BuildCar.deceleration))
        else:
            # If asphalt_condition_buttons is empty, show error label
            self.error_label.configure(text="You don't have the condition of the asphalt")

    def show_graph_button_function(self) -> None:
        """
        Displays a plot with information about the car in any condition of the asphalt
        """
        print('Show Graph button was pressed.')  # Print a message indicating that the button was pressed.

        # Create a new CustomTkinter root window for the plots
        self.plot_root = ctk.CTk()
        self.plot_root.title('Plots')
        self.plot_root.geometry('640x960')
        self.plot_root.resizable(False, False)

        # Create two frames within the root window to hold the plots
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

        # Get braking times for different road conditions
        braking_time_dry = BuildCar.built_car.braking_time_max_speed('Dry')
        braking_time_wet = BuildCar.built_car.braking_time_max_speed('Wet')
        braking_time_frozen = BuildCar.built_car.braking_time_max_speed('Frozen')

        # Create a new figure object and a plot on this figure for braking times
        fig, ax = plt.subplots()

        # Data for the plot
        ax.plot([0, braking_time_dry], [BuildCar.built_car.max_speed_km_h, 0], marker='o',
                label='Dry')  # Plot for dry road
        ax.plot([0, braking_time_wet], [BuildCar.built_car.max_speed_km_h, 0], marker='o',
                label='Wet')  # Plot for wet road
        ax.plot([0, braking_time_frozen], [BuildCar.built_car.max_speed_km_h, 0], marker='o',
                label='Frozen')  # Plot for frozen road
        ax.set_xlabel('Braking Time (seconds)')
        ax.set_ylabel('Speed (km/h)')
        ax.set_title('Braking Time from Maximum Speed to 0')
        ax.legend()  # Add a legend to indicate road conditions

        # Embed the plot into the CustomTkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Get braking distances for different road conditions
        braking_distance_dry = BuildCar.built_car.braking_distance('Dry')
        braking_distance_wet = BuildCar.built_car.braking_distance('Wet')
        braking_distance_frozen = BuildCar.built_car.braking_distance('Frozen')

        # Create a new figure object and a plot on this figure for braking distances
        fig2, ax2 = plt.subplots()

        # Data for the plot
        ax2.plot([0, braking_distance_dry], [BuildCar.built_car.max_speed_km_h, 0], marker='o',
                 label='Dry')  # Plot for dry road
        ax2.plot([0, braking_distance_wet], [BuildCar.built_car.max_speed_km_h, 0], marker='o',
                 label='Wet')  # Plot for wet road
        ax2.plot([0, braking_distance_frozen], [BuildCar.built_car.max_speed_km_h, 0], marker='o',
                 label='Frozen')  # Plot for frozen road
        ax2.set_xlabel('Braking Distance (meters)')
        ax2.set_ylabel('Speed (km/h)')
        ax2.set_title('Braking Distance from Maximum Speed to 0')
        ax2.legend()  # Add a legend to indicate road conditions

        # Embed the plot into the CustomTkinter window
        canvas2 = FigureCanvasTkAgg(fig2, master=self.frame2)
        canvas2.draw()
        canvas2.get_tk_widget().pack()

        # Start the CustomTkinter event loop to display the plots
        self.plot_root.mainloop()


if __name__ == '__main__':

    root = ctk.CTk()
    root.geometry('600x400')
    menu = BuildCar(root)
    menu.gui()
    root.mainloop()
