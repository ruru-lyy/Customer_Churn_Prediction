import streamlit as st
import pandas as pd
import joblib
from PIL import Image

model = joblib.load('vault\\xgboost_model.pkl')  
preprocessor = joblib.load('vault\\churn_preprocessor.pkl')

st.set_page_config(page_title="Churn Predictor", page_icon="👨‍💼")
st.title("🙆‍♀️ Customer Churn Predictor")

# cartoon char shud be in center
col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
with col_img2:
    img = Image.open("assets/Cute_Cartoon.png")
    st.image(img, caption="Meet Alex – Our Curious Customer!", use_column_width=True)

st.markdown("Enter customer details below to check if they're likely to churn!")

# Input form
with st.form("churn_form"):
    st.header("Customer Information")
    
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100, 30)
        tenure = st.number_input("Tenure (months)", 0, 120, 24)
        usage_freq = st.number_input("Usage Frequency (per month)", 0, 100, 12)
        support_calls = st.number_input("Support Calls", 0, 50, 2)
        payment_delay = st.number_input("Payment Delay (days)", 0, 30, 5)
        total_spend = st.number_input("Total Spend ($)", 0.0, 10000.0, 1000.0)
        last_interaction = st.number_input("Days Since Last Interaction", 0, 365, 30)

    with col2:
        clv = st.number_input("Customer Lifetime Value (CLV)", 0.0, 50000.0, 5000.0)
        monthly_spend = st.number_input("Monthly Spend ($)", 0.0, 5000.0, 50.0)
        usage_intensity = st.number_input("Usage Intensity", 0.0, 1.0, 0.5)
        support_call_rate = st.number_input("Support Call Rate", 0.0, 1.0, 0.1)
        interaction_ratio = st.number_input("Last Interaction Ratio", 0.0, 1.0, 0.2)
        delay_ratio = st.number_input("Payment Delay/Tenure Ratio", 0.0, 2.0, 0.2)

        gender = st.selectbox("Gender", ["Male", "Female"])
        subscription = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
        contract = st.selectbox("Contract Length", ["Monthly", "Quarterly", "Annual"])
        age_group = st.selectbox("Age Group", ["Under 25", "25-35", "36-50", "51-65", "65+"])
        tenure_group = st.selectbox("Tenure Group", ["< 1 Year", "1-2 Years", "2-3 Years", "3+ Years"])

    submit = st.form_submit_button("Predict Churn")

# Prediction logic
if submit:
    input_df = pd.DataFrame([{
        'Age': age,
        'Tenure': tenure,
        'Usage Frequency': usage_freq,
        'Support Calls': support_calls,
        'Payment Delay': payment_delay,
        'Total Spend': total_spend,
        'Last Interaction': last_interaction,
        'CLV': clv,
        'Monthly_Spend': monthly_spend,
        'Usage_Intensity': usage_intensity,
        'Support_Call_Rate': support_call_rate,
        'Last_Interaction_Ratio': interaction_ratio,
        'Payment_Delay_Tenure_Ratio': delay_ratio,
        'Gender': gender,
        'Subscription Type': subscription,
        'Contract Length': contract,
        'Age_Group': age_group,
        'Tenure_Group': tenure_group
    }])

    X_transformed = preprocessor.transform(input_df)
    prediction = model.predict(X_transformed)[0]
    probability = model.predict_proba(X_transformed)[0][1]

    st.subheader("🔮 Prediction Result")
    if prediction == 1:
        st.error(f"Customer is likely to churn with {probability:.2%} probability.")
    else:
        st.success(f"Customer is unlikely to churn. Risk level: {probability:.2%}.")
