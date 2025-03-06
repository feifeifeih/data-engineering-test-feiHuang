import pandas as pd

def read_data(file_path: str) ->pd.DataFrame:
    """
    read the dataset from csv file
    """
    df = pd.read_csv(file_path)
    return df

def validata_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    performs data validation
    """
    important_info = ["ITEM TYPE", "RETAIL SALES"]
    for col in important_info:
        if df[col].isnull().any():
            df[col] = df[col].fillna(0)

    return df
            
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """ 
    transfrom data by converting the date to standar format
    and aggregate the RETAIL SALES data
    """
    grouping = df.groupby("ITEM TYPE", as_index=False)["RETAIL SALES"].sum()
    grouping.rename(columns = {"RETAIL SALES": "Total_SALES"}, inplace=True)
    return grouping

def load_to_csv(df: pd.DataFrame, output_file: str):
    df.to_csv(output_file, index=False)

def main():
    input_file = "Warehouse_and_Retail_Sales.csv"
    output_csv = "processed_data.csv"

    # read data
    df = read_data(input_file)

    # validate data 
    df = validata_data(df)

    # transform data
    trans_data = transform_data(df)

    # lodad to csv
    load_to_csv(trans_data, output_csv)

    print("data pipeline done!")

if __name__ == "__main__":
    main()