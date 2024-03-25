# Network Packet Data

#  importin pytong "random" module that provides functions for generating random numbers and performing random selection from sequences
def jls_extract_def():
    
    return 


Python = jls_extract_def()
import random

# Importing CSV Module that provides classes for reading and writing CSV files.

import csv

# defining a function to generate random network packet data

def generate_network_packet_data(num_samples):

    data = []

    for _ in range(num_samples):

        source_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

        destination_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))

        source_port = random.randint(1, 65535)

        destination_port = random.randint(1, 65535)

        data.append([source_ip, destination_ip, source_port, destination_port])
    return data

# in order to Generate 200 samples of network packet data

num_samples = 200

network_packet_data = generate_network_packet_data(num_samples)

# up: the 200 variable is used to specify the number of network packet samples that we want to generate

# we are addressing the function defined earlier

# when we call our function with the argument it gonna generate synthetic network packet data based on the specified number of samples.

# Specify the file path

file_path = "network_packet_data.csv"


# Writing data to CSV file without feature names as the first row

with open(file_path, "w", newline="") as csv_file:

    csv_writer = csv.writer(csv_file)

    csv_writer.writerows(network_packet_data)
    import random
import pandas as pd

# Define a function to generate random network packet data
def generate_network_packet_data(num_samples):
    data = []
    for _ in range(num_samples):
        source_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        destination_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        source_port = random.randint(1, 65535)
        destination_port = random.randint(1, 65535)
        data.append([source_ip, destination_ip, source_port, destination_port])
    return data

# Generate 200 samples of network packet data
num_samples = 200
network_packet_data = generate_network_packet_data(num_samples)

# Create a DataFrame from the generated data
df = pd.DataFrame(network_packet_data, columns=['Source IP', 'Destination IP', 'Source Port', 'Destination Port'])

# Specify the file path for the Excel file
excel_file_path = "network_packet_data.xlsx"

# Write the DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)

print("Network packet data has been written to", excel_file_path)
import pandas as pd
# Read the CSV data into a DataFrame
df = pd.read_csv("this_csvfile.csv", header=None)
# Split the single column into four columns: Source IP, Destination IP, Source Port, Destination Port
df = df[0].str.split(',', expand=True)
df.columns = ['Source IP', 'Destination IP', 'Source Port', 'Destination Port']
# Convert IP addresses from string to numerical format
def ip_to_numeric(ip):
    parts = ip.split('.')
    numeric_ip = 0
    for part in parts:
        numeric_ip = numeric_ip * 256 + int(part)
    return numeric_ip
    df['Source IP'] = df['Source IP'].apply(ip_to_numeric)
df['Destination IP'] = df['Destination IP'].apply(ip_to_numeric)
# Convert Port numbers from string to numeric
df['Source Port'] = pd.to_numeric(df['Source Port'])
df['Destination Port'] = pd.to_numeric(df['Destination Port'])
# Calculate the correlation matrix using Pearson correlation coefficient
correlation_matrix = df.corr(method='pearson')
# Print or display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)
# Correlation Matrix couldnot  measured as the csv details must to e in numerical format, trying another way 







