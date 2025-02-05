import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
import HardwareDevelopment.main as HDT
import AIDevelopment.ai as AID

class Beverage:
    def __init__(self, name, info_text, ingredients, image_path=None):
        self.name = name
        self.info_text = info_text
        self.ingredients = ingredients
        self.image_path = image_path
        self.checked = False
        self.image = self.load_image(image_path)

    def load_image(self, image_path):
        try:
            img = Image.open(image_path)
            img = img.resize((250, 250))
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Bild konnte nicht geladen werden: {e}")
            return None

    def __str__(self):
        ingredients_str = "\n".join([f"{k}: {v}" for k, v in self.ingredients.items()])
        return f"{self.name}\n{self.info_text}\nIngredients:\n{ingredients_str}"

def bind_selection(widget, beverage, frame):
    try:
        if widget.cget("text") == "i":
            return
    except Exception:
        pass
    widget.bind("<Button-1>", lambda event, b=beverage, frame=frame: grid_element_clicked(b, frame))
    for child in widget.winfo_children():
        bind_selection(child, beverage, frame)

def on_button_click():
    global error_label
    global beverages
    error_label = None
    for widget in root.winfo_children():
        widget.destroy()
    beverages_label = ctk.CTkLabel(root, text="Getränke", font=("Arial", 40))
    beverages_label.place(relx=0.5, rely=0.02, anchor="n")
    frame = ctk.CTkFrame(root)
    frame.place(relx=0.5, rely=0.12, anchor="n")
    beverage1 = Beverage("Cola / 50ml", "A classic cola drink", {
        "Kalorien": "42 kcal",
        "Energie": "180 kJ",
        "Fett": "0 g",
        "davon gesättigte Fettsäuren": "0 g",
        "Kohlenhydrate": "10,6 g",
        "davon Zucker": "10,6 g",
        "Eiweiß": "0 g",
        "Salz": "0 g",
    }, image_path="Interface/drinks/cola.png")
    beverage2 = Beverage("Fanta / 50ml", "A tangy orange soda", {
        "Kalorien": "42 kcal",
        "Energie": "178 kJ",
        "Fett": "0 g",
        "davon gesättigte Fettsäuren": "0 g",
        "Kohlenhydrate": "10,3 g",
        "davon Zucker": "10,3 g",
        "Eiweiß": "0 g",
        "Natrium": "0 g",
    }, image_path="Interface/drinks/fanta.png")
    beverages = [beverage1, beverage2]
    for i, beverage in enumerate(beverages):
        object_frame = ctk.CTkFrame(frame)
        object_frame.grid(row=0, column=i, padx=20, pady=20, sticky="nsew")
        object_frame.default_color = object_frame.cget("fg_color")
        if beverage.image:
            image_label = ctk.CTkLabel(object_frame, image=beverage.image, text="")
        else:
            image_label = ctk.CTkLabel(object_frame, text="Bild konnte nicht geladen werden")
        image_label.image = beverage.image
        image_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        name_label = ctk.CTkLabel(object_frame, text=beverage.name, font=("Arial", 18))
        name_label.grid(row=1, column=0, padx=10, pady=10)
        button_frame = ctk.CTkFrame(object_frame, fg_color="transparent")
        button_frame.grid(row=2, column=0, pady=10)
        info_button = ctk.CTkButton(button_frame, text="i", font=("Arial", 18, "bold"),
                            width=55, height=55,
                            corner_radius=27,
                            fg_color="#6A0DAD", hover_color="#620A80",
                            command=lambda b=beverage: info_button_clicked(b))

        info_button.grid(row=0, column=0)
        bind_selection(object_frame, beverage, object_frame)

    back_button = ctk.CTkButton(root, text="Zurück", font=("Arial", 18), width=180, height=60,
                                command=back_to_initial, fg_color="#6A0DAD", hover_color="#620A80")
    back_button.place(relx=0.05, rely=0.05, anchor="nw")

    mix_button = ctk.CTkButton(root, text="Mischen", font=("Arial", 18), width=180, height=60,
                               command=lambda: mix_button_clicked(beverages), fg_color="#6A0DAD", hover_color="#620A80")
    mix_button.place(relx=0.5, rely=0.92, anchor="center")

