"""
Removes duplicate rows based on the 'Address' column
"""
import pandas as pd

INPUT_CSV_PATH = 'chainlink/feed/v3/contracts.csv'
OUTPUT_CSV_PATH = 'chainlink/feed/v3/contract_dedup.csv'

try:
    df = pd.read_csv(INPUT_CSV_PATH)
    if 'Address' not in df.columns:
        print(f"错误: CSV文件 '{INPUT_CSV_PATH}' 中不包含名为 'Address' 的列。")
    else:
        df_deduplicated = df.drop_duplicates(subset=['Address'], keep='first')
        df_deduplicated.to_csv(OUTPUT_CSV_PATH, index=False)
except FileNotFoundError:
    print(f"错误: 未找到文件 '{INPUT_CSV_PATH}'。请检查路径是否正确。")
