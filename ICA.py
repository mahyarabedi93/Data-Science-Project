import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv("data.csv")
Data=Data.drop(labels=["Unnamed: 32"],axis=1)

# Create distplot with custom bin_size

st.write("""
# Breast Cancer Visualization
""")

st.write("""
# Jointplot Visualization
""")
Column_Names = st.multiselect(
    "Columns Name for Jointplot",
    ["radius_mean", "texture_mean", "perimeter_mean", "area_mean","smoothness_mean", "compactness_mean",
    "concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se",
    "texture_se","perimeter_se", "area_se", "smoothness_se","compactness_se", "concavity_se",
    "concave points_se", "symmetry_se","fractal_dimension_se", "radius_worst", "texture_worst",
    "perimeter_worst", "area_worst", "smoothness_worst","compactness_worst", "concavity_worst",
    "concave points_worst","symmetry_worst", "fractal_dimension_worst"],
    ["radius_mean", "texture_mean", "perimeter_mean", "area_mean","smoothness_mean", "compactness_mean",
    "concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se",
    "texture_se","perimeter_se", "area_se", "smoothness_se","compactness_se", "concavity_se",
    "concave points_se", "symmetry_se","fractal_dimension_se", "radius_worst", "texture_worst",
    "perimeter_worst", "area_worst", "smoothness_worst","compactness_worst", "concavity_worst",
    "concave points_worst","symmetry_worst", "fractal_dimension_worst"])

option = st.selectbox(
    "Joint Plot Kind Option",
    ("kde", "hex", "scatter" , "reg","resid","hist"))
if option =="scatter":
    fig=sns.jointplot(data=Data,x=Data[Column_Names[0]], y=Data[Column_Names[1]], kind=option,hue="diagnosis")
elif option =="hex":
        fig=sns.jointplot(data=Data,x=Data[Column_Names[0]], y=Data[Column_Names[1]], kind=option, color="#4CB391")
else:
    fig=sns.jointplot(data=Data,x=Data[Column_Names[0]], y=Data[Column_Names[1]], kind=option,hue="diagnosis")
plt.show()
st.pyplot(fig)

st.write("""
# Catplot Visualization
""")

Column_Name = st.selectbox(
    "Columns Name for Catplot",
    ("radius_mean", "texture_mean", "perimeter_mean", "area_mean","smoothness_mean", "compactness_mean",
    "concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se",
    "texture_se","perimeter_se", "area_se", "smoothness_se","compactness_se", "concavity_se",
    "concave points_se", "symmetry_se","fractal_dimension_se", "radius_worst", "texture_worst",
    "perimeter_worst", "area_worst", "smoothness_worst","compactness_worst", "concavity_worst",
    "concave points_worst","symmetry_worst", "fractal_dimension_worst"))

option = st.selectbox(
    "Select Axis for Classifier Catplot",
    ("x", "y"))
    
if option == "x":
    fig=sns.catplot(data=Data, x="diagnosis", y=Column_Name)
else:
    fig=sns.catplot(data=Data, x=Column_Name, y="diagnosis")
plt.show()
st.pyplot(fig)

st.write("""
# Displot Visualization
""")

Column_Names = st.multiselect(
    "Columns Name for Displot",
    ["radius_mean", "texture_mean", "perimeter_mean", "area_mean","smoothness_mean", "compactness_mean",
    "concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se",
    "texture_se","perimeter_se", "area_se", "smoothness_se","compactness_se", "concavity_se",
    "concave points_se", "symmetry_se","fractal_dimension_se", "radius_worst", "texture_worst",
    "perimeter_worst", "area_worst", "smoothness_worst","compactness_worst", "concavity_worst",
    "concave points_worst","symmetry_worst", "fractal_dimension_worst"])
fig=sns.displot(Data[Column_Names],kind="kde")
plt.show()
st.pyplot(fig)

st.write("""
# Lmplot Visualization
""")

option_x = st.selectbox(
    "Select Feature for Axis X Lmplot",
    ("radius_mean", "texture_mean", "perimeter_mean", "area_mean","smoothness_mean", "compactness_mean",
    "concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se",
    "texture_se","perimeter_se", "area_se", "smoothness_se","compactness_se", "concavity_se",
    "concave points_se", "symmetry_se","fractal_dimension_se", "radius_worst", "texture_worst",
    "perimeter_worst", "area_worst", "smoothness_worst","compactness_worst", "concavity_worst",
    "concave points_worst","symmetry_worst", "fractal_dimension_worst"))

option_y = st.selectbox(
    "Select Feature for Axis Y Lmplot",
    ("radius_mean", "texture_mean", "perimeter_mean", "area_mean","smoothness_mean", "compactness_mean",
    "concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se",
    "texture_se","perimeter_se", "area_se", "smoothness_se","compactness_se", "concavity_se",
    "concave points_se", "symmetry_se","fractal_dimension_se", "radius_worst", "texture_worst",
    "perimeter_worst", "area_worst", "smoothness_worst","compactness_worst", "concavity_worst",
    "concave points_worst","symmetry_worst", "fractal_dimension_worst"))

option_hue = st.selectbox(
    "Select Feature for hue Lmplot",
    ("diagnosis","none"))

Lowess = st.selectbox(
    "Do you want lowess option Lmplot",
    ("True", "False"))


if option_hue == "diagnosis":
    if Lowess == "True":
        fig=sns.lmplot(x=option_x, y=option_y, data=Data,lowess=True,palette='brg',hue=option_hue)
    else:
        fig=sns.lmplot(x=option_x, y=option_y, data=Data,lowess=False,palette='brg',hue=option_hue)
else:
    if Lowess == "True":
        fig=sns.lmplot(x=option_x, y=option_y, data=Data,lowess=True,palette='brg')
    else:
        fig=sns.lmplot(x=option_x, y=option_y, data=Data,lowess=False,palette='brg')
plt.show()
st.pyplot(fig)
