import plotly.express as px
import pandas as pd
import csv

df = pd.read_csv("Cases.csv")
fig = px.scatter(df, x="date", y="cases",
	          size="cases",color="country",
                   size_max=60)
fig.show()
