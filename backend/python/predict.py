import sys
import joblib
import numpy as np
import json

model = joblib.load("../model/model.pkl")
label_encoder = joblib.load("../model/label_encoder.pkl")
symptom_index = joblib.load("../model/symptom_index.pkl")
severity_dict = joblib.load("../model/severity_dict.pkl")

input_symptoms = json.loads(sys.argv[1])

vector = np.zeros(len(symptom_index))
for symptom in input_symptoms:
    symptom = symptom.strip().lower()
    if symptom in symptom_index and symptom in severity_dict:
        idx = symptom_index[symptom]
        vector[idx] = severity_dict[symptom]

prediction = model.predict([vector])[0]
predicted_disease = label_encoder.inverse_transform([prediction])[0]

# Load descriptions and precautions
import pandas as pd
info = {}
try:
    desc_df = pd.read_csv("../model/symptom_Description.csv")
    prec_df = pd.read_csv("../model/symptom_precaution.csv")
    
    desc_row = desc_df[desc_df['Disease'] == predicted_disease]
    info['description'] = desc_row['Description'].values[0] if not desc_row.empty else "No description found."
    
    prec_row = prec_df[prec_df['Disease'] == predicted_disease]
    if not prec_row.empty:
        precautions = [prec_row[f'Precaution_{i}'].values[0] for i in range(1, 5) if pd.notna(prec_row[f'Precaution_{i}'].values[0])]
        info['precautions'] = precautions
    else:
        info['precautions'] = []
except Exception as e:
    info['description'] = "Error loading info."
    info['precautions'] = []

print(json.dumps({
    "prediction": predicted_disease,
    "description": info['description'],
    "precautions": info['precautions']
}))
