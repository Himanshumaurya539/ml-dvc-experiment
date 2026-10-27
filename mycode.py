import pandas as pd
import os 

os.makedirs('data', exist_ok=True)
df = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
})

df.to_csv('data/sample_data.csv', index=False)
print("Sample data saved to 'data/sample_data.csv'")    