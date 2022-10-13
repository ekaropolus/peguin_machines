import pandas as pd
from sklearn.naive_bayes import GaussianNB

import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("penguins_size_test.csv")
print(df.shape[0])
df = df.dropna()
print(df.shape[0])
print(df.dtypes)
# df.to_csv("out.csv",index=False)


y = df["species"]
X = df.iloc[:,[2,3,4,5]]

clf = GaussianNB()
clf.fit(X, y)

import joblib

joblib.dump(clf, "clf.pkl")
sns.pairplot(df, hue="species", size=3,diag_kind="hist")