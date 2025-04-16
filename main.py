import pandas as pd
import os
from cargo_calculations import calculate_min_imported_cargo, calculate_max_imported_cargo, most_imported_type
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
            df.loc[df['Тип груза'] == cargo_type, column] += value
            df.to_csv(self.file_path, index=False)
        else:
            print(f"Тип груза '{cargo_type}' не найден в таблице.")

    def display(self):
        df = pd.read_csv(self.file_path)
        print(df)

    def delete_file(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            print(f"Файл '{self.file_path}' успешно удален.")
        else:
            print(f"Файл '{self.file_path}' не существует.")

    def write_conclusion(self):
        def conclusion_auto(words, subject, value):
            for i in subject:
                words += (f"\t{i} - {value}, ")
            return words[:-2]
            
        min_stations, min_imported = calculate_min_imported_cargo(self.file_path)
        max_stations, max_imported = calculate_max_imported_cargo(self.file_path)
        most_imported_cargo_type, most_imported_value = most_imported_type(self.file_path)
        with open('conclusion.txt', 'w', encoding='utf-8') as file:
            # file.write(f"\tСамый ввозимый груз:\n")
            # file.write(f"\t\t{most_imported_cargo_type}: {most_imported_value}\n")
            file.write(conclusion_auto("Меньше всего груза ввезли в склад(ы): \n", min_stations, min_imported))
            file.write(conclusion_auto(".\nБольше всего груза ввезли в склад(ы): \n", max_stations, max_imported))
            file.write(conclusion_auto(".\nСамый ввозимый груз:\n", most_imported_cargo_type, most_imported_value))

            string_words3 = ""

    def graph(self):
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

manager = CargoTableManager()
manager.update_value('Цемент', 'A вывезено', 100)
manager.update_value('Кирпич', 'B ввезено', 100)
# manager.display() - дисплей выводит таблицу в консоль
# manager.update_value('Цемент', 'A вывезено', 100) - добавляет данные в таблицу
# manager.update_value('Кирпич', 'B ввезено', 200)
# manager.display()

# вызов графика
# graph()

if __name__ == '__main__':
    manager = CargoTableManager()
    manager.write_conclusion()
    manager.graph()
    manager.delete_file()