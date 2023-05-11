import imp
import pandas as pd
from termcolor import colored as cl
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

style.use("seaborn-whitegrid")
plt.rcParams["figure.figsize"] = (16,7)

df = sb.load_dataset("iris")
print(cl(df,attrs = ["bold"]))

print(cl(df.describe(), attrs = ["bold"]))
df.info

sb.scatterplot("sepal_length", "sepal_width", data = df, hue = "species", palette = "Set2", edgecolor = "b", s = 150, alpha = 0.7)
plt.title("SEPAL LENGTH / SEPAL WIDTH")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend(loc = "upper left", fontsize = 12)
plt.savefig("sepal.png")

sb.scatterplot('petal_length', 'petal_width', data = df, hue = 'species', palette = 'magma', edgecolor = 'b', s = 150, 
               alpha = 0.7)
plt.title('PETAL LENGTH / PETAL WIDTH')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend(loc = 'upper left', fontsize = 12)
plt.savefig('petal.png')

df_corr = df.corr()

sb.heatmap(df_corr, cmap = "Blues", annot = True, xticklabels = df_corr.columns.values, yticklabels = df_corr.columns.values)
plt.title("iris data Heatmap", fontsize = 15)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)

plt.savefig("heatmap.png")

sb.pairplot(data = df, hue = "species", palette = ["Red", "Blue", "Limegreen"])
plt.savefig("pairplot.png")

plt.subplot(211)
sb.kdeplot(df["sepal_Length"], color = "r", shade = True, label = "Sapel Length")
sb.kdeplot(df["sepal_width"], color = "b", shade = True, label = "Sapel Width")

plt.subplot(212)
sb.kdeplot(df["petal_length"], color = "coral", shade = True, label = "Petal Length")
sb.kdeplot(df["petal_width"], color = "green", shade = True, label = "Petal Width")

plt.savefig("dist.png")

