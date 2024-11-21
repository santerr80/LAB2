import pandas as pd


def clean_data(input_file, output_file):
    # Пример очистки данных
    df = pd.read_csv(input_file)
    df = df.dropna()  # Удаление пропущенных значений
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    clean_data('data/Sleep_health_and_lifestyle_dataset.csv',
               'data/cleaned_data.csv')
