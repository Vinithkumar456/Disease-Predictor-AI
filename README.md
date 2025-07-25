# 🧠 Disease Predictor using Machine Learning

A smart disease prediction system built with **React.js** for the frontend and **Python (Flask)** for the backend. The model predicts possible diseases based on user-selected symptoms and provides descriptions and precautions.

---

## 📊 Dataset

- **Source**: [Disease Symptom Description Dataset – Kaggle](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset)
- Includes:
  - Symptom-to-disease mappings
  - Disease descriptions
  - Precautionary measures

> ⚠️ **Note**: The full dataset is not included in this repo. Only a sample is provided (`sample_symptoms.csv`). Please download the full dataset from [Kaggle](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset) for training.

---

## 💡 Features

- ✅ Predict diseases based on symptoms
- ✅ Display detailed disease descriptions
- ✅ Show recommended precautions
- ✅ Clean, interactive React UI
- ✅ Trained machine learning model using scikit-learn

---

## ⚙️ Tech Stack

| Layer      | Technology               |
|------------|--------------------------|
| Frontend   | React.js                 |
| Backend    | Node.js                  |
| ML Model   | scikit-learn             |
| Dataset    | Kaggle (linked above)    |

---

## 📂 Project Structure

```
Disease-Predictor/
├── backend/                # Flask backend + trained model
│   ├── app.py
│   └── model.pkl
├── frontend/               # React frontend
│   └── src/
├── model/                  # Jupyter notebook + sample data
│   ├── train_model.ipynb
│   └── sample_symptoms.csv
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com//disease-predictor.git
cd disease-predictor
```

### 2️⃣ Run Backend (Flask)

```bash
cd backend
pip install -r ../requirements.txt
python app.py
```

### 3️⃣ Run Frontend (React)

```bash
cd ../frontend
npm install
npm start
```

- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:5000`

---

## 🔮 Future Improvements

- Deploy the app (Render, Netlify, or Vercel + Heroku)
- Add multilingual support
- Include user authentication
- Make model more robust with larger datasets

---

## 🙏 Acknowledgements

- Dataset by [Itachi9604 on Kaggle](https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset)
- Flask, React, scikit-learn documentation

---

## 📜 License

This project is open-source and free to use for educational purposes.
