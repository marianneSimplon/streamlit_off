import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

data = pd.read_csv(r"data/data_cleaned.csv", decimal='.')

st.title("Open Food Fact")
st.write("Bienvenue ! "
"Prenez place et découvrez Cholesterôle, l'application qui vous conseille sur les rôle des aliments dans votre diabète.")

st.write(data)

fig1 = px.histogram(data, x="pnns_groups_2", color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending")
st.plotly_chart(fig1)

fig2 = px.histogram(data, x="pnns_groups_1", color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending")
st.plotly_chart(fig2)

fig3 = px.histogram(data, x="fat_100g", color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending")
st.plotly_chart(fig3)

fig4 = px.histogram(data, x="saturated-fat_100g", color="nutriscore_grade").update_xaxes(categoryorder="category ascending")
st.plotly_chart(fig4)

fig5 = px.histogram(data, x="nova_group", color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending")
st.plotly_chart(fig5)

fig6 = px.histogram(data, x="ingredients_from_palm_oil_n", color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending")
st.plotly_chart(fig6)

fig7 = px.histogram(data, x="ingredients_that_may_be_from_palm_oil_n", color="saturated_fat_in_g").update_xaxes(categoryorder="category ascending")
st.plotly_chart(fig7)