#import packages 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Load the dataset and convert to long-form
datasetVariable = sns.load_dataset("datasetName")
datasetVar = datasetVariable.pivot("column1", "column2", "column3")

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(datasetVar, annot=True, fmt="d", linewidths=.5, ax=ax)
