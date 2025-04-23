# import requests

# table_number = "1410035301"  # Replace with your Table Number
# url = f"https://www150.statcan.gc.ca/t1/wds/rest/getCubeMetadataByTableNum/1410035301/en"

# response = requests.get(url)

# print(response)

# if response.status_code == 200:
#     data = response.json()
#     if "object" in data and data["object"]:
#         product_id = data["object"]["cubeId"]
#         print("Product ID:", product_id)
#     else:
#         print("No Product ID found.")
# else:
#     print("Request failed with status:", response.status_code)

import pandas as pd

# Download and load the CSV manually
csv_url = "https://www150.statcan.gc.ca/t1/tbl1/en/dtl!downloadDb-nonTraduit.action?pid=1410035301&fileType=csv"
df = pd.read_csv(csv_url)

# Show first 5 rows
print(df.head())
