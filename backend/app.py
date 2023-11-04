from flask import Flask, request, jsonify
from flask_cors import CORS
from homebuyer import validBuy  # Import your validBuy function
from gpt import chat_with_gpt

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/validate-buy', methods=['POST'])
def validate_buy():
    data = request.json
    gross_monthly_income = data.get('gross_monthly_income')
    credit_card_payment = data.get('credit_card_payment')
    car_payment = data.get('car_payment')
    student_loan_payment = data.get('student_loan_payment')
    appraised_value = data.get('appraised_value')
    down_payment = data.get('down_payment')
    loan_amount = data.get('loan_amount')
    mortgage_payment = data.get('mortgage_payment')
    credit_score = data.get('credit_score')

    violation = validBuy(
        gross_monthly_income, credit_card_payment, car_payment,
        student_loan_payment, appraised_value, down_payment,
        loan_amount, mortgage_payment, credit_score
    )

    return jsonify({"violation": violation})


@app.route('/api/chat-with-gpt', methods=['POST'])
def chat_gpt():
    data = request.json
    user_input = data.get('user_input')  # Get the user's input from the request

    response = chat_with_gpt(user_input)  # Call your chat_with_gpt function
    
    return jsonify({"chat_response": response})


if __name__ == '__main__':
    app.run(debug=True)
