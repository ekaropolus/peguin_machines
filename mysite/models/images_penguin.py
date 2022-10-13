# importing required modules
import seaborn as sns
import pandas as pd

# creating plotting data
df = pd.read_csv("penguins_size_test.csv")
df = df.dropna()

# plotting
plot = sns.pairplot(df, hue="species", size=3,diag_kind="hist")
fig = plot.fig


# saving the file.Make sure you
# use savefig() before show().
fig.savefig("/home/3karopolus/mysite/static/seas.png")