def grid_element_clicked(beverage, object_frame):
    HIGHLIGHT_COLOR = "#3e3e3e"
    DEFAULT_COLOR = object_frame.default_color
    beverage.checked = not beverage.checked
    if beverage.checked:
        object_frame.configure(fg_color=HIGHLIGHT_COLOR)
    else: 
        object_frame.configure(fg_color=DEFAULT_COLOR)
    print(f"{beverage.name} ausgewählt: {beverage.checked}")

def info_button_clicked(beverage):
    info_window = ctk.CTkToplevel(root)
    info_window.geometry("500x500")
    info_window.title(f"Info - Cola")
    info_window.resizable(False, False)
    info_window.grab_set()

    cola_label = ctk.CTkLabel(info_window, text="Cola", font=("Arial", 22, "bold"))
    cola_label.pack(padx=20, pady=10)

    table_frame = ctk.CTkFrame(info_window)
    table_frame.pack(pady=10, padx=20, fill="both", expand=True)

    treeview = ttk.Treeview(table_frame, columns=("Inhaltsstoff", "Menge (pro 100ml)"), show="headings")
    treeview.heading("Inhaltsstoff", text="Inhaltsstoff")
    treeview.heading("Menge (pro 100ml)", text="Menge (pro 100ml)")

    for i, (ingredient, value) in enumerate(beverage.ingredients.items()):
        treeview.insert("", "end", values=(ingredient, value))
    
    treeview.tag_configure("font", font=("Arial", 18))
    treeview.pack(fill="both", expand=True)

    close_button = ctk.CTkButton(info_window, text="Schließen", font=("Arial", 16),
                                 command=info_window.destroy, fg_color="#6A0DAD",
                                 hover_color="#620A80", width=180, height=50, corner_radius=10)
    close_button.pack(pady=10)

def back_to_initial():
    for widget in root.winfo_children():
        widget.destroy()
        
    content_text = ctk.CTkLabel(root, text="Willkommen zu Sip Tech One", font=("Arial", 30))
    content_text.place(relx=0.5, rely=0.3, anchor="center")

    button = ctk.CTkButton(root, text="Getränk erstellen", font=("Arial", 40), width=350, height=80,
                           fg_color="#6A0DAD", hover_color="#620A80", command=on_button_click)
    button.place(relx=0.5, rely=0.5, anchor="center")

def mix_button_clicked(beverages):
    global error_label
    selected_beverages = [beverage for beverage in beverages if beverage.checked]
    selected_count = len(selected_beverages)
    if error_label:
        error_label.destroy()
    if selected_count == 0:
        error_label = ctk.CTkLabel(root, text="Es muss mindestens 1 Getränk ausgewählt werden!",
                                   font=("Arial", 18), text_color="#FF0000",  
                                   fg_color="#555555", corner_radius=10)
        error_label.place(relx=0.5, rely=0.82, anchor="n")
    elif selected_count > 2:
        error_label = ctk.CTkLabel(root, text="Es können nicht mehr als 2 Getränke ausgewählt werden!",
                                   font=("Arial", 18), text_color="#FF0000",  
                                   fg_color="#555555", corner_radius=10)
        error_label.place(relx=0.5, rely=0.98, anchor="n")

    else:
        selected_names = [beverage.name.split(" /")[0] for beverage in selected_beverages]
        if "Cola" in selected_names and "Fanta" in selected_names:
            selected_names = ["Spezi"]
        print(f"Ausgewählte Getränke: {selected_names}")
        
        result_tuple = tuple(selected_names)
        print(f"Resultat-Tuple: {result_tuple}")
        
        value = AID.detect_blue()
        if(value == 1):
            print('Yeah')
            HDT.run(str(result_tuple[0]))
            
        print(result_tuple)
        
        print(f"Rückgabewert: {result.returncode}")
        print(f"Standardoutput: {result.stdout}")
        print(f"Fehlerausgabe: {result.stderr}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.geometry("1024x600")
root.resizable(False, False)
root.title("Sip Tech One")
back_to_initial()
root.mainloop()
