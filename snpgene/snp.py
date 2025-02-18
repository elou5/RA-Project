import pandas as pd

# Load both CSV files
df1 = pd.read_csv("kinase_sample.csv")   # Original file
df2 = pd.read_csv("snps_sample.csv")  # File to compare

# List to store matched rows
matched_rows = []

# Loop through each row in file2.csv
for index2, row2 in df2.iterrows():
    column1_value_file2 = row2["chromosome"]
    column2_value_file2 = row2["snp_position"]
    column4_value_file2 = row2["snp_name"]
    
    # Loop through each row in file.csv to find matches
    for index1, row1 in df1.iterrows():
        column1_value_file1 = row1["chromosome"]
        column2_value_file1 = row1["kinase_start"]
        column3_value_file1 = row1["kinase_end"]
        column4_value_file1 = row1["gene_name"]
        
        # Check if Column1 values match
        if column1_value_file2 == column1_value_file1:
            # Check if Column3 in file2 is within the specified range
            if (column2_value_file1 - 10000) < column2_value_file2 < (column3_value_file1 + 10000):
                # If both conditions are met, add the row to matched_rows
                matched_rows.append({
                    "chromosome": column1_value_file2,
                    "snp_position": column2_value_file2,
                    "snp_name": column4_value_file2,
                    "kinase_start": column2_value_file1,
                    "kinase_end": column3_value_file1,
                    "gene_name": column4_value_file1
                })

# Convert matched rows to a DataFrame and write to a new CSV file
output_df = pd.DataFrame(matched_rows)
output_df.to_csv("match.csv", index=False)