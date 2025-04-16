import pandas as pd

def calculate_min_imported_cargo(file_path):
    df = pd.read_csv(file_path)
    imported_columns = [col for col in df.columns if 'ввезено' in col]
    min_imported = df[imported_columns].sum().min()
    min_stations = df[imported_columns].sum()[df[imported_columns].sum() == min_imported].index.tolist()
    return min_stations, min_imported

def calculate_max_imported_cargo(file_path):
    df = pd.read_csv(file_path)
    imported_columns = [col for col in df.columns if 'ввезено' in col]
    max_imported = df[imported_columns].sum().max()
    max_stations = df[imported_columns].sum()[df[imported_columns].sum() == max_imported].index.tolist()
    return max_stations, max_imported


def most_imported_type(file_path):
    df = pd.read_csv(file_path)

    # Проверка данных
    print("Данные из CSV-файла:")
    print(df)

    imported_columns = [col for col in df.columns if 'ввезено' in col]
    df['Total Imported'] = df[imported_columns].sum(axis=1)

    # Проверка суммы ввезенного груза
    print("Сумма ввезенного груза:")
    print(df[['Тип груза', 'Total Imported']])

    max_imported_value = df['Total Imported'].max()
    max_imported_cargo_types = df[df['Total Imported'] == max_imported_value]['Тип груза'].tolist()

    return max_imported_cargo_types, max_imported_value