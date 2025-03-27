import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def read_dataset(file_path = 'sp_retro_data.xls'):
    data = pd.read_excel(
        file_path,
        header=0,
        skiprows=2,
        sheet_name='Discretized Data (Final)',
        na_values=['?'],
        engine='xlrd')
    return data

def visualize(data):
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(x='binary_target', data=data, palette='viridis', dodge=False)
    plt.title('Binary Target Distribution')
    plt.xlabel('Class (1: CONSULT, 0: DISCHARGE+CLINIC)')
    plt.ylabel('Count')

    total = len(data)
    for p in ax.patches:
        print(p)   
        percentage = f'{100 * p.get_height() / total:.1f}%'
        x = p.get_x() + p.get_width() / 2
        y = p.get_height() + 5
        ax.annotate(percentage, (x, y), ha='center')

    plt.show()

