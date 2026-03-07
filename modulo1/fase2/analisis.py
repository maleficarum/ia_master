import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

"""
    Loads data from the given location and creates a DataFrame.

"""
def load_data(data_location):
    file_path = Path(data_location)

    if file_path.exists():
        print(f"The path {file_path} exists.")

        df = pd.read_csv(data_location)

        return df
    else:
        print(f"The path {file_path} doesn't exist.")

    return None

def print_statistics(df, max = 10):
    print(f'\t====\tPreview')
    print(df.head(max))

    print('')
    print(f"The Number of Rows are {df.shape[0]}, and columns are {df.shape[1]}.")

    print(f'\t====\tInfo')
    print(df.info())

    print(f'\t====\tNull summary')
    print(df.isnull().sum().sort_values(ascending = False))

def describe_data_frame(df):
    print('')
    print(df.describe())

def plot(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df[df['WH_ID'] == 400], x='ITEM')
    plt.title('Item Counts for refurbished devices')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show(block=True)

    # Convert MOVEMENT_DATE to datetime
    df['MOVEMENT_DATE'] = pd.to_datetime(df['MOVEMENT_DATE'])

    # Filter and group by month
    df_filtered = df[df['WH_ID'] == 400]
    monthly_counts = df_filtered.resample('ME', on='MOVEMENT_DATE')['ITEM'].count()

    plt.figure(figsize=(12, 6))
    monthly_counts.plot(kind='line', marker='o')
    plt.title('Item Movement Over Time refurbished devices')
    plt.xlabel('Date')
    plt.ylabel('Number of Items')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show(block=True)

    # synthesis = pd.crosstab(
    #     index=df['MOVEMENT_DATE'].dt.date, 
    #     columns=df['WH_ID'],
    #     values=df['ITEM'],
    #     aggfunc='count'
    # ).fillna(0)

    # # Visualizar la síntesis con heatmap
    # plt.figure(figsize=(12, 8))
    # sns.heatmap(synthesis, annot=True, fmt='g', cmap='YlOrRd')
    # plt.title('Síntesis de Movimientos por Día y Almacén')
    # plt.xlabel('WH_ID')
    # plt.ylabel('Fecha')
    # plt.tight_layout()
    # plt.show(block=True)    

def explain_data(df):
    explain_1 = df.groupby(['ITEM', 'WH_ID']).size().reset_index(name='CONTEO')
    explain_2 = df.groupby('WH_ID').agg({
    'ITEM': ['count', 'nunique'],  # conteo total y items únicos
    'SERIE': 'count'  # conteo de series
    }).round(2)

    df['MOVEMENT_DATE'] = pd.to_datetime(df['MOVEMENT_DATE'])

    # Síntesis: Movimientos por mes
    explain_3 = df.set_index('MOVEMENT_DATE').groupby([pd.Grouper(freq='ME'), 'WH_ID']).size().unstack(fill_value=0)    
    
    return {"explain1": explain_1, "explain2": explain_2, "explain3": explain_3}


# Prepare the pandas
pd.set_option('display.max_columns', None) 

df = load_data('../fase1/historico_reparaciones.csv')
print_statistics(df, 20)
describe_data_frame(df)
plot(df)

explain = explain_data(df)

print(explain["explain1"])
print(explain["explain2"])
print(explain["explain3"])

