import tkinter

from database import Database

class SearchDish:
    def __init__(self, master):
        self.master = master
        self.database = Database('calorie_tracker', 'your_username', 'your_password')
        self.database.connect()
        self.create_search_window()

    def create_search_window(self):
        self.search_window = tkinter.Toplevel(self.master)
        self.search_window.title("Поиск блюда")

        label_search = tkinter.Label(self.search_window, text="Введите название:")
        label_search.pack()
        self.entry_search = tkinter.Entry(self.search_window)
        self.entry_search.pack()

        button_search = tkinter.Button(self.search_window, text="Поиск", command=self.display_dish)
        button_search.pack()

    def search_dish(self, name):
        if self.database.cursor is None:
            print("нету базы данных")
            return None

        try:
            self.database.cursor.execute("SELECT * FROM dishes WHERE name=%s", (name,))
            dish = self.database.cursor.fetchone()
            return dish
        except Exception as e:
            print(f"ошибка: {e}")
            return None

    def display_dish(self):
        dish_name = self.entry_search.get()
        dish = self.search_dish(dish_name)

        if dish:
            label_result = tkinter.Label(self.search_window, text=f"Name: {dish[1]}\nCalories: {dish[2]}\nProteins: {dish[3]}\nFats: {dish[4]}\nCarbs: {dish[5]}")
            label_result.pack()
        else:
            label_result = tkinter.Label(self.search_window, text="Блюдо не найдено")
            label_result.pack()