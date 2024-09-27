**Predicting Customer Churn**
## Identifying Customers that are Susceptible to Churn in order to Enhance Retention Strategies and Boost Business Growth

**Project Learning Objectives**
The primary objective of this project is to develop a predictive model that can accurately forecast customer churn within the telecommunications industry. 
Specifically, the project aims to leverage historical customer data and relevant features to create a machine learning model capable of identifying customers who are likely to churn. 
The model's performance will be assessed using appropriate evaluation metrics.

**Learning Skills**
- Python Proficiency
- Data Preprocessing
- Exploratory Data Analysis
- Model Development
- Churn Prediction

**A quick overview of the dataset**

- `CustomerID`: A unique identifier for each customer.
- `Name`: The name of the customer.
- `Age`: The age of the customer.
- `Gender`: The gender of the customer.
- `Location`: The location or city where the customer is based.
- `Email`: The email address of the customer.
- `Phone`: The phone number of the customer.
- `Address`: The postal address of the customer.
- `Segment`: The customer segment or category to which the customer belongs (e.g., Segment A, Segment B, Segment C).
- `PurchaseHistory`: A list of dictionaries representing the customer's purchase history. Each dictionary includes details about products purchased, purchase frequency, and purchase value.
    - `Product`: Product name.
    - `Frequency`: The number of times this product was purchased by the customer.
    - `Value`: Cost of  this product.
- `SubscriptionDetails`: A dictionary containing information about the customer's subscription plan, including the plan name, start date, and end date.
    - `Plan`: Name of the subscription plan.
    - `StartDate`: Start date of subscription plan.
    - - `EndDate`: End date of subscription plan.
- `ServiceInteractions`: A list of dictionaries representing the customer's interactions with customer service. Each dictionary includes the type of interaction (e.g., Call, Email, Chat) and the date of the interaction.
    - `Type`: Type of service, it could be Call, Email or Chat.
    - `Date`: Date of the service interaction.
- `PaymentHistory`: A list of dictionaries representing the customer's payment history. Each dictionary includes the payment method (e.g., Credit Card, PayPal) and the number of late payments.
    - `Method`: Payment method, can either be Credit Card, PayPal or Bank Transfer.
    - `LatePayments`: Number of late payments.
- `WebsiteUsage`: A dictionary containing metrics related to the customer's usage of a website or app, including the number of page views and time spent (in minutes).
- `PageViews`: The number of website page views from the customer.
- `TimeSpent`: Time spent on the website by a customer in minutes.
- `ClickstreamData`: A list of dictionaries representing the customer's clickstream data, including actions such as clicks, searches, and adding items to the cart. Each dictionary includes the action type, the page where the action occurred, and a timestamp.
    - `Action`: Clickstream action of the user, could be Click, Search or Add to Cart.
    - `Page`: The website page in which the user performed this action.
    - `Timestamp`: Timestamp of the clickstream action.
- `EngagementMetrics`: A dictionary containing engagement metrics, such as the number of logins and the frequency of engagement (e.g., Daily, Weekly, Monthly).
    - `Logins`: The number of logins the user made.
    - - `Frequency`: How often a customer logs in to the platform. Could be Daily, Weekly or Monthly.
- `Feedback`: Feedback provided by the customer, including a rating (e.g., 1 to 5) and a comment.
    - `Rating`: A value between 1 and 5 that indicates the customer’s feedback rating.
    - `Comment`: The comment left by the customer for the feedback.
- `MarketingCommunication`: A list of dictionaries representing the customer's history of marketing communication, including dates when emails were sent, opened, and clicked.
    - `EmailSent`: Date when email was sent.
    - `EmailOpened`: Date when email was opened.
    - `EmailClicked`: Date when email was clicked.
- `NPS`: The Net Promoter Score (NPS) of the customer, which measures customer loyalty and satisfaction on a scale of 0 to 10.
- `ChurnLabel`: A binary label indicating whether the customer has churned (1 for churn, 0 for no churn).
- `Timestamp`: The timestamp indicating when the data was recorded for the customer.

As you can see from the above, the dataset has alot of nested columns which we drilled into in the feature engineering phase of the project but Our target feature is 'ChurnLabel'.

**Data Preprocessing & Feature Engineering**

In the Data Preprocessing and Feature Engineering step, we aim to achieve a few things:
- create new features that may have predictive power.
- convert categorical variables to numeric variables, using encoding techniques,
- scale or normalize numeric variables if necessary,
- split the data into training and testing subsets.
- remove irrelevant features.

From our correlation analysis, we saw that:
- `NPS` exhibits some moderate negative correlation (-0.5) with the `ChurnLabel`,
- `WebsiteTimeSpent` exhibits some moderate negative correlation (-0.6) with the `ChurnLabel`,
- `ServiceInteractions_Call` exhibits some moderate postive correlation (0.6) with the `ChurnLabel`,
- `ServiceInteractions_Email` exhibits some moderate positive correlation (0.6) with the `ChurnLabel`,
- `ServiceInteractions_Chat` exhibits some moderate positive correlation (0.6) with the `ChurnLabel`,
- `PaymentHistoryNoOfLatePayments` exhibits some high positive correlation (0.9) with the `ChurnLabel`,
- `PaymentHistoryAvgNoOfLatePayments` exhibits some high positive correlation (0.9) with the `ChurnLabel`,

**Modelling**

The `ChurnLabel` was engineered with two models, to see the best performing one. The models are:
- LogisticRegression,
- DecisionTreeClassifier.

On the validation dataset:
- for Accuracy score: the Decision Tree model performed slightly better,
- for Precision score: the Decision Tree model performed slightly better,
- for Recall score: the Logistic Regression model performed slightly better,
- for F1 score: the Decision Tree model performed slightly better.

On this test dataset:
- for Accuracy score: the Decision Tree model performed slightly better,
- for Precision score: the Decision Tree model performed slightly better,
- for Recall score: the Decision Tree model performed slightly better,
- for F1 score: the Decision Tree model performed slightly better.

This is consistent with the evaluation results of the validation subset.

From the decision matrix of both models,
- They both performed well at predicting customers that did not churn,
- Decision Tree performed better at predicting customers that churned.

**Conclusion**

The parameters that were most important in determining whether or not a customer will churn are:
- the number of Service Interactions the customer has had with customer service through Call, Email and Chat,
- the number of times the customer has made Late Payments,
- the time spent on the company's website,
- and the Net Promoter Score (NPS) of the customer, which measures customer loyalty and satisfaction.
