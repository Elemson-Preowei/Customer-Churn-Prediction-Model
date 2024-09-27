import pandas as pd
import streamlit as st
import pickle

# Load pre-trained model
with open('model2.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    loaded_scaler = pickle.load(f)


def prediction(data):
    # Create a dataframe from input data
    df = pd.DataFrame([data], columns=[
        'ID', 'Name', 'Email', 'Phone', 'Address', 'Age', 'Gender', 'NPS',
        'PurchaseFrequency', 'PurchaseValue', 'WebsitePageViews',
        'WebsiteTimeSpent', 'EngagementMetricsLogins', 'EngagementMetricsFrequency',
        'FeedbackRating', 'ServiceInteractions_Call', 'ServiceInteractions_Email',
        'ServiceInteractions_Chat', 'PaymentHistoryNoOfLatePayments', 'SubscriptionDuration'])

    # Drop non-essential columns
    df = df.drop(columns=['ID', 'Name', 'Email', 'Phone', 'Address'])

    # Encode categorical columns
    gender_map = {'Male': 0, 'Female': 1}
    engagement_frequency_map = {'Weekly': 0, 'Daily': 1,'Monthly': 2}

    df['Gender'] = df['Gender'].map(gender_map)
    df['EngagementMetricsFrequency'] = df['EngagementMetricsFrequency'].map(engagement_frequency_map)

    # Standardize the numerical columns using the loaded scaler
    working_data = loaded_scaler.transform(df)

    # Make a prediction
    pred = loaded_model.predict(working_data)

    # Return result based on prediction
    if pred[0] == 0:
        return "The customer will not churn"
    else:
        return "The customer will churn"


def main():
    # Collect input from the user
    st.title("Elemson's Customer Churn Prediction Model")
    ID = st.text_input("Enter customer ID: ")
    Name = st.text_input("Enter customer name: ")
    Email = st.text_input("Enter customer email: ")
    Phone = st.text_input("Enter customer phone number: ")
    Address = st.text_input("Enter customer address: ")
    Age = st.number_input("How old is the customer?: ")
    Gender = st.radio("Customer Gender:", ("Male", "Female"))
    NPS = st.number_input("Net Promoter Score on a scale of 1-10: ")
    PurchaseFrequency = st.number_input("How many times has the customer made purchases? ")
    PurchaseValue = st.number_input("What is the total value of the customer's purchases? ")
    WebsitePageViews = st.number_input("How many times did the customer visit the website? ")
    WebsiteTimeSpent = st.number_input("Enter total hours the customer has spent on the website? ")
    EngagementMetricsLogins = st.number_input("Enter total number of times this customer logged in on the website ")
    EngagementMetricsFrequency = st.radio("How often does the customer log in?", ('Weekly', 'Monthly', 'Daily'))
    FeedbackRating = st.number_input("What was the customer's rating? ")
    ServiceInteractions_Call = st.number_input("How many times did the customer interact via phone call? ")
    ServiceInteractions_Email = st.number_input("How many times did the customer interact via phone email? ")
    ServiceInteractions_Chat = st.number_input("How many times did the customer interact via phone chat? ")
    PaymentHistoryNoOfLatePayments = st.number_input("How many late payments did the customer make? ")
    SubscriptionDuration = st.number_input("How many days has the customer's subscription plan been active for? ")

    ChurnLabel = ""

    if st.button("Result"):
        ChurnLabel = prediction([ID, Name, Email, Phone, Address, Age, Gender, NPS, PurchaseFrequency,
                                 PurchaseValue, WebsitePageViews, WebsiteTimeSpent,
                                 EngagementMetricsLogins, EngagementMetricsFrequency, FeedbackRating,
                                 ServiceInteractions_Call, ServiceInteractions_Email, ServiceInteractions_Chat,
                                 PaymentHistoryNoOfLatePayments, SubscriptionDuration])

        st.success(ChurnLabel)


if __name__ == "__main__":
    main()