import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['species'] = pd.Categorical.from_codes(data.target, data.target_names)

# Show summary statistics
print('Summary statistics:')
print(df.describe())
print('\nSpecies counts:')
print(df['species'].value_counts())

# Plot histograms for each feature
df.hist(figsize=(10, 8))
plt.suptitle('Histograms of Iris Features')
plt.tight_layout()
plt.show()

# Scatter plot: sepal length vs petal length, colored by species
plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x='sepal length (cm)',
    y='petal length (cm)',
    hue='species',
    palette='Set1',
    s=70
)
plt.title('Sepal Length vs Petal Length by Species')
plt.show() 