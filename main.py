import pandas as pd
import os
import matplotlib.pyplot as plt

class CargoTableManager:
    def __init__(self, file_path='cargo_table.csv'):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            self.create_default_table()

    def create_default_table(self):
        data = {
            'Тип груза': ['Цемент', 'Кирпич', 'Краска', 'Плитка'],
            'A вывезено': [0, 0, 0, 0],
            'B вывезено': [0, 0, 0, 0],
            'C вывезено': [0, 0, 0, 0],
            'D вывезено': [0, 0, 0, 0],
            'A ввезено': [0, 0, 0, 0],
            'B ввезено': [0, 0, 0, 0],
            'C ввезено': [0, 0, 0, 0],
            'D ввезено': [0, 0, 0, 0]
        }

        df = pd.DataFrame(data)
        df.to_csv(self.file_path, index=False)

    def update_value(self, cargo_type, column, value):
        df = pd.read_csv(self.file_path)

        if cargo_type in df['Тип груза'].values:
            df.loc[df['Тип груза'] == cargo_type, column] = value
            df.to_csv(self.file_path, index=False)
        else:
            print(f"Тип груза '{cargo_type}' не найден в таблице.")

    def display(self):
        df = pd.read_csv(self.file_path)
        print(df)

manager = CargoTableManager()

manager.display()
manager.update_value('Цемент', 'A вывезено', 100)
manager.update_value('Кирпич', 'B ввезено', 200)
manager.display()

def graph():
    df = pd.read_csv(manager.file_path)
    df.set_index('Тип груза').plot(kind='bar', figsize=(10, 6))

    # настройка
    plt.title('Вывезено и ввезено грузов')
    plt.xlabel('Тип груза')
    plt.ylabel('Количество')
    plt.xticks(rotation=45)
    plt.legend(title='Категория')
    plt.tight_layout()
    plt.show()

# вызов графика
graph()

