import tkinter
from tkinter import messagebox

from make_plots import Plot
from add_dish import AddDish
from find_redact_dish import SearchDish

class AppWindow:
    def __init__(self, master):
        self.master = master
        self.dish_manager = AddDish()
        self.plot = Plot()
        
        master.title("Рацион медведя")
        master.geometry("900x900")

        self.label = tkinter.Label(master, text="Добро пожаловать!")
        self.label.pack()

        self.add_button = tkinter.Button(master, text="Добавить блюдо", command=self.open_add_dish_window)
        self.add_button.pack()

        self.search_button = tkinter.Button(master, text="Поиск блюда", command=self.open_search_window)
        self.search_button.pack()
        
        self.graph_button = tkinter.Button(master, text="Показать график", command=self.open_search_window)
        self.graph_button.pack()

    def open_add_dish_window(self):
        self.add_dish_window = tkinter.Toplevel(self.master)
        self.add_dish_window.title("Добавить блюдо")
        self.add_dish_window.geometry("300x300")

        self.label_name = tkinter.Label(self.add_dish_window, text="Название блюда")
        self.label_name.pack()
        self.entry_name = tkinter.Entry(self.add_dish_window)
        self.entry_name.pack()

        self.label_calories = tkinter.Label(self.add_dish_window, text="Калории")
        self.label_calories.pack()
        self.entry_calories = tkinter.Entry(self.add_dish_window)
        self.entry_calories.pack()

        self.label_proteins = tkinter.Label(self.add_dish_window, text="Протеины")
        self.label_proteins.pack()
        self.entry_proteins = tkinter.Entry(self.add_dish_window)
        self.entry_proteins.pack()

        self.label_fats = tkinter.Label(self.add_dish_window, text="Жиры")
        self.label_fats.pack()
        self.entry_fats = tkinter.Entry(self.add_dish_window)
        self.entry_fats.pack()

        self.label_carbs = tkinter.Label(self.add_dish_window, text="Углеводы")
        self.label_carbs.pack()
        self.entry_carbs = tkinter.Entry(self.add_dish_window)
        self.entry_carbs.pack()

        self.button_add = tkinter.Button(self.add_dish_window, text="Добавьте блюдо", command=self.add_dish)
        self.button_add.pack()

    def add_dish(self):
        name = self.entry_name.get()
        calories = self.entry_calories.get()
        proteins = self.entry_proteins.get()
        fats = self.entry_fats.get()
        carbs = self.entry_carbs.get()

        if name and calories and proteins and fats and carbs:
            try:
                calories = float(calories)
                proteins = float(proteins)
                fats = float(fats)
                carbs = float(carbs)

                result = self.dish_manager.add_dish(name, calories, proteins, fats, carbs)
                messagebox.showinfo("Данные записаны", result)
                self.add_dish_window.destroy()
            except ValueError:
                messagebox.showwarning("Ошибка, обратитесь к админимстратору")
        else:
            messagebox.showwarning("Ошибка, заполните все поля")

    def open_search_window(self):
        self.find_dish = SearchDish(self.master)
        self.find_dish.display_dish()
    
    def show_calories_graph(self):
        self.plot.show_calories_graph()

def run_app():
    root = tkinter.Tk()
    app = AppWindow(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
