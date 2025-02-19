import customtkinter as ctk
from PIL import Image
import HardwareDevelopment.main as HDT
import AIDevelopment.ai as AID

class Getraenk:
    def __init__(self, name, image_path):
        self.name = name
        self.image_path = image_path

    def __str__(self):
        return self.name

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.window_width = 1800 
        self.window_height = 900
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.window_width) // 2
        y = (screen_height - self.window_height) // 2
        self.geometry(f"{self.window_width}x{self.window_height}+{x}+{y}")
        self.title("SIP GUI")
        self.selected_drinks = set()
        self.buttons = []
        self.create_initial_view()

    def create_initial_view(self):
        for widget in self.winfo_children():
            widget.destroy()
        header_label = ctk.CTkLabel(self, text="Willkommen bei Sip Tech One!", font=("Arial", 34, "bold"))
        header_label.pack(pady=(120, 30))
        create_button = ctk.CTkButton(
            self,
            text="Getränk erstellen",
            fg_color="orchid",
            text_color="white",
            corner_radius=20,
            font=("Arial", 24, "bold"),
            width=300,
            height=80,
            cursor="hand2",
            command=self.show_drink_selection,
            hover_color="orchid"
        )
        create_button.pack(pady=30)

    def show_drink_selection(self):
        self.selected_drinks.clear()
        self.buttons.clear()
        for widget in self.winfo_children():
            widget.destroy()
        header_frame = ctk.CTkFrame(self, height=120, fg_color="#F0E6F6")
        header_frame.pack(fill="x", pady=(20, 30), padx=30)
        back_button = ctk.CTkButton(
            header_frame,
            text="Zurück",
            fg_color="orchid",
            text_color="white",
            corner_radius=20,
            font=("Arial", 20, "bold"),
            width=180,
            height=60,
            cursor="hand2",
            command=self.go_back,
            hover_color="orchid"
        )
        back_button.place(relx=0.02, rely=0.5, anchor="w")
        header_label = ctk.CTkLabel(
            header_frame,
            text="Wähle ein Getränk",
            font=("Arial", 38, "bold"),
            text_color="black"
        )
        header_label.place(relx=0.5, rely=0.5, anchor="center")
        grid_frame = ctk.CTkFrame(self, fg_color="#E8DFF5")
        grid_frame.pack(pady=30, padx=30)
        getraenke = [
            Getraenk("Fanta", "Interface/drinks/apfel.png"),
            Getraenk("Cola", "Interface/drinks/wasser.png")
        ]
        columns = 2
        for index, getraenk in enumerate(getraenke):
            row = index // columns
            col = index % columns
            pil_image = Image.open(getraenk.image_path)
            drink_image = ctk.CTkImage(light_image=pil_image, size=(280, 280))
            drink_button = ctk.CTkButton(
                grid_frame,
                text="",
                image=drink_image,
                fg_color="#FFFFFF",
                corner_radius=20,
                width=280,
                height=280,
                cursor="hand2",
                hover_color="#FFFFFF"
            )
            drink_button.selected = False
            drink_button.configure(command=lambda b=drink_button, d=getraenk: self.toggle_drink(b, d))
            drink_button.grid(row=row, column=col, padx=30, pady=30)
            self.buttons.append(drink_button)
        for col in range(columns):
            grid_frame.grid_columnconfigure(col, weight=1)
        mix_button = ctk.CTkButton(
            self,
            text="Mischen",
            fg_color="orchid",
            text_color="white",
            corner_radius=20,
            font=("Arial", 24, "bold"),
            width=300,
            height=80,
            cursor="hand2",
            command=self.mix_drinks,
            hover_color="orchid"
        )
        mix_button.pack(pady=30)
        self.buttons.append(mix_button)

    def go_back(self):
        self.selected_drinks.clear()
        self.create_initial_view()

    def toggle_drink(self, button, getraenk):
        if not button.selected:
            button.configure(fg_color="#CE93D8", hover_color="#CE93D8")
            button.selected = True
            self.selected_drinks.add(getraenk.name)
        else:
            button.configure(fg_color="#FFFFFF", hover_color="#FFFFFF")
            button.selected = False
            self.selected_drinks.discard(getraenk.name)

    def mix_drinks(self):
        if not self.selected_drinks:
            return
        result = " + ".join(self.selected_drinks) if len(self.selected_drinks) > 1 else list(self.selected_drinks)[0]
        print(result)
        for btn in self.buttons:
            btn.configure(state="disabled")
        self.run_external_process(result)

    def run_external_process(self, result):
        try:
            value = AID.detect_blue()
            if value == 1:
                print('Yeah')
                HDT.run(result)
        except Exception as e:
            print(f"Fehler beim Ausführen von HDT.run(): {e}")
        self.show_success_screen()

    def show_success_screen(self):
        for widget in self.winfo_children():
            widget.destroy()
        success_label = ctk.CTkLabel(
            self,
            text="Mischung erfolgreich!",
            font=("Arial", 38, "bold"),
            text_color="black"
        )
        success_label.pack(pady=(120, 30))
        success_button = ctk.CTkButton(
            self,
            text="Erfolg",
            fg_color="orchid",
            text_color="white",
            corner_radius=20,
            font=("Arial", 24, "bold"),
            width=300,
            height=80,
            cursor="hand2",
            command=self.create_initial_view,
            hover_color="orchid"
        )
        success_button.pack(pady=30)

if __name__ == "__main__":
    app = App()
    app.mainloop()