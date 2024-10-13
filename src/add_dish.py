from database import Database
from tkinter import messagebox

class AddDish:
    def __init__(self):
        self.database = Database('calorie_tracker', 'your_username', 'your_password')
        self.database.connect()
        self.create_table()

    def create_table(self):
        self.database.create_tables()

    def add_dish(self, name, calories, proteins, fats, carbs):
        if self.database.cursor is None:
            messagebox.showwarning("нет соединения")
            return

        try:
            self.database.cursor.execute('''
                INSERT INTO dishes (name, calories, proteins, fats, carbs)
                VALUES (%s, %s, %s, %s, %s)
            ''', (name, calories, proteins, fats, carbs))
            self.database.connection.commit()
            messagebox.showinfo("блюдо добавое")
        except Exception as e:
            messagebox.showwarning(f"ошибка вставки: {e}")
        finally:
            pass