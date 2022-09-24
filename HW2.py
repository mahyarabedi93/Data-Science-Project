import seaborn as sns
import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
from sklearn.datasets import load_iris

iris_data = sns.load_dataset("iris")

# Create distplot with custom bin_size

st.write("""
# Iris Dataset
How are Sepal lenght and width in addition to petal width is correlated to Iris Species?
""")

fig = px.scatter_3d(iris_data, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')

st.plotly_chart(fig)
