# Python Program 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# in order to generate data with 4 features and 200 samples
np.random.seed(0)
data = np.random.rand(200, 4)
# take the generated data into the CSV file format
df = pd.DataFrame(data)
df.to_csv('network_data.csv', index=False, header=False)
# to read and calculate matrix 
df = pd.read_csv('network_data.csv', header=None)
correlation_matrix = df.corr(method='pearson')
# to see the generated data names 
feature_names = [f'Feature_{i+1}' for i in range(4)]
correlation_matrix.columns = feature_names
correlation_matrix.index = feature_names
# to complete the joand save the data into pdf file format
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.pdf')
# another task to find the two highest correlation feature 
correlation_values = correlation_matrix.unstack()
sorted_correlation_values = correlation_values.sort_values(ascending=False)
highest_correlation = sorted_correlation_values[sorted_correlation_values < 1].head(2)
# to save the generated two highest features name into pdf
try:
    with open('highest_correlation.pdf', 'w') as f:
        f.write(f'Two features with the highest correlation: {highest_correlation.index[0][0]} and {highest_correlation.index[1][0]}')
    print("Successfully saved 'highest_correlation.pdf'.")
except Exception as e:
    print("Error saving 'highest_correlation.pdf':", e)
# to see the corellation
plt.show()
