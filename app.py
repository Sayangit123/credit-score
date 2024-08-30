from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

model_pipeline = joblib.load('model_pipeline.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the form data
        Month = object(request.form['Month'])
        Age = int(request.form['Age'])
        Occupation = object(request.form['Occupation'])
        Annual_Income = float(request.form['Annual_Income'])
        Monthly_Inhand_Salary =float(request.form['Monthly_Inhand_Salary'])
        Num_Bank_Accounts =int (request.form['Num_Bank_Accounts'])
        Num_Credit_Card = int(request.form['Num_Credit_Card'])
        Interest_Rate = int(request.form['Interest_Rate'])
        Num_of_Loan = float(request.form['Num_of_Loan'])
        Delay_from_due_date = int(request.form['Delay_from_due_date'])
        Num_Credit_Inquiries = float(request.form['Num_Credit_Inquiries'])
        Outstanding_Debt = float(request.form['Oustanding_Debt'])
        Credit_Utilization_Ratio = float(request.form['Credit_Utilization_Ratio'])
        Total_EMI_per_month = float(request.form['Total_EMI_per_month'])
        Payment_Behaviour = object(request.form['Payment_Behaviour'])
        Amount_invested_monthly = float(request.form['Amount_invested_monthly'])
        Monthly_Balance = float(request.form['Monthly_Balance'])
       
        # Create DataFrame from input features
        features = pd.DataFrame({
            'Age': [Age],
            'Month':[Month],
            'Occupation':[Occupation],
            'Anuual_Income': [Annual_Income],
            'Monthly_Inhand_Salary': [Monthly_Inhand_Salary],
            'Num_Bank_Accounts': [Num_Bank_Accounts],
            'Num_Credit_Card': [Num_Credit_Card],
            'Interest_Rate': [Interest_Rate],
            'Num_of_Loan': [Num_of_Loan],
            'Delay_from_due_date':[Delay_from_due_date],
            'Num_Credit_Inquiries': [Num_Credit_Inquiries],
            'Outstanding_Debt': [Outstanding_Debt],
            'Credit_Utilization_Ratio': [Credit_Utilization_Ratio],
            'Total_EMI_per_month': [Total_EMI_per_month],
            'Payment_Behaviour': [Payment_Behaviour],
            'Amount_invested_monthly' : [Amount_invested_monthly],
             'Monthly_Balance' : [Monthly_Balance]
        })

         # Make prediction
        Credit_Score = model_pipeline.predict(features)

        return render_template('index.html', prediction_text='Predicted Credit Score: ${:.2f}'.format(Credit_Score[0]))
    
    if __name__ == "__main__":
        app.run(debug=True)