import pandas as pd # data processing
from termcolor import colored as cl # elegant printing of text
import seaborn as sb # visualizations
import matplotlib.pyplot as plt # editing visualizations
from matplotlib import style # setting styles for plots
from sklearn.preprocessing import StandardScaler # normalizing data
from sklearn.neighbors import KNeighborsClassifier # KNN algorithm
from sklearn.metrics import accuracy_score # algorithm accuracy
from sklearn.model_selection import train_test_split # splitting the data

style.use('seaborn-whitegrid')
plt.rcParams['figure.figsize'] = (20, 10)

# Importing Data

df = sb.load_dataset('iris.csv')
print(cl(df, attrs = ['bold']))

# Data Description

print(cl(df.describe(), attrs = ['bold']))

# Data Info

df.info()

# Visualizing Data

# 1. Sepal scatter visualization

plt.subplot(211)
sb.scatterplot('sepal_length', 'sepal_width', data = df, hue = 'species', palette = 'Set2', edgecolor = 'b', s = 150, 
               alpha = 0.7)
plt.title('SEPAL LENGTH / SEPAL WIDTH')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend(loc = 'upper left', fontsize = 12)
plt.savefig('sepal.png')

plt.subplot(212)
sb.scatterplot('petal_length', 'petal_width', data = df, hue = 'species', palette = 'magma', edgecolor = 'b', s = 150, 
               alpha = 0.7)
plt.title('PETAL LENGTH / PETAL WIDTH')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend(loc = 'upper left', fontsize = 12)
plt.savefig('petal.png')

# 2. Data Heatmap

df_corr = df.corr()
sb.heatmap(df_corr, cmap = 'Blues', annot = True, xticklabels = df_corr.columns.values, yticklabels = df_corr.columns.values)
plt.title('Iris Data Heatmap', fontsize = 15)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.savefig('heatmap.png')

# 3. Scatter Matrix

sb.pairplot(data = df, hue = 'species', palette = ['Red', 'Blue', 'limegreen'])
plt.savefig('pairplot.png')

# 4. Distribution plot

plt.subplot(211)
sb.kdeplot(df['sepal_length'], color = 'r', shade = True, label = 'Sepal Length')
sb.kdeplot(df['sepal_width'], color = 'b', shade = True, label = 'Sepal Width')
plt.subplot(212)
sb.kdeplot(df['petal_length'], color = 'coral', shade = True, label = 'Petal Length')
sb.kdeplot(df['petal_width'], color = 'green', shade = True, label = 'Petal Width')
plt.savefig('dist.png')

X_var = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
y_var = df['species'].values

print(cl('X varaiable :', attrs = ['bold']), X_var[:5])
print(cl('Y variable :', attrs = ['bold']), y_var[:5])

X_var = StandardScaler().fit(X_var).transform(X_var.astype(float))
print(cl(X_var[:5], attrs = ['bold']))

X_train, X_test, y_train, y_test = train_test_split(X_var, y_var, test_size = 0.3, random_state = 0)

print(cl('Train set shape :', attrs = ['bold']), X_train.shape, y_train.shape)
print(cl('Test set shape :', attrs = ['bold']), X_test.shape, y_test.shape)

k = 3

neigh = KNeighborsClassifier(n_neighbors = k)
neigh.fit(X_train, y_train)

print(cl(neigh, attrs = ['bold']))

yhat = neigh.predict(X_test)

print(cl('Prediction Accuracy Score (%) :', attrs = ['bold']), round(accuracy_score(y_test, yhat)*100, 2))