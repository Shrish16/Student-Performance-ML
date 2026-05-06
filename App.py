import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("🎓 Student Score Predictor")

hours = st.slider("Study Hours", 1, 10)

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([30,40,50,60,70])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[hours]])

st.success(f"Predicted Score: {prediction[0]:.2f}")
