
# 💼 AlexChurn - Customer Churn Prediction App

A streamlined, interactive web application built to predict customer churn using machine learning. Designed for business analysts and decision-makers who need quick, interpretable insights on retention risks.

![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)

---

## 🚀 Live Demo  

Want to know if your customer, Alex, will leave or not??

🔗 **Launch the app now**:  
[https://alexchurn.streamlit.app](https://alexchurn.streamlit.app/?embed_options=show_toolbar,show_colored_line,light_theme,show_padding,show_footer,dark_theme)

Experience real-time predictions, feature insights, and churn risk explanations via a clean UI.

---

## 🧠 Models Used

- **Logistic Regression** – Baseline model for interpretability and clarity.
- **Random Forest** – Ensemble model that handles non-linearity and provides robust feature importance.
- **XGBoost** – Optimized gradient boosting model for best accuracy and class imbalance handling.

---

## 🧰 Tech Stack

- **Python**
- **Scikit-learn**, **XGBoost**, **Pandas**, **Matplotlib**, **SHAP**
- **Streamlit** – For deployment-ready interactive UI
- **Joblib/Pickle** – For saving and loading models

---

## 📂 Project Structure

```
Customer_Churn_Prediction/
│
├── app.py                   # Streamlit app
├── model/
│   └── xgboost_model.pkl    # Trained model
├── data/
│   └── sample_input.csv     # Example input
├── notebooks/               # Exploratory & model training
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation (Local)

```bash
# Clone the repository
git clone https://github.com/ruru-lyy/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📝 Features

- Upload your own customer data
- Predict churn likelihood
- Visualize key factors influencing each prediction (via SHAP)
- Built-in sample dataset for testing

---

## 📈 Future Enhancements

- Model selection dropdown in-app
- Batch processing for large datasets
- Connect to live data sources (via API or DB)

---

## 🧠 Author

**Nirupama Laishram**  
Data Analyst & Aspiring Data Engineer | Bangalore  
🔗 [LinkedIn](https://www.linkedin.com/in/nirupama-l-a14179221/) 

