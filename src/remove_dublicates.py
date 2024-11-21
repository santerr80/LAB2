import pandas as pd


def remove_duplicates(input_file, output_file):
    # Чтение данных
    df = pd.read_csv(input_file)
    # Удаление дубликатов
    df = df.drop_duplicates()
    # Сохранение результата
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    remove_duplicates('data/cleaned_data.csv',
                      'data/remdublicated_data.csv')
