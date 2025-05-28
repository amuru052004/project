import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("AI-Based Career Counselor")

st.markdown("### Enter your details:")

education = st.selectbox("Select your education level", ["Bachelor's", "Master's", "Diploma", "PhD"])
skills = st.text_input("Enter your primary skill (e.g. Python, ML, VLSI)")
interests = st.text_input("Enter your interest area (e.g. AI, Design, Research)")

if st.button("Predict Career"):
    from sklearn.preprocessing import LabelEncoder

    # Hardcoded encoding based on original training
    # Ideally, you should store & load encoders but for now this mock example assumes encoders are similar
    def encode_input(val, le_name):
        encoders = {
            "Bachelor's": 0, "Master's": 1, "Diploma": 2, "PhD": 3,
            "Python": 0, "ML": 1, "VLSI": 2,
            "AI": 0, "Design": 1, "Research": 2
        }
        return encoders.get(val, 0)

    edu = encode_input(education, 'Education')
    skill = encode_input(skills, 'Skills')
    interest = encode_input(interests, 'Interests')

    input_data = np.array([[edu, skill, interest]])
    prediction = model.predict(input_data)
    st.success(f"Recommended Career ID: {prediction[0]} (use label encoder to map to real name)")
