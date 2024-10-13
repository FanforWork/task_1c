import matplotlib.pyplot as plt
from tkinter import messagebox

from database import Database

class Plot:
    def __init__(self):
        self.database = Database('calorie_tracker', 'your_username', 'your_password')
        self.database.connect()
    
    def show_calories_graph(self):
        cursor = cursor()
        cursor.execute('''
        SELECT date, SUM((amount / 100.0) * calories) as total_calories
        FROM meals
        JOIN dishes ON meals.dish_id = dishes.id
        GROUP BY date
        ''')
        data = cursor.fetchall()

        if data:
            dates = [row[0] for row in data]
            calories = [row[1] for row in data]

            plt.figure(figsize=(6, 6))
            plt.plot(dates, calories, marker='o')
            plt.title("Потребление калорий")
            plt.xlabel("Дата")
            plt.ylabel("Калорий")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            messagebox.showinfo("нет информации")