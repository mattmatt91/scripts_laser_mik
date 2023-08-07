import pandas as pd
import json
from io import StringIO

# Read the text file and extract the data rows
with open('F:\\test_measurements\\as1.txt', 'r') as file:
    lines = file.readlines()

# Extract data rows from the lines
data_rows = []
for line in lines:
    if line.startswith('1\t'):
        data_rows.append(line.strip())

# Create a DataFrame from the data rows
df = pd.read_csv(StringIO('\n'.join(data_rows)), delimiter='\t', header=None)
df.columns = ['Index', 'X-Axis Value', 'Y-Axis Value']

# Get the header information and store it in a JSON object
header_info = {}
for line in lines:
    if line.startswith('Header Size:') or line.startswith('Pulse Version:') or line.startswith('Running Pulse Version:'):
        key, value = line.strip().split(':', 1)
        header_info[key.strip()] = value.strip()

# Convert the header information to a JSON object
header_json = json.dumps(header_info)

# Display the DataFrame and JSON object
print("DataFrame:")
print(df)

print("\nJSON Object:")
print(header_json)
