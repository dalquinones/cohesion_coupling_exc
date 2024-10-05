
import pandas as pd
def process_file_and_filter():
    file_path = input("Ingresa la ruta del archivo CSV: ")
    df = pd.read_csv(file_path)

    search_term = input("Ingresa el término de búsqueda: ")
    filtered_df = df[df['data'].str.contains(search_term, case=False)]

    output_file = input("Ingresa el nombre del archivo para guardar los resultados filtrados: ")
    filtered_df.to_csv(output_file, index=False)
    
    print(filtered_df.head())

if __name__ == "__main__":
    process_file_and_filter()