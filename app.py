import streamlit as st
import joblib
import numpy as np

# --- Load trained model ---
model = joblib.load("cr_predictor_model.pkl")

# --- Application title and description ---
st.title('D&D 5e Monster CR Predictor')
st.markdown("""
Enter your monster's stat block below to receive a predicted Challenge Rating.
Use this tool to validate custom monster designs against a model trained on 428 
official monsters from the fifth edition Monster Manual.
""")

# --- Preset example monsters for reference ---
st.header('Load an Example Monster')
example = st.selectbox(
    "Select a known monster to see how the model performs:",
    ["None", "Goblin (CR 1/4)", "Ogre (CR 2)", "Adult Red Dragon (CR 17)"]
)

# --- Default values ---
default_hp = 50
default_ac = 12
default_str = 10
default_dex = 10
default_con = 10
default_int = 10
default_wis = 10
default_cha = 10

# --- Load preset stats from selection ---
if example == "Goblin (CR 1/4)":
    default_hp = 7
    default_ac = 15
    default_str = 8
    default_dex = 14
    default_con = 10
    default_int = 10
    default_wis = 8
    default_cha = 8

elif example == "Ogre (CR 2/4)":
    default_hp = 59
    default_ac = 11
    default_str = 19
    default_dex = 8
    default_con = 16
    default_int = 5
    default_wis = 7
    default_cha = 7

elif example == "Adult Red Dragon (CR 17)":
    default_hp = 256
    default_ac = 19
    default_str = 27
    default_dex = 10
    default_con = 25
    default_int = 16
    default_wis = 13
    default_cha = 21

# --- Stat input sliders ---
st.header("Monster Stat Block")

col1, col2 = st.columns(2)

with col1:
    hp = st.number_input("Hit Points", 1, 615, default_hp)
    ac = st.slider("Armor Class", 1, 50, default_ac)
    str_ = st.slider("Strength (STR)", 1, 30, default_str)
    dex = st.slider("Dexterity (DEX)", 1, 30, default_dex)

with col2:
    con = st.slider("Constitution (CON)", 1, 30, default_con)
    int_ = st.slider("Intelligence (INT)", 1, 30, default_int)
    wis = st.slider("Wisdom (WIS)", 1, 30, default_wis)
    cha = st.slider("Charisma (CHA)", 1, 30, default_cha)

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
