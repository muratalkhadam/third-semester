import tkinter
import customtkinter
from DenseIndex import *


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Algo | Lab 3")
        self.geometry(f"{300}x{500}")
        self.resizable(False, False)

        self.action = tkinter.StringVar(value="")

        self.pack_widgets()

        self.di = DenseIndex("data.txt", "index.txt")
        self.di.build_index()

    def pack_widgets(self):
        self.key_value_frame = customtkinter.CTkFrame(self, corner_radius=50)
        self.key_value_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.key_label = customtkinter.CTkLabel(self.key_value_frame, text="Your KEY")
        self.key_label.grid(row=0, column=0, padx=40)

        self.value_label = customtkinter.CTkLabel(self.key_value_frame, text="Your VALUE")
        self.value_label.grid(row=0, column=1, padx=40)

        self.key_value_entry_frame = customtkinter.CTkFrame(self, corner_radius=50)
        self.key_value_entry_frame.grid(row=1, column=0, columnspan=2, sticky="ew")

        self.key_entry = customtkinter.CTkEntry(self.key_value_entry_frame, placeholder_text="input your key here...")
        self.key_entry.grid(row=1, column=0)

        self.value_entry = customtkinter.CTkEntry(self.key_value_entry_frame, placeholder_text="input your value here...")
        self.value_entry.grid(row=1, column=1)

        self.action_frame = customtkinter.CTkFrame(self)
        self.action_frame.grid(row=2, column=0, padx=10, pady=5, columnspan=2, sticky="nsew")

        self.radio_insert = customtkinter.CTkRadioButton(self.action_frame, variable=self.action,
                                                         value="insert", text="insert")
        self.radio_insert.grid(row=0, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.radio_delete = customtkinter.CTkRadioButton(self.action_frame, variable=self.action,
                                                         value="delete", text="delete")
        self.radio_delete.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.radio_update = customtkinter.CTkRadioButton(self.action_frame, variable=self.action,
                                                         value="update", text="update")
        self.radio_update.grid(row=2, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.radio_find = customtkinter.CTkRadioButton(self.action_frame, variable=self.action,
                                                       value="find", text="find")
        self.radio_find.grid(row=3, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        self.execute_button = customtkinter.CTkButton(self, text="Execute", command=self.execute)
        self.execute_button.grid(row=3, column=0, columnspan=2, sticky="we")

        self.info_area = customtkinter.CTkTextbox(self)
        self.info_area.insert("0.0", "Loading...")
        self.info_area.configure(state="disabled")
        self.info_area.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="snwe")

    @staticmethod
    def clear_area(area):
        area.configure(state="normal")
        area.delete("1.0", customtkinter.END)
        area.configure(state="disabled")

    def insert_area(self, area, to_insert):
        self.clear_area(area)
        area.configure(state="normal")

        area.insert("0.0", to_insert)
        area.configure(state="disabled")

    def execute(self):
        action_value = self.action.get()
        self.clear_area(self.info_area)
        if action_value:
            # self.insert_area(self.info_area, "rabotaet")
            if action_value == "insert":
                key_to_insert = self.key_entry.get()
                value_to_insert = self.value_entry.get()

                record_to_insert = f"{key_to_insert}, {value_to_insert}"
                self.di.insert(record_to_insert)

                self.insert_area(self.info_area,
                                  f"Record with key {key_to_insert} was inserted with value {value_to_insert}")
            elif action_value == "delete":
                key_to_delete = int(self.key_entry.get())
                self.di.delete(key_to_delete)

                self.insert_area(self.info_area,
                                  f"Founded record with key {key_to_delete} was deleted")
            elif action_value == "update":
                key_to_update = int(self.key_entry.get())
                value_to_update = self.value_entry.get()

                self.di.update(f"{key_to_update}, {value_to_update}")

                self.insert_area(self.info_area,
                                  f"The value with {key_to_update} was updated by new value {value_to_update}")

            elif action_value == "find":
                self.insert_area(self.info_area, f"The value was founded with ... key...")
                pass
        else:
            self.insert_area(self.info_area, "Pick the option firstly!")

    def insert_in_index_file(self):
        key_to_insert = self.key_entry.get()
        value_to_insert = self.value_entry.get()

        record_to_insert = f"{key_to_insert}, {value_to_insert}"
        self.di.insert(record_to_insert)


if __name__ == "__main__":
    app = App()
    app.mainloop()
