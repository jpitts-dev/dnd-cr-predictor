import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("cr_predictor_model.pkl")

# Application details
st.title('D&D 5e Monster CR Predictor')
st.markdown("""
Enter your monster's stat block below to receive a predicted Challenge Rating.
Use this tool to validate custom monster designs against a model trained on 428 
official monsters from the fifth edition Monster Manual.
""")

# Input sliders
st.header("Monster Stat Block")

col1, col2 = st.columns(2)

with col1:
    hp = st.number_input("Hit Points", 1, 500, 50)
    ac = st.slider("Armor Class", 1, 50, 12)
    str_ = st.slider("Strength (STR)", 1, 30, 10)
    dex = st.slider("Dexterity (DEX)", 1, 30, 10)

with col2:
    con = st.slider("Constitution (CON)", 1, 30, 10)
    int_ = st.slider("Intelligence (INT)", 1, 30, 10)
    wis = st.slider("Wisdom (WIS)", 1, 30, 10)
    cha = st.slider("Charisma (CHA)", 1, 30, 10)

# Prediction button
if st.button("Predict CR"):
    features = np.array([[ac, hp, str_, dex, con, int_, wis, cha]])
    prediction = model.predict(features)[0]
    prediction = round(prediction * 4) / 4

    st.success(f"Predicted Challenge Rating: **{prediction}**")

    st.markdown("---")
    st.caption("""
    Note: This model is trained on official fifth edition monsters and is most accurate 
    at low to mid CR values. Homebrew monsters with unconventional stat distributions or 
    special abilities not captured by raw stats may produce less precise predictions.
    """)
