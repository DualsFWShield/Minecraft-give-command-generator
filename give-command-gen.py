import tkinter as tk
from tkinter import ttk
import json

class MinecraftCommandGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Command Generator")

        # Charger les JSON
        with open(r'C:\Users\Toyger\Downloads\enchantments.json') as f:
            enchantments_data = json.load(f)
        with open(r'C:\Users\Toyger\Downloads\items-output.json') as f:
            items_data = json.load(f)

        # Récupérer les listes des enchantements et des objets
        enchantment_names = [enchantment['name'] for enchantment in enchantments_data['enchantments']]
        item_names = [item['name'] for item in items_data['items']]

        # Création des onglets
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        self.give_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.give_frame, text="Give")

        # Création des champs pour la commande give
        self.target_label = ttk.Label(self.give_frame, text="Cible :")
        self.target_label.pack()
        self.target_entry = ttk.Entry(self.give_frame)
        self.target_entry.pack()

        self.item_label = ttk.Label(self.give_frame, text="Objet :")
        self.item_label.pack()
        self.item_selector = ttk.Combobox(self.give_frame)
        self.item_selector.pack()
        self.item_selector['values'] = tuple(item_names)

        self.count_label = ttk.Label(self.give_frame, text="Quantité :")
        self.count_label.pack()
        self.count_entry = ttk.Entry(self.give_frame)
        self.count_entry.pack()

        self.enchantment_label = ttk.Label(self.give_frame, text="Enchantement(s) :")
        self.enchantment_label.pack()
        self.enchantment_selector = ttk.Combobox(self.give_frame)
        self.enchantment_selector.pack()
        self.enchantment_selector['values'] = tuple(enchantment_names)

        self.enchantment_level_label = ttk.Label(self.give_frame, text="Niveau de l'enchantement :")
        self.enchantment_level_label.pack()
        self.enchantment_level_entry = ttk.Entry(self.give_frame)
        self.enchantment_level_entry.pack()

        self.add_enchantment_button = ttk.Button(self.give_frame, text="Ajouter un enchantement", command=self.add_enchantment)
        self.add_enchantment_button.pack()

        self.enchantments_listbox = tk.Listbox(self.give_frame)
        self.enchantments_listbox.pack()

        self.generate_button = ttk.Button(self.give_frame, text="Générer la commande", command=self.generate_give_command)
        self.generate_button.pack()

        self.enchantments = []

    def add_enchantment(self):
        enchantment = self.enchantment_selector.get()
        level = self.enchantment_level_entry.get()
        if enchantment and level:
            self.enchantments.append((enchantment, level))
            self.enchantments_listbox.insert(tk.END, f"{enchantment} (niveau {level})")
            self.enchantment_selector.set("")
            self.enchantment_level_entry.delete(0, tk.END)

    def generate_give_command(self):
        target = self.target_entry.get()
        item = self.item_selector.get()
        count = self.count_entry.get()

        command = f"/give {target} {item}"
        if self.enchantments:
            enchantments_str = ",".join(f"{enchantment.lower().replace(' ', '_')}:{int(level)}" for enchantment, level in self.enchantments)
            command += f"[enchantments={{levels:{{{enchantments_str}}}}}]"
        command += f" {count}"

        print(command)

if __name__ == "__main__":
    root = tk.Tk()
    app = MinecraftCommandGenerator(root)
    root.mainloop()
